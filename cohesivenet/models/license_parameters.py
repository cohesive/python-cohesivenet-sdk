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


class LicenseParameters(object):
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
        'subnet': 'str',
        'controllers': 'list[str]',
        'clients': 'list[str]',
        'my_manager_vip': 'str'
    }

    attribute_map = {
        'subnet': 'subnet',
        'controllers': 'controllers',
        'clients': 'clients',
        'my_manager_vip': 'my_manager_vip'
    }

    def __init__(self, subnet=None, controllers=None, clients=None, my_manager_vip=None):  # noqa: E501
        """LicenseParameters - a model defined in OpenAPI"""  # noqa: E501

        self._subnet = None
        self._controllers = None
        self._clients = None
        self._my_manager_vip = None
        self.discriminator = None

        if subnet is not None:
            self.subnet = subnet
        if controllers is not None:
            self.controllers = controllers
        if clients is not None:
            self.clients = clients
        if my_manager_vip is not None:
            self.my_manager_vip = my_manager_vip

    @property
    def subnet(self):
        """Gets the subnet of this LicenseParameters.  # noqa: E501


        :return: The subnet of this LicenseParameters.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this LicenseParameters.


        :param subnet: The subnet of this LicenseParameters.  # noqa: E501
        :type: str
        """

        self._subnet = subnet

    @property
    def controllers(self):
        """Gets the controllers of this LicenseParameters.  # noqa: E501

        IP addresses of VNS3 controllers in topology  # noqa: E501

        :return: The controllers of this LicenseParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """Sets the controllers of this LicenseParameters.

        IP addresses of VNS3 controllers in topology  # noqa: E501

        :param controllers: The controllers of this LicenseParameters.  # noqa: E501
        :type: list[str]
        """

        self._controllers = controllers

    @property
    def clients(self):
        """Gets the clients of this LicenseParameters.  # noqa: E501

        IP addresses of clients in topology  # noqa: E501

        :return: The clients of this LicenseParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this LicenseParameters.

        IP addresses of clients in topology  # noqa: E501

        :param clients: The clients of this LicenseParameters.  # noqa: E501
        :type: list[str]
        """

        self._clients = clients

    @property
    def my_manager_vip(self):
        """Gets the my_manager_vip of this LicenseParameters.  # noqa: E501


        :return: The my_manager_vip of this LicenseParameters.  # noqa: E501
        :rtype: str
        """
        return self._my_manager_vip

    @my_manager_vip.setter
    def my_manager_vip(self, my_manager_vip):
        """Sets the my_manager_vip of this LicenseParameters.


        :param my_manager_vip: The my_manager_vip of this LicenseParameters.  # noqa: E501
        :type: str
        """

        self._my_manager_vip = my_manager_vip

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
        if not isinstance(other, LicenseParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other