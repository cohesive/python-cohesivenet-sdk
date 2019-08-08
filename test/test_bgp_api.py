# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API for configuring and retrieving VNS3 controller  # noqa: E501

    The version of the OpenAPI document: 4.7
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.bgp_api import BGPApi  # noqa: E501
from openapi_client.rest import ApiException


class TestBGPApi(unittest.TestCase):
    """BGPApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.bgp_api.BGPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_ipsec_endpoint_bgp_peer(self):
        """Test case for delete_ipsec_endpoint_bgp_peer

        """
        pass

    def test_post_create_ipsec_endpoint_bgp_peer(self):
        """Test case for post_create_ipsec_endpoint_bgp_peer

        """
        pass

    def test_put_edit_ipsec_endpoint_bgp_peer(self):
        """Test case for put_edit_ipsec_endpoint_bgp_peer

        """
        pass


if __name__ == '__main__':
    unittest.main()
