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
from cohesivenet.api.vns3.ipsec_api import IPsecApi  # noqa: E501
from cohesivenet.rest import ApiException


class TestIPsecApi(unittest.TestCase):
    """IPsecApi unit test stubs"""

    def setUp(self):
        self.api = cohesivenet.api.vns3.ipsec_api.IPsecApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_ipsec_endpoint(self):
        """Test case for delete_ipsec_endpoint

        """
        pass

    def test_delete_ipsec_endpoint_tunnel(self):
        """Test case for delete_ipsec_endpoint_tunnel

        """
        pass

    def test_get_ipsec(self):
        """Test case for get_ipsec

        """
        pass

    def test_get_ipsec_endpoint(self):
        """Test case for get_ipsec_endpoint

        """
        pass

    def test_get_ipsec_status(self):
        """Test case for get_ipsec_status

        """
        pass

    def test_get_link_history(self):
        """Test case for get_link_history

        """
        pass

    def test_post_create_ipsec_endpoint(self):
        """Test case for post_create_ipsec_endpoint

        """
        pass

    def test_post_create_ipsec_endpoint_tunnel(self):
        """Test case for post_create_ipsec_endpoint_tunnel

        """
        pass

    def test_post_restart_ipsec_action(self):
        """Test case for post_restart_ipsec_action

        """
        pass

    def test_put_edit_ipsec_endpoint(self):
        """Test case for put_edit_ipsec_endpoint

        """
        pass

    def test_put_edit_ipsec_endpoint_tunnel(self):
        """Test case for put_edit_ipsec_endpoint_tunnel

        """
        pass

    def test_put_ipsec_config(self):
        """Test case for put_ipsec_config

        """
        pass


if __name__ == "__main__":
    unittest.main()
