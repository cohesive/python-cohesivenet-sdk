import pytest

from tests.rest_mock import RestClientMock

from cohesivenet import VNS3Client, Configuration, __vns3_spec__, __vns3_version__


SPEC = "https://cohesive-networks.s3.amazonaws.com/apis/vns3/vns3-v4-8-1.oasv3.json"


def fetch_spec(spec):
    import urllib3, json

    http = urllib3.PoolManager()
    response = http.request("GET", spec)
    if response.status != 200:
        raise RuntimeError(
            "No specification available for testing. "
            "Expected VNS3 specification at %s" % spec
        )
    from tests.openapi import resolve_refs

    open("spec.json", "w").write(response.data.decode("utf8").strip())
    resolved = resolve_refs(json.loads(response.data.decode("utf8").strip()))
    open("spec-resolved.json", "w").write(json.dumps(resolved, indent=2))
    return json.loads(response.data.decode("utf8").strip())


API_SCHEMA = fetch_spec(__vns3_spec__)


class MockConstants(object):
    Host = "0.0.0.0"
    Port = "8000"
    User = "api"
    Password = "mockpass1234"
    VerifySSL = False


@pytest.fixture
def api_schema():
    from tests.openapi import resolve_refs

    return resolve_refs(API_SCHEMA)


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
