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
from cohesivenet.api.vns3 import firewall_api
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.vns3.stub_data import FirewallApiData


class TestFirewallApi(object):
    """FirewallApi unit test stubs"""

    def test_post_create_firewall_rule_v1(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_create_firewall_rule_v1"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/firewall/rules",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "status": "submitted",
                    "rule": "POSTROUTING_CUST -o eth0 -s 198.51.100.0/28 -j SNAT --to 10.0.1.120",
                    "token": "15798987631596_5280108744805298913050300048466684878015928855",
                }
            },
        )(firewall_api.post_create_firewall_rule_v1)

    def test_delete_firewall_rule_by_position(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for delete_firewall_rule_by_position"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/firewall/rules/{position}",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "status": "submitted",
                    "rule": "MACRO_CUST -o eth0 -s 198.51.100.0/28 -j MASQUERADE\n",
                    "position": 1,
                    "token": "15799073889568_958635609379530042894988535092666127141377814351",
                }
            },
        )(firewall_api.delete_firewall_rule_by_position)

    def test_delete_firewall_rule_by_rule(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for delete_firewall_rule_by_rule"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/firewall/rules",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "status": ":finished_ok, Matching rule found.",
                    "rule": "FORWARD_CUST -s 10.0.1.0/24 -d 10.0.3.0/24 -j ACCEPT",
                    "position": 4,
                }
            },
        )(firewall_api.delete_firewall_rule_by_rule)

    def test_delete_firewall_subgroup(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for delete_firewall_subgroup"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/firewall/rules/subgroup",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": {"status": "finished_ok"}},
        )(firewall_api.delete_firewall_subgroup)

    def test_get_firewall_fw_sets(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for get_firewall_fw_sets"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/firewall/fwsets",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": ["PORTS_policy53 1194-1197", "PORTS_policy53 8080"]
            },
        )(firewall_api.get_firewall_fw_sets)

    def test_post_create_firewall_fw_set(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_create_firewall_fw_set"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/firewall/fwsets",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "status": "ok",
                    "rules": "PORTS_policy53 1194-1197\n PORTS_policy53 8080",
                }
            },
        )(firewall_api.post_create_firewall_fw_set)

    def test_delete_firewall_fw_set(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for delete_firewall_fw_set"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "delete",
            "/firewall/fwsets",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={"response": {"status": "finished_ok"}},
        )(firewall_api.delete_firewall_fw_set)

    def test_get_firewall_rules_v1(self, rest_mocker, vns3_client, vns3_api_schema: dict):
        """Test case for get_firewall_rules_v1"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/firewall/rules",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": [
                    [
                        "POSTROUTING_CUST -o eth0 -s 198.51.100.0/28 -j SNAT --to 10.0.1.120\n",
                        0,
                    ],
                    ["MACRO_CUST -o eth0 -s 198.51.100.0/28 -j MASQUERADE\n", 1],
                    ["FORWARD_CUST -s 198.51.100.0/28 -j ACCEPT\n", 2],
                    ["FORWARD_CUST -d 198.51.100.0/28 -j ACCEPT\n", 3],
                    [
                        "PREROUTING_CUST -i eth0 -p tcp -s 0.0.0.0/0 --dport 44 -j DNAT --to 198.51.100.2:22\n",
                        4,
                    ],
                    ["FORWARD_CUST -s 10.0.1.0/24 -d 10.0.3.0/24 -j ACCEPT\n", 5],
                    ["FORWARD_CUST -d 10.0.1.0/24 -s 10.0.3.0/24 -j ACCEPT", 6],
                ]
            },
        )(firewall_api.get_firewall_rules_v1)

    def test_get_firewall_rule_subgroups(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for get_firewall_rule_subgroups"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "get",
            "/firewall/rules/subgroup",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": [
                    ["INP_C_bensothergroup"],
                    ["INP_C_bensnewgroup -s 198.31.50.0/24 -j DROP"],
                ]
            },
        )(firewall_api.get_firewall_rule_subgroups)

    def test_post_create_firewall_subgroup(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for post_create_firewall_subgroup"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "post",
            "/firewall/rules/subgroup",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={
                "response": {
                    "status": "ok",
                    "rules": "INP_C_bensnewgro -s 198.31.50.0/24 -j DROP\n",
                }
            },
        )(firewall_api.post_create_firewall_subgroup)

    def test_put_reinitialize_fw_sets(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for put_reinitialize_fw_sets"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/firewall/fwsets",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={},
        )(firewall_api.put_reinitialize_fw_sets)

    def test_put_reinitialize_subgroups(
        self, rest_mocker, vns3_client, vns3_api_schema: dict
    ):
        """Test case for put_reinitialize_subgroups"""
        generate_method_test(
            vns3_client,
            vns3_api_schema,
            "put",
            "/firewall/rules/subgroup",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response={},
        )(firewall_api.put_reinitialize_subgroups)
