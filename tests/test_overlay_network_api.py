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
from cohesivenet.api.overlay_network_api import OverlayNetworkApi  # noqa: E501
from cohesivenet.rest import ApiException


class TestOverlayNetworkApi(unittest.TestCase):
    """OverlayNetworkApi unit test stubs"""

    def setUp(self):
        self.api = cohesivenet.api.overlay_network_api.OverlayNetworkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_clientpack_tag(self):
        """Test case for delete_clientpack_tag

        """
        pass

    def test_get_clientpack(self):
        """Test case for get_clientpack

        """
        pass

    def test_get_clientpacks(self):
        """Test case for get_clientpacks

        """
        pass

    def test_get_clients_status(self):
        """Test case for get_clients_status

        """
        pass

    def test_get_connected_subnets(self):
        """Test case for get_connected_subnets

        """
        pass

    def test_get_download_clientpack(self):
        """Test case for get_download_clientpack

        """
        pass

    def test_post_calc_next_clientpack(self):
        """Test case for post_calc_next_clientpack

        """
        pass

    def test_post_clientpack_tag(self):
        """Test case for post_clientpack_tag

        """
        pass

    def test_post_reset_all_clients(self):
        """Test case for post_reset_all_clients

        """
        pass

    def test_post_reset_client(self):
        """Test case for post_reset_client

        """
        pass

    def test_put_add_clientpacks(self):
        """Test case for put_add_clientpacks

        """
        pass

    def test_put_clientpack(self):
        """Test case for put_clientpack

        """
        pass

    def test_put_disconnect_clientpack(self):
        """Test case for put_disconnect_clientpack

        """
        pass

    def test_put_update_clientpacks(self):
        """Test case for put_update_clientpacks

        """
        pass


if __name__ == '__main__':
    unittest.main()