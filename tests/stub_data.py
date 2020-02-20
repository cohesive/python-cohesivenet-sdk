ipsec_endpoint_detail = {
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
                "ping_interface": "tun0",
                "ping_interval": None
            }
        },
        "bgp_peers": {},
        "type": "ipsec",
        "vpn_type": "policy",
        "psk": "testtest"
    }
}


bgp_peer_detail = {
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