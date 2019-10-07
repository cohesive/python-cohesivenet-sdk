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


class UpdateKeysetRequest(object):
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
        'source': 'str',
        'token': 'str',
        'topology_name': 'str',
        'sealed_network': 'bool'
    }

    attribute_map = {
        'source': 'source',
        'token': 'token',
        'topology_name': 'topology_name',
        'sealed_network': 'sealed_network'
    }

    def __init__(self, source=None, token=None, topology_name=None, sealed_network=None):  # noqa: E501
        """UpdateKeysetRequest - a model defined in OpenAPI"""  # noqa: E501

        self._source = None
        self._token = None
        self._topology_name = None
        self._sealed_network = None
        self.discriminator = None

        if source is not None:
            self.source = source
        self.token = token
        if topology_name is not None:
            self.topology_name = topology_name
        if sealed_network is not None:
            self.sealed_network = sealed_network

    @property
    def source(self):
        """Gets the source of this UpdateKeysetRequest.  # noqa: E501

        If provided, fetches keyset from source manager  # noqa: E501

        :return: The source of this UpdateKeysetRequest.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UpdateKeysetRequest.

        If provided, fetches keyset from source manager  # noqa: E501

        :param source: The source of this UpdateKeysetRequest.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def token(self):
        """Gets the token of this UpdateKeysetRequest.  # noqa: E501

        Arbitrary key used to help randomize the checksum, it must be identical for each manager in a topology.  # noqa: E501

        :return: The token of this UpdateKeysetRequest.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this UpdateKeysetRequest.

        Arbitrary key used to help randomize the checksum, it must be identical for each manager in a topology.  # noqa: E501

        :param token: The token of this UpdateKeysetRequest.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def topology_name(self):
        """Gets the topology_name of this UpdateKeysetRequest.  # noqa: E501

        Name for the topology  # noqa: E501

        :return: The topology_name of this UpdateKeysetRequest.  # noqa: E501
        :rtype: str
        """
        return self._topology_name

    @topology_name.setter
    def topology_name(self, topology_name):
        """Sets the topology_name of this UpdateKeysetRequest.

        Name for the topology  # noqa: E501

        :param topology_name: The topology_name of this UpdateKeysetRequest.  # noqa: E501
        :type: str
        """

        self._topology_name = topology_name

    @property
    def sealed_network(self):
        """Gets the sealed_network of this UpdateKeysetRequest.  # noqa: E501

        UPDATEME  # noqa: E501

        :return: The sealed_network of this UpdateKeysetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sealed_network

    @sealed_network.setter
    def sealed_network(self, sealed_network):
        """Sets the sealed_network of this UpdateKeysetRequest.

        UPDATEME  # noqa: E501

        :param sealed_network: The sealed_network of this UpdateKeysetRequest.  # noqa: E501
        :type: bool
        """

        self._sealed_network = sealed_network

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
        if not isinstance(other, UpdateKeysetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other