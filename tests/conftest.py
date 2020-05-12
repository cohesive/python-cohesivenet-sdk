import pytest

from tests.rest_mock import RestClientMock

from cohesivenet import VNS3Client, Configuration, __vns3_spec__, __vns3_version__


class MockConstants(object):
    Host = "0.0.0.0"
    Port = "8000"
    User = "api"
    Password = "mockpass1234"
    VerifySSL = False


@pytest.fixture(scope="session")
def api_schema():
    from tests.openapi import resolve_refs, fetch_spec

    return resolve_refs(fetch_spec(__vns3_spec__))


@pytest.fixture
def rest_mocker(mocker):
    return RestClientMock(mocker)


@pytest.fixture
def api_client():
    return VNS3Client(
        configuration=Configuration(
            host="%s:%s" % (MockConstants.Host, MockConstants.Port),
            username=MockConstants.User,
            password=MockConstants.Password,
            verify_ssl=MockConstants.VerifySSL,
        )
    )
