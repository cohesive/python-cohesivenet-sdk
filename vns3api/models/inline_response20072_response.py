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


class InlineResponse20072Response(object):
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
        'latest_snapshot': 'str',
        'snapshots': 'dict(str, object)'
    }

    attribute_map = {
        'latest_snapshot': 'latest_snapshot',
        'snapshots': 'snapshots'
    }

    def __init__(self, latest_snapshot=None, snapshots=None):  # noqa: E501
        """InlineResponse20072Response - a model defined in OpenAPI"""  # noqa: E501

        self._latest_snapshot = None
        self._snapshots = None
        self.discriminator = None

        if latest_snapshot is not None:
            self.latest_snapshot = latest_snapshot
        if snapshots is not None:
            self.snapshots = snapshots

    @property
    def latest_snapshot(self):
        """Gets the latest_snapshot of this InlineResponse20072Response.  # noqa: E501

        Name of the latest snapshot taken  # noqa: E501

        :return: The latest_snapshot of this InlineResponse20072Response.  # noqa: E501
        :rtype: str
        """
        return self._latest_snapshot

    @latest_snapshot.setter
    def latest_snapshot(self, latest_snapshot):
        """Sets the latest_snapshot of this InlineResponse20072Response.

        Name of the latest snapshot taken  # noqa: E501

        :param latest_snapshot: The latest_snapshot of this InlineResponse20072Response.  # noqa: E501
        :type: str
        """

        self._latest_snapshot = latest_snapshot

    @property
    def snapshots(self):
        """Gets the snapshots of this InlineResponse20072Response.  # noqa: E501


        :return: The snapshots of this InlineResponse20072Response.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this InlineResponse20072Response.


        :param snapshots: The snapshots of this InlineResponse20072Response.  # noqa: E501
        :type: dict(str, object)
        """

        self._snapshots = snapshots

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
        if not isinstance(other, InlineResponse20072Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
