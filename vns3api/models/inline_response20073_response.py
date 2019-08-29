# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20073Response(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'snapshot': 'str',
        'log_lines': 'list[str]'
    }

    attribute_map = {
        'snapshot': 'snapshot',
        'log_lines': 'log_lines'
    }

    def __init__(self, snapshot=None, log_lines=None):  # noqa: E501
        """InlineResponse20073Response - a model defined in OpenAPI"""  # noqa: E501

        self._snapshot = None
        self._log_lines = None
        self.discriminator = None

        if snapshot is not None:
            self.snapshot = snapshot
        if log_lines is not None:
            self.log_lines = log_lines

    @property
    def snapshot(self):
        """Gets the snapshot of this InlineResponse20073Response.  # noqa: E501

        Status of import  # noqa: E501

        :return: The snapshot of this InlineResponse20073Response.  # noqa: E501
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this InlineResponse20073Response.

        Status of import  # noqa: E501

        :param snapshot: The snapshot of this InlineResponse20073Response.  # noqa: E501
        :type: str
        """

        self._snapshot = snapshot

    @property
    def log_lines(self):
        """Gets the log_lines of this InlineResponse20073Response.  # noqa: E501

        Log details if failed  # noqa: E501

        :return: The log_lines of this InlineResponse20073Response.  # noqa: E501
        :rtype: list[str]
        """
        return self._log_lines

    @log_lines.setter
    def log_lines(self, log_lines):
        """Sets the log_lines of this InlineResponse20073Response.

        Log details if failed  # noqa: E501

        :param log_lines: The log_lines of this InlineResponse20073Response.  # noqa: E501
        :type: list[str]
        """

        self._log_lines = log_lines

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20073Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other