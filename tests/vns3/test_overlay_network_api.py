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
from cohesivenet.api.vns3 import overlay_network_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3.stub_data import OverlayNetworkApiData


class TestOverlayNetworkApi(object):
    """OverlayNetworkApi unit test stubs"""

    def test_get_clientpack(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_clientpack
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/clientpacks/{clientpack_name}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=OverlayNetworkApiData.ClientpackDetail,
        )(overlay_network_api.get_clientpack)

    def test_get_clientpacks(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_clientpacks

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/clientpacks",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=OverlayNetworkApiData.ClientpacksListResponse,
        )(overlay_network_api.get_clientpacks)

    def test_get_clients_status(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_clients_status

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/status/clients",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "172.31.1.1": {
                        "overlay_ipaddress": "172.31.1.1",
                        "managerid": 1,
                        "ipaddress": "10.10.10.27",
                        "tags": {},
                    }
                }
            },
        )(overlay_network_api.get_clients_status)

    def test_get_connected_subnets(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for get_connected_subnets
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/status/connected_subnets",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": [["10.0.1.0", "255.255.255.0"]]},
        )(overlay_network_api.get_connected_subnets)

    def test_get_download_clientpack(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for get_download_clientpack

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/clientpack",
            rest_mocker,
            resp_content_type="application/octet-stream",
            mock_request_from_schema=True,
            mock_response="asdofnaosdfnoasdfiasodiffilefilefilefile",
        )(overlay_network_api.get_download_clientpack)

    def test_post_checkout_next_clientpack(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_checkout_next_clientpack

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/clientpacks/next_available",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=OverlayNetworkApiData.NextClientpackResponse,
        )(overlay_network_api.post_checkout_next_clientpack)

    def test_post_create_clientpack_tag(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_create_clientpack_tag

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/clientpack/{clientpack_name}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=OverlayNetworkApiData.ClientpackTagsResponse,
        )(overlay_network_api.post_create_clientpack_tag)

    def test_delete_clientpack_tag(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for delete_clientpack_tag

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/clientpack/{clientpack_name}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=OverlayNetworkApiData.ClientpackTagsResponse,
        )(overlay_network_api.delete_clientpack_tag)

    def test_post_reset_all_clients(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_reset_all_clients

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/clients/reset_all",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": {"resetting": ["172.16.1.1"]}},
        )(overlay_network_api.post_reset_all_clients)

    def test_post_reset_client(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for post_reset_client

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/client/reset",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "disconnecting": "172_31_1_2",
                    "overlay_ipaddress": "172.31.1.2",
                }
            },
        )(overlay_network_api.post_reset_client)

    def test_post_add_clientpacks(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_add_clientpacks
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/clientpacks/add_clientpacks",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": "15801670638979_696771229646571095757665467757884236311815995938"
            },
        )(overlay_network_api.post_add_clientpacks)

    def test_put_update_clientpack(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for put_update_clientpack

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/clientpack",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": OverlayNetworkApiData.Clientpack},
        )(overlay_network_api.put_update_clientpack)

    def test_put_disconnect_clientpack(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for put_disconnect_clientpack

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/clientpack/{clientpack_name}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "disconnecting": "172_31_1_2",
                    "overlay_ipaddress": "172.31.1.2",
                }
            },
        )(overlay_network_api.put_disconnect_clientpack)

    def test_put_update_all_clientpacks(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for put_update_all_clientpacks
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/clientpacks",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": {"enabled": True, "checked_out": True}},
        )(overlay_network_api.put_update_all_clientpacks)
