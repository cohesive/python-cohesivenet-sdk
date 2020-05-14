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
from cohesivenet.api.vns3ms import administration_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.vns3ms.stub_data import AdminApiData
from tests.openapi import generate_method_test


class TestMSAdminApi(object):
    """VNS3:ms Admin API unit tests"""

    def test_put_enable_ldap(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_enable_ldap
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/admin/ldap",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type":"success",
                "response":{"ldap_enabled":False}
            },
        )(administration_api.put_enable_ldap)

    def test_get_ldap_settings(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_ldap_settings
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/admin/ldap/settings",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AdminApiData.LdapSettingsResponse,
        )(administration_api.get_ldap_settings)

    def test_put_ldap_settings(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_ldap_settings
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/admin/ldap/settings",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response_type":"success","response":"Settings updated"},
        )(administration_api.put_ldap_settings)

    def test_post_validate_ldap_settings(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_validate_ldap_settings
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/admin/ldap/settings",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type":"error",
                "response":{
                    "connect_success":False,
                    "message":"Connection timed out - user specified timeout"
                }
            },
        )(administration_api.post_validate_ldap_settings)

    def test_get_ldap_user_schema(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_ldap_user_schema
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/admin/ldap/user_schema",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AdminApiData.LdapUserSchemaResponse
        )(administration_api.get_ldap_user_schema)

    def test_put_ldap_user_schema(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_ldap_user_schema
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/admin/ldap/user_schema",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(administration_api.put_ldap_user_schema)

    def test_post_validate_ldap_user_schema(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_validate_ldap_user_schema
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/admin/ldap/user_schema",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": [
                    "user"
                ]
            }
        )(administration_api.post_validate_ldap_user_schema)

    def test_get_ldap_group_schema(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_ldap_group_schema
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/admin/ldap/group_schema",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AdminApiData.LdapGroupSchemaResponse
        )(administration_api.get_ldap_group_schema)

    def test_put_ldap_group_schema(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_ldap_group_schema
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/admin/ldap/group_schema",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True
        )(administration_api.put_ldap_group_schema)

    def test_post_validate_ldap_group_schema(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for post_validate_ldap_group_schema
        """
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/admin/ldap/group_schema",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": [
                    "group"
                ]
            }
        )(administration_api.post_validate_ldap_group_schema)
