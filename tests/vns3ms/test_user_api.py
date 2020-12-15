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
from cohesivenet.api.vns3ms import user_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3ms.stub_data import UserApiData


class TestMSUserApi(object):
    """VNS3:ms User API unit tests"""

    def test_put_user_password(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for put_user_password"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/user/password",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(user_api.put_user_password)

    def test_get_user_credentials(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for get_user_credentials"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "GET",
            "/user/credentials",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=UserApiData.CredsList,
        )(user_api.get_user_credentials)

    def test_post_create_user_credential(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for post_create_user_credential"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "POST",
            "/user/credentials",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response_type": "success",
                "response": {"message": "User credentials saved. Validating.", "id": 1},
            },
        )(user_api.post_create_user_credential)

    def test_put_update_user_credential(
        self, rest_mocker, ms_client, ms_api_schema: dict
    ):
        """Test case for put_update_user_credential"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "PUT",
            "/user/credentials/{credential_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(user_api.put_update_user_credential)

    def test_delete_user_credential(self, rest_mocker, ms_client, ms_api_schema: dict):
        """Test case for delete_user_credential"""
        generate_method_test(
            ms_client,
            ms_api_schema,
            "DELETE",
            "/user/credentials/{credential_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response_from_schema=True,
        )(user_api.delete_user_credential)
