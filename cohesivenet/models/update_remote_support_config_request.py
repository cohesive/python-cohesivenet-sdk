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


class UpdateRemoteSupportConfigRequest(object):
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
    openapi_types = {"enabled": "bool", "revoke_credential": "bool"}

    attribute_map = {"enabled": "enabled", "revoke_credential": "revoke_credential"}

    def __init__(self, enabled=None, revoke_credential=None):  # noqa: E501
        """UpdateRemoteSupportConfigRequest - a model defined in OpenAPI"""  # noqa: E501

        self._enabled = None
        self._revoke_credential = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if revoke_credential is not None:
            self.revoke_credential = revoke_credential

    @property
    def enabled(self):
        """Gets the enabled of this UpdateRemoteSupportConfigRequest.  # noqa: E501

        True if remote support should be enabled  # noqa: E501

        :return: The enabled of this UpdateRemoteSupportConfigRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateRemoteSupportConfigRequest.

        True if remote support should be enabled  # noqa: E501

        :param enabled: The enabled of this UpdateRemoteSupportConfigRequest.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def revoke_credential(self):
        """Gets the revoke_credential of this UpdateRemoteSupportConfigRequest.  # noqa: E501

        True if remote support credential should be revoked  # noqa: E501

        :return: The revoke_credential of this UpdateRemoteSupportConfigRequest.  # noqa: E501
        :rtype: bool
        """
        return self._revoke_credential

    @revoke_credential.setter
    def revoke_credential(self, revoke_credential):
        """Sets the revoke_credential of this UpdateRemoteSupportConfigRequest.

        True if remote support credential should be revoked  # noqa: E501

        :param revoke_credential: The revoke_credential of this UpdateRemoteSupportConfigRequest.  # noqa: E501
        :type: bool
        """

        self._revoke_credential = revoke_credential

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
        if not isinstance(other, UpdateRemoteSupportConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
