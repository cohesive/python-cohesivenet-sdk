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


class HaConfig(object):
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
        "type": "str",
        "status": "str",
        "last_sync": "str",
        "last_sync_update": "str",
        "primary_ip": "str",
        "backup_ip": "str",
    }

    attribute_map = {
        "type": "type",
        "status": "status",
        "last_sync": "last_sync",
        "last_sync_update": "last_sync_update",
        "primary_ip": "primary_ip",
        "backup_ip": "backup_ip",
    }

    def __init__(
        self,
        type=None,
        status=None,
        last_sync=None,
        last_sync_update=None,
        primary_ip=None,
        backup_ip=None,
    ):  # noqa: E501
        """HaConfig - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._status = None
        self._last_sync = None
        self._last_sync_update = None
        self._primary_ip = None
        self._backup_ip = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        self.last_sync = last_sync
        self.last_sync_update = last_sync_update
        self.primary_ip = primary_ip
        self.backup_ip = backup_ip

    @property
    def type(self):
        """Gets the type of this HaConfig.  # noqa: E501

        primary or backup  # noqa: E501

        :return: The type of this HaConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type_str):
        """Sets the type of this HaConfig.

        primary or backup  # noqa: E501

        :param type: The type of this HaConfig.  # noqa: E501
        :type: str
        """
        self._type = type_str

    @property
    def status(self):
        """Gets the status of this HaConfig.  # noqa: E501

        initialised or not initialised  # noqa: E501

        :return: The status of this HaConfig.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HaConfig.

        initialised or not initialised  # noqa: E501

        :param status: The status of this HaConfig.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def last_sync(self):
        """Gets the last_sync of this HaConfig.  # noqa: E501


        :return: The last_sync of this HaConfig.  # noqa: E501
        :rtype: str
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this HaConfig.


        :param last_sync: The last_sync of this HaConfig.  # noqa: E501
        :type: str
        """

        self._last_sync = last_sync

    @property
    def last_sync_update(self):
        """Gets the last_sync_update of this HaConfig.  # noqa: E501


        :return: The last_sync_update of this HaConfig.  # noqa: E501
        :rtype: str
        """
        return self._last_sync_update

    @last_sync_update.setter
    def last_sync_update(self, last_sync_update):
        """Sets the last_sync_update of this HaConfig.


        :param last_sync_update: The last_sync_update of this HaConfig.  # noqa: E501
        :type: str
        """

        self._last_sync_update = last_sync_update

    @property
    def primary_ip(self):
        """Gets the primary_ip of this HaConfig.  # noqa: E501


        :return: The primary_ip of this HaConfig.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this HaConfig.


        :param primary_ip: The primary_ip of this HaConfig.  # noqa: E501
        :type: str
        """

        self._primary_ip = primary_ip

    @property
    def backup_ip(self):
        """Gets the backup_ip of this HaConfig.  # noqa: E501


        :return: The backup_ip of this HaConfig.  # noqa: E501
        :rtype: str
        """
        return self._backup_ip

    @backup_ip.setter
    def backup_ip(self, backup_ip):
        """Sets the backup_ip of this HaConfig.


        :param backup_ip: The backup_ip of this HaConfig.  # noqa: E501
        :type: str
        """

        self._backup_ip = backup_ip

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
        if not isinstance(other, HaConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
