# coding: utf-8
"""
    Cohesive Networks SDK

    Cohesive Networks SDK is a thin wrapper around our product APIs providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import datetime
import json
import mimetypes
from multiprocessing.pool import ThreadPool
import os
import re
import tempfile

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

from cohesivenet.api_client import APIClient, api_as_property
from cohesivenet.configuration import Configuration
import cohesivenet.models
from cohesivenet import rest
from cohesivenet.exceptions import ApiValueError

from cohesivenet.api.vns3 import BGPApi
from cohesivenet.api.vns3 import ConfigurationApi
from cohesivenet.api.vns3 import FirewallApi
from cohesivenet.api.vns3 import HighAvailabilityApi
from cohesivenet.api.vns3 import IPsecApi
from cohesivenet.api.vns3 import InterfacesApi
from cohesivenet.api.vns3 import LicensingApi
from cohesivenet.api.vns3 import MonitoringAlertingApi
from cohesivenet.api.vns3 import NetworkEdgePluginsApi
from cohesivenet.api.vns3 import OverlayNetworkApi
from cohesivenet.api.vns3 import PeeringApi
from cohesivenet.api.vns3 import RoutingApi
from cohesivenet.api.vns3 import SnapshotsApi
from cohesivenet.api.vns3 import SystemAdministrationApi


class VNS3Client(APIClient):
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    BASE_PATH = "api"
    DEF_REQ_TIMEOUT = 15.0

    # Client API Groups available as attributes: e.g. vns3_client.peering.delete_peer(4)
    bgp = api_as_property("bgp", BGPApi)
    config = api_as_property("config", ConfigurationApi)
    firewall = api_as_property("firewall", FirewallApi)
    high_availability = api_as_property("high_availability", HighAvailabilityApi)
    ipsec = api_as_property("ipsec", IPsecApi)
    interfaces = api_as_property("interfaces", InterfacesApi)
    licensing = api_as_property("licensing", LicensingApi)
    monitoring = api_as_property("monitoring", MonitoringAlertingApi)
    network_edge_plugins = api_as_property(
        "network_edge_plugins", NetworkEdgePluginsApi
    )
    overlay_network = api_as_property("overlay_network", OverlayNetworkApi)
    peering = api_as_property("peering", PeeringApi)
    routing = api_as_property("routing", RoutingApi)
    snapshots = api_as_property("snapshots", SnapshotsApi)
    sys_admin = api_as_property("sys_admin", SystemAdministrationApi)

    @property
    def controller_state(self):
        return getattr(self, "_state", {})

    def add_to_state(self, key, value):
        state = getattr(self, "_state", {})
        state[key] = value
        setattr(self, "_state", state)
        return None

    def query_state(self, key):
        return self.controller_state.get(key)

    @property
    def host_uri(self):
        return self.configuration.host_uri
