import json

import cohesivenet
from cohesivenet import six, urllib3
from cohesivenet.rest import RESTResponse


class RestClientMock(object):
    COMMON_HOST_ENDPOINT = '0.0.0.0'
    COMMON_PORT = '8000'
    COMMON_HOST = '%s:%s' % (COMMON_HOST_ENDPOINT, COMMON_PORT)


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
        if url.startswith('http'):
            return url
        return 'https://%s%s' % (self.COMMON_HOST, url)

    def _patched_request(self, requestor, method, url, *args, **kwargs):
        response = self._stub_request_handler.get_response(method, url)
        print(self._stub_request_handler._entries)
        if response is not None:
            return response

        return self._real_request(requestor, method, url, *args, *kwargs)

    def stub_request(self, method, url, rbody={}, rcode=200, rheaders={}):
        self._stub_request_handler.register(
            method, url, rbody, rcode, rheaders
        )

    def assert_requested(self, method, url, query_params=None, headers=None, body=None, post_params=None):
        query_params = query_params or self._mocker.ANY
        headers = headers or self._mocker.ANY
        body = body or self._mocker.ANY
        post_params = post_params or self._mocker.ANY
        called = False
        exception = None
        method_expected = method.upper()
        url_expected = self.get_expected_url(url)

        # Sadly, ANY does not match a missing optional argument, so we
        # check all the possible signatures of the request method
        call_args = (
            self._mocker.ANY,
            method_expected,
            url_expected,
        )
        call_kwargs = {
            '_preload_content': self._mocker.ANY,
            '_request_timeout': self._mocker.ANY,
            'headers': self._mocker.ANY,
            'post_params': [],
            'query_params': [],
            'body': None
        }

        if query_params:
            call_kwargs.update(query_params=query_params)
        if headers:
            call_kwargs.update(headers=headers)
        if body:
            call_kwargs.update(body=body)
        if post_params:
            call_kwargs.update(post_params=post_params)

        try:
            self.request_patcher.assert_called_with(*call_args, **call_kwargs)
        except AssertionError as e:
            exception = e
        else:
            called = True

        if not called:
            raise exception

    def assert_no_request(self):
        if self.request_patcher.call_count != 0:
            msg = (
                "Expected 'request' to not have been called. "
                "Called %s times." % (self.request_patcher.call_count)
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
        url_no_protocol = url.lstrip('https://')
        uri = url_no_protocol[url_no_protocol.index('/'):]

        if (method, uri) in self._entries:
            rbody, rstatus, rheaders = self._entries.pop((method, uri))
            if not isinstance(rbody, six.string_types):
                rbody = json.dumps(rbody)
            response = RESTResponse(
                urllib3.response.HTTPResponse(
                    body=rbody,
                    headers=rheaders,
                    status=rstatus
                )
            )
            return response

        return None