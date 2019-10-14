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


class SystemInterface(object):
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
        "id": "int",
        "name": "str",
        "interface_type": "str",
        "description": "str",
        "ip_internal": "str",
        "mtu": "int",
        "enabled": "bool",
        "status": "str",
        "mask_bits": "str",
        "gateway": "str",
        "system_default": "bool",
        "ip_external": "str",
        "tags": "list[str]",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "interface_type": "interface_type",
        "description": "description",
        "ip_internal": "ip_internal",
        "mtu": "mtu",
        "enabled": "enabled",
        "status": "status",
        "mask_bits": "mask_bits",
        "gateway": "gateway",
        "system_default": "system_default",
        "ip_external": "ip_external",
        "tags": "tags",
    }

    def __init__(
        self,
        id=None,
        name=None,
        interface_type=None,
        description=None,
        ip_internal=None,
        mtu=None,
        enabled=None,
        status=None,
        mask_bits=None,
        gateway=None,
        system_default=None,
        ip_external=None,
        tags=None,
    ):  # noqa: E501
        """SystemInterface - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._interface_type = None
        self._description = None
        self._ip_internal = None
        self._mtu = None
        self._enabled = None
        self._status = None
        self._mask_bits = None
        self._gateway = None
        self._system_default = None
        self._ip_external = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if interface_type is not None:
            self.interface_type = interface_type
        if description is not None:
            self.description = description
        if ip_internal is not None:
            self.ip_internal = ip_internal
        if mtu is not None:
            self.mtu = mtu
        if enabled is not None:
            self.enabled = enabled
        if status is not None:
            self.status = status
        if mask_bits is not None:
            self.mask_bits = mask_bits
        self.gateway = gateway
        if system_default is not None:
            self.system_default = system_default
        self.ip_external = ip_external
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this SystemInterface.  # noqa: E501


        :return: The id of this SystemInterface.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SystemInterface.


        :param id: The id of this SystemInterface.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SystemInterface.  # noqa: E501


        :return: The name of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInterface.


        :param name: The name of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def interface_type(self):
        """Gets the interface_type of this SystemInterface.  # noqa: E501

        system or system_virtual  # noqa: E501

        :return: The interface_type of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this SystemInterface.

        system or system_virtual  # noqa: E501

        :param interface_type: The interface_type of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._interface_type = interface_type

    @property
    def description(self):
        """Gets the description of this SystemInterface.  # noqa: E501


        :return: The description of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemInterface.


        :param description: The description of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_internal(self):
        """Gets the ip_internal of this SystemInterface.  # noqa: E501


        :return: The ip_internal of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._ip_internal

    @ip_internal.setter
    def ip_internal(self, ip_internal):
        """Sets the ip_internal of this SystemInterface.


        :param ip_internal: The ip_internal of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._ip_internal = ip_internal

    @property
    def mtu(self):
        """Gets the mtu of this SystemInterface.  # noqa: E501


        :return: The mtu of this SystemInterface.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this SystemInterface.


        :param mtu: The mtu of this SystemInterface.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def enabled(self):
        """Gets the enabled of this SystemInterface.  # noqa: E501


        :return: The enabled of this SystemInterface.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SystemInterface.


        :param enabled: The enabled of this SystemInterface.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def status(self):
        """Gets the status of this SystemInterface.  # noqa: E501

        Availability of interface, Up or Down  # noqa: E501

        :return: The status of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SystemInterface.

        Availability of interface, Up or Down  # noqa: E501

        :param status: The status of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def mask_bits(self):
        """Gets the mask_bits of this SystemInterface.  # noqa: E501


        :return: The mask_bits of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._mask_bits

    @mask_bits.setter
    def mask_bits(self, mask_bits):
        """Sets the mask_bits of this SystemInterface.


        :param mask_bits: The mask_bits of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._mask_bits = mask_bits

    @property
    def gateway(self):
        """Gets the gateway of this SystemInterface.  # noqa: E501


        :return: The gateway of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this SystemInterface.


        :param gateway: The gateway of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def system_default(self):
        """Gets the system_default of this SystemInterface.  # noqa: E501


        :return: The system_default of this SystemInterface.  # noqa: E501
        :rtype: bool
        """
        return self._system_default

    @system_default.setter
    def system_default(self, system_default):
        """Sets the system_default of this SystemInterface.


        :param system_default: The system_default of this SystemInterface.  # noqa: E501
        :type: bool
        """

        self._system_default = system_default

    @property
    def ip_external(self):
        """Gets the ip_external of this SystemInterface.  # noqa: E501


        :return: The ip_external of this SystemInterface.  # noqa: E501
        :rtype: str
        """
        return self._ip_external

    @ip_external.setter
    def ip_external(self, ip_external):
        """Sets the ip_external of this SystemInterface.


        :param ip_external: The ip_external of this SystemInterface.  # noqa: E501
        :type: str
        """

        self._ip_external = ip_external

    @property
    def tags(self):
        """Gets the tags of this SystemInterface.  # noqa: E501


        :return: The tags of this SystemInterface.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SystemInterface.


        :param tags: The tags of this SystemInterface.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, SystemInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
