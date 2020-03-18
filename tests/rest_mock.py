import json
import six

import cohesivenet
from cohesivenet import urllib3
from cohesivenet.rest import RESTResponse


class RestClientMock(object):
    COMMON_HOST_ENDPOINT = "0.0.0.0"
    COMMON_PORT = "8000"
    COMMON_HOST = "%s:%s" % (COMMON_HOST_ENDPOINT, COMMON_PORT)

    def __init__(self, mocker):
        self._mocker = mocker
        self._client = None

        self._real_request = cohesivenet.rest.RESTClientObject.request
        self._stub_request_handler = StubRequestHandler()

        self.constructor_patcher = self._mocker.patch(
            "cohesivenet.api_client.rest.RESTClientObject.__init__",
            side_effect=cohesivenet.rest.RESTClientObject.__init__,
            autospec=True,
        )

        self.request_patcher = self._mocker.patch(
            "cohesivenet.api_client.rest.RESTClientObject.request",
            side_effect=self._patched_request,
            autospec=True,
        )

    def get_expected_url(self, url):
        if url.startswith("http"):
            return url
        return "https://%s%s" % (self.COMMON_HOST, url)

    def _patched_request(self, requestor, method, url, *args, **kwargs):
        response = self._stub_request_handler.get_response(method, url)
        if response is not None:
            return response

        return self._real_request(requestor, method, url, *args, **kwargs)

    def stub_request(self, method, url, rbody={}, rcode=200, rheaders={}):
        self._stub_request_handler.register(method, url, rbody, rcode, rheaders)

    def assert_requested(
        self, method, url, query_params=None, headers=None, body=None, post_params=None
    ):
        called = False
        exception = None
        method_expected = method.upper()
        url_expected = self.get_expected_url(url)

        call_args = (
            self._mocker.ANY,  # api self instance
            method_expected,
            url_expected,
        )

        expected_call_kwargs = {
            "_preload_content": self._mocker.ANY,
            "_request_timeout": self._mocker.ANY,
            "headers": self._mocker.ANY,
        }

        if query_params:
            expected_call_kwargs.update(query_params=query_params)
        if headers:
            expected_call_kwargs.update(headers=headers)
        if body:
            expected_call_kwargs.update(body=body)
        if post_params:
            expected_call_kwargs.update(post_params=post_params)

        optional_params = ["query_params", "body", "post_params"]
        any_call_kwargs = {
            p: self._mocker.ANY
            for p in optional_params
            if p not in expected_call_kwargs
        }

        if method.lower() == "delete":
            any_call_kwargs.pop("post_params")
        elif method.lower() == "get":
            any_call_kwargs.pop("post_params")
            any_call_kwargs.pop("body")

        kwarg_assertions = [
            expected_call_kwargs,
            dict(any_call_kwargs, **expected_call_kwargs),
        ]

        # Sadly, ANY does not match a missing optional argument, so we
        # check all the possible signatures of the request method

        call_args = tuple(self.request_patcher.call_args)
        path_args = call_args[0]
        method_kwargs = call_args[1]

        method_called = path_args[1]
        endpoint_called = path_args[2]
        query_called = method_kwargs.get("query_params")
        body_called = method_kwargs.get("body")
        post_params_called = method_kwargs.get("post_params")
        headers_called = method_kwargs.get("headers")

        assert method_called == method.upper(), "Unexpected method %s. Expected %s." % (
            method_called,
            method.upper(),
        )
        assert endpoint_called == url_expected, "Unexpected URL %s. Expected %s." % (
            endpoint_called,
            url_expected,
        )

        if query_params is not None:
            assert set(query_called) == set(query_params), (
                "Unexpected query params %s. Expected %s. Order ignored."
                % (query_called, query_params)
            )
        if headers is not None:
            assert headers_called == headers, "Unexpected headers %s. Expected %s." % (
                headers_called,
                headers,
            )
        if post_params is not None:
            assert post_params_called == post_params, (
                "Unexpected POST params %s. Expected %s."
                % (post_params_called, post_params)
            )
        if body is not None:
            assert body_called == body, "Unexpected Body %s. Expected %s." % (
                body_called,
                body,
            )

    def assert_no_request(self):
        if self.request_patcher.call_count != 0:
            msg = "Expected 'request' to not have been called. " "Called %s times." % (
                self.request_patcher.call_count
            )
            raise AssertionError(msg)

    def reset_mock(self):
        self.request_patcher.reset_mock()


class StubRequestHandler(object):
    def __init__(self):
        self._entries = {}

    def register(self, method, url, rbody={}, rstatus=200, rheaders={}):
        self._entries[(method.lower(), url)] = (rbody, rstatus, rheaders)

    def get_response(self, method, url):
        method = method.lower()
        url_no_protocol = url.lstrip("https://")
        uri = url_no_protocol[url_no_protocol.index("/") :]
        if (method, uri) in self._entries:
            rbody, rstatus, rheaders = self._entries.pop((method, uri))
            if not isinstance(rbody, six.string_types):
                rbody = json.dumps(rbody)
            response = RESTResponse(
                urllib3.response.HTTPResponse(
                    body=rbody, headers=rheaders, status=rstatus
                )
            )
            return response

        return None
