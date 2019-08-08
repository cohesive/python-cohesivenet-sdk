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


class InlineObject43(object):
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
        'discover_new_primary_adapters': 'bool',
        'discover_ips': 'bool',
        'manage_overlay_interfaces': 'bool'
    }

    attribute_map = {
        'discover_new_primary_adapters': 'discover_new_primary_adapters',
        'discover_ips': 'discover_ips',
        'manage_overlay_interfaces': 'manage_overlay_interfaces'
    }

    def __init__(self, discover_new_primary_adapters=None, discover_ips=None, manage_overlay_interfaces=None):  # noqa: E501
        """InlineObject43 - a model defined in OpenAPI"""  # noqa: E501

        self._discover_new_primary_adapters = None
        self._discover_ips = None
        self._manage_overlay_interfaces = None
        self.discriminator = None

        if discover_new_primary_adapters is not None:
            self.discover_new_primary_adapters = discover_new_primary_adapters
        if discover_ips is not None:
            self.discover_ips = discover_ips
        if manage_overlay_interfaces is not None:
            self.manage_overlay_interfaces = manage_overlay_interfaces

    @property
    def discover_new_primary_adapters(self):
        """Gets the discover_new_primary_adapters of this InlineObject43.  # noqa: E501

        Run discovery for new primary adapters  # noqa: E501

        :return: The discover_new_primary_adapters of this InlineObject43.  # noqa: E501
        :rtype: bool
        """
        return self._discover_new_primary_adapters

    @discover_new_primary_adapters.setter
    def discover_new_primary_adapters(self, discover_new_primary_adapters):
        """Sets the discover_new_primary_adapters of this InlineObject43.

        Run discovery for new primary adapters  # noqa: E501

        :param discover_new_primary_adapters: The discover_new_primary_adapters of this InlineObject43.  # noqa: E501
        :type: bool
        """

        self._discover_new_primary_adapters = discover_new_primary_adapters

    @property
    def discover_ips(self):
        """Gets the discover_ips of this InlineObject43.  # noqa: E501


        :return: The discover_ips of this InlineObject43.  # noqa: E501
        :rtype: bool
        """
        return self._discover_ips

    @discover_ips.setter
    def discover_ips(self, discover_ips):
        """Sets the discover_ips of this InlineObject43.


        :param discover_ips: The discover_ips of this InlineObject43.  # noqa: E501
        :type: bool
        """

        self._discover_ips = discover_ips

    @property
    def manage_overlay_interfaces(self):
        """Gets the manage_overlay_interfaces of this InlineObject43.  # noqa: E501


        :return: The manage_overlay_interfaces of this InlineObject43.  # noqa: E501
        :rtype: bool
        """
        return self._manage_overlay_interfaces

    @manage_overlay_interfaces.setter
    def manage_overlay_interfaces(self, manage_overlay_interfaces):
        """Sets the manage_overlay_interfaces of this InlineObject43.


        :param manage_overlay_interfaces: The manage_overlay_interfaces of this InlineObject43.  # noqa: E501
        :type: bool
        """

        self._manage_overlay_interfaces = manage_overlay_interfaces

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
        if not isinstance(other, InlineObject43):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
