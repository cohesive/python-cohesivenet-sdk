# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API for configuring and retrieving VNS3 controller  # noqa: E501

    The version of the OpenAPI document: 4.7
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineObject34(object):
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
        'rule': 'str',
        'position': 'int'
    }

    attribute_map = {
        'rule': 'rule',
        'position': 'position'
    }

    def __init__(self, rule=None, position=None):  # noqa: E501
        """InlineObject34 - a model defined in OpenAPI"""  # noqa: E501

        self._rule = None
        self._position = None
        self.discriminator = None

        self.rule = rule
        if position is not None:
            self.position = position

    @property
    def rule(self):
        """Gets the rule of this InlineObject34.  # noqa: E501

        New firewall rule string that needs to be compatible with a Linux \"iptables\" statement  # noqa: E501

        :return: The rule of this InlineObject34.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this InlineObject34.

        New firewall rule string that needs to be compatible with a Linux \"iptables\" statement  # noqa: E501

        :param rule: The rule of this InlineObject34.  # noqa: E501
        :type: str
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

    @property
    def position(self):
        """Gets the position of this InlineObject34.  # noqa: E501

        Position which the rule will be inserted in the list of Firewall rules.  Default is 0, which is first in the ruleset   # noqa: E501

        :return: The position of this InlineObject34.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this InlineObject34.

        Position which the rule will be inserted in the list of Firewall rules.  Default is 0, which is first in the ruleset   # noqa: E501

        :param position: The position of this InlineObject34.  # noqa: E501
        :type: int
        """

        self._position = position

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
        if not isinstance(other, InlineObject34):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
