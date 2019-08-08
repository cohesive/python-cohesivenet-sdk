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


class RuntimeConfig(object):
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
        'asn': 'int',
        'topology_name': 'str',
        'topology_checksum': 'str',
        'manager_id': 'int',
        'ntp_hosts': 'str',
        'vns3_version': 'str',
        'licensed': 'bool',
        'overlay_ipaddress': 'str',
        'peered': 'bool',
        'public_ipaddress': 'str',
        'private_ipaddress': 'str',
        'security_token': 'str'
    }

    attribute_map = {
        'asn': 'asn',
        'topology_name': 'topology_name',
        'topology_checksum': 'topology_checksum',
        'manager_id': 'manager_id',
        'ntp_hosts': 'ntp_hosts',
        'vns3_version': 'vns3_version',
        'licensed': 'licensed',
        'overlay_ipaddress': 'overlay_ipaddress',
        'peered': 'peered',
        'public_ipaddress': 'public_ipaddress',
        'private_ipaddress': 'private_ipaddress',
        'security_token': 'security_token'
    }

    def __init__(self, asn=None, topology_name=None, topology_checksum=None, manager_id=None, ntp_hosts=None, vns3_version=None, licensed=None, overlay_ipaddress=None, peered=None, public_ipaddress=None, private_ipaddress=None, security_token=None):  # noqa: E501
        """RuntimeConfig - a model defined in OpenAPI"""  # noqa: E501

        self._asn = None
        self._topology_name = None
        self._topology_checksum = None
        self._manager_id = None
        self._ntp_hosts = None
        self._vns3_version = None
        self._licensed = None
        self._overlay_ipaddress = None
        self._peered = None
        self._public_ipaddress = None
        self._private_ipaddress = None
        self._security_token = None
        self.discriminator = None

        if asn is not None:
            self.asn = asn
        if topology_name is not None:
            self.topology_name = topology_name
        if topology_checksum is not None:
            self.topology_checksum = topology_checksum
        if manager_id is not None:
            self.manager_id = manager_id
        if ntp_hosts is not None:
            self.ntp_hosts = ntp_hosts
        if vns3_version is not None:
            self.vns3_version = vns3_version
        if licensed is not None:
            self.licensed = licensed
        if overlay_ipaddress is not None:
            self.overlay_ipaddress = overlay_ipaddress
        if peered is not None:
            self.peered = peered
        if public_ipaddress is not None:
            self.public_ipaddress = public_ipaddress
        if private_ipaddress is not None:
            self.private_ipaddress = private_ipaddress
        if security_token is not None:
            self.security_token = security_token

    @property
    def asn(self):
        """Gets the asn of this RuntimeConfig.  # noqa: E501

        Autonomous system number for controller if peered  # noqa: E501

        :return: The asn of this RuntimeConfig.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this RuntimeConfig.

        Autonomous system number for controller if peered  # noqa: E501

        :param asn: The asn of this RuntimeConfig.  # noqa: E501
        :type: int
        """

        self._asn = asn

    @property
    def topology_name(self):
        """Gets the topology_name of this RuntimeConfig.  # noqa: E501


        :return: The topology_name of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._topology_name

    @topology_name.setter
    def topology_name(self, topology_name):
        """Sets the topology_name of this RuntimeConfig.


        :param topology_name: The topology_name of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._topology_name = topology_name

    @property
    def topology_checksum(self):
        """Gets the topology_checksum of this RuntimeConfig.  # noqa: E501


        :return: The topology_checksum of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._topology_checksum

    @topology_checksum.setter
    def topology_checksum(self, topology_checksum):
        """Sets the topology_checksum of this RuntimeConfig.


        :param topology_checksum: The topology_checksum of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._topology_checksum = topology_checksum

    @property
    def manager_id(self):
        """Gets the manager_id of this RuntimeConfig.  # noqa: E501

        This managers ID in peered topology  # noqa: E501

        :return: The manager_id of this RuntimeConfig.  # noqa: E501
        :rtype: int
        """
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        """Sets the manager_id of this RuntimeConfig.

        This managers ID in peered topology  # noqa: E501

        :param manager_id: The manager_id of this RuntimeConfig.  # noqa: E501
        :type: int
        """

        self._manager_id = manager_id

    @property
    def ntp_hosts(self):
        """Gets the ntp_hosts of this RuntimeConfig.  # noqa: E501

        NTP host endpoints, whitespace delimited  # noqa: E501

        :return: The ntp_hosts of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._ntp_hosts

    @ntp_hosts.setter
    def ntp_hosts(self, ntp_hosts):
        """Sets the ntp_hosts of this RuntimeConfig.

        NTP host endpoints, whitespace delimited  # noqa: E501

        :param ntp_hosts: The ntp_hosts of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._ntp_hosts = ntp_hosts

    @property
    def vns3_version(self):
        """Gets the vns3_version of this RuntimeConfig.  # noqa: E501


        :return: The vns3_version of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._vns3_version

    @vns3_version.setter
    def vns3_version(self, vns3_version):
        """Sets the vns3_version of this RuntimeConfig.


        :param vns3_version: The vns3_version of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._vns3_version = vns3_version

    @property
    def licensed(self):
        """Gets the licensed of this RuntimeConfig.  # noqa: E501


        :return: The licensed of this RuntimeConfig.  # noqa: E501
        :rtype: bool
        """
        return self._licensed

    @licensed.setter
    def licensed(self, licensed):
        """Sets the licensed of this RuntimeConfig.


        :param licensed: The licensed of this RuntimeConfig.  # noqa: E501
        :type: bool
        """

        self._licensed = licensed

    @property
    def overlay_ipaddress(self):
        """Gets the overlay_ipaddress of this RuntimeConfig.  # noqa: E501

        This managers overlay IP in peered topology  # noqa: E501

        :return: The overlay_ipaddress of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._overlay_ipaddress

    @overlay_ipaddress.setter
    def overlay_ipaddress(self, overlay_ipaddress):
        """Sets the overlay_ipaddress of this RuntimeConfig.

        This managers overlay IP in peered topology  # noqa: E501

        :param overlay_ipaddress: The overlay_ipaddress of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._overlay_ipaddress = overlay_ipaddress

    @property
    def peered(self):
        """Gets the peered of this RuntimeConfig.  # noqa: E501


        :return: The peered of this RuntimeConfig.  # noqa: E501
        :rtype: bool
        """
        return self._peered

    @peered.setter
    def peered(self, peered):
        """Sets the peered of this RuntimeConfig.


        :param peered: The peered of this RuntimeConfig.  # noqa: E501
        :type: bool
        """

        self._peered = peered

    @property
    def public_ipaddress(self):
        """Gets the public_ipaddress of this RuntimeConfig.  # noqa: E501


        :return: The public_ipaddress of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._public_ipaddress

    @public_ipaddress.setter
    def public_ipaddress(self, public_ipaddress):
        """Sets the public_ipaddress of this RuntimeConfig.


        :param public_ipaddress: The public_ipaddress of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._public_ipaddress = public_ipaddress

    @property
    def private_ipaddress(self):
        """Gets the private_ipaddress of this RuntimeConfig.  # noqa: E501


        :return: The private_ipaddress of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._private_ipaddress

    @private_ipaddress.setter
    def private_ipaddress(self, private_ipaddress):
        """Sets the private_ipaddress of this RuntimeConfig.


        :param private_ipaddress: The private_ipaddress of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._private_ipaddress = private_ipaddress

    @property
    def security_token(self):
        """Gets the security_token of this RuntimeConfig.  # noqa: E501

        Security token in peered topology  # noqa: E501

        :return: The security_token of this RuntimeConfig.  # noqa: E501
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this RuntimeConfig.

        Security token in peered topology  # noqa: E501

        :param security_token: The security_token of this RuntimeConfig.  # noqa: E501
        :type: str
        """

        self._security_token = security_token

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
        if not isinstance(other, RuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
