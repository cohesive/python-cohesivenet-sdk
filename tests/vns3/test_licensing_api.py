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
from cohesivenet.api.vns3 import licensing_api  # noqa: E501
from cohesivenet.rest import ApiException

from tests.openapi import generate_method_test
from tests.stub_data import LicensingApiData


class TestLicensingApi(object):
    """LicensingApi unit test stubs"""

    def test_get_license(self, rest_mocker, api_client, api_schema: dict):
        """Test case for get_license
        """
        generate_method_test(
            api_client,
            api_schema,
            "get",
            "/license",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=LicensingApiData.LicenseDetail,
        )(licensing_api.get_license)

    def test_put_license_upgrade(self, rest_mocker, api_client, api_schema: dict):
        """Test case for put_license_upgrade

        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/license/upgrade",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=LicensingApiData.UpgradeLicenseResponse,
        )(licensing_api.put_license_upgrade)

    def test_put_set_license_parameters(
        self, rest_mocker, api_client, api_schema: dict
    ):
        """Test case for put_set_license_parameters
        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/license/parameters",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=LicensingApiData.LicenseParamsResponse,
        )(licensing_api.put_set_license_parameters)

    def test_upload_license(self, rest_mocker, api_client, api_schema: dict):
        """Test case for upload_license

        """
        generate_method_test(
            api_client,
            api_schema,
            "put",
            "/license",
            rest_mocker,
            mock_request_from_schema=True,
            mock_response=LicensingApiData.LicenseUploadDetail,
        )(licensing_api.upload_license)
