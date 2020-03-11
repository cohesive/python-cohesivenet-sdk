class ConfigurationApiData(object):
    ConfigDetail = {
        "response": {
            "private_ipaddress": "10.0.1.211", 
            "public_ipaddress": "52.202.254.43",
            "topology_checksum": "9e29c480e3a20f1a9e4fd7f453f8da7280bdada4",
            "vns3_version":"4.8.4-20191220",
            "topology_name":"My-topology-name",
            "ntp_hosts": "0.ubuntu.pool.ntp.org 1.ubuntu.pool.ntp.org 2.ubuntu.pool.ntp.org 3.ubuntu.pool.ntp.org ntp.ubuntu.com time.apple.com",
            "licensed": False
        }
    }

    KeysetDetail = {
        "response": {
            "keyset_present": True,
            "created_at":"2020-01-24T20:42:56.500+00:00",
            "created_at_i": 1579898576,
            "checksum": "8e4f8ae182a41a047c206c099c62fa0ea59ebbcb",
            "uuid": "184f06f0-3eea-11ea-ad17-02e11c8e6b1d"
        }
    }

    UpdateUIAdminResponse = {
        "response": {
            "enabled": True,
            # "username": "vnscubed",
            "admin_username": "vnscubed"
        }
    }

class IpsecApiData(object):
    IpsecEndpointDetail = {
        "response": {
            "name": "EndpointB",
            "ipaddress": "13.53.72.182",
            "pfs": True,
            "id": 1,
            # "ike_version": 1,
            "ike_version": "1",
            "nat_t_enabled": True,
            "private_ipaddress": "192.0.2.254",
            "extra_config": [],
            "tunnels": {
                "3": {
                    "id": 3,
                    "local_subnet": "172.31.0.0/28",
                    "remote_subnet": "192.168.10.0/22",
                    "endpoint_id": 1,
                    # "enabled": True,
                    "description": "tunnel",
                    "ping_ipaddress": "",
                    "ping_interface": "tun0",
                    # "ping_interval": None
                }
            },
            "bgp_peers": {},
            "type": "ipsec",
            "vpn_type": "policy",
            "psk": "testtest"
        }
    }


class BGPApiData(object):
    BGPPeerDetail = {
        "response": {
            "id": 1,
            "ipaddress": "55.55.55.55",
            "asn": 65123,
            "bgp_password": "",
            "access_list": "",
            "add_network_distance": False,
            "add_network_distance_direction": "",
            "add_network_distance_hops": 0
        }
    }


class AccessApiData(object):
    AccessUrl = {
        "id": 24,
        "url": "https://0.0.0.0:8000/?access=a03875aa97ca232fbfb08225389f135bf212f49e675e171b8e7516f22021469c",
        "created_at": "2020-01-24T17:41:51.476Z",
        "created_ip": "24.222.238.197",
        "description": "Created at 2020-01-24T17:41:51+00:00 for 1h",
        "lifetime": "1h",
        "expires_at": "2020-01-24T18:41:51.484Z",
        "expired": False,
        # "last_accessed_at": "2020-01-24T17:41:51.476Z",
        "last_access_at": "2020-01-24T17:41:51.476Z",
        "last_accessed_ip": "2020-01-24T17:41:51.476Z"
    }
    AccessUrlDetail = {
        "response": AccessUrl
    }
    AccessUrlListResponse = {
        "response": [AccessUrl]
    }
    AccessToken = {
        "id": 1,
        "created_at": "2019-08-19T19:07:49.662Z",
        # "token": "12vupgeuate2kbpjiltp",
        "created_ip": "24.222.238.197",
        "description": "sadfasdf",
        # "expires_at": "2019-08-19T19:37:49.663Z",
        "expires_at": 1280301203,
        "lifetime": "30m",
        # "refreshes": False,
        "refreshes": "False",
        "expired": True,
        # "last_accessed_at": "2019-08-19T19:07:49.662Z",
        "last_access_at": "2019-08-19T19:07:49.662Z",
        "last_accessed_ip": "2019-08-19T19:07:49.662Z"
    }
    AccessTokenDetail = {
        "response": AccessToken
    }
    AccessTokenListResponse = {
        "response": [AccessToken]
    }
    AccessUrlDeleteResponse = {
        "response": "Access url deleted"
    }
    AccessTokenDeleteResponse = {
        "response": "Token deleted"
    }
