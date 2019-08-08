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


class IpsecTunnelParams(object):
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
        'phase2': 'str',
        'outbound_spi': 'str',
        'inbound_spi': 'str',
        'esp_time_remaining': 'str',
        'esp_port': 'str',
        'phase2_algo': 'str',
        'phase2_hash': 'str',
        'nat_t': 'str',
        'dpd': 'str',
        'phase1': 'str',
        'isakmp_port': 'str',
        'phase1_prf': 'str',
        'phase1_dh_group': 'int'
    }

    attribute_map = {
        'phase2': 'phase2',
        'outbound_spi': 'outbound_spi',
        'inbound_spi': 'inbound_spi',
        'esp_time_remaining': 'esp_time_remaining',
        'esp_port': 'esp_port',
        'phase2_algo': 'phase2_algo',
        'phase2_hash': 'phase2_hash',
        'nat_t': 'nat_t',
        'dpd': 'dpd',
        'phase1': 'phase1',
        'isakmp_port': 'isakmp_port',
        'phase1_prf': 'phase1_prf',
        'phase1_dh_group': 'phase1_dh_group'
    }

    def __init__(self, phase2=None, outbound_spi=None, inbound_spi=None, esp_time_remaining=None, esp_port=None, phase2_algo=None, phase2_hash=None, nat_t=None, dpd=None, phase1=None, isakmp_port=None, phase1_prf=None, phase1_dh_group=None):  # noqa: E501
        """IpsecTunnelParams - a model defined in OpenAPI"""  # noqa: E501

        self._phase2 = None
        self._outbound_spi = None
        self._inbound_spi = None
        self._esp_time_remaining = None
        self._esp_port = None
        self._phase2_algo = None
        self._phase2_hash = None
        self._nat_t = None
        self._dpd = None
        self._phase1 = None
        self._isakmp_port = None
        self._phase1_prf = None
        self._phase1_dh_group = None
        self.discriminator = None

        if phase2 is not None:
            self.phase2 = phase2
        if outbound_spi is not None:
            self.outbound_spi = outbound_spi
        if inbound_spi is not None:
            self.inbound_spi = inbound_spi
        if esp_time_remaining is not None:
            self.esp_time_remaining = esp_time_remaining
        if esp_port is not None:
            self.esp_port = esp_port
        if phase2_algo is not None:
            self.phase2_algo = phase2_algo
        if phase2_hash is not None:
            self.phase2_hash = phase2_hash
        if nat_t is not None:
            self.nat_t = nat_t
        if dpd is not None:
            self.dpd = dpd
        if phase1 is not None:
            self.phase1 = phase1
        if isakmp_port is not None:
            self.isakmp_port = isakmp_port
        if phase1_prf is not None:
            self.phase1_prf = phase1_prf
        if phase1_dh_group is not None:
            self.phase1_dh_group = phase1_dh_group

    @property
    def phase2(self):
        """Gets the phase2 of this IpsecTunnelParams.  # noqa: E501


        :return: The phase2 of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._phase2

    @phase2.setter
    def phase2(self, phase2):
        """Sets the phase2 of this IpsecTunnelParams.


        :param phase2: The phase2 of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._phase2 = phase2

    @property
    def outbound_spi(self):
        """Gets the outbound_spi of this IpsecTunnelParams.  # noqa: E501


        :return: The outbound_spi of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._outbound_spi

    @outbound_spi.setter
    def outbound_spi(self, outbound_spi):
        """Sets the outbound_spi of this IpsecTunnelParams.


        :param outbound_spi: The outbound_spi of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._outbound_spi = outbound_spi

    @property
    def inbound_spi(self):
        """Gets the inbound_spi of this IpsecTunnelParams.  # noqa: E501


        :return: The inbound_spi of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._inbound_spi

    @inbound_spi.setter
    def inbound_spi(self, inbound_spi):
        """Sets the inbound_spi of this IpsecTunnelParams.


        :param inbound_spi: The inbound_spi of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._inbound_spi = inbound_spi

    @property
    def esp_time_remaining(self):
        """Gets the esp_time_remaining of this IpsecTunnelParams.  # noqa: E501


        :return: The esp_time_remaining of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._esp_time_remaining

    @esp_time_remaining.setter
    def esp_time_remaining(self, esp_time_remaining):
        """Sets the esp_time_remaining of this IpsecTunnelParams.


        :param esp_time_remaining: The esp_time_remaining of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._esp_time_remaining = esp_time_remaining

    @property
    def esp_port(self):
        """Gets the esp_port of this IpsecTunnelParams.  # noqa: E501


        :return: The esp_port of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._esp_port

    @esp_port.setter
    def esp_port(self, esp_port):
        """Sets the esp_port of this IpsecTunnelParams.


        :param esp_port: The esp_port of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._esp_port = esp_port

    @property
    def phase2_algo(self):
        """Gets the phase2_algo of this IpsecTunnelParams.  # noqa: E501


        :return: The phase2_algo of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._phase2_algo

    @phase2_algo.setter
    def phase2_algo(self, phase2_algo):
        """Sets the phase2_algo of this IpsecTunnelParams.


        :param phase2_algo: The phase2_algo of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._phase2_algo = phase2_algo

    @property
    def phase2_hash(self):
        """Gets the phase2_hash of this IpsecTunnelParams.  # noqa: E501


        :return: The phase2_hash of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._phase2_hash

    @phase2_hash.setter
    def phase2_hash(self, phase2_hash):
        """Sets the phase2_hash of this IpsecTunnelParams.


        :param phase2_hash: The phase2_hash of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._phase2_hash = phase2_hash

    @property
    def nat_t(self):
        """Gets the nat_t of this IpsecTunnelParams.  # noqa: E501


        :return: The nat_t of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._nat_t

    @nat_t.setter
    def nat_t(self, nat_t):
        """Sets the nat_t of this IpsecTunnelParams.


        :param nat_t: The nat_t of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._nat_t = nat_t

    @property
    def dpd(self):
        """Gets the dpd of this IpsecTunnelParams.  # noqa: E501


        :return: The dpd of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._dpd

    @dpd.setter
    def dpd(self, dpd):
        """Sets the dpd of this IpsecTunnelParams.


        :param dpd: The dpd of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._dpd = dpd

    @property
    def phase1(self):
        """Gets the phase1 of this IpsecTunnelParams.  # noqa: E501


        :return: The phase1 of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._phase1

    @phase1.setter
    def phase1(self, phase1):
        """Sets the phase1 of this IpsecTunnelParams.


        :param phase1: The phase1 of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._phase1 = phase1

    @property
    def isakmp_port(self):
        """Gets the isakmp_port of this IpsecTunnelParams.  # noqa: E501


        :return: The isakmp_port of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._isakmp_port

    @isakmp_port.setter
    def isakmp_port(self, isakmp_port):
        """Sets the isakmp_port of this IpsecTunnelParams.


        :param isakmp_port: The isakmp_port of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._isakmp_port = isakmp_port

    @property
    def phase1_prf(self):
        """Gets the phase1_prf of this IpsecTunnelParams.  # noqa: E501


        :return: The phase1_prf of this IpsecTunnelParams.  # noqa: E501
        :rtype: str
        """
        return self._phase1_prf

    @phase1_prf.setter
    def phase1_prf(self, phase1_prf):
        """Sets the phase1_prf of this IpsecTunnelParams.


        :param phase1_prf: The phase1_prf of this IpsecTunnelParams.  # noqa: E501
        :type: str
        """

        self._phase1_prf = phase1_prf

    @property
    def phase1_dh_group(self):
        """Gets the phase1_dh_group of this IpsecTunnelParams.  # noqa: E501


        :return: The phase1_dh_group of this IpsecTunnelParams.  # noqa: E501
        :rtype: int
        """
        return self._phase1_dh_group

    @phase1_dh_group.setter
    def phase1_dh_group(self, phase1_dh_group):
        """Sets the phase1_dh_group of this IpsecTunnelParams.


        :param phase1_dh_group: The phase1_dh_group of this IpsecTunnelParams.  # noqa: E501
        :type: int
        """

        self._phase1_dh_group = phase1_dh_group

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
        if not isinstance(other, IpsecTunnelParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
