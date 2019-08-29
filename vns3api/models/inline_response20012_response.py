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


class InlineResponse20012Response(object):
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
        'password_reset': 'str'
    }

    attribute_map = {
        'password_reset': 'password_reset'
    }

    def __init__(self, password_reset=None):  # noqa: E501
        """InlineResponse20012Response - a model defined in OpenAPI"""  # noqa: E501

        self._password_reset = None
        self.discriminator = None

        if password_reset is not None:
            self.password_reset = password_reset

    @property
    def password_reset(self):
        """Gets the password_reset of this InlineResponse20012Response.  # noqa: E501


        :return: The password_reset of this InlineResponse20012Response.  # noqa: E501
        :rtype: str
        """
        return self._password_reset

    @password_reset.setter
    def password_reset(self, password_reset):
        """Sets the password_reset of this InlineResponse20012Response.


        :param password_reset: The password_reset of this InlineResponse20012Response.  # noqa: E501
        :type: str
        """

        self._password_reset = password_reset

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
        if not isinstance(other, InlineResponse20012Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
