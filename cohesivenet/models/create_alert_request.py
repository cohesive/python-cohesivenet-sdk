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


class CreateAlertRequest(object):
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
        "description": "str",
        "url": "str",
        "webhook_id": "int",
        "events": "list[str]",
        "custom_properties": "dict(str, str)",
        "enabled": "bool",
    }

    attribute_map = {
        "description": "description",
        "url": "url",
        "webhook_id": "webhook_id",
        "events": "events",
        "custom_properties": "custom_properties",
        "enabled": "enabled",
    }

    def __init__(
        self,
        description=None,
        url=None,
        webhook_id=None,
        events=None,
        custom_properties=None,
        enabled=True,
    ):  # noqa: E501
        """CreateAlertRequest - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._url = None
        self._webhook_id = None
        self._events = None
        self._custom_properties = None
        self._enabled = None
        self.discriminator = None

        self.description = description
        self.url = url
        self.webhook_id = webhook_id
        if events is not None:
            self.events = events
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if enabled is not None:
            self.enabled = enabled

    @property
    def description(self):
        """Gets the description of this CreateAlertRequest.  # noqa: E501


        :return: The description of this CreateAlertRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAlertRequest.


        :param description: The description of this CreateAlertRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError(
                "Invalid value for `description`, must not be `None`"
            )  # noqa: E501

        self._description = description

    @property
    def url(self):
        """Gets the url of this CreateAlertRequest.  # noqa: E501


        :return: The url of this CreateAlertRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateAlertRequest.


        :param url: The url of this CreateAlertRequest.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError(
                "Invalid value for `url`, must not be `None`"
            )  # noqa: E501

        self._url = url

    @property
    def webhook_id(self):
        """Gets the webhook_id of this CreateAlertRequest.  # noqa: E501


        :return: The webhook_id of this CreateAlertRequest.  # noqa: E501
        :rtype: int
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this CreateAlertRequest.


        :param webhook_id: The webhook_id of this CreateAlertRequest.  # noqa: E501
        :type: int
        """
        if webhook_id is None:
            raise ValueError(
                "Invalid value for `webhook_id`, must not be `None`"
            )  # noqa: E501

        self._webhook_id = webhook_id

    @property
    def events(self):
        """Gets the events of this CreateAlertRequest.  # noqa: E501


        :return: The events of this CreateAlertRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this CreateAlertRequest.


        :param events: The events of this CreateAlertRequest.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def custom_properties(self):
        """Gets the custom_properties of this CreateAlertRequest.  # noqa: E501


        :return: The custom_properties of this CreateAlertRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this CreateAlertRequest.


        :param custom_properties: The custom_properties of this CreateAlertRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    @property
    def enabled(self):
        """Gets the enabled of this CreateAlertRequest.  # noqa: E501


        :return: The enabled of this CreateAlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateAlertRequest.


        :param enabled: The enabled of this CreateAlertRequest.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, CreateAlertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
