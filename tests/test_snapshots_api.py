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
from cohesivenet.api.snapshots_api import SnapshotsApi  # noqa: E501
from cohesivenet.rest import ApiException


class TestSnapshotsApi(unittest.TestCase):
    """SnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = cohesivenet.api.snapshots_api.SnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_snapshot(self):
        """Test case for delete_snapshot

        """
        pass

    def test_get_download_snapshot(self):
        """Test case for get_download_snapshot

        """
        pass

    def test_get_snapshots(self):
        """Test case for get_snapshots

        """
        pass

    def test_post_create_snapshot(self):
        """Test case for post_create_snapshot

        """
        pass

    def test_put_import_snapshot(self):
        """Test case for put_import_snapshot

        """
        pass


if __name__ == "__main__":
    unittest.main()
