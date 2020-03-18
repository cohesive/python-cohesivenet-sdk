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
from cohesivenet.api.vns3 import access_api
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.stub_data import AccessApiData


class TestAccessApi(object):
    """AccessApi unit tests stubs"""

    def test_create_access_url(self, rest_mocker, api_client, api_schema: dict):
        """Test case for create_access_url
        """
        generate_method_test(
            api_client,
            api_schema,
            "post",
            "/access/url",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessUrlDetail,
        )(access_api.create_access_url)

    def test_create_api_token(self, rest_mocker, api_client, api_schema: dict):
        """Test case for create_api_token
        """
        generate_method_test(
            api_client,
            api_schema,
            "post",
            "/access/token",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessTokenDetail,
        )(access_api.create_api_token)

    def test_delete_access_url(self, rest_mocker, api_client, api_schema: dict):
        """Test case for delete_access_url
        """
        generate_method_test(
            api_client,
            api_schema,
            "delete",
            "/access/url/{access_url_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessUrlDeleteResponse,
        )(access_api.delete_access_url)

    def test_delete_access_url_by_search(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for delete_access_url_by_search
        """
        generate_method_test(
            api_client,
            api_schema,
            "delete",
            "/access/url",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessUrlDeleteResponse,
        )(access_api.delete_access_url_by_search)

    def test_delete_api_token(self, rest_mocker, api_client, api_schema: dict):
        """Test case for delete_api_token
        """
        generate_method_test(
            api_client,
            api_schema,
            "delete",
            "/access/token/{token_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessTokenDeleteResponse,
        )(access_api.delete_api_token)

    def test_get_access_urls(self, rest_mocker, api_client, api_schema: dict):
        """Test case for get_access_urls
        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/access/urls",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessUrlListResponse,
        )(access_api.get_access_urls)

    def test_get_access_url(self, rest_mocker, api_client, api_schema: dict):
        """Test case for get_access_url
        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/access/url/{access_url_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessUrlDetail,
        )(access_api.get_access_url)

    def test_get_api_token(self, rest_mocker, api_client, api_schema: dict):
        """Test case for get_api_token
        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/access/token/{token_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessTokenDetail,
        )(access_api.get_api_token)

    def test_get_api_tokens(self, rest_mocker, api_client, api_schema: dict):
        """Test case for get_api_tokens
        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/access/tokens",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessTokenListResponse,
        )(access_api.get_api_tokens)

    def test_put_expire_access_url(self, rest_mocker, api_client, api_schema: dict):
        """Test case for put_expire_access_url
        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/access/url/{access_url_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessUrlDetail,
        )(access_api.put_expire_access_url)

    def test_put_expire_api_token(self, rest_mocker, api_client, api_schema: dict):
        """Test case for put_expire_api_token
        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/access/token/{token_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=AccessApiData.AccessTokenDetail,
        )(access_api.put_expire_api_token)
