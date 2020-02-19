import pytest

from tests.rest_mock import RestClientMock

from cohesivenet import VNS3Client, Configuration, __vns3_spec__, __vns3_version__


def fetch_spec():
    import urllib3, json
    http = urllib3.PoolManager()
    response = http.request("GET", __vns3_spec__)
    if response.status != 200:
        raise RuntimeError(
            "No specification available for testing. "
            "Expected VNS3 v%s specification at %s" % (__vns3_version__, __vns3_spec__))

    return json.loads(response.data.decode("utf8").strip())


API_SCHEMA = fetch_spec()

class MockConstants(object):
    Host = "0.0.0.0"
    Port = "8000"
    User = "api"
    Password = "mockpass1234"
    VerifySSL = False


@pytest.fixture
def api_schema():
    return API_SCHEMA


@pytest.fixture
def rest_mock(mocker):
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
