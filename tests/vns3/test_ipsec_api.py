# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import pytest

import cohesivenet
from cohesivenet.api.vns3 import ipsec_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3.stub_data import IpsecApiData


class TestIPsecApi(object):
    """IPsecApi unit test stubs"""

    def test_delete_ipsec_endpoint(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for delete_ipsec_endpoint
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/ipsec/endpoints/{endpoint_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecSystemDetailResponse,
        )(ipsec_api.delete_ipsec_endpoint)

    def test_delete_ipsec_endpoint_tunnel(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for delete_ipsec_endpoint_tunnel
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/ipsec/endpoints/{endpoint_id}/tunnels/{tunnel_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecEndpointDetailNoTunnels,
        )(ipsec_api.delete_ipsec_endpoint_tunnel)

    def test_get_ipsec_details(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_ipsec_details
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/ipsec",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecSystemDetailResponse,
        )(ipsec_api.get_ipsec_details)

    def test_get_ipsec_endpoint(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_ipsec_endpoint
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/ipsec/endpoints/{endpoint_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecEndpointDetail,
        )(ipsec_api.get_ipsec_endpoint)

    def test_get_ipsec_status(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_ipsec_status
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/status/ipsec",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecStatusResponse,
        )(ipsec_api.get_ipsec_status)

    def test_get_ipsec_link_history(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_ipsec_link_history
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/status/link_history",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.LinkHistoryResponse,
        )(ipsec_api.get_ipsec_link_history)

    def test_post_create_ipsec_endpoint(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_create_ipsec_endpoint
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/ipsec/endpoints",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecEndpointDetail,
        )(ipsec_api.post_create_ipsec_endpoint)

    def test_post_create_ipsec_endpoint_tunnel(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_create_ipsec_endpoint_tunnel

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/ipsec/endpoints/{endpoint_id}/tunnels",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecEndpointDetail,
        )(ipsec_api.post_create_ipsec_endpoint_tunnel)

    def test_post_restart_ipsec_action(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for post_restart_ipsec_action
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/ipsec",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": {"restart": True}},
        )(ipsec_api.post_restart_ipsec_action)

    def test_put_update_ipsec_endpoint(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for put_update_ipsec_endpoint

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/ipsec/endpoints/{endpoint_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecEndpointDetail,
        )(ipsec_api.put_update_ipsec_endpoint)

    def test_put_update_ipsec_endpoint_tunnel(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for put_update_ipsec_endpoint_tunnel

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/ipsec/endpoints/{endpoint_id}/tunnels/{tunnel_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecTunnelDetail,
        )(ipsec_api.put_update_ipsec_endpoint_tunnel)

    def test_put_update_ipsec_config(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for put_update_ipsec_config
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/ipsec",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=IpsecApiData.IpsecSystemDetailResponse,
        )(ipsec_api.put_update_ipsec_config)
