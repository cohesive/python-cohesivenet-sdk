import os
import logging
import sys
import urllib3
import pprint
from itertools import combinations

from cohesivenet import (
    constants,
    ApiException,
    CohesiveSDKException,
    VNS3Client,
    util,
    Logger,
)
from cohesivenet.clouds import networkmath
from cohesivenet.macros import (
    connect,
    config,
    routes,
    ipsec,
    admin,
    peering,
    routing,
    state,
)

Logger.silence_urllib3()


def setup_clients(host_password_dicts):
    """setup_clients Connect to clients

    Arguments:
        args: List[Dict] - {
            host: str,
            password: str
        }

    Returns:
        List[VNS3Client]
    """
    assert type(host_password_dicts) is list, "setup_clients expects list as input."

    return connect.get_clients(
        *[
            dict(
                util.take_keys(["host", "password"], connect_args),
                verify=False,
                username="api",
            )
            for connect_args in host_password_dicts
        ]
    )


def update_client_passwords(clients, master_password):
    """[summary]

    Arguments:
        clients {List[VNS3Client]}
        master_password {str}

    Returns:
        List[VNS3Client]
    """
    api_roll_resp = admin.roll_api_password(master_password, clients)
    ui_toggle_resp = admin.roll_ui_credentials(
        {"username": "vnscubed", "password": master_password}, clients, enable_ui=True
    )
    return api_roll_resp, ui_toggle_resp


def get_env():
    """Fetch variables from environment:

    CONTROLLER_HOSTS_CSV: CSV of VNS3 hosts
    CONTROLLER_PASSWORDS_CSV: CSV of VNS3 host passwords
    MASTER_PASSWORD: master password to be used for API
    ROOT_CONTROLLER: (Optional, defaults to first in HOSTS list) select root controller by host. Root will be licensed first
    ROOT_CONTROLLER_PASSWORD: (Optional) Password for root controller
    LICENSE: path to license file
    KEYSET_TOKEN: secret token to be used for keyset

    Raises:
        RuntimeError: Raise runtime error if environment is not properly configured

    Returns:
        Dict -- Parsed data for configuring a mesh network
    """
    license_file = os.getenv("LICENSE")
    keyset_token = os.getenv("KEYSET_TOKEN")
    master_set = os.getenv("MASTER_SET", "False").lower() not in ("0", "false")
    controller_hosts = os.getenv("CONTROLLER_HOSTS_CSV").split(",")
    controller_passwords = os.getenv("CONTROLLER_PASSWORDS_CSV").split(",")
    controller_subnets = os.getenv("CONTROLLER_SUBNETS").split(",")
    assert (
        len(controller_hosts) == len(controller_passwords) == len(controller_subnets)
    ), "CONTROLLER_HOSTS_CSV and CONTROLLER_PASSWORDS_CSV must have same number of elements"

    host_password_dict = dict(zip(controller_hosts, controller_passwords))
    host_subnet_dict = dict(zip(controller_hosts, controller_subnets))
    master_password = os.getenv("MASTER_PASSWORD")
    root_controller_host = os.getenv("ROOT_CONTROLLER")
    root_controller_password = os.getenv("ROOT_CONTROLLER_PASSWORD")
    if root_controller_host and not root_controller_password:
        raise RuntimeError(
            "ROOT_CONTROLLER_PASSWORD is required if ROOT_CONTROLLER is provided"
        )

    if not root_controller_host:
        root_controller_host = controller_hosts.pop()
        root_controller_password = host_password_dict[root_controller_host]
        root_controller_subnet = host_subnet_dict[root_controller_host]
        host_password_dict.pop(root_controller_host)

    return {
        "controllers": [
            {
                "host": host + ":8000",
                "password": password if not master_set else master_password,
                "subnet": host_subnet_dict[host],
            }
            for host, password in host_password_dict.items()
        ],
        "master_password": master_password,
        "master_set": master_set,
        "root_controller": {
            "host": root_controller_host + ":8000",
            "password": root_controller_password if not master_set else master_password,
            "subnet": host_subnet_dict[root_controller_host],
        },
        "topology_name": "VNS3 Peering Mesh Example",
        "license": license_file,
        "keyset_token": keyset_token,
    }


def create_clients(**parameters):
    root_client = setup_clients([parameters["root_controller"]])[0]
    peer_clients = setup_clients(parameters["controllers"])

    if not parameters.get("master_set"):
        print("Setting master")
        update_client_passwords(
            [root_client] + peer_clients, parameters.get("master_password")
        )

    return root_client, peer_clients


def build_mesh(root_client, peer_clients, parameters):
    """Run configure and create peering mesh and route advertisements

    Arguments:
        root_client {VNS3Client}
        peer_clients {List[VNS3Client]}
        parameters {Dict} - values from get_env
    """
    print("Configuring root controller with license and keyset")
    keyset_token = parameters["keyset_token"]
    config.setup_controller(
        root_client,
        parameters["topology_name"],
        parameters["license"],
        license_parameters={"default": True},
        keyset_parameters={"token": keyset_token},
        reboot_timeout=240,
        keyset_timeout=240,
    )

    print("Fetching keysets")
    config.fetch_keysets(
        peer_clients, state.get_primary_private_ip(root_client), keyset_token
    )

    print("Setting peering Ids")
    peering.set_peer_ids(peer_clients, ids=[2, 3, 4])
    print("Creating peering mesh")
    peering.peer_mesh([root_client] + peer_clients)
    print("Creating route advertisements")
    ordered_subnets = [parameters["root_controller"]["subnet"]] + [
        c["subnet"] for c in parameters["controllers"]
    ]
    routing.create_route_advertisements([root_client] + peer_clients, ordered_subnets)


def run():
    """Run create peering mesh.
    """
    parameters = get_env()
    root_client, peer_clients = create_clients(**parameters)
    build_mesh(root_client, peer_clients, parameters)
