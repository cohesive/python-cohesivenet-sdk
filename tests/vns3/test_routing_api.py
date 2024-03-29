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
from cohesivenet.api.vns3 import routing_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3.stub_data import RoutingApiData


class TestRoutingApi(object):
    """RoutingApi unit test stubs"""

    def test_delete_route(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for delete_route"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/routes/{route_id}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=RoutingApiData.RoutesResponse,
        )(routing_api.delete_route)

    def test_get_routes(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_routes"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/routes",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=RoutingApiData.RoutesResponse,
        )(routing_api.get_routes)

    def test_post_create_route(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for post_create_route"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/routes",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=RoutingApiData.RoutesResponse,
        )(routing_api.post_create_route)

    def test_disable_route(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for disable_route"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/routes/{route_id}/disable",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=RoutingApiData.RouteDetailResponse,
        )(routing_api.disable_route)

    def test_enable_route(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for enable_route"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/routes/{route_id}/enable",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=RoutingApiData.RouteDetailResponse,
        )(routing_api.enable_route)

    def test_post_create_route_already_exists(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_create_route_if_not_exists"""
        # need custom method for this one. different interface
        pass
