import pytest

from tests.rest_mock import RestClientMock

from cohesivenet import VNS3Client, Configuration


class MockConstants(object):
    Host = '0.0.0.0'
    Port = '8000'
    User = 'api'
    Password = 'mockpass1234'
    VerifySSL = False


@pytest.fixture
def rest_mock(mocker):
    return RestClientMock(mocker)


@pytest.fixture
def api_client():
    return VNS3Client(
        configuration=Configuration(
            host='%s:%s' % (MockConstants.Host, MockConstants.Port),
            username=MockConstants.User,
            password=MockConstants.Password,
            verify_ssl=MockConstants.VerifySSL
        )
    )