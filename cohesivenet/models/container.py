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


class Container(object):
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
        'id': 'str',
        'created': 'str',
        'path': 'str',
        'args': 'list[str]',
        'config': 'dict(str, object)',
        'state': 'RunningContainersDetailState',
        'image': 'str',
        'network_settings': 'RunningContainersDetailNetworkSettings',
        'resolv_conf_path': 'str',
        'hostname_path': 'str',
        'hosts_path': 'str',
        'name': 'str',
        'driver': 'str',
        'exec_driver': 'str',
        'volumes': 'dict(str, object)',
        'volumes_rw': 'dict(str, object)',
        'host_config': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'ID',
        'created': 'Created',
        'path': 'Path',
        'args': 'Args',
        'config': 'Config',
        'state': 'State',
        'image': 'Image',
        'network_settings': 'NetworkSettings',
        'resolv_conf_path': 'ResolvConfPath',
        'hostname_path': 'HostnamePath',
        'hosts_path': 'HostsPath',
        'name': 'Name',
        'driver': 'Driver',
        'exec_driver': 'ExecDriver',
        'volumes': 'Volumes',
        'volumes_rw': 'VolumesRW',
        'host_config': 'HostConfig'
    }

    def __init__(self, id=None, created=None, path=None, args=None, config=None, state=None, image=None, network_settings=None, resolv_conf_path=None, hostname_path=None, hosts_path=None, name=None, driver=None, exec_driver=None, volumes=None, volumes_rw=None, host_config=None):  # noqa: E501
        """Container - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._created = None
        self._path = None
        self._args = None
        self._config = None
        self._state = None
        self._image = None
        self._network_settings = None
        self._resolv_conf_path = None
        self._hostname_path = None
        self._hosts_path = None
        self._name = None
        self._driver = None
        self._exec_driver = None
        self._volumes = None
        self._volumes_rw = None
        self._host_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created is not None:
            self.created = created
        if path is not None:
            self.path = path
        if args is not None:
            self.args = args
        if config is not None:
            self.config = config
        if state is not None:
            self.state = state
        if image is not None:
            self.image = image
        if network_settings is not None:
            self.network_settings = network_settings
        if resolv_conf_path is not None:
            self.resolv_conf_path = resolv_conf_path
        if hostname_path is not None:
            self.hostname_path = hostname_path
        if hosts_path is not None:
            self.hosts_path = hosts_path
        if name is not None:
            self.name = name
        if driver is not None:
            self.driver = driver
        if exec_driver is not None:
            self.exec_driver = exec_driver
        self.volumes = volumes
        self.volumes_rw = volumes_rw
        self.host_config = host_config

    @property
    def id(self):
        """Gets the id of this Container.  # noqa: E501


        :return: The id of this Container.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Container.


        :param id: The id of this Container.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this Container.  # noqa: E501


        :return: The created of this Container.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Container.


        :param created: The created of this Container.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def path(self):
        """Gets the path of this Container.  # noqa: E501


        :return: The path of this Container.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Container.


        :param path: The path of this Container.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def args(self):
        """Gets the args of this Container.  # noqa: E501


        :return: The args of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Container.


        :param args: The args of this Container.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def config(self):
        """Gets the config of this Container.  # noqa: E501


        :return: The config of this Container.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Container.


        :param config: The config of this Container.  # noqa: E501
        :type: dict(str, object)
        """

        self._config = config

    @property
    def state(self):
        """Gets the state of this Container.  # noqa: E501


        :return: The state of this Container.  # noqa: E501
        :rtype: RunningContainersDetailState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Container.


        :param state: The state of this Container.  # noqa: E501
        :type: RunningContainersDetailState
        """

        self._state = state

    @property
    def image(self):
        """Gets the image of this Container.  # noqa: E501


        :return: The image of this Container.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Container.


        :param image: The image of this Container.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def network_settings(self):
        """Gets the network_settings of this Container.  # noqa: E501


        :return: The network_settings of this Container.  # noqa: E501
        :rtype: RunningContainersDetailNetworkSettings
        """
        return self._network_settings

    @network_settings.setter
    def network_settings(self, network_settings):
        """Sets the network_settings of this Container.


        :param network_settings: The network_settings of this Container.  # noqa: E501
        :type: RunningContainersDetailNetworkSettings
        """

        self._network_settings = network_settings

    @property
    def resolv_conf_path(self):
        """Gets the resolv_conf_path of this Container.  # noqa: E501


        :return: The resolv_conf_path of this Container.  # noqa: E501
        :rtype: str
        """
        return self._resolv_conf_path

    @resolv_conf_path.setter
    def resolv_conf_path(self, resolv_conf_path):
        """Sets the resolv_conf_path of this Container.


        :param resolv_conf_path: The resolv_conf_path of this Container.  # noqa: E501
        :type: str
        """

        self._resolv_conf_path = resolv_conf_path

    @property
    def hostname_path(self):
        """Gets the hostname_path of this Container.  # noqa: E501


        :return: The hostname_path of this Container.  # noqa: E501
        :rtype: str
        """
        return self._hostname_path

    @hostname_path.setter
    def hostname_path(self, hostname_path):
        """Sets the hostname_path of this Container.


        :param hostname_path: The hostname_path of this Container.  # noqa: E501
        :type: str
        """

        self._hostname_path = hostname_path

    @property
    def hosts_path(self):
        """Gets the hosts_path of this Container.  # noqa: E501


        :return: The hosts_path of this Container.  # noqa: E501
        :rtype: str
        """
        return self._hosts_path

    @hosts_path.setter
    def hosts_path(self, hosts_path):
        """Sets the hosts_path of this Container.


        :param hosts_path: The hosts_path of this Container.  # noqa: E501
        :type: str
        """

        self._hosts_path = hosts_path

    @property
    def name(self):
        """Gets the name of this Container.  # noqa: E501


        :return: The name of this Container.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Container.


        :param name: The name of this Container.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def driver(self):
        """Gets the driver of this Container.  # noqa: E501


        :return: The driver of this Container.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this Container.


        :param driver: The driver of this Container.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def exec_driver(self):
        """Gets the exec_driver of this Container.  # noqa: E501


        :return: The exec_driver of this Container.  # noqa: E501
        :rtype: str
        """
        return self._exec_driver

    @exec_driver.setter
    def exec_driver(self, exec_driver):
        """Sets the exec_driver of this Container.


        :param exec_driver: The exec_driver of this Container.  # noqa: E501
        :type: str
        """

        self._exec_driver = exec_driver

    @property
    def volumes(self):
        """Gets the volumes of this Container.  # noqa: E501


        :return: The volumes of this Container.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Container.


        :param volumes: The volumes of this Container.  # noqa: E501
        :type: dict(str, object)
        """

        self._volumes = volumes

    @property
    def volumes_rw(self):
        """Gets the volumes_rw of this Container.  # noqa: E501


        :return: The volumes_rw of this Container.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._volumes_rw

    @volumes_rw.setter
    def volumes_rw(self, volumes_rw):
        """Sets the volumes_rw of this Container.


        :param volumes_rw: The volumes_rw of this Container.  # noqa: E501
        :type: dict(str, object)
        """

        self._volumes_rw = volumes_rw

    @property
    def host_config(self):
        """Gets the host_config of this Container.  # noqa: E501


        :return: The host_config of this Container.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._host_config

    @host_config.setter
    def host_config(self, host_config):
        """Sets the host_config of this Container.


        :param host_config: The host_config of this Container.  # noqa: E501
        :type: dict(str, object)
        """

        self._host_config = host_config

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
        if not isinstance(other, Container):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other