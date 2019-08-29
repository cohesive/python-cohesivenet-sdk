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


class InlineResponse20019Response(object):
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
        'in_progress': 'bool',
        'running': 'int',
        'keyset_present': 'bool',
        'checksum': 'str',
        'created_at': 'str',
        'created_at_i': 'int',
        'started_at': 'str',
        'started_at_i': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'in_progress': 'in_progress',
        'running': 'running',
        'keyset_present': 'keyset_present',
        'checksum': 'checksum',
        'created_at': 'created_at',
        'created_at_i': 'created_at_i',
        'started_at': 'started_at',
        'started_at_i': 'started_at_i',
        'uuid': 'uuid'
    }

    def __init__(self, in_progress=None, running=None, keyset_present=None, checksum=None, created_at=None, created_at_i=None, started_at=None, started_at_i=None, uuid=None):  # noqa: E501
        """InlineResponse20019Response - a model defined in OpenAPI"""  # noqa: E501

        self._in_progress = None
        self._running = None
        self._keyset_present = None
        self._checksum = None
        self._created_at = None
        self._created_at_i = None
        self._started_at = None
        self._started_at_i = None
        self._uuid = None
        self.discriminator = None

        if in_progress is not None:
            self.in_progress = in_progress
        if running is not None:
            self.running = running
        if keyset_present is not None:
            self.keyset_present = keyset_present
        if checksum is not None:
            self.checksum = checksum
        if created_at is not None:
            self.created_at = created_at
        if created_at_i is not None:
            self.created_at_i = created_at_i
        if started_at is not None:
            self.started_at = started_at
        if started_at_i is not None:
            self.started_at_i = started_at_i
        if uuid is not None:
            self.uuid = uuid

    @property
    def in_progress(self):
        """Gets the in_progress of this InlineResponse20019Response.  # noqa: E501


        :return: The in_progress of this InlineResponse20019Response.  # noqa: E501
        :rtype: bool
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this InlineResponse20019Response.


        :param in_progress: The in_progress of this InlineResponse20019Response.  # noqa: E501
        :type: bool
        """

        self._in_progress = in_progress

    @property
    def running(self):
        """Gets the running of this InlineResponse20019Response.  # noqa: E501


        :return: The running of this InlineResponse20019Response.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this InlineResponse20019Response.


        :param running: The running of this InlineResponse20019Response.  # noqa: E501
        :type: int
        """

        self._running = running

    @property
    def keyset_present(self):
        """Gets the keyset_present of this InlineResponse20019Response.  # noqa: E501


        :return: The keyset_present of this InlineResponse20019Response.  # noqa: E501
        :rtype: bool
        """
        return self._keyset_present

    @keyset_present.setter
    def keyset_present(self, keyset_present):
        """Sets the keyset_present of this InlineResponse20019Response.


        :param keyset_present: The keyset_present of this InlineResponse20019Response.  # noqa: E501
        :type: bool
        """

        self._keyset_present = keyset_present

    @property
    def checksum(self):
        """Gets the checksum of this InlineResponse20019Response.  # noqa: E501


        :return: The checksum of this InlineResponse20019Response.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this InlineResponse20019Response.


        :param checksum: The checksum of this InlineResponse20019Response.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20019Response.  # noqa: E501


        :return: The created_at of this InlineResponse20019Response.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20019Response.


        :param created_at: The created_at of this InlineResponse20019Response.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_at_i(self):
        """Gets the created_at_i of this InlineResponse20019Response.  # noqa: E501


        :return: The created_at_i of this InlineResponse20019Response.  # noqa: E501
        :rtype: int
        """
        return self._created_at_i

    @created_at_i.setter
    def created_at_i(self, created_at_i):
        """Sets the created_at_i of this InlineResponse20019Response.


        :param created_at_i: The created_at_i of this InlineResponse20019Response.  # noqa: E501
        :type: int
        """

        self._created_at_i = created_at_i

    @property
    def started_at(self):
        """Gets the started_at of this InlineResponse20019Response.  # noqa: E501


        :return: The started_at of this InlineResponse20019Response.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this InlineResponse20019Response.


        :param started_at: The started_at of this InlineResponse20019Response.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def started_at_i(self):
        """Gets the started_at_i of this InlineResponse20019Response.  # noqa: E501


        :return: The started_at_i of this InlineResponse20019Response.  # noqa: E501
        :rtype: int
        """
        return self._started_at_i

    @started_at_i.setter
    def started_at_i(self, started_at_i):
        """Sets the started_at_i of this InlineResponse20019Response.


        :param started_at_i: The started_at_i of this InlineResponse20019Response.  # noqa: E501
        :type: int
        """

        self._started_at_i = started_at_i

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse20019Response.  # noqa: E501


        :return: The uuid of this InlineResponse20019Response.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse20019Response.


        :param uuid: The uuid of this InlineResponse20019Response.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, InlineResponse20019Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
