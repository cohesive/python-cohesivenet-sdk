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
from cohesivenet.api.vns3ms import system_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3ms.stub_data import SystemApiData


class TestMSSystemApi(object):
    """VNS3:ms System API unit tests"""

    def test_get_remote_support_details(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_remote_support_details
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/remote_support",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response_type":"success","response":{"remote_support_enabled":False}}
        )(system_api.get_remote_support_details)

    def test_put_remote_support(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_remote_support
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/system/remote_support",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.put_remote_support)

    def test_get_remote_support_keypair_details(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_remote_support_keypair_details
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/remote_support/keypair",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.get_remote_support_keypair_details)

    def test_post_generate_remote_support_keypair(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_generate_remote_support_keypair
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/system/remote_support/keypair",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.post_generate_remote_support_keypair)

    def test_delete_remote_support_keypair(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_remote_support_keypair
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/system/remote_support/keypair",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response_type":"success","response":{"keypair_installed":False}}
        )(system_api.delete_remote_support_keypair)

    def test_get_system_status(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_system_status
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/status",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=SystemApiData.SystemStatusResponse
        )(system_api.get_system_status)

    def test_get_credential_types(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_credential_types
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/credential_types",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response_type":"success","response":[{"name":"EC2","code":"ec2"}]}
        )(system_api.get_credential_types)

    def test_get_credential_type_details(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_credential_type_details
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/credential_types/{code}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.get_credential_type_details)

    def test_get_system_ntp_hosts(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_system_ntp_hosts
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/ntp_hosts",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=SystemApiData.NTPHosts
        )(system_api.get_system_ntp_hosts)

    def test_post_add_ntp_host(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_add_ntp_host
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/system/ntp_hosts",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.post_add_ntp_host)

    def test_delete_ntp_host(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_ntp_host
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/system/ntp_hosts/{host_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.delete_ntp_host)

    def test_delete_ssl_install(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_ssl_install
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/system/ssl",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.delete_ssl_install)

    def test_get_ssl_install_status(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_ssl_install_status
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/ssl/install/{uuid}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.test_get_ssl_install_status)

    def test_put_upload_ssl_certs(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_upload_ssl_certs
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/system/ssl/keypair",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.put_upload_ssl_certs)

    def test_put_install_ssl_certs(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_install_ssl_certs
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/system/ssl/install",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.put_install_ssl_certs)

    def test_get_job_status(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_job_status
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/system/jobs/{uuid}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(system_api.get_job_status)
