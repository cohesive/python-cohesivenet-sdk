# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
"""


import pprint
import re  # noqa: F401

import six


class EC2CloudInfo(object):
    """
    Metadata returned from AWS instance metadata call. 
    For more, see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval.

    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        "account_id": "str",
        "availability_zone": "str",
        "ramdisk_id": "str",
        "kernel_id": "str",
        "pending_time": "str",
        "architecture": "str",
        "private_ip": "str",
        "devpay_product_codes": "str",
        "marketplace_product_codes": "str",
        "version": "str",
        "region": "str",
        "image_id": "str",
        "billing_products": "str",
        "instance_id": "str",
        "instance_type": "str",
    }

    attribute_map = {
        "account_id": "accountId",
        "availability_zone": "availabilityZone",
        "ramdisk_id": "ramdiskId",
        "kernel_id": "kernelId",
        "pending_time": "pendingTime",
        "architecture": "architecture",
        "private_ip": "privateIp",
        "devpay_product_codes": "devpayProductCodes",
        "marketplace_product_codes": "marketplaceProductCodes",
        "version": "version",
        "region": "region",
        "image_id": "imageId",
        "billing_products": "billingProducts",
        "instance_id": "instanceId",
        "instance_type": "instanceType",
    }

    def __init__(
        self,
        account_id=None,
        availability_zone=None,
        ramdisk_id=None,
        kernel_id=None,
        pending_time=None,
        architecture=None,
        private_ip=None,
        devpay_product_codes=None,
        marketplace_product_codes=None,
        version=None,
        region=None,
        image_id=None,
        billing_products=None,
        instance_id=None,
        instance_type=None,
    ):  # noqa: E501
        """EC2CloudInfo - a model defined in OpenAPI"""  # noqa: E501

        self._account_id = None
        self._availability_zone = None
        self._ramdisk_id = None  # nullable
        self._kernel_id = None  # nullable
        self._pending_time = None
        self._architecture = None
        self._private_ip = None
        self._devpay_product_codes = None  # nullable
        self._marketplace_product_codes = None  # nullable
        self._version = None
        self._region = None
        self._image_id = None
        self._billing_products = None
        self._instance_id = None
        self._instance_type = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if availability_zone is not None:
            self.availability_zone = availability_zone

        self.ramdisk_id = ramdisk_id  # nullable
        self.kernel_id = kernel_id  # nullable

        if pending_time is not None:
            self.pending_time = pending_time
        if architecture is not None:
            self.architecture = architecture
        if private_ip is not None:
            self.private_ip = private_ip

        self.devpay_product_codes = devpay_product_codes  # nullable
        self.marketplace_product_codes = marketplace_product_codes  # nullable

        if version is not None:
            self.version = version
        if region is not None:
            self.region = region
        if image_id is not None:
            self.image_id = image_id
        if billing_products is not None:
            self.billing_products = billing_products
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def account_id(self):
        """Gets the accountId of this ECCloudInfo.  # noqa: E501

        :return: The accountId of this ECCloudInfo.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @rules.setter
    def account_id(self, account_id):
        """Sets the accountId of this ECCloudInfo.  # noqa: E501

        :param account_id: The account_id of this ECCloudInfo.  # noqa: E501
        :type: str
        """
        self._account_id = account_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ECCloudInfo.  # noqa: E501

        :return: The availability_zone of this ECCloudInfo.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @rules.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ECCloudInfo.  # noqa: E501

        :param availability_zone: The availability_zone of this ECCloudInfo.  # noqa: E501
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def ramdisk_id(self):
        """Gets the ramdisk_id of this EC2 Instance.  # noqa: E501

        :return: The ramdisk_id of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._ramdisk_id

    @rules.setter
    def ramdisk_id(self, ramdisk_id):
        """Sets the ramdisk_id of this ECCloudInfo.  # noqa: E501

        :param ramdisk_id: The ramdisk_id of this ECCloudInfo.  # noqa: E501
        :type: str
        """
        self._ramdisk_id = ramdisk_id

    @property
    def kernel_id(self):
        """Gets the kernel_id of this EC2 Instance.  # noqa: E501

        :return: The kernel_id of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._kernel_id

    @rules.setter
    def kernel_id(self, kernel_id):
        """Sets the kernel_id of this ECCloudInfo.  # noqa: E501

        :param kernel_id: The kernel_id of this ECCloudInfo.  # noqa: E501
        :type: str
        """
        self._kernel_id = kernel_id

    @property
    def pending_time(self):
        """Gets the pending_time of this EC2 Instance.  # noqa: E501

        :return: The pending_time of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._pending_time

    @rules.setter
    def pending_time(self, pending_time):
        """Sets the pending_time of this ECCloudInfo.  # noqa: E501

        :param pending_time: The pending_time of this ECCloudInfo.  # noqa: E501
        :type: str
        """
        self._pending_time = pending_time

    @property
    def architecture(self):
        """Gets the architecture of this EC2 Instance.  # noqa: E501

        :return: The architecture of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @rules.setter
    def architecture(self, architecture):
        """Sets the architecture of this EC2 Instance.  # noqa: E501

        :param architecture: The architecture of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._architecture = architecture

    @property
    def private_ip(self):
        """Gets the private_ip of this EC2 Instance.  # noqa: E501

        :return: The private_ip of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._private_ip

    @rules.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this EC2 Instance.  # noqa: E501

        :param private_ip: The private_ip of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._private_ip = private_ip

    @property
    def devpay_product_codes(self):
        """Gets the devpay_product_codes of this EC2 Instance.  # noqa: E501

        :return: The devpay_product_codes of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._devpay_product_codes

    @rules.setter
    def devpay_product_codes(self, devpay_product_codes):
        """Sets the devpay_product_codes of this EC2 Instance.  # noqa: E501

        :param devpay_product_codes: The devpay_product_codes of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._devpay_product_codes = devpay_product_codes

    @property
    def marketplace_product_codes(self):
        """Gets the marketplace_product_codes of this EC2 Instance.  # noqa: E501

        :return: The marketplace_product_codes of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_product_codes

    @rules.setter
    def marketplace_product_codes(self, marketplace_product_codes):
        """Sets the marketplace_product_codes of this EC2 Instance.  # noqa: E501

        :param marketplace_product_codes: The marketplace_product_codes of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._marketplace_product_codes = marketplace_product_codes

    @property
    def version(self):
        """Gets the version of this EC2 Instance.  # noqa: E501

        :return: The version of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._version

    @rules.setter
    def version(self, version):
        """Sets the version of this EC2 Instance.  # noqa: E501

        :param version: The version of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._version = version

    @property
    def region(self):
        """Gets the region of this EC2 Instance.  # noqa: E501

        :return: The region of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._region

    @rules.setter
    def region(self, region):
        """Sets the region of this EC2 Instance.  # noqa: E501

        :param region: The region of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._region = region

    @property
    def image_id(self):
        """Gets the image_id of this EC2 Instance.  # noqa: E501

        :return: The image_id of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @rules.setter
    def image_id(self, image_id):
        """Sets the image_id of this EC2 Instance.  # noqa: E501

        :param image_id: The image_id of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._image_id = image_id

    @property
    def billing_products(self):
        """Gets the billing_products of this EC2 Instance.  # noqa: E501

        :return: The billing_products of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._billing_products

    @rules.setter
    def billing_products(self, billing_products):
        """Sets the billing_products of this EC2 Instance.  # noqa: E501

        :param billing_products: The billing_products of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._billing_products = billing_products

    @property
    def instance_id(self):
        """Gets the instance_id of this EC2 Instance.  # noqa: E501

        :return: The instance_id of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @rules.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EC2 Instance.  # noqa: E501

        :param instance_id: The instance_id of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this EC2 Instance.  # noqa: E501

        :return: The instance_type of this EC2 Instance.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @rules.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this EC2 Instance.  # noqa: E501

        :param instance_type: The instance_type of this EC2 Instance.  # noqa: E501
        :type: str
        """
        self._instance_type = instance_type

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
        if not isinstance(other, EC2CloudInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
