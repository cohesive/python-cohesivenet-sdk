# coding: utf-8

# flake8: noqa

"""
    Cohesive Networks SDK

    Cohesive Networks SDK is a thin wrapper around our product APIs providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

from cohesivenet.log_util import Logger

import os
import urllib3

COHESIVE_LOG_LEVEL = os.environ.get("COHESIVE_LOG_LEVEL", "").lower()
Logger.set_null()
if COHESIVE_LOG_LEVEL:
    Logger.set_stream_handler(COHESIVE_LOG_LEVEL)

from cohesivenet.version import (
    VERSION,
    LATEST_VNS3_VERSION,
    LATEST_VNS3_API_SPEC,
    LATEST_VNS3_MS_VERSION,
    LATEST_VNS3_MS_API_SPEC,
)

__version__ = VERSION
__vns3_version__ = LATEST_VNS3_VERSION
__vns3_spec__ = LATEST_VNS3_API_SPEC
__vns3_ms_version__ = LATEST_VNS3_MS_VERSION
__vns3_ms_spec__ = LATEST_VNS3_MS_API_SPEC

from cohesivenet.rest import HTTPStatus
from cohesivenet.exceptions import UrlLib3ConnExceptions
from cohesivenet.exceptions import CohesiveSDKException
from cohesivenet.exceptions import ApiException
from cohesivenet.exceptions import ApiKeyError
from cohesivenet.exceptions import ApiValueError
from cohesivenet.exceptions import ApiTypeError
from cohesivenet.exceptions import OpenApiException
from cohesivenet.configuration import Configuration
from cohesivenet.vns3_client import VNS3Client

from cohesivenet.api.vns3.bgp_api import BGPApiRouter as BGPApi
from cohesivenet.api.vns3.configuration_api import (
    ConfigurationApiRouter as ConfigurationApi,
)
from cohesivenet.api.vns3.firewall_api import FirewallApiRouter as FirewallApi
from cohesivenet.api.vns3.ipsec_api import IPsecApiRouter as IPsecApi
from cohesivenet.api.vns3.interfaces_api import InterfacesApiRouter as InterfacesApi
from cohesivenet.api.vns3.licensing_api import LicensingApiRouter as LicensingApi
from cohesivenet.api.vns3.monitoring_alerting_api import (
    MonitoringAlertingApiRouter as MonitoringAlertingApi,
)
from cohesivenet.api.vns3.network_edge_plugins_api import (
    NetworkEdgePluginsApiRouter as NetworkEdgePluginsApi,
)
from cohesivenet.api.vns3.overlay_network_api import (
    OverlayNetworkApiRouter as OverlayNetworkApi,
)
from cohesivenet.api.vns3.peering_api import PeeringApiRouter as PeeringApi
from cohesivenet.api.vns3.routing_api import RoutingApiRouter as RoutingApi
from cohesivenet.api.vns3.snapshots_api import SnapshotsApiRouter as SnapshotsApi
from cohesivenet.api.vns3.system_administration_api import (
    SystemAdministrationApiRouter as SystemAdministrationApi,
)
from cohesivenet.api.vns3.access_api import AccessApiRouter as AccessApi


from cohesivenet.ms_client import MSClient
