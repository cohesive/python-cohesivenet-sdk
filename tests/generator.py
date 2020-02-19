import string
import random

from cohesivenet.api_client import APIResponse

random.seed(None)

# Generate Openapi values
#
#   OpenAPIv3 datatypes:
#       number
#       integer
#       boolean
#       array
#       object
# https://swagger.io/docs/specification/data-models/data-types/


def random_int(minimum=1, maximum=100):
    """Generate a random int"""
    return random.randint(minimum, maximum)


def random_string(minLength=10, maxLength=15):
    """Generate a random string of fixed length """
    length = random_int(minLength, maxLength)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def random_enum(options=[]):
    return random.choice(options)


def get_schema_ref(schema, ref):
    ref_parts = ref.lstrip('#/').split('/')
    _schema_pointer = schema
    for p in ref_parts:
        _schema_pointer = _schema_pointer.get(p.replace("~1", "/"))
        if type(_schema_pointer) is not dict:
            break
    return _schema_pointer


def generate_api_var(var_schema):
    api_type = var_schema["type"]
    if api_type == "string":
        enums = var_schema.get("enum")
        if enums:
            return random_enum(options=enums)
        kwargs = {} # map string constrains
        # TODO: add format options
        return random_string(**kwargs)
    elif api_type == "integer":
        # TODO map string constrains
        return random_int()
    elif api_type == "boolean":
        return True
    raise RuntimeError("Unsupport type for generation %s" % str(api_type))



def get_mock_call_args(method_schema):
    """Generate mock call args for endpoint path args
    
    Arguments:
        method_schema {dict} - parses parameters - https://swagger.io/docs/specification/describing-parameters/
    
    Returns:
        tuple
    """
    request_parameters = method_schema.get("parameters")
    if not request_parameters:
        return ()

    path_params = [
        p for p in request_parameters if p["in"] == "path"
    ]

    args = ()
    for param in path_params:
        param_schema = param["schema"]
        api_type = param_schema["type"]
        args = args + (generate_api_var(param["schema"]),)
    return args

def get_mock_call_kwargs(method_schema):
    """Generate mock request query parameters or request body from schema
    
    Arguments:
        method_schema {dict} -- dict under http methods - https://swagger.io/docs/specification/paths-and-operations/
    
    Raises:
        RuntimeError - invalid test declaration or unsupported
    
    Returns:
        dict
    """
    request_body = method_schema.get("requestBody")
    request_parameters = method_schema.get("parameters")
    query_dict = {}
    if request_parameters:
        query_params = [
            p for p in request_parameters if p["in"] == "query"
        ]
        query_dict = {
            query_param["name"]: generate_api_var(query_param["schema"])
            for query_param in query_params
        }

    body_params = {}
    if request_body:
        content_obj = request_body["content"]
        if "application/json" in content_obj:
            object_schema = content_obj["application/json"]["schema"]["properties"]
            body_params = {
                name: generate_api_var(prop_schema)
                for name, prop_schema in object_schema.items()
            }
        elif "text/plain" in content_obj:
            body_params = {
                "body": random_string(minLength=300, maxLength=300)
            }
        else:
            raise RuntimeError(
                "Unsupported content type(s) for generation: %s" % list(content_obj.keys()))
    return dict(query_params, **body_params)


def configure_method_test(
    client,
    schema,
    http_method,
    path,
    rest_mocker,
    request_args=None,
    request_kwargs=None,
    mock_request_from_schema=False,
    mock_response=None,
    mock_response_from_schema=False,
    expected_response_status=200,
    allow_fail=False
):
    """Run API test

    Arguments:
        client {} -- [description]
        schema {[type]} -- [description]
        http_method {[type]} -- [description]
        path {[type]} -- [description]
        rest_mocker {[type]} -- [description]

    Keyword Arguments:
        request {[type]} -- [description] (default: {None})
        mock_response {[type]} -- [description] (default: {None})
        mock_response_from_schema {bool} -- [description] (default: {False})
        allow_fail {bool} -- [description] (default: {False})

    Raises:
        AssertionError: Test setup failed
    """
    should_fail = not allow_fail
    _path = path if path.startswith("/") else "/%s" % path
    _method = http_method.lower()
    endpoint_schema = schema["paths"].get(path)

    if not endpoint_schema and should_fail:
        raise AssertionError("No path %s in schema" % path)

    method_schema = endpoint_schema.get(_method)
    if not method_schema and should_fail:
        raise AssertionError("No HTTP method %s in for endpoint %s" % (http_method, path))

    if mock_response is not None and mock_response_from_schema:
        raise RuntimeError(
            "Can't determine how to mock response. Only 1 of mock_response or "
            "mock_response_from_schema should be passed.")

    _full_api_path = "/api%s" % _path
    expected_response = {}
    if mock_response:
        expected_response = mock_response
        rest_mocker.stub_request(
            _method,
            _full_api_path,
            rbody=mock_response,
            rcode=expected_response_status
        )
    elif mock_response_from_schema:
        method_responses = method_schema["responses"]
        response_schema = method_responses.get(str(expected_response_status))
        if not response_schema:
            raise RuntimeError(
                "No response schema provided for status code %s" % str(expected_response_status))
        example_response =  response_schema.get("content", {}).get("application/json", {}).get("example")
        if not response_schema:
            raise RuntimeError(
                "No response example provided for status code %s" % str(expected_response_status))

        expected_response = example_response
        rest_mocker.stub_request(
            _method,
            _full_api_path,
            rbody=example_response,
            rcode=expected_response_status
        )
    else:
        rest_mocker.stub_request(
            _method,
            _full_api_path,
            rbody=expected_response,
            rcode=expected_response_status
        )

    call_args = None
    if request_args is not None:
        call_args = request_args
    elif mock_request_from_schema:
        call_args = get_mock_call_args(method_schema)
    else:
        call_args = ()

    call_kwargs = None
    if request_kwargs is not None:
        call_kwargs = request_kwargs
    elif mock_request_from_schema:
        call_kwargs = get_mock_call_kwargs(method_schema)
    else:
        call_kwargs = {}

    def __test(call):
        response = call(client, *call_args, **call_kwargs)
        assert type(response) is APIResponse, "Unexpected response type %s" % str(type(response))
        assert response.json() == expected_response, "Unexpected response"
        assert response.status == expected_response_status, (
            "Unexpected response status %d. Expected %s" % (response.status, expected_response_status)
        )

    return __test