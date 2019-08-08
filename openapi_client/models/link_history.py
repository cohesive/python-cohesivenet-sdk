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


class LinkHistory(object):
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
        'remote': 'str',
        'local': 'str',
        'tunnelid': 'int',
        'history': 'list[LinkEvent]'
    }

    attribute_map = {
        'remote': 'remote',
        'local': 'local',
        'tunnelid': 'tunnelid',
        'history': 'history'
    }

    def __init__(self, remote=None, local=None, tunnelid=None, history=None):  # noqa: E501
        """LinkHistory - a model defined in OpenAPI"""  # noqa: E501

        self._remote = None
        self._local = None
        self._tunnelid = None
        self._history = None
        self.discriminator = None

        if remote is not None:
            self.remote = remote
        if local is not None:
            self.local = local
        if tunnelid is not None:
            self.tunnelid = tunnelid
        if history is not None:
            self.history = history

    @property
    def remote(self):
        """Gets the remote of this LinkHistory.  # noqa: E501


        :return: The remote of this LinkHistory.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this LinkHistory.


        :param remote: The remote of this LinkHistory.  # noqa: E501
        :type: str
        """

        self._remote = remote

    @property
    def local(self):
        """Gets the local of this LinkHistory.  # noqa: E501


        :return: The local of this LinkHistory.  # noqa: E501
        :rtype: str
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this LinkHistory.


        :param local: The local of this LinkHistory.  # noqa: E501
        :type: str
        """

        self._local = local

    @property
    def tunnelid(self):
        """Gets the tunnelid of this LinkHistory.  # noqa: E501


        :return: The tunnelid of this LinkHistory.  # noqa: E501
        :rtype: int
        """
        return self._tunnelid

    @tunnelid.setter
    def tunnelid(self, tunnelid):
        """Sets the tunnelid of this LinkHistory.


        :param tunnelid: The tunnelid of this LinkHistory.  # noqa: E501
        :type: int
        """

        self._tunnelid = tunnelid

    @property
    def history(self):
        """Gets the history of this LinkHistory.  # noqa: E501


        :return: The history of this LinkHistory.  # noqa: E501
        :rtype: list[LinkEvent]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this LinkHistory.


        :param history: The history of this LinkHistory.  # noqa: E501
        :type: list[LinkEvent]
        """

        self._history = history

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
        if not isinstance(other, LinkHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
