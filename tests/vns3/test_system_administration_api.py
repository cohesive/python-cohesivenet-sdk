# # coding: utf-8

# """
#     VNS3 Controller API

#     Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

#     The version of the OpenAPI document: 4.8
#     Contact: solutions@cohesive.net
#     Generated by: https://openapi-generator.tech
# """


# from __future__ import absolute_import

# import pytest

# from tests.rest_mock import RestClientMock

# from cohesivenet import VNS3Client, models, Configuration
# from cohesivenet.rest import ApiException


# class TestSystemAdministrationApi(object):
#     """SystemAdministrationApi unit test stubs. Unlicensed allowed"""

#     def test_delete_access_url(self):
#         """Test case for delete_access_url

#         """
#         pass

#     def test_delete_access_url_by_id(self):
#         """Test case for delete_access_url_by_id

#         """
#         pass

#     def test_delete_api_access_token(self):
#         """Test case for delete_api_access_token

#         """
#         pass

#     def test_get_access_urls(self):
#         """Test case for get_access_urls

#         """
#         pass

#     def test_get_access_url(self):
#         """Test case for get_access_url

#         """
#         pass

#     def test_get_api_access_token(self):
#         """Test case for get_api_access_token

#         """
#         pass

#     def test_get_api_access_tokens(self):
#         """Test case for get_api_access_tokens

#         """
#         pass

#     def test_get_cloud_data_aws(self, rest_mocker):
#         """Test case for get_cloud_data

#         """
#         rest_mocker.stub_request(
#             "get",
#             "/api/cloud_data",
#             {
#                 "response": {
#                     "cloud_data": {
#                         "accountId": "947761958079",
#                         "architecture": "x86_64",
#                         "availabilityZone": "us-east-1a",
#                         "billingProducts": None,
#                         "devpayProductCodes": None,
#                         "imageId": "ami-034b377bde620d2a8",
#                         "instanceId": "i-0b96e779c3143cf66",
#                         "instanceType": "t3.small",
#                         "kernelId": None,
#                         "marketplaceProductCodes": None,
#                         "pendingTime": "2019-11-08T16:18:38Z",
#                         "privateIp": "10.0.1.37",
#                         "ramdiskId": None,
#                         "region": "us-east-1",
#                         "version": "2017-09-30",
#                     },
#                     "cloud_type": "ec2",
#                 }
#             },
#         )

#         api_client = VNS3Client(
#             configuration=Configuration(
#                 host="0.0.0.0:8000",
#                 username="api",
#                 password="password",
#                 verify_ssl=False,
#             )
#         )

#         resp = api_client.sys_admin.get_cloud_data()
#         assert type(resp) is models.CloudInfoDetail
#         assert resp.response.cloud_type == "ec2"
#         assert resp.response.cloud_data["accountId"] == "947761958079"

#     @pytest.mark.licensed
#     def test_get_status(self):
#         """Test case for get_status

#         """
#         pass

#     @pytest.mark.licensed
#     def test_get_system_status(self):
#         """Test case for get_system_status

#         """
#         pass

#     @pytest.mark.licensed
#     def test_get_task_status(self):
#         """Test case for get_task_status

#         """
#         pass

#     def test_post_create_access_url(self):
#         """Test case for post_create_access_url

#         """
#         pass

#     def test_post_create_api_access_token(self):
#         """Test case for post_create_api_access_token

#         """
#         pass

#     def test_post_generate_keypair(self):
#         """Test case for post_generate_keypair

#         """
#         pass

#     def test_put_expire_access_url(self):
#         """Test case for put_expire_access_url

#         """
#         pass

#     def test_put_expire_api_access_token(self):
#         """Test case for put_expire_api_access_token

#         """
#         pass

#     def test_put_remote_support(self, rest_mock: RestClientMock):
#         """Test case for put_remote_support

#         """
#         method, uri = "put", "/api/remote_support"
#         rest_mock.stub_request(
#             method, uri, {"response": {"enabled": False, "revoke_credential": True}}
#         )

#         api_client = VNS3Client(
#             configuration=Configuration(
#                 host="0.0.0.0:8000",
#                 username="api",
#                 password="password",
#                 verify_ssl=False,
#             )
#         )

#         request = {"enabled": False, "revoke": True}
#         resp = api_client.sys_admin.put_remote_support(request)
#         assert type(resp) is models.RemoteSupportStatusResponse
#         assert not resp.response.enabled and resp.response.revoke_credential
#         rest_mock.assert_requested(method, uri, body=request)

#     @pytest.mark.licensed
#     def test_put_server_action(self):
#         """Test case for put_server_action

#         """
#         pass
