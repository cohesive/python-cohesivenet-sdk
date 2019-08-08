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


class Alert(object):
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
        'id': 'int',
        'description': 'str',
        'url': 'str',
        'enabled': 'bool',
        'events': 'list[str]',
        'custom_properties': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'url': 'url',
        'enabled': 'enabled',
        'events': 'events',
        'custom_properties': 'custom_properties'
    }

    def __init__(self, id=None, description=None, url=None, enabled=None, events=None, custom_properties=None):  # noqa: E501
        """Alert - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._description = None
        self._url = None
        self._enabled = None
        self._events = None
        self._custom_properties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if url is not None:
            self.url = url
        if enabled is not None:
            self.enabled = enabled
        if events is not None:
            self.events = events
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def id(self):
        """Gets the id of this Alert.  # noqa: E501


        :return: The id of this Alert.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alert.


        :param id: The id of this Alert.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this Alert.  # noqa: E501


        :return: The description of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Alert.


        :param description: The description of this Alert.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this Alert.  # noqa: E501


        :return: The url of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Alert.


        :param url: The url of this Alert.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def enabled(self):
        """Gets the enabled of this Alert.  # noqa: E501


        :return: The enabled of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Alert.


        :param enabled: The enabled of this Alert.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def events(self):
        """Gets the events of this Alert.  # noqa: E501


        :return: The events of this Alert.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Alert.


        :param events: The events of this Alert.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def custom_properties(self):
        """Gets the custom_properties of this Alert.  # noqa: E501


        :return: The custom_properties of this Alert.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this Alert.


        :param custom_properties: The custom_properties of this Alert.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
