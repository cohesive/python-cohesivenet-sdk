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
            "username": "vnscubed",
        }
    }

class IpsecApiData(object):
    IpsecEndpointDetail = {
        "response": {
            "name": "EndpointB",
            "ipaddress": "13.53.72.182",
            "pfs": True,
            "id": 1,
            "ike_version": 1,
            "nat_t_enabled": True,
            "private_ipaddress": "192.0.2.254",
            "extra_config": [],
            "tunnels": {
                "3": {
                    "id": 3,
                    "local_subnet": "172.31.0.0/28",
                    "remote_subnet": "192.168.10.0/22",
                    "endpoint_id": 1,
                    "enabled": True,
                    "description": "tunnel",
                    "ping_ipaddress": "",
                    "ping_interface": "tun0"
                }
            },
            "bgp_peers": {},
            "type": "ipsec",
            "vpn_type": "policy",
            "psk": "testtest"
        }
    }

    IpsecEndpointDetailNoTunnels = {
        "response": {
            "name": "EndpointC",
            "ipaddress": "13.53.72.182",
            "pfs": True,
            "id": 1,
            "ike_version": 2,
            "nat_t_enabled": True,
            "private_ipaddress": "192.0.2.254",
            "extra_config": [],
            "tunnels": {},
            "bgp_peers": {},
            "type": "ipsec",
            "vpn_type": "policy",
            "psk": "nnotnot"
        }
    }

    IpsecSystemDetailResponse = {
        "response": {
            "remote_endpoints": {
                "1": {
                    "name": "EndpointB",
                    "ipaddress": "13.53.72.182",
                    "pfs": True,
                    "id": 1,
                    "ike_version": 1,
                    "nat_t_enabled": True,
                    "private_ipaddress": "192.0.2.254",
                    "extra_config": [],
                    "tunnels": {
                        "1": {
                            "id": 1,
                            "local_subnet": "172.31.0.0/22",
                            "remote_subnet": "192.168.10.0/28",
                            "endpoint_id": 1,
                            "enabled": True,
                            "description": "Tunnel A",
                            "ping_ipaddress": "",
                            "ping_interface": "tun0",
                            "ping_interval": 30
                        }
                    },
                    "bgp_peers": {},
                    "type": "ipsec",
                    "vpn_type": "policy",
                    "psk": "testtest"
                }
            },
            "this_endpoint": {
                "ipaddress": "13.48.194.23",
                "overlay_subnet": "172.31.0.0/22",
                "private_ipaddress": "192.0.2.254",
                "ipsec_local_ipaddress": "192.0.2.254",
                "asn": 65001
            }
        }
    }

    IpsecStatusResponse = {
        "response": {
            "5": {
                "local_subnet": "172.31.0.0/28",
                "remote_subnet": "192.168.10.0/22",
                "endpointid": 5,
                "endpoint_name": "EndpointB",
                "active": True,
                "description": "tunnel",
                "connected": True,
                "tunnel_params": {
                    "phase2": "up",
                    "outbound_spi": "e7a4b70c",
                    "inbound_spi": "64dd6ec8",
                    "bytes_in": "0",
                    "bytes_out": "0",
                    "esp_time_remaining": "20756s",
                    "esp_port": "4500",
                    "phase2_algo": "AES 128",
                    "phase2_hash": "SHA1",
                    "nat_t": "on",
                    "dpd": "off",
                    "pfs_dh_group": 14,
                    "phase1": "up",
                    "isakmp_port": "4500",
                    "isakmp_time_remaining": "1227s",
                    "last_dpd": "None",
                    "phase1_cipher": "AES 256",
                    "phase1_prf": "SHA2_256",
                    "phase1_dh_group": 14,
                    "ike_version": "IKEv1"
                }
            }
        }
    }

    IpsecTunnelDetail = {
        "response": {
            "id": 2,
            "local_subnet": "172.31.0.0/28",
            "remote_subnet": "192.168.10.0/22",
            "endpoint_id": 1,
            "enabled": True,
            "description": "tunnel",
            "ping_ipaddress": "",
            "ping_interface": "",
            "ping_interval": None
        }
    }

    LinkHistoryResponse = {
        "response": {
            "remote": "172.31.0.0/28",
            "history": [{
            "event": "Tunnel up",
            "timestamp": "2020-01-24T17:41:51.476Z",
            "timestamp_i": 1564089901
            }],
            "local": "192.168.10.0/22"
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
        "last_accessed_at": "2020-01-24T17:41:51.476Z",
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
        "token": "12vupgeuate2kbpjiltp",
        "created_ip": "24.222.238.197",
        "description": "sadfasdf",
        "expires_at": "2019-08-19T19:37:49.663Z",
        "lifetime": "30m",
        "refreshes": False,
        "expired": True,
        "last_accessed_at": "2019-08-19T19:07:49.662Z",
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


class FirewallApiData(object):
    pass


class InterfacesApiData(object):
    Interface1 = {
        "id": 4,
        "name": "eth0",
        "interface_type": "system",
        "description": "Auto-created interface",
        "ip_internal": "10.0.1.120",
        "mtu":9001,
        "enabled":True,
        "status": "Up",
        "mask_bits": "25",
        "gateway": None,
        "system_default": True,
        "ip_external": "3.212.92.239",
        "tags": []
    }

    Interface2 = {
        "id": 5,
        "name": "lo",
        "interface_type": "system",
        "description": "Auto-created interface",
        "ip_internal": "127.0.0.1",
        "mtu": 65536,
        "enabled": True,
        "status": "Up",
        "mask_bits": "8",
        "gateway": None,
        "system_default": True,
        "ip_external": None,
        "tags": []
    }

    InterfaceDetail = {
        "response": Interface2
    }

    InterfaceListResponse = {
        "response": [
            Interface1,
            Interface2
        ]
    }

    GREEndpoint = {
        "id": 8,
        "interface_id": 4,
        "name": "gre2",
        "interface_type": "gre",
        "description": "Gre endpoint",
        "ip_internal": "127.0.0.1",
        "mtu": 65536,
        "enabled": True,
        "status": "Up",
        "mask_bits": "8",
        "gateway": None,
        "system_default": False,
        "ip_external": None,
        "tags": [],
        "local_connection_ip": "10.1.0.1",
        "remote_connection_ip": "10.2.0.1",
        "ttl": 255
    }

    GREEndpointDetail = {
        "response": GREEndpoint
    }

    GREEndpointListResponse = {
        "response": [
            GREEndpoint
        ]
    }


class LicensingApiData(object):
    LicenseUploadDetail = {
        "response": {
            "license": "accepted",
            "finalized": False,
            "license_present": True,
            "capabilities": [
                "IPsec",
                "eBGP",
                "LinearAddressing",
                "LinearAddressingConfigurable",
                "CloudWAN",
                "Containers"
            ],
            "default_topology": {
                "managers": [
                    {
                        "manager_id": 1,
                        "overlay_ipaddress": {
                            "ip_address": "100.127.255.253",
                            "octets": [
                                100,
                                127,
                                255,
                                253
                            ]
                        },
                        "asn": 65001
                    },
                    {
                        "manager_id": 2,
                        "overlay_ipaddress": {
                            "ip_address": "100.127.255.252",
                            "octets": [
                                100,
                                127,
                                255,
                                252
                            ]
                        },
                        "asn": 65002
                    },
                    {
                        "manager_id": 3,
                        "overlay_ipaddress": {
                            "ip_address": "100.127.255.251",
                            "octets": [
                                100,
                                127,
                                255,
                                251
                            ]
                        },
                        "asn": 65003
                    },
                    {
                        "manager_id": 4,
                        "overlay_ipaddress": {
                            "ip_address": "100.127.255.250",
                            "octets": [
                                100,
                                127,
                                255,
                                250
                            ]
                        },
                        "asn": 65004
                    }
                ],
                "clients": [
                    {
                        "ip_address": "100.127.255.193",
                        "octets": [
                            100,
                            127,
                            255,
                            193
                        ]
                    },
                    {
                        "ip_address": "100.127.255.194",
                        "octets": [
                            100,
                            127,
                            255,
                            194
                        ]
                    },
                    {
                        "ip_address": "100.127.255.195",
                        "octets": [
                            100,
                            127,
                            255,
                            195
                        ]
                    },
                    {
                        "ip_address": "100.127.255.196",
                        "octets": [
                            100,
                            127,
                            255,
                            196
                        ]
                    },
                    {
                        "ip_address": "100.127.255.197",
                        "octets": [
                            100,
                            127,
                            255,
                            197
                        ]
                    },
                    {
                        "ip_address": "100.127.255.198",
                        "octets": [
                            100,
                            127,
                            255,
                            198
                        ]
                    },
                    {
                        "ip_address": "100.127.255.199",
                        "octets": [
                            100,
                            127,
                            255,
                            199
                        ]
                    },
                    {
                        "ip_address": "100.127.255.200",
                        "octets": [
                            100,
                            127,
                            255,
                            200
                        ]
                    },
                    {
                        "ip_address": "100.127.255.217",
                        "octets": [
                            100,
                            127,
                            255,
                            217
                        ]
                    }
                ],
                "total_clients": 25,
                "overlay_max_clients": 25,
                "overlay_subnet": "100.127.255.192/26",
                "ipsec_max_endpoints": 4,
                "ipsec_max_subnets": 16
            }
        }
    }

    LicenseDetail = {
        "response": {
            "license_present": True,
            "sha1_checksum": "4320fce04d8db1c5d19a1648990a04e13ffc4419",
            "uploaded_at": "2020-01-24 20:39:59 +0000",
            "uploaded_at_i": 1579898399,
            "topology": {
                "managers": [
                    {
                        "manager_id": 1,
                        "overlay_ipaddress": {
                            "ip_address": "172.31.1.253",
                            "octets": [
                                172,
                                31,
                                1,
                                253
                            ]
                        },
                        "asn": 34001
                    },
                    {
                        "manager_id": 2,
                        "overlay_ipaddress": {
                            "ip_address": "172.31.1.252",
                            "octets": [
                                172,
                                31,
                                1,
                                252
                            ]
                        },
                        "asn": 34002
                    },
                    {
                        "manager_id": 3,
                        "overlay_ipaddress": {
                            "ip_address": "172.31.1.251",
                            "octets": [
                                172,
                                31,
                                1,
                                251
                            ]
                        },
                        "asn": 35011
                    },
                    {
                        "manager_id": 4,
                        "overlay_ipaddress": {
                            "ip_address": "172.31.1.250",
                            "octets": [
                                172,
                                31,
                                1,
                                250
                            ]
                        },
                        "asn": 35012
                    }
                ],
                "clients": [
                    {
                        "ip_address": "172.31.1.1",
                        "octets": [
                            172,
                            31,
                            1,
                            1
                        ]
                    }
                ],
                "total_clients": 1,
                "overlay_max_clients": 25,
                "overlay_subnet": "172.31.1.0/24",
                "ipsec_max_endpoints": 4,
                "ipsec_max_subnets": 16
            },
            "capabilities": [
                "IPsec",
                "eBGP",
                "LinearAddressing",
                "LinearAddressingConfigurable",
                "CloudWAN",
                "Containers"
            ],
            "container_details": {
                "containers_run_count": 4,
                "containers_image_count": 50
            },
            "finalized": True,
            "custom_addressing": True
        }
    }

    LicenseParamsResponse = {
        "response": {
            "license": "accepted",
            "finalized": True,
            "parameters": {
                "subnet": "172.31.1.0/24",
                "managers":[
                    "172.31.1.253",
                    "172.31.1.252",
                    "172.31.1.251",
                    "172.31.1.250"
                ],
                "clients": [
                    "172.31.1.1"
                ],
                "asns": [
                    34001,
                    34002,
                    35011,
                    35012
                ],
                "my_manager_vip": "172.31.1.254"
            }
        }
    }

    UpgradeLicenseResponse = {
        "response": {
            "finalized": True,
            "uniq": "4320fce04d8db1c5d19a1648990a04e13ffc4419",
            "license": "in-progress",
            "new_clientpacks": 50,
            "new_managers": 4
        }
    }


class MonitoringApiData(object):
    Alert = {
        "id": 23,
        "webhook_id": 21,
        "name": "Slack Tunnel Alerts",
        "enabled": True,
        "created_at": "2020-01-14T17:32:55.904Z",
        "updated_at": "2020-01-14T17:32:55.904Z",
        "url": "https://hooks.slack.com/services/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",
        "custom_properties": [],
        "events": [
            "tunnel_up",
            "tunnel_down"
        ]
    }

    AlertDetail = {
        "response": Alert
    }

    AlertsListResponse = {
        "response": [
            Alert
        ]
    }

    Webhook = {
        "body": "{\n"
        '    "attachments": [{\n'
        '      "author_name": "Tunnel %{status}: '
        '%{tunnel_description}",\n'
        '      "author_link": "%{tunnel_url}",\n'
        '      "fields": [\n'
        '        {"title": "VNS3 Controller", "value": '
        '"%{topo_name}" , "short": True},\n'
        '        {"title": "Endpoint", "value": "%{ipsec_name} '
        '(%{ipsec_ip})", "short": True},\n'
        '        {"title": "Local Subnet", "value": '
        '"%{local_subnet}", "short": True},\n'
        '        {"title": "Remote Subnet", "value": '
        '"%{remote_subnet}", "short": True}\n'
        "      ]\n"
        "    }]\n"
        "  }",
        "created_at": "2019-11-12T16:03:28.554000",
        "custom_properties": [],
        "events": ["tunnel_up", "tunnel_down"],
        "headers": [],
        "id": 2,
        "name": "Test Slack",
        "parameters": [],
        "updated_at": "2019-11-12T16:03:28.554000",
        "url": "",
        "validate_cert": True,
    }

    WebhookDetail = {
        "response": Webhook
    }

    WebhookListResponse = {
        "response": [Webhook]
    }


class NetworkEdgePluginsApiData(object):
    pass


class OverlayNetworkApiData(object):
    pass


class PeeringApiData(object):
    PeeringStatus = {
        "response": {
            "peered": True,
            "managers": {
                "1": {
                    "overlay_ipaddress": "172.31.1.253",
                    "self": True,
                    "id": 1
                },
                "2": {
                    "overlay_ipaddress": "172.31.1.252",
                    "not_set": True,
                    "id": 2
                },
                "3": {
                    "overlay_ipaddress": "172.31.1.251",
                    "not_set": True,
                    "id": 3
                },
                "4": {
                    "overlay_ipaddress": "172.31.1.250",
                    "not_set": True,
                    "id": 4
                }
            },
            "id": 1
        }
    }


class RoutingApiData(object):
    RoutesResponse = {
        "response": {
            "1": {
                "cidr": "224.0.0.0/4",
                "id": 1,
                "netmask": "240.0.0.0",
                "interface": "tun0",
                "description": "Multicast (auto-added)",
                "advertise": False,
                "metric": 0
            },
            "2": {
                "cidr": "10.121.11.212/32",
                "id": 3,
                "netmask": "255.255.255.255",
                "interface": "eth0",
                "gateway": "10.121.11.209",
                "description": "Local Route subnet gateway",
                "advertise": False,
                "metric": 0
            },
            "3": {
                "cidr": "10.121.11.213/32",
                "id": 4,
                "netmask": "255.255.255.255",
                "interface": "eth0",
                "gateway": "10.121.11.209",
                "description": "Local Secondary IP",
                "advertise": False,
                "metric": 0
            },
            "4": {
                "cidr": "10.0.0.0/8",
                "id": 8,
                "netmask": "255.0.0.0",
                "interface": "_notset",
                "description": "On Prem AWS",
                "advertise": True,
                "metric": 0
            },
        }
    }


class SnapshotsApiData(object):
    SnapshotData = {
        "snapshot_20200127_1580154368_3.212.92.239": {
            "sha1_checksum": "869c0dc6bfa3f811b1f7affee4051a29a7ecac8b",
            "created_at": "2020-01-27T19:46:09.634+00:00",
            "created_at_i": 1580154369,
            "size": 1479421
        }
    }

    SnapshotDetail = {
        "response": SnapshotData
    }

    SnapshotsListResponse = {
        "response": {
            "latest_snapshot": "snapshot_20200127_1580154368_3.212.92.239",
            "snapshots": SnapshotData
        }
    }

    SnapshotImportResponse = {
        "response": {
            "snapshot":"accepted"
        }
    }

class SystemAdminApiData(object):
    CloudDataDetail = {
        "response": {
            "cloud_data": {
                "accountId": "947761958079",
                "architecture": "x86_64",
                "availabilityZone": "us-east-1a",
                "billingProducts": None,
                "devpayProductCodes": None,
                "imageId": "ami-034b377bde620d2a8",
                "instanceId": "i-0b96e779c3143cf66",
                "instanceType": "t3.small",
                "kernelId": None,
                "marketplaceProductCodes": None,
                "pendingTime": "2019-11-08T16:18:38Z",
                "privateIp": "10.0.1.37",
                "ramdiskId": None,
                "region": "us-east-1",
                "version": "2017-09-30",
            },
            "cloud_type": "ec2",
        }


    }

    UpdateRemoteSupportResponse = {
        "response": {
            "enabled": False,
            "revoke_credential": True
        }
    }

    VNS3Status = {
        "response": {
            "connected_clients": {},
            "connected_subnets": [
                ["10.0.1.0","255.255.255.0"]
            ],
            "ipsec": {}
        }
    }

    SystemStatus = {
        "response": {
            "data": {
                "sysstat": [
                    [
                        "vnscubed",
                        "600",
                        "1580160301",
                        "all",
                        "%user",
                        "2.16"
                    ],
                    [
                        "vnscubed",
                        "600",
                        "1580160301",
                        "all",
                        "%nice",
                        "0.01"
                    ],
                    [
                        "vnscubed",
                        "600",
                        "1580160301",
                        "cpu0",
                        "%user",
                        "2.23"
                    ],
                    [
                        "vnscubed",
                        "600",
                        "1580160301",
                        "cpu0",
                        "%nice",
                        "0.01"
                    ],
                    [
                        "vnscubed",
                        "600",
                        "1580160301",
                        "cpu0",
                        "%system",
                        "1.26"
                    ],
                    [
                        "vnscubed",
                        "600",
                        "1580160301",
                        "cpu0",
                        "%iowait",
                        "0.02"
                    ]
                ]
            },
            "timestamp": "2020-01-27 21:46:35 +0000",
            "timestamp_i": 1580161595,
            "vns3_version": "Cohesive Networks VNS3 4.9.0-20200121",
            "kernel_version": "Linux 4.4.0-154-generic",
            "uptime": 263155,
            "loadavg": [
                "0.00",
                "0.05",
                "0.07",
                "1/328",
                "20398"
            ],
            "diskinfo": [
                [
                    "/dev/nvme0n1p1",
                    "31571570688",
                    "5974278144",
                    "23986741248",
                    "20%",
                    "/",
                    "13%"
                ]
            ],
            "meminfo": [
                "8264527872",
                "4446773248",
                "3817754624",
                "90910720",
                "241074176",
                "3327860736",
                "877838336",
                "7386689536"
            ],
            "swapinfo": [
                "1073737728",
                "0",
                "1073737728"
            ],
            "container_system": {
                "container_system_running": True,
                "images_limit": 50,
                "images_stored": 3,
                "containers_limit": 4,
                "containers_active": 1,
                "container_network": "198.51.100.0/28"
            }
        }
    }
    