import json

import cohesivenet
from cohesivenet import six, urllib3
from cohesivenet.rest import RESTResponse


class RestClientMock(object):
    def __init__(self, mocker):
        self._mocker = mocker

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


    def _patched_request(self, requestor, method, url, *args, **kwargs):
        response = self._stub_request_handler.get_response(method, url)
        print('response %s' % response)
        if response is not None:
            return response

        return self._real_request(requestor, method, url, *args, *kwargs)

    def stub_request(self, method, url, rbody={}, rcode=200, rheaders={}):
        self._stub_request_handler.register(
            method, url, rbody, rcode, rheaders
        )

    def assert_requested(self, method, url, query_params=None, headers=None, body=None, post_params=None):
        params = params or self._mocker.ANY
        headers = headers or self._mocker.ANY
        called = False
        exception = None

        # Sadly, ANY does not match a missing optional argument, so we
        # check all the possible signatures of the request method
        possible_called_args = [
            # (self._mocker.ANY, method, url),
            # (self._mocker.ANY, method, url, params),
            # (self._mocker.ANY, method, url, params, headers),
            (self._mocker.ANY, method, url, query_params, headers, body, post_params),
        ]

        for args in possible_called_args:
            try:
                self.request_patcher.assert_called_with(*args)
            except AssertionError as e:
                exception = e
            else:
                called = True
                break

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
        url_no_protocol = url.strip('https://')
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