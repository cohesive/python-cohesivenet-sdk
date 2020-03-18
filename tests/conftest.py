import pytest

from tests.rest_mock import RestClientMock

from cohesivenet import VNS3Client, Configuration, __vns3_spec__, __vns3_version__


def fetch_spec(spec):
    import urllib3, json, os

    http = urllib3.PoolManager()
    response = http.request("GET", spec)
    if response.status != 200:
        raise RuntimeError(
            "No specification available for testing. "
            "Expected VNS3 specification at %s" % spec
        )
    from tests.openapi import resolve_refs

    _raw_spec = response.data.decode("utf8").strip()

    if os.environ.get("DOWNLOAD_SPECS"):
        open("spec.json", "w").write(_raw_spec)
        open("spec-resolved.json", "w").write(json.dumps(resolve_refs(_raw_spec), indent=2))
    return json.loads(_raw_spec)


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
