# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import cohesivenet
from cohesivenet.api.interfaces_api import InterfacesApi  # noqa: E501
from cohesivenet.rest import ApiException


class TestInterfacesApi(unittest.TestCase):
    """InterfacesApi unit test stubs"""

    def setUp(self):
        self.api = cohesivenet.api.interfaces_api.InterfacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_gre_endpoint(self):
        """Test case for delete_gre_endpoint

        """
        pass

    def test_delete_system_interface(self):
        """Test case for delete_system_interface

        """
        pass

    def test_get_edge_gre_endpoints(self):
        """Test case for get_edge_gre_endpoints

        """
        pass

    def test_get_gre_endpoint_details(self):
        """Test case for get_gre_endpoint_details

        """
        pass

    def test_get_interfaces(self):
        """Test case for get_interfaces

        """
        pass

    def test_get_system_interface_details(self):
        """Test case for get_system_interface_details

        """
        pass

    def test_get_system_interfaces(self):
        """Test case for get_system_interfaces

        """
        pass

    def test_post_action_interfaces(self):
        """Test case for post_action_interfaces

        """
        pass

    def test_post_create_gre_endpoint(self):
        """Test case for post_create_gre_endpoint

        """
        pass

    def test_post_create_system_interface(self):
        """Test case for post_create_system_interface

        """
        pass

    def test_put_update_gre_endpoint(self):
        """Test case for put_update_gre_endpoint

        """
        pass

    def test_put_update_system_interface(self):
        """Test case for put_update_system_interface

        """
        pass


if __name__ == "__main__":
    unittest.main()
