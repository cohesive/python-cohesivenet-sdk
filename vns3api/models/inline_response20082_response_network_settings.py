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


class InlineResponse20082ResponseNetworkSettings(object):
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
        'ip_address': 'str',
        'ip_prefix_len': 'int',
        'gateway': 'str',
        'bridge': 'str',
        'port_mapping': 'dict(str, object)',
        'ports': 'dict(str, object)'
    }

    attribute_map = {
        'ip_address': 'IPAddress',
        'ip_prefix_len': 'IPPrefixLen',
        'gateway': 'Gateway',
        'bridge': 'Bridge',
        'port_mapping': 'PortMapping',
        'ports': 'Ports'
    }

    def __init__(self, ip_address=None, ip_prefix_len=None, gateway=None, bridge=None, port_mapping=None, ports=None):  # noqa: E501
        """InlineResponse20082ResponseNetworkSettings - a model defined in OpenAPI"""  # noqa: E501

        self._ip_address = None
        self._ip_prefix_len = None
        self._gateway = None
        self._bridge = None
        self._port_mapping = None
        self._ports = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        if ip_prefix_len is not None:
            self.ip_prefix_len = ip_prefix_len
        if gateway is not None:
            self.gateway = gateway
        if bridge is not None:
            self.bridge = bridge
        self.port_mapping = port_mapping
        self.ports = ports

    @property
    def ip_address(self):
        """Gets the ip_address of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501


        :return: The ip_address of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this InlineResponse20082ResponseNetworkSettings.


        :param ip_address: The ip_address of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ip_prefix_len(self):
        """Gets the ip_prefix_len of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501


        :return: The ip_prefix_len of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :rtype: int
        """
        return self._ip_prefix_len

    @ip_prefix_len.setter
    def ip_prefix_len(self, ip_prefix_len):
        """Sets the ip_prefix_len of this InlineResponse20082ResponseNetworkSettings.


        :param ip_prefix_len: The ip_prefix_len of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :type: int
        """

        self._ip_prefix_len = ip_prefix_len

    @property
    def gateway(self):
        """Gets the gateway of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501


        :return: The gateway of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this InlineResponse20082ResponseNetworkSettings.


        :param gateway: The gateway of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def bridge(self):
        """Gets the bridge of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501


        :return: The bridge of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :rtype: str
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this InlineResponse20082ResponseNetworkSettings.


        :param bridge: The bridge of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :type: str
        """

        self._bridge = bridge

    @property
    def port_mapping(self):
        """Gets the port_mapping of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501


        :return: The port_mapping of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._port_mapping

    @port_mapping.setter
    def port_mapping(self, port_mapping):
        """Sets the port_mapping of this InlineResponse20082ResponseNetworkSettings.


        :param port_mapping: The port_mapping of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :type: dict(str, object)
        """

        self._port_mapping = port_mapping

    @property
    def ports(self):
        """Gets the ports of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501


        :return: The ports of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this InlineResponse20082ResponseNetworkSettings.


        :param ports: The ports of this InlineResponse20082ResponseNetworkSettings.  # noqa: E501
        :type: dict(str, object)
        """

        self._ports = ports

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
        if not isinstance(other, InlineResponse20082ResponseNetworkSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other