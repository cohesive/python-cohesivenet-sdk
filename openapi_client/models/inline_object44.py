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


class InlineObject44(object):
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
        'uuid': 'str',
        'primary_ip': 'str',
        'backup_ip': 'str',
        'ms_ip': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'primary_ip': 'primary_ip',
        'backup_ip': 'backup_ip',
        'ms_ip': 'ms_ip'
    }

    def __init__(self, uuid=None, primary_ip=None, backup_ip=None, ms_ip=None):  # noqa: E501
        """InlineObject44 - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._primary_ip = None
        self._backup_ip = None
        self._ms_ip = None
        self.discriminator = None

        self.uuid = uuid
        self.primary_ip = primary_ip
        self.backup_ip = backup_ip
        self.ms_ip = ms_ip

    @property
    def uuid(self):
        """Gets the uuid of this InlineObject44.  # noqa: E501


        :return: The uuid of this InlineObject44.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineObject44.


        :param uuid: The uuid of this InlineObject44.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def primary_ip(self):
        """Gets the primary_ip of this InlineObject44.  # noqa: E501


        :return: The primary_ip of this InlineObject44.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this InlineObject44.


        :param primary_ip: The primary_ip of this InlineObject44.  # noqa: E501
        :type: str
        """
        if primary_ip is None:
            raise ValueError("Invalid value for `primary_ip`, must not be `None`")  # noqa: E501

        self._primary_ip = primary_ip

    @property
    def backup_ip(self):
        """Gets the backup_ip of this InlineObject44.  # noqa: E501

        Controller to be used as backup  # noqa: E501

        :return: The backup_ip of this InlineObject44.  # noqa: E501
        :rtype: str
        """
        return self._backup_ip

    @backup_ip.setter
    def backup_ip(self, backup_ip):
        """Sets the backup_ip of this InlineObject44.

        Controller to be used as backup  # noqa: E501

        :param backup_ip: The backup_ip of this InlineObject44.  # noqa: E501
        :type: str
        """
        if backup_ip is None:
            raise ValueError("Invalid value for `backup_ip`, must not be `None`")  # noqa: E501

        self._backup_ip = backup_ip

    @property
    def ms_ip(self):
        """Gets the ms_ip of this InlineObject44.  # noqa: E501

        IP of VNS3 MS managing HA  # noqa: E501

        :return: The ms_ip of this InlineObject44.  # noqa: E501
        :rtype: str
        """
        return self._ms_ip

    @ms_ip.setter
    def ms_ip(self, ms_ip):
        """Sets the ms_ip of this InlineObject44.

        IP of VNS3 MS managing HA  # noqa: E501

        :param ms_ip: The ms_ip of this InlineObject44.  # noqa: E501
        :type: str
        """
        if ms_ip is None:
            raise ValueError("Invalid value for `ms_ip`, must not be `None`")  # noqa: E501

        self._ms_ip = ms_ip

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
        if not isinstance(other, InlineObject44):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
