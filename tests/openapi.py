from collections import OrderedDict

from cohesivenet.api_client import APIResponse
from tests.generator import generate_api_var, random_string, random_from_list


class OpenAPITypes(object):
    String = "string"
    Number = "number"
    Integer = "integer"
    Boolean = "boolean"
    Array = "array"
    Object = "object"

    PyTypes = {
        String: (str, bytes),
        Number: (float, int),
        Integer: (int,),
        Boolean: (bool,),
        Array: (list, tuple),
        Object: (dict,)
    }


def get_mock_call_args(method_schema):
    """Generate mock call args for endpoint path args
    
    Arguments:
        method_schema {dict} - parses parameters - https://swagger.io/docs/specification/describing-parameters/
    
    Returns:
        tuple
    """
    request_parameters = method_schema.get("parameters")
    args = OrderedDict()
    if not request_parameters:
        return args

    path_params = [
        p for p in request_parameters if p["in"] == "path"
    ]

    for param in path_params:
        param_schema = param["schema"]
        api_type = param_schema["type"]
        args[param["name"]] = generate_api_var(param["schema"])
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
            object_schema = content_obj["application/json"]["schema"]["properties"].items()
            one_of = content_obj["application/json"]["schema"].get("oneOf")
            if one_of:
                required_set = random_from_list([option["required"] for option in one_of])
                object_schema = [(k, v) for k, v in object_schema if k in required_set]

            body_params = {
                name: generate_api_var(prop_schema)
                for name, prop_schema in object_schema
            }
        elif "text/plain" in content_obj:
            body_params = {
                "body": random_string(minLength=300, maxLength=300)
            }
        else:
            raise RuntimeError(
                "Unsupported content type(s) for generation: %s" % list(content_obj.keys()))

    return dict(query_dict, **body_params)


def resolve_ref(schema, ref):
    ref_parts = ref.lstrip('#/').split('/')
    _schema_pointer = schema

    parts = []
    for p in ref_parts:
        part = p.replace("~1", "/").replace("%7B", "{").replace("%7D", "}")
        parts.append(part)

        if not _schema_pointer:
            raise Exception("Failed to resolve ref %s" % ref)
        elif type(_schema_pointer) is list:
            if not part.isdigit():
                raise Exception("Failed to resolve ref %s. Expected list index." % ref)
            _schema_pointer = _schema_pointer[int(part)]
        elif type(_schema_pointer) is dict:
            _schema_pointer = _schema_pointer.get(part)

    if _schema_pointer is None:
        raise Exception("Failed to resolve ref %s" % ref)
    return _schema_pointer


def resolve_refs(schema, refs_cache={}, full_schema=None):
    full_schema = full_schema or schema
    if type(schema) is not dict:
        return

    for k, v in schema.items():
        if type(v) is dict:
            if "$ref" in v:
                ref = v["$ref"]
                if ref not in refs_cache:
                    refs_cache[ref] = resolve_ref(full_schema, ref)
                schema[k] = refs_cache[ref]
            else:
                resolve_refs(v, refs_cache, full_schema)
        elif type(v) is list:
            for i, item in enumerate(v):
                if type(item) is dict:
                    if "$ref" in item:
                        ref = item["$ref"]
                        if ref not in refs_cache:
                            refs_cache[ref] = resolve_ref(full_schema, ref)
                        v[i] = refs_cache[ref]
                    else:
                        resolve_refs(item, refs_cache, full_schema)
    return schema


def get_method_success_response(method_schema, full_schema, content_type=None):
    """[summary]
    
    Arguments:
        method_schema {[type]} -- [description]
        full_schema {[type]} -- [description]
    
    Keyword Arguments:
        content_type {[type]} -- [description] (default: {None})
    
    Raises:
        RuntimeError: [description]
        RuntimeError: [description]
    
    Returns:
        [type] -- [description]
    """
    responses = method_schema.get("responses")
    http_success_codes = ("200", "201", "202")

    for status, response_schema in responses.items():
        if status not in http_success_codes:
            continue

        if "content" not in response_schema:
            return int(status), {}

        content_schema = response_schema["content"]
        if content_type and content_type not in content_schema:
            raise RuntimeError(
                "Schema error: No schema for operation %s response %s content type %s" 
                % (method_schema["operationId"], status, content_type))
        elif not content_type:
            # choose first content type. likely only 1
            content_type = next(iter(content_schema.keys()))
        return int(status), content_schema[content_type]
    raise RuntimeError("Schema error: No success code response schema found for %s" % method_schema["operationId"])



def assert_on_response_type(val, type_schema, path=[], should_raise=True):
    if type_schema is None:
        assert val is None or val == {}, "Expected no content"
        return

    if "oneOf" in type_schema:
        one_of_types = type_schema["oneOf"]
        failed = True
        assertion_errors = []

        # succeed on first assertion that doesnt fail
        for optional_type in one_of_types:
            assertion_error = assert_on_response_type(val, optional_type, should_raise=False)
            if not assertion_error:
                failed = False
                break
            assertion_errors.append(assertion_error)
        if failed:
            raise AssertionError(
                "Response failed to conform to optional types. Errors: [%s]"
                % (",".join(map(str, assertion_errors))))
        return None
    elif "allOf" in type_schema:
        all_types = type_schema["allOf"]
        _final_props = {}
        for required_type in all_types:
            assert required_type["type"] == OpenAPITypes.Object, "Can only merge object types"
            _final_props.update(**required_type["properties"])

        type_schema = {
            "type": "object",
            "properties": _final_props
        }

    elif "type" not in type_schema:
        raise Exception("Unsupported schema for assertions: %s" % type_schema)

    exp_type = type_schema["type"]
    try:
        valid_types = OpenAPITypes.PyTypes[exp_type] + ((type(None),) if type_schema.get("nullable") else ())
        assert type(val) in valid_types, "Bad type for path=%s Val=%s Expected %s" % (".".join(path), str(val), exp_type)
        if exp_type == OpenAPITypes.Object: 
            required_props = type_schema.get("required", [])
            missing_props = [prop for prop in required_props if prop not in val]
            assert len(missing_props) == 0, "Missing required properties for %s" % ".".join(path)
            properties_schema = type_schema.get("properties", {})
            val_type = type_schema.get("additionalProperties", {})

            if properties_schema:
                for prop, prop_val in val.items():
                    assert prop in properties_schema, "Unexpected property '%s' @ %s" % (prop, ".".join(path))
                    assert_on_response_type(prop_val, properties_schema[prop], path=path + [prop])
            elif val_type:
                for prop, prop_val in val.items():
                    assert_on_response_type(prop_val, val_type, path=path + [prop])
            else:
                raise RuntimeError("Unexpected type schema format: %s" % type_schema)
        elif exp_type == OpenAPITypes.Array:
            item_schema = type_schema["items"]
            for i, val_item in enumerate(val):
                assert_on_response_type(val_item, item_schema, path=path + [str(i)])
        else:
            # todo: add checks like enum and max min
            pass
        return None
    except AssertionError as e:
        if should_raise:
            raise e
        return e


def generate_method_test(
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

    call_args = ()
    path_params = {}
    if request_args is not None:
        if type(request_args) is dict:
            path_params = request_args
            call_args = tuple(request_args.values())
        else:
            call_args = request_args
    elif mock_request_from_schema:
        path_params = get_mock_call_args(method_schema)
        call_args = tuple(path_params.values())

    call_kwargs = {}
    if request_kwargs is not None:
        call_kwargs = request_kwargs
    elif mock_request_from_schema:
        call_kwargs = get_mock_call_kwargs(method_schema)

    _full_api_path = ("/api%s" % _path).format(**path_params)
    response_code, method_response = get_method_success_response(method_schema, schema)
    response_schema = method_response.get("schema")
    expected_response = {}
    if mock_response:
        expected_response = mock_response
        rest_mocker.stub_request(
            _method,
            _full_api_path,
            rbody=mock_response,
            rcode=response_code
        )
    elif mock_response_from_schema:
        example_response = method_response.get("example")
        if not example_response:
            example_response = response_schema.get("example") if response_schema else None
            if not expected_response:
                raise RuntimeError(
                    "No response example provided for status code %s" % str(response_code))

        expected_response = example_response
        rest_mocker.stub_request(
            _method,
            _full_api_path,
            rbody=example_response,
            rcode=response_code
        )
    else:
        rest_mocker.stub_request(
            _method,
            _full_api_path,
            rbody=expected_response,
            rcode=response_code
        )

    # constants will have to change based on spec, specifically Content Type
    expected_request_args = {
        'headers': {
            'User-Agent': 'OpenAPI-Generator/1.0.0/python',
            'Accept': 'application/json',
            'Authorization': 'Basic YXBpOm1vY2twYXNzMTIzNA==',
        }
    }

    if _method in ('post', 'put', 'delete'):
        request_body = method_schema.get('requestBody')
        if request_body:
            expected_request_args['headers']['Content-Type'] = next(iter(request_body['content'].keys()))

        if call_kwargs:
            if expected_request_args['headers'].get('Content-Type') == "text/plain":
                # Currently expecting all file uploads to pass body kwarg as file
                expected_request_args["body"] = call_kwargs["body"]
            else:
                expected_request_args["body"] = call_kwargs
    elif _method in ('get'):
        if call_kwargs:
            expected_request_args["query_params"] = list(call_kwargs.items())

    def __test(call):
        response = call(client, *call_args, **call_kwargs)
        assert type(response) is APIResponse, "Unexpected response type %s" % str(type(response))
        assert response.json() == expected_response, "Unexpected response"
        assert response.status == response_code, (
            "Unexpected response status %d. Expected %s" % (response.status, response_code)
        )
        rest_mocker.assert_requested(
            _method.upper(),
            "%s%s" % (client.configuration.endpoint, _full_api_path),
            **expected_request_args
        )
        assert_on_response_type(response.json(), response_schema)
    return __test