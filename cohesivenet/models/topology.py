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


class Topology(object):
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
        "clients": "list[OverlayIPAddress]",
        "managers": "list[VNS3Controller]",
        "total_clients": "int",
        "ipsec_max_subnets": "int",
        "ipsec_max_endpoints": "int",
        "license_upgrades": "list[str]",
        "overlay_max_clients": "int",
        "overlay_subnet": "str",
    }

    attribute_map = {
        "clients": "clients",
        "managers": "managers",
        "total_clients": "total_clients",
        "ipsec_max_subnets": "ipsec_max_subnets",
        "ipsec_max_endpoints": "ipsec_max_endpoints",
        "license_upgrades": "license_upgrades",
        "overlay_max_clients": "overlay_max_clients",
        "overlay_subnet": "overlay_subnet",
    }

    def __init__(
        self,
        clients=None,
        managers=None,
        total_clients=None,
        ipsec_max_subnets=None,
        ipsec_max_endpoints=None,
        license_upgrades=None,
        overlay_max_clients=None,
        overlay_subnet=None,
    ):  # noqa: E501
        """Topology - a model defined in OpenAPI"""  # noqa: E501

        self._clients = None
        self._managers = None
        self._total_clients = None
        self._ipsec_max_subnets = None
        self._ipsec_max_endpoints = None
        self._license_upgrades = None
        self._overlay_max_clients = None
        self._overlay_subnet = None
        self.discriminator = None

        if clients is not None:
            self.clients = clients
        if managers is not None:
            self.managers = managers
        if total_clients is not None:
            self.total_clients = total_clients
        if ipsec_max_subnets is not None:
            self.ipsec_max_subnets = ipsec_max_subnets
        if ipsec_max_endpoints is not None:
            self.ipsec_max_endpoints = ipsec_max_endpoints
        if license_upgrades is not None:
            self.license_upgrades = license_upgrades
        if overlay_max_clients is not None:
            self.overlay_max_clients = overlay_max_clients
        if overlay_subnet is not None:
            self.overlay_subnet = overlay_subnet

    @property
    def clients(self):
        """Gets the clients of this Topology.  # noqa: E501

        IPs for clientpacks  # noqa: E501

        :return: The clients of this Topology.  # noqa: E501
        :rtype: list[OverlayIPAddress]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this Topology.

        IPs for clientpacks  # noqa: E501

        :param clients: The clients of this Topology.  # noqa: E501
        :type: list[OverlayIPAddress]
        """

        self._clients = clients

    @property
    def managers(self):
        """Gets the managers of this Topology.  # noqa: E501


        :return: The managers of this Topology.  # noqa: E501
        :rtype: list[VNS3Controller]
        """
        return self._managers

    @managers.setter
    def managers(self, managers):
        """Sets the managers of this Topology.


        :param managers: The managers of this Topology.  # noqa: E501
        :type: list[VNS3Controller]
        """

        self._managers = managers

    @property
    def total_clients(self):
        """Gets the total_clients of this Topology.  # noqa: E501


        :return: The total_clients of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._total_clients

    @total_clients.setter
    def total_clients(self, total_clients):
        """Sets the total_clients of this Topology.


        :param total_clients: The total_clients of this Topology.  # noqa: E501
        :type: int
        """

        self._total_clients = total_clients

    @property
    def ipsec_max_subnets(self):
        """Gets the ipsec_max_subnets of this Topology.  # noqa: E501


        :return: The ipsec_max_subnets of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._ipsec_max_subnets

    @ipsec_max_subnets.setter
    def ipsec_max_subnets(self, ipsec_max_subnets):
        """Sets the ipsec_max_subnets of this Topology.


        :param ipsec_max_subnets: The ipsec_max_subnets of this Topology.  # noqa: E501
        :type: int
        """

        self._ipsec_max_subnets = ipsec_max_subnets

    @property
    def ipsec_max_endpoints(self):
        """Gets the ipsec_max_endpoints of this Topology.  # noqa: E501


        :return: The ipsec_max_endpoints of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._ipsec_max_endpoints

    @ipsec_max_endpoints.setter
    def ipsec_max_endpoints(self, ipsec_max_endpoints):
        """Sets the ipsec_max_endpoints of this Topology.


        :param ipsec_max_endpoints: The ipsec_max_endpoints of this Topology.  # noqa: E501
        :type: int
        """

        self._ipsec_max_endpoints = ipsec_max_endpoints

    @property
    def license_upgrades(self):
        """Gets the license_upgrades of this Topology.  # noqa: E501


        :return: The license_upgrades of this Topology.  # noqa: E501
        :rtype: list[str]
        """
        return self._license_upgrades

    @license_upgrades.setter
    def license_upgrades(self, license_upgrades):
        """Sets the license_upgrades of this Topology.


        :param license_upgrades: The license_upgrades of this Topology.  # noqa: E501
        :type: list[str]
        """

        self._license_upgrades = license_upgrades

    @property
    def overlay_max_clients(self):
        """Gets the overlay_max_clients of this Topology.  # noqa: E501


        :return: The overlay_max_clients of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._overlay_max_clients

    @overlay_max_clients.setter
    def overlay_max_clients(self, overlay_max_clients):
        """Sets the overlay_max_clients of this Topology.


        :param overlay_max_clients: The overlay_max_clients of this Topology.  # noqa: E501
        :type: int
        """

        self._overlay_max_clients = overlay_max_clients

    @property
    def overlay_subnet(self):
        """Gets the overlay_subnet of this Topology.  # noqa: E501

        CIDR for overlay clients  # noqa: E501

        :return: The overlay_subnet of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._overlay_subnet

    @overlay_subnet.setter
    def overlay_subnet(self, overlay_subnet):
        """Sets the overlay_subnet of this Topology.

        CIDR for overlay clients  # noqa: E501

        :param overlay_subnet: The overlay_subnet of this Topology.  # noqa: E501
        :type: str
        """

        self._overlay_subnet = overlay_subnet

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
        if not isinstance(other, Topology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
