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
from cohesivenet.api.vns3 import system_administration_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3.stub_data import SystemAdminApiData


class TestSystemAdministrationApi(object):
    """SystemAdministrationApi unit test stubs. Unlicensed allowed"""

    def test_get_cloud_data_aws(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_cloud_data

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/cloud_data",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=SystemAdminApiData.CloudDataDetail,
        )(system_administration_api.get_cloud_data)

    def test_get_runtime_status(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_runtime_status

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/status",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=SystemAdminApiData.VNS3Status,
        )(system_administration_api.get_runtime_status)

    def test_get_system_status(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_system_status

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/status/system",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=SystemAdminApiData.SystemStatus,
        )(system_administration_api.get_system_status)

    def test_get_task_status(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_task_status

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/status/task",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": {"task_status": "finished_fail"}},
        )(system_administration_api.get_task_status)

    def test_post_generate_support_keypair(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_generate_support_keypair

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/remote_support/keypair",
            rest_mocker,
            resp_content_type="application/octet-stream",
            mock_request_from_schema=True,
            mock_response=b"filefilefilefilefilefilefilefile",
        )(system_administration_api.post_generate_support_keypair)

    def test_get_remote_support_details(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for get_remote_support_details
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/remote_support",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=SystemAdminApiData.RemoteSupportDetails,
        )(system_administration_api.get_remote_support_details)

    def test_put_update_remote_support(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for put_update_remote_support
        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/remote_support",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=SystemAdminApiData.UpdateRemoteSupportResponse,
        )(system_administration_api.put_update_remote_support)

    def test_put_server_action(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for put_server_action

        """
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/server",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": {"status": "rebooting"}},
        )(system_administration_api.put_server_action)

    def test_wait_for_api(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for wait_for_api
        """
        pass
