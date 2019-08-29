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
        'endpoint_name': 'str',
        'description': 'str',
        'ip_internal': 'str',
        'mtu': 'int',
        'enabled': 'bool',
        'mask_bits': 'str',
        'gateway': 'str',
        'system_default': 'bool',
        'local_connection_ip': 'str',
        'remote_connection_ip': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'endpoint_name': 'endpoint_name',
        'description': 'description',
        'ip_internal': 'ip_internal',
        'mtu': 'mtu',
        'enabled': 'enabled',
        'mask_bits': 'mask_bits',
        'gateway': 'gateway',
        'system_default': 'system_default',
        'local_connection_ip': 'local_connection_ip',
        'remote_connection_ip': 'remote_connection_ip',
        'ttl': 'ttl'
    }

    def __init__(self, endpoint_name=None, description=None, ip_internal=None, mtu=None, enabled=False, mask_bits=None, gateway=None, system_default=False, local_connection_ip=None, remote_connection_ip=None, ttl=255):  # noqa: E501
        """InlineObject43 - a model defined in OpenAPI"""  # noqa: E501

        self._endpoint_name = None
        self._description = None
        self._ip_internal = None
        self._mtu = None
        self._enabled = None
        self._mask_bits = None
        self._gateway = None
        self._system_default = None
        self._local_connection_ip = None
        self._remote_connection_ip = None
        self._ttl = None
        self.discriminator = None

        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if description is not None:
            self.description = description
        if ip_internal is not None:
            self.ip_internal = ip_internal
        if mtu is not None:
            self.mtu = mtu
        if enabled is not None:
            self.enabled = enabled
        if mask_bits is not None:
            self.mask_bits = mask_bits
        self.gateway = gateway
        if system_default is not None:
            self.system_default = system_default
        if local_connection_ip is not None:
            self.local_connection_ip = local_connection_ip
        if remote_connection_ip is not None:
            self.remote_connection_ip = remote_connection_ip
        if ttl is not None:
            self.ttl = ttl

    @property
    def endpoint_name(self):
        """Gets the endpoint_name of this InlineObject43.  # noqa: E501


        :return: The endpoint_name of this InlineObject43.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """Sets the endpoint_name of this InlineObject43.


        :param endpoint_name: The endpoint_name of this InlineObject43.  # noqa: E501
        :type: str
        """

        self._endpoint_name = endpoint_name

    @property
    def description(self):
        """Gets the description of this InlineObject43.  # noqa: E501


        :return: The description of this InlineObject43.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject43.


        :param description: The description of this InlineObject43.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_internal(self):
        """Gets the ip_internal of this InlineObject43.  # noqa: E501


        :return: The ip_internal of this InlineObject43.  # noqa: E501
        :rtype: str
        """
        return self._ip_internal

    @ip_internal.setter
    def ip_internal(self, ip_internal):
        """Sets the ip_internal of this InlineObject43.


        :param ip_internal: The ip_internal of this InlineObject43.  # noqa: E501
        :type: str
        """

        self._ip_internal = ip_internal

    @property
    def mtu(self):
        """Gets the mtu of this InlineObject43.  # noqa: E501


        :return: The mtu of this InlineObject43.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this InlineObject43.


        :param mtu: The mtu of this InlineObject43.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def enabled(self):
        """Gets the enabled of this InlineObject43.  # noqa: E501


        :return: The enabled of this InlineObject43.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InlineObject43.


        :param enabled: The enabled of this InlineObject43.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def mask_bits(self):
        """Gets the mask_bits of this InlineObject43.  # noqa: E501


        :return: The mask_bits of this InlineObject43.  # noqa: E501
        :rtype: str
        """
        return self._mask_bits

    @mask_bits.setter
    def mask_bits(self, mask_bits):
        """Sets the mask_bits of this InlineObject43.


        :param mask_bits: The mask_bits of this InlineObject43.  # noqa: E501
        :type: str
        """

        self._mask_bits = mask_bits

    @property
    def gateway(self):
        """Gets the gateway of this InlineObject43.  # noqa: E501


        :return: The gateway of this InlineObject43.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this InlineObject43.


        :param gateway: The gateway of this InlineObject43.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def system_default(self):
        """Gets the system_default of this InlineObject43.  # noqa: E501


        :return: The system_default of this InlineObject43.  # noqa: E501
        :rtype: bool
        """
        return self._system_default

    @system_default.setter
    def system_default(self, system_default):
        """Sets the system_default of this InlineObject43.


        :param system_default: The system_default of this InlineObject43.  # noqa: E501
        :type: bool
        """

        self._system_default = system_default

    @property
    def local_connection_ip(self):
        """Gets the local_connection_ip of this InlineObject43.  # noqa: E501


        :return: The local_connection_ip of this InlineObject43.  # noqa: E501
        :rtype: str
        """
        return self._local_connection_ip

    @local_connection_ip.setter
    def local_connection_ip(self, local_connection_ip):
        """Sets the local_connection_ip of this InlineObject43.


        :param local_connection_ip: The local_connection_ip of this InlineObject43.  # noqa: E501
        :type: str
        """

        self._local_connection_ip = local_connection_ip

    @property
    def remote_connection_ip(self):
        """Gets the remote_connection_ip of this InlineObject43.  # noqa: E501


        :return: The remote_connection_ip of this InlineObject43.  # noqa: E501
        :rtype: str
        """
        return self._remote_connection_ip

    @remote_connection_ip.setter
    def remote_connection_ip(self, remote_connection_ip):
        """Sets the remote_connection_ip of this InlineObject43.


        :param remote_connection_ip: The remote_connection_ip of this InlineObject43.  # noqa: E501
        :type: str
        """

        self._remote_connection_ip = remote_connection_ip

    @property
    def ttl(self):
        """Gets the ttl of this InlineObject43.  # noqa: E501


        :return: The ttl of this InlineObject43.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this InlineObject43.


        :param ttl: The ttl of this InlineObject43.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

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