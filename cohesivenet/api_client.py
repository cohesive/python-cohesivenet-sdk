# coding: utf-8
"""
    Cohesive Networks SDK

    Cohesive Networks SDK is a thin wrapper around our product APIs providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import mimetypes
import io
import os

from urllib.parse import quote

import cohesivenet.util
from cohesivenet.serialization import Serializer
from cohesivenet.configuration import Configuration
from cohesivenet import rest
from cohesivenet.exceptions import ApiValueError


class DataDict(dict):
    def __init__(self, *args, **kwargs):
        super(DataDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __getattribute__(self, name):
        if name in self:
            if type(self[name]) is dict:
                return DataDict(**self[name])
            return super().__getattribute__(name)
        return None


class APIResponse(io.IOBase):
    def __init__(self, rest_response):
        self.urllib3_response = rest_response.urllib3_response
        self.status = rest_response.status
        self.reason = rest_response.reason
        self.raw_data = rest_response.data
        self._rest_response = rest_response
        self._serializer = Serializer()
        self._data_serialized = None

    def get_headers(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def get_header(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)

    @property
    def data(self):
        return self._rest_response.data

    def json(self):
        if self._data_serialized:
            return self._data_serialized
        self._data_serialized = self._serializer.deserialize(self._rest_response)
        return self._data_serialized

    @property
    def response(self):
        data = self.json()
        if "response" in data:
            resp = data["response"]
            if type(resp) is dict:
                return DataDict(**resp)
            return resp
        return None


class APIClient(object):
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    BASE_PATH = None
    DEF_REQ_TIMEOUT = None

    def __init__(
        self, configuration=None, header_name=None, header_value=None, cookie=None
    ):
        self.configuration = configuration  # see configuration.setter
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = "OpenAPI-Generator/1.0.0/python"
        self._base_path = "/%s" % self.BASE_PATH.strip("/") if self.BASE_PATH else ""
        self._api_versions_cache = {}
        self.client_side_validation = self.configuration.client_side_validation
        self.serializer = Serializer(self.configuration)

    @property
    def configuration(self):
        return self._configuration

    @configuration.setter
    def configuration(self, value):
        config = value
        if config is None:
            config = Configuration()
        self._configuration = config
        self._api_versions_cache = {}
        self.rest_client = rest.RESTClientObject(self.configuration)

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers["User-Agent"]

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers["User-Agent"] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def reset_api_version_sdk(self):
        self._api_versions_cache = {}
        return self

    def __call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        auth_settings=None,
        _return_http_data_only=None,  # deprecated
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
    ):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params["Cookie"] = self.cookie
        if header_params:
            header_params = self.serializer.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params, collection_formats)
            )

        # path parameters
        if path_params:
            path_params = self.serializer.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    "{%s}" % k, quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = self.serializer.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params, collection_formats)

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.serializer.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params, collection_formats)
            post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = self.serializer.sanitize_for_serialization(body)

        # request url
        if _host is None:
            url = self.configuration.endpoint + self._base_path + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + self._base_path + resource_path

        # perform request and return response
        rest_response = self.request(
            method,
            url,
            query_params=query_params,
            headers=header_params,
            post_params=post_params,
            body=body,
            _preload_content=_preload_content,
            _request_timeout=(_request_timeout or self.DEF_REQ_TIMEOUT),
        )

        self.last_response = rest_response
        return APIResponse(rest_response)

    def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        auth_settings=None,
        async_req=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
    ):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(
                resource_path,
                method,
                path_params,
                query_params,
                header_params,
                body,
                post_params,
                files,
                response_type,
                auth_settings,
                _return_http_data_only,
                collection_formats,
                _preload_content,
                _request_timeout,
                _host,
            )
        else:
            # return coroutine
            return cohesivenet.util.force_async(
                self.__call_api,
                (
                    resource_path,
                    method,
                    path_params,
                    query_params,
                    header_params,
                    body,
                    post_params,
                    files,
                    response_type,
                    auth_settings,
                    _return_http_data_only,
                    collection_formats,
                    _preload_content,
                    _request_timeout,
                    _host,
                ),
            )

    def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "HEAD":
            return self.rest_client.HEAD(
                url,
                query_params=query_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                headers=headers,
            )
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "POST":
            return self.rest_client.POST(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PUT":
            return self.rest_client.PUT(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "PATCH":
            return self.rest_client.PATCH(
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        elif method == "DELETE":
            return self.rest_client.DELETE(
                url,
                query_params=query_params,
                headers=headers,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                body=body,
            )
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in (
            params.items() if isinstance(params, dict) else params
        ):  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == "multi":
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == "ssv":
                        delimiter = " "
                    elif collection_format == "tsv":
                        delimiter = "\t"
                    elif collection_format == "pipes":
                        delimiter = "|"
                    else:  # csv is the default
                        delimiter = ","
                    new_params.append((k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def files_parameters(self, files=None):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if files:
            for k, v in files.items():
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, "rb") as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (
                            mimetypes.guess_type(filename)[0]
                            or "application/octet-stream"
                        )
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if "application/json" in accepts:
            return "application/json"
        else:
            return ", ".join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return "application/json"

        content_types = [x.lower() for x in content_types]

        if "application/json" in content_types or "*/*" in content_types:
            return "application/json"
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                if not auth_setting["value"]:
                    continue
                elif auth_setting["in"] == "cookie":
                    headers["Cookie"] = auth_setting["value"]
                elif auth_setting["in"] == "header":
                    headers[auth_setting["key"]] = auth_setting["value"]
                elif auth_setting["in"] == "query":
                    querys.append((auth_setting["key"], auth_setting["value"]))
                else:
                    raise ApiValueError(
                        "Authentication token must be in `query` or `header`"
                    )


def prop_setter_exception(name):
    def _raise(_s, _v):
        raise AttributeError("Can't reset attr %s" % name)

    _raise.__name__ = "raise_set_%s_exception" % name
    return _raise


def prop_get_api(name, api_class):
    def _get_api(client):
        if not hasattr(client, "_api_versions_cache"):
            return api_class(client)
        elif name in client._api_versions_cache:
            return client._api_versions_cache[name]

        _api = api_class(client)
        client._api_versions_cache[name] = _api
        return _api

    _get_api.__name__ = "get_%s_api" % name
    return _get_api


def api_as_property(name, api_class):
    return property(prop_get_api(name, api_class), prop_setter_exception(name))
