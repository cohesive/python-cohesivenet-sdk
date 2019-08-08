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


class LicenseContainerDetails(object):
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
        'containers_run_count': 'int',
        'containers_image_count': 'int'
    }

    attribute_map = {
        'containers_run_count': 'containers_run_count',
        'containers_image_count': 'containers_image_count'
    }

    def __init__(self, containers_run_count=None, containers_image_count=None):  # noqa: E501
        """LicenseContainerDetails - a model defined in OpenAPI"""  # noqa: E501

        self._containers_run_count = None
        self._containers_image_count = None
        self.discriminator = None

        if containers_run_count is not None:
            self.containers_run_count = containers_run_count
        if containers_image_count is not None:
            self.containers_image_count = containers_image_count

    @property
    def containers_run_count(self):
        """Gets the containers_run_count of this LicenseContainerDetails.  # noqa: E501


        :return: The containers_run_count of this LicenseContainerDetails.  # noqa: E501
        :rtype: int
        """
        return self._containers_run_count

    @containers_run_count.setter
    def containers_run_count(self, containers_run_count):
        """Sets the containers_run_count of this LicenseContainerDetails.


        :param containers_run_count: The containers_run_count of this LicenseContainerDetails.  # noqa: E501
        :type: int
        """

        self._containers_run_count = containers_run_count

    @property
    def containers_image_count(self):
        """Gets the containers_image_count of this LicenseContainerDetails.  # noqa: E501


        :return: The containers_image_count of this LicenseContainerDetails.  # noqa: E501
        :rtype: int
        """
        return self._containers_image_count

    @containers_image_count.setter
    def containers_image_count(self, containers_image_count):
        """Sets the containers_image_count of this LicenseContainerDetails.


        :param containers_image_count: The containers_image_count of this LicenseContainerDetails.  # noqa: E501
        :type: int
        """

        self._containers_image_count = containers_image_count

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
        if not isinstance(other, LicenseContainerDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
