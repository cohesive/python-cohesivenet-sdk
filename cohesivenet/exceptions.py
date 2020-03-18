# coding: utf-8

"""
    Cohesive Networks SDK

    Cohesive Networks SDK is a thin wrapper around our product APIs providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""

import re
import six
import json
import urllib3


UrlLib3ConnExceptions = (
    urllib3.exceptions.ConnectTimeoutError,
    urllib3.exceptions.NewConnectionError,
    urllib3.exceptions.MaxRetryError,
)


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class CohesiveSDKException(Exception):
    """The base exception class for SDK Client exceptions"""


class ApiMethodUnsupportedError(Exception):
    def __init__(self, method_name, version, supported_versions, *args, **kwargs):
        self.method = method_name
        self.version = version
        self.supported_versions = supported_versions
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Custom error messages for ApiMethodUnsupportedError"""
        return (
            "API method %s not supported on version %s. Supported versions are %s."
            % (self.method, self.version, self.supported_versions)
        )

    def __repr__(self):
        return "%s(method=%s,version=%s,supported_versions=%s)" % (
            self.__class__.__name__,
            self.method,
            self.version,
            self.supported_versions,
        )


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None, key_type=None):
        """ Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiException(OpenApiException):
    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message

    def __repr__(self):
        return "%s(status=%s,reason=%s,http_resp.body=%s)" % (
            self.__class__.__name__,
            self.status,
            self.reason,
            self.body,
        )

    def get_error_message(self):
        error_obj = self.error.get("error")
        if type(error_obj) is dict:
            return error_obj.get("message")
        return self.body

    @property
    def error(self):
        _data = self.body or self.reason
        try:
            error_response_str = re.findall(r"{\"error\".*}", _data)
            if error_response_str:
                return json.loads(error_response_str[0])
            return json.loads(_data)
        except json.decoder.JSONDecodeError:
            return {"error": _data}


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, six.integer_types):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result
