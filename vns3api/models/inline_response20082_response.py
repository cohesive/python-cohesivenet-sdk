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


class InlineResponse20082Response(object):
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
        'containers': 'list[InlineResponse20082ResponseContainers]'
    }

    attribute_map = {
        'containers': 'containers'
    }

    def __init__(self, containers=None):  # noqa: E501
        """InlineResponse20082Response - a model defined in OpenAPI"""  # noqa: E501

        self._containers = None
        self.discriminator = None

        if containers is not None:
            self.containers = containers

    @property
    def containers(self):
        """Gets the containers of this InlineResponse20082Response.  # noqa: E501


        :return: The containers of this InlineResponse20082Response.  # noqa: E501
        :rtype: list[InlineResponse20082ResponseContainers]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this InlineResponse20082Response.


        :param containers: The containers of this InlineResponse20082Response.  # noqa: E501
        :type: list[InlineResponse20082ResponseContainers]
        """

        self._containers = containers

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
        if not isinstance(other, InlineResponse20082Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
