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


class InlineResponse20090Response(object):
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
        'sync_uuid': 'str',
        'sync_status': 'str',
        'sync_timestamp': 'datetime'
    }

    attribute_map = {
        'sync_uuid': 'sync_uuid',
        'sync_status': 'sync_status',
        'sync_timestamp': 'sync_timestamp'
    }

    def __init__(self, sync_uuid=None, sync_status=None, sync_timestamp=None):  # noqa: E501
        """InlineResponse20090Response - a model defined in OpenAPI"""  # noqa: E501

        self._sync_uuid = None
        self._sync_status = None
        self._sync_timestamp = None
        self.discriminator = None

        if sync_uuid is not None:
            self.sync_uuid = sync_uuid
        if sync_status is not None:
            self.sync_status = sync_status
        if sync_timestamp is not None:
            self.sync_timestamp = sync_timestamp

    @property
    def sync_uuid(self):
        """Gets the sync_uuid of this InlineResponse20090Response.  # noqa: E501


        :return: The sync_uuid of this InlineResponse20090Response.  # noqa: E501
        :rtype: str
        """
        return self._sync_uuid

    @sync_uuid.setter
    def sync_uuid(self, sync_uuid):
        """Sets the sync_uuid of this InlineResponse20090Response.


        :param sync_uuid: The sync_uuid of this InlineResponse20090Response.  # noqa: E501
        :type: str
        """

        self._sync_uuid = sync_uuid

    @property
    def sync_status(self):
        """Gets the sync_status of this InlineResponse20090Response.  # noqa: E501


        :return: The sync_status of this InlineResponse20090Response.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this InlineResponse20090Response.


        :param sync_status: The sync_status of this InlineResponse20090Response.  # noqa: E501
        :type: str
        """

        self._sync_status = sync_status

    @property
    def sync_timestamp(self):
        """Gets the sync_timestamp of this InlineResponse20090Response.  # noqa: E501


        :return: The sync_timestamp of this InlineResponse20090Response.  # noqa: E501
        :rtype: datetime
        """
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, sync_timestamp):
        """Sets the sync_timestamp of this InlineResponse20090Response.


        :param sync_timestamp: The sync_timestamp of this InlineResponse20090Response.  # noqa: E501
        :type: datetime
        """

        self._sync_timestamp = sync_timestamp

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
        if not isinstance(other, InlineResponse20090Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
