import pytest

from tests.rest_mock import RestClientMock
from tests.stub_data import MockConstants

from cohesivenet import (
    VNS3Client,
    MSClient,
    Configuration,
    __vns3_spec__,
    __vns3_version__,
    __vns3_ms_version__,
    __vns3_ms_spec__
)


@pytest.fixture(scope="session")
def vns3_api_schema():
    from tests.openapi import resolve_refs, fetch_spec
    return resolve_refs(fetch_spec(__vns3_spec__))


@pytest.fixture(scope="session")
def ms_api_schema():
    from tests.openapi import resolve_refs, fetch_spec
    return resolve_refs(fetch_spec(__vns3_ms_spec__))


@pytest.fixture
def rest_mocker(mocker):
    return RestClientMock(mocker)


@pytest.fixture
def vns3_client():
    return VNS3Client(
        configuration=Configuration(
            host="%s:%s" % (MockConstants.Host, MockConstants.Port),
            username=MockConstants.User,
            password=MockConstants.Password,
            verify_ssl=MockConstants.VerifySSL,
        )
    )



@pytest.fixture
def ms_client():
    return MSClient(
        configuration=Configuration(
            host=MockConstants.Host,
            username=MockConstants.User,
            api_key=MockConstants.ApiKey,
            api_token=MockConstants.ApiToken,
            verify_ssl=MockConstants.VerifySSL,
        )
    )
