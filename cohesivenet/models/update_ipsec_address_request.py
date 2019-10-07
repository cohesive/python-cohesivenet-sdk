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


class UpdateIpsecAddressRequest(object):
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
        'ipsec_local_address': 'str'
    }

    attribute_map = {
        'ipsec_local_address': 'ipsec_local_address'
    }

    def __init__(self, ipsec_local_address=None):  # noqa: E501
        """UpdateIpsecAddressRequest - a model defined in OpenAPI"""  # noqa: E501

        self._ipsec_local_address = None
        self.discriminator = None

        self.ipsec_local_address = ipsec_local_address

    @property
    def ipsec_local_address(self):
        """Gets the ipsec_local_address of this UpdateIpsecAddressRequest.  # noqa: E501

        This is effectively a \"cloud NAT\" address, since you don't know what your LAN address  will be between invocations in a cloud, this address can be used by remote endpoints  as your \"behind a NAT\" address, sometimes referred to Peer or IKE ID, if needed (e.g. Watchguard or Juniper). It can ALSO be thought of even more simply as an IPsec \"loopback\" interface that you can use to terminate traffic.   # noqa: E501

        :return: The ipsec_local_address of this UpdateIpsecAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipsec_local_address

    @ipsec_local_address.setter
    def ipsec_local_address(self, ipsec_local_address):
        """Sets the ipsec_local_address of this UpdateIpsecAddressRequest.

        This is effectively a \"cloud NAT\" address, since you don't know what your LAN address  will be between invocations in a cloud, this address can be used by remote endpoints  as your \"behind a NAT\" address, sometimes referred to Peer or IKE ID, if needed (e.g. Watchguard or Juniper). It can ALSO be thought of even more simply as an IPsec \"loopback\" interface that you can use to terminate traffic.   # noqa: E501

        :param ipsec_local_address: The ipsec_local_address of this UpdateIpsecAddressRequest.  # noqa: E501
        :type: str
        """
        if ipsec_local_address is None:
            raise ValueError("Invalid value for `ipsec_local_address`, must not be `None`")  # noqa: E501

        self._ipsec_local_address = ipsec_local_address

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
        if not isinstance(other, UpdateIpsecAddressRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other