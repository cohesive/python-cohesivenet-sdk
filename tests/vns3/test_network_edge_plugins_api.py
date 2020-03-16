# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network"s addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import pytest

import cohesivenet
from cohesivenet.api.vns3 import network_edge_plugins_api
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.stub_data import NetworkEdgePluginsApiData


class TestNetworkEdgePluginsApi(object):
    """NetworkEdgePluginsApi unit test stubs"""

    def test_delete_container(self, rest_mocker, api_client, api_schema: dict):
        """Test case for delete_container

        """
        generate_method_test(
            api_client,
            api_schema,
            "delete",
            "/container_system/containers/{uuid}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "uuid": "5c22b4e31cccfc568b770fd576b41865f36aee1293cd354cbee5494cc1e81f21",
                    "container_deleted": True,
                }
            },
        )(network_edge_plugins_api.delete_container)

    def test_delete_container_image(self, rest_mocker, api_client, api_schema: dict):
        """Test case for delete_container_image

        """
        generate_method_test(
            api_client,
            api_schema,
            "delete",
            "/container_system/images/{uuid}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "image_deleted": True,
                    "uuid": "0a796fbe41436924cebfedac0c8966c6f491e1089c35b5582955d48f94d5397c",
                }
            },
        )(network_edge_plugins_api.delete_container_image)

    def test_get_container_logs(self, rest_mocker, api_client, api_schema: dict):
        """Test case for get_container_logs

        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/container_system/containers/{uuid}/logs",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=NetworkEdgePluginsApiData.ContainerLogsResponse,
        )(network_edge_plugins_api.get_container_logs)

    def test_get_container_system_ips(self, rest_mocker, api_client, api_schema: dict):
        """Test case for get_container_system_ips

        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/container_system/ip_addresses",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=NetworkEdgePluginsApiData.ContainerSystemIPs,
        )(network_edge_plugins_api.get_container_system_ips)

    def test_get_container_system_images(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for get_container_system_images
        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/container_system/images",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=NetworkEdgePluginsApiData.ContainerImagesResponse,
        )(network_edge_plugins_api.get_container_system_images)

    def test_get_container_system_running_containers(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for get_container_system_running_containers

        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/container_system/containers",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=NetworkEdgePluginsApiData.ContainersListResponse,
        )(network_edge_plugins_api.get_container_system_running_containers)

    def test_get_container_system_status(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for get_container_system_status

        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/container_system",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=NetworkEdgePluginsApiData.ContainerSystemStatus,
        )(network_edge_plugins_api.get_container_system_status)

    def test_post_action_container_system(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for post_action_container_system

        """
        generate_method_test(
            api_client,
            api_schema,
            "post",
            "/container_system",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {"running": "starting", "network": "198.51.100.0/28"}
            },
        )(network_edge_plugins_api.post_action_container_system)

    def test_post_commit_container(self, rest_mocker, api_client, api_schema: dict):
        """Test case for post_commit_container

        """
        generate_method_test(
            api_client,
            api_schema,
            "post",
            "/container_system/containers/{uuid}/commit",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "uuid": "sha256:1108c298fc5f02dcc21c655a1ca7ae7abf2c9ef05617a0d620dc8b6ba59bd0ae",
                    "name": "bens-new-image",
                }
            },
        )(network_edge_plugins_api.post_commit_container)

    def test_post_create_container_image(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for post_create_container_image

        """
        generate_method_test(
            api_client,
            api_schema,
            "post",
            "/container_system/images",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "import_uuid": "1108c298fc5f02dcc21c655a1ca7ae7abf2c9ef05617a0d620dc8b6ba59bd0ae",
                    "status": "Image being uploaded",
                }
            },
        )(network_edge_plugins_api.post_create_container_image)

    def test_post_start_container(self, rest_mocker, api_client, api_schema: dict):
        """Test case for post_start_container

        """
        generate_method_test(
            api_client,
            api_schema,
            "post",
            "/container_system/containers",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "ip_address": "198.51.100.3",
                    "status": "Running",
                    "uuid": "09334531f1892b6a9bbd63c9e8aff64ac237aea18159dd41d645814ba95b733f",
                    "container_started": True,
                }
            },
        )(network_edge_plugins_api.post_start_container)

    def test_put_configure_container_system(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for put_configure_container_system

        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/container_system",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=NetworkEdgePluginsApiData.ContainerSystemStatus,
        )(network_edge_plugins_api.put_configure_container_system)

    def test_put_edit_container_image(self, rest_mocker, api_client, api_schema: dict):
        """Test case for put_edit_container_image

        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/container_system/images/{uuid}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "status": "Image updated",
                    "uuid": "sha256:3ba915f8153cb7443aafce77cb4f250b1d0fcb861c297ae7d04ec67f7ec259fa",
                }
            },
        )(network_edge_plugins_api.put_edit_container_image)

    def test_put_stop_container(self, rest_mocker, api_client, api_schema: dict):
        """Test case for put_stop_container
        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/container_system/containers/{uuid}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "status": "Stopped",
                    "uuid": "5c22b4e31cccfc568b770fd576b41865f36aee1293cd354cbee5494cc1e81f21",
                }
            },
        )(network_edge_plugins_api.put_stop_container)
