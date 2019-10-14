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


class RunContainerDetail(object):
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
        "uuid": "str",
        "container_started": "bool",
        "ip_addr": "str",
        "status": "str",
    }

    attribute_map = {
        "uuid": "uuid",
        "container_started": "container_started",
        "ip_addr": "ip_addr",
        "status": "status",
    }

    def __init__(
        self, uuid=None, container_started=None, ip_addr=None, status=None
    ):  # noqa: E501
        """RunContainerDetail - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._container_started = None
        self._ip_addr = None
        self._status = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if container_started is not None:
            self.container_started = container_started
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if status is not None:
            self.status = status

    @property
    def uuid(self):
        """Gets the uuid of this RunContainerDetail.  # noqa: E501


        :return: The uuid of this RunContainerDetail.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RunContainerDetail.


        :param uuid: The uuid of this RunContainerDetail.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def container_started(self):
        """Gets the container_started of this RunContainerDetail.  # noqa: E501


        :return: The container_started of this RunContainerDetail.  # noqa: E501
        :rtype: bool
        """
        return self._container_started

    @container_started.setter
    def container_started(self, container_started):
        """Sets the container_started of this RunContainerDetail.


        :param container_started: The container_started of this RunContainerDetail.  # noqa: E501
        :type: bool
        """

        self._container_started = container_started

    @property
    def ip_addr(self):
        """Gets the ip_addr of this RunContainerDetail.  # noqa: E501


        :return: The ip_addr of this RunContainerDetail.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this RunContainerDetail.


        :param ip_addr: The ip_addr of this RunContainerDetail.  # noqa: E501
        :type: str
        """

        self._ip_addr = ip_addr

    @property
    def status(self):
        """Gets the status of this RunContainerDetail.  # noqa: E501

        Container system status for allocated container  # noqa: E501

        :return: The status of this RunContainerDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunContainerDetail.

        Container system status for allocated container  # noqa: E501

        :param status: The status of this RunContainerDetail.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, RunContainerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
