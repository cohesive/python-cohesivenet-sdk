# coding: utf-8

"""
    VNS3:ms API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import pytest

import cohesivenet
from cohesivenet.api.vns3ms import cloud_monitoring_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3ms.stub_data import CloudMonitoringApiData


class TestMSMonitoringApi(object):
    """VNS3:ms Cloud Monitoring API unit tests"""

    def test_get_cloud_vlan_components(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for get_cloud_vlan_components"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/cloud_vlan_components",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.CloudVlanComponentList,
        )(cloud_monitoring_api.get_cloud_vlan_components)

    def test_post_create_vlan_component(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for post_create_vlan_component"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/cloud_vlan_components",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": {"msg": "Cloud VLAN Component created", "id": 1},
            },
        )(cloud_monitoring_api.post_create_vlan_component)

    def test_get_cloud_vlan_component(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for get_cloud_vlan_component"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/cloud_vlan_components/{component_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.CloudVlanComponentDetail,
        )(cloud_monitoring_api.get_cloud_vlan_component)

    def test_put_update_vlan_component(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for put_update_vlan_component"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/cloud_vlan_components/{component_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(cloud_monitoring_api.put_update_vlan_component)

    def test_delete_vlan_component(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_vlan_component"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/cloud_vlan_components/{component_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(cloud_monitoring_api.delete_vlan_component)

    def test_get_cloud_vlans(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_cloud_vlans"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/cloud_vlans",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.CloudVlanList,
        )(cloud_monitoring_api.get_cloud_vlans)

    def test_post_create_cloud_vlan(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_create_cloud_vlan"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/cloud_vlans",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": {"msg": "Cloud VLAN created", "id": 1},
            },
        )(cloud_monitoring_api.post_create_cloud_vlan)

    def test_get_cloud_vlan(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_cloud_vlan"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/cloud_vlans/{vlan_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.CloudVlanDetail,
        )(cloud_monitoring_api.get_cloud_vlan)

    def test_put_update_cloud_vlan(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_update_cloud_vlan"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/cloud_vlans/{vlan_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(cloud_monitoring_api.put_update_cloud_vlan)

    def test_delete_cloud_vlan(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_cloud_vlan"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/cloud_vlans/{vlan_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": "Deleted Cloud Vlan 1",
            },
        )(cloud_monitoring_api.delete_cloud_vlan)

    def test_get_virtual_networks(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_virtual_networks"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/virtual_networks",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.VirtualNetworkList,
        )(cloud_monitoring_api.get_virtual_networks)

    def test_post_create_virtual_network(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for post_create_virtual_network"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/virtual_networks",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.CreateVirtualNetworkResponse,
        )(cloud_monitoring_api.post_create_virtual_network)

    def test_get_virtual_network(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_virtual_network"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/virtual_networks/{virtual_network_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.VirtualNetworkDetail,
        )(cloud_monitoring_api.get_virtual_network)

    def test_put_update_virtual_network(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for put_update_virtual_network"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/virtual_networks/{virtual_network_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": "Updated Virtual Network",
            },
        )(cloud_monitoring_api.put_update_virtual_network)

    def test_delete_virtual_network(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_virtual_network"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/virtual_networks/{virtual_network_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": "Deleted Virtual Network 1",
            },
        )(cloud_monitoring_api.delete_virtual_network)

    def test_get_export_virtual_networks(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for get_export_virtual_networks"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/virtual_networks/export",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response="imafileimafileimafileimafileimafileimafileimafileimafile",
        )(cloud_monitoring_api.get_export_virtual_networks)

    def test_post_import_virtual_networks(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for post_import_virtual_networks"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/virtual_networks/import",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(cloud_monitoring_api.post_import_virtual_networks)

    def test_get_vns3_topologies(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_vns3_topologies"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/vns3_topologies",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.Vns3TopologyList,
        )(cloud_monitoring_api.get_vns3_topologies)

    def test_post_create_vns3_topology(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for post_create_vns3_topology"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/vns3_topologies",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.CreateVns3TopologyResponse,
        )(cloud_monitoring_api.post_create_vns3_topology)

    def test_get_vns3_topology(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_vns3_topology"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/vns3_topologies/{vns3_topology_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.Vns3TopologyDetail,
        )(cloud_monitoring_api.get_vns3_topology)

    def test_put_update_vns3_topology(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for put_update_vns3_topology"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/vns3_topologies/{vns3_topology_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(cloud_monitoring_api.put_update_vns3_topology)

    def test_delete_vns3_topology(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_vns3_topology"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/vns3_topologies/{vns3_topology_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(cloud_monitoring_api.delete_vns3_topology)

    def test_get_webhooks(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_webhooks"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/webhooks",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.WebhookListResponse,
        )(cloud_monitoring_api.get_webhooks)

    def test_post_create_webhook(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_create_webhook"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/webhook",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.WebhookDetail,
        )(cloud_monitoring_api.post_create_webhook)

    def test_get_webhook(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_webhook"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/webhook/{webhook_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.WebhookDetail,
        )(cloud_monitoring_api.get_webhook)

    def test_put_update_webhook(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_update_webhook"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/webhook/{webhook_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.WebhookDetail,
        )(cloud_monitoring_api.put_update_webhook)

    def test_delete_webhook(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_webhook"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/webhook/{webhook_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.WebhookDetail,
        )(cloud_monitoring_api.delete_webhook)

    def test_get_alerts(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_alerts"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/alerts",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.AlertListResponse,
        )(cloud_monitoring_api.get_alerts)

    def test_get_alert(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_alert"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/alert/{alert_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.AlertDetail,
        )(cloud_monitoring_api.get_alert)

    def test_post_create_alert(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_create_alert"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/alert",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.AlertDetail,
        )(cloud_monitoring_api.post_create_alert)

    def test_put_update_alert(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_update_alert"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/alert/{alert_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.AlertDetail,
        )(cloud_monitoring_api.put_update_alert)

    def test_delete_alert(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_alert"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/alert/{alert_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.AlertDetail,
        )(cloud_monitoring_api.delete_alert)

    def test_post_test_alert(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_test_alert"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/alert/{alert_id}/test",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": "Alert sent successfully.",
            },
        )(cloud_monitoring_api.post_test_alert)

    def test_post_toggle_enable_alert(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for post_toggle_enable_alert"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/alert/{alert_id}/toggle_enabled",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=CloudMonitoringApiData.AlertDetail,
        )(cloud_monitoring_api.post_toggle_enable_alert)
