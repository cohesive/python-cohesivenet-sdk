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


class Route(object):
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
        'netmask': 'str',
        'id': 'int',
        'cidr': 'str',
        'interface': 'str',
        'description': 'str',
        'advertise': 'bool',
        'metric': 'int',
        'gateway': 'str'
    }

    attribute_map = {
        'netmask': 'netmask',
        'id': 'id',
        'cidr': 'cidr',
        'interface': 'interface',
        'description': 'description',
        'advertise': 'advertise',
        'metric': 'metric',
        'gateway': 'gateway'
    }

    def __init__(self, netmask=None, id=None, cidr=None, interface=None, description=None, advertise=None, metric=None, gateway=None):  # noqa: E501
        """Route - a model defined in OpenAPI"""  # noqa: E501

        self._netmask = None
        self._id = None
        self._cidr = None
        self._interface = None
        self._description = None
        self._advertise = None
        self._metric = None
        self._gateway = None
        self.discriminator = None

        if netmask is not None:
            self.netmask = netmask
        if id is not None:
            self.id = id
        if cidr is not None:
            self.cidr = cidr
        if interface is not None:
            self.interface = interface
        if description is not None:
            self.description = description
        if advertise is not None:
            self.advertise = advertise
        if metric is not None:
            self.metric = metric
        if gateway is not None:
            self.gateway = gateway

    @property
    def netmask(self):
        """Gets the netmask of this Route.  # noqa: E501


        :return: The netmask of this Route.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this Route.


        :param netmask: The netmask of this Route.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

    @property
    def id(self):
        """Gets the id of this Route.  # noqa: E501


        :return: The id of this Route.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Route.


        :param id: The id of this Route.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def cidr(self):
        """Gets the cidr of this Route.  # noqa: E501


        :return: The cidr of this Route.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Route.


        :param cidr: The cidr of this Route.  # noqa: E501
        :type: str
        """

        self._cidr = cidr

    @property
    def interface(self):
        """Gets the interface of this Route.  # noqa: E501


        :return: The interface of this Route.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this Route.


        :param interface: The interface of this Route.  # noqa: E501
        :type: str
        """

        self._interface = interface

    @property
    def description(self):
        """Gets the description of this Route.  # noqa: E501


        :return: The description of this Route.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Route.


        :param description: The description of this Route.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def advertise(self):
        """Gets the advertise of this Route.  # noqa: E501


        :return: The advertise of this Route.  # noqa: E501
        :rtype: bool
        """
        return self._advertise

    @advertise.setter
    def advertise(self, advertise):
        """Sets the advertise of this Route.


        :param advertise: The advertise of this Route.  # noqa: E501
        :type: bool
        """

        self._advertise = advertise

    @property
    def metric(self):
        """Gets the metric of this Route.  # noqa: E501


        :return: The metric of this Route.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Route.


        :param metric: The metric of this Route.  # noqa: E501
        :type: int
        """

        self._metric = metric

    @property
    def gateway(self):
        """Gets the gateway of this Route.  # noqa: E501


        :return: The gateway of this Route.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this Route.


        :param gateway: The gateway of this Route.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

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
        if not isinstance(other, Route):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
