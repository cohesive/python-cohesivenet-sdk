# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

from tests.rest_mock import RestClientMock

from cohesivenet import VNS3Client, models, Configuration
from cohesivenet.rest import ApiException


class TestConfigurationApi(object):
    """
    ConfigurationApi unit test stubs
    
    Under test: cohesivenet.api.vns3.configuration_api.ConfigurationApi
    """

    def test_get_config(self, rest_mock: RestClientMock):
        """Test case for get_config

        """
        print(rest_mock)
        rest_mock.stub_request('get', '/api/config', {
            'response': {
                'asn': None,
                'licensed': False,
                'manager_id': None,
                'ntp_hosts': '0.ubuntu.pool.ntp.org 1.ubuntu.pool.ntp.org '
                            '2.ubuntu.pool.ntp.org 3.ubuntu.pool.ntp.org '
                            'ntp.ubuntu.com time.apple.com',
                'overlay_ipaddress': None,
                'peered': None,
                'private_ipaddress': '10.0.1.56',
                'public_ipaddress': '3.86.152.210',
                'security_token': None,
                'topology_checksum': 'fdae64751d4090aee13b8a26c5890eef7f75dc82',
                'topology_name': None,
                'vns3_version': '4.8.3-20190926'
            }
        })

        api_client = VNS3Client(
            configuration=Configuration(
                host='0.0.0.0:8000',
                username='api',
                password='password',
                verify_ssl=False
            )
        )

        resp = api_client.config.get_config()
        assert type(resp) is models.ConfigDetail
        assert resp.response.licensed is False


    def test_get_keyset(self):
        """Test case for get_keyset

        """
        pass

    def test_get_runtime(self):
        """Test case for get_runtime

        """
        pass

    def test_get_ssl_install_status(self):
        """Test case for get_ssl_install_status

        """
        pass

    def test_put_config(self):
        """Test case for put_config

        """
        pass

    def test_put_install_ssl_keypair(self):
        """Test case for put_install_ssl_keypair

        """
        pass

    def test_put_keyset(self):
        """Test case for put_keyset

        """
        pass

    def test_put_update_admin_ui(self):
        """Test case for put_update_admin_ui

        """
        # {'response': {'admin_password': None, 'admin_username': None, 'enabled': True}}

    def test_put_update_api_password(self):
        """Test case for put_update_api_password

        """
        # {'response': {'password_reset': 'ok'}}

    def test_put_upload_ssl_keypair(self):
        """Test case for put_upload_ssl_keypair

        """
        pass
