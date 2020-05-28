import os
from datetime import datetime

from cohesivenet import Logger
from cohesivenet.macros import connect, config, admin, peering, routing, state

Logger.silence_urllib3()
Logger.set_stream_handler(os.getenv("COHESIVE_LOG_LEVEL", "info").lower())

TOPOLOGY = "VNS3 Peering Mesh Example"


def print_log(message, level="info", module="peering_mesh"):
    print(
        "[%s] [%s] [%s] [%s]" % (str(datetime.utcnow()), module, level.upper(), message)
    )


def get_env_config():
    """Fetch variables from environment:

    CONTROLLER_HOSTS_CSV: CSV of VNS3 hosts
    CONTROLLER_PASSWORDS_CSV: CSV of VNS3 host passwords
    MASTER_PASSWORD: master password to be used for API
    ROOT_CONTROLLER: (Optional, defaults to first in HOSTS list) select root controller by host. Root will be licensed first
    ROOT_CONTROLLER_PASSWORD: (Optional) Password for root controller
    CONTROLLER_SUBNETS_CSV: specific subnet for controllers, e.g. 10.0.1.0/25,10.0.1.128/25
    LICENSE: path to license file
    KEYSET_TOKEN: secret token to be used for keyset

    example env file:


    Raises:
        RuntimeError: Raise runtime error if environment is not properly configured

    Returns:
        Dict -- Parsed data for configuring a mesh network
    """
    license_file = os.getenv("LICENSE")
    keyset_token = os.getenv("KEYSET_TOKEN")
    controller_hosts = os.getenv("CONTROLLER_HOSTS_CSV").split(",")
    controller_passwords = os.getenv("CONTROLLER_PASSWORDS_CSV")
    master_password = os.getenv("MASTER_PASSWORD")
    # use master password if none provided
    if controller_passwords:
        controller_passwords = controller_passwords.split(",")
    else:
        controller_passwords = [master_password for _ in range(len(controller_hosts))]

    controller_subnets = os.getenv("CONTROLLER_SUBNETS_CSV").split(",")
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
        root_controller_host = controller_hosts.pop(0)
        root_controller_password = host_password_dict[root_controller_host]
        host_password_dict.pop(root_controller_host)

    return {
        "controllers": [
            {
                "host": host + ":8000",
                "password": password,
                "state": {"subnet": host_subnet_dict[host]},
            }
            for host, password in host_password_dict.items()
        ],
        "master_password": master_password,
        "root_controller": {
            "host": root_controller_host + ":8000",
            "password": root_controller_password,
            "state": {"subnet": host_subnet_dict[root_controller_host]},
        },
        "topology_name": TOPOLOGY,
        "license": license_file,
        "keyset_token": keyset_token,
    }


def connect_clients(host_password_dicts):
    """connect_clients Connect to clients

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
                host=connect_args["host"],
                password=connect_args["password"],
                verify=False,
                username="api",
            )
            for connect_args in host_password_dicts
        ]
    )


def create_clients(**parameters):
    """[summary]

    Returns:
        [type] -- [description]
    """
    root_client = connect_clients([parameters["root_controller"]])[0]
    peer_clients = connect_clients(parameters["controllers"])

    master_password = parameters.get("master_password")
    if master_password is None:
        return root_client, peer_clients

    all_clients = [root_client] + peer_clients
    for client in all_clients:
        if client.configuration.password != master_password:
            print_log("Updating controller %s passwords" % client.host_uri)
            admin.roll_api_password(master_password, [client])
            admin.roll_ui_credentials(
                {"username": "vnscubed", "password": master_password},
                [client],
                enable_ui=True,
            )

    controller_states = [parameters["root_controller"]["state"]] + [
        c["state"] for c in parameters["controllers"]
    ]

    # set network information on client for use later
    for i, client in enumerate(all_clients):
        client.update_state(controller_states[i])

    return root_client, peer_clients


def build_mesh(root_client, peer_clients, parameters):
    """Run configure and create peering mesh and route advertisements

    Arguments:
        root_client {VNS3Client}
        peer_clients {List[VNS3Client]}
        parameters {Dict} - values from get_env
    """
    ordered_clients = [root_client] + peer_clients
    print_log("Configuring root controller with license and keyset")
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

    print_log("Fetching keysets")
    config.fetch_keysets(
        peer_clients, state.get_primary_private_ip(root_client), keyset_token
    )

    print_log("Setting peering Ids")
    peering.set_peer_ids(peer_clients, ids=[2, 3, 4])
    print_log("Creating peer routes")
    routing.create_peer_mesh_local_gw_routes(ordered_clients)
    print_log("Creating peering mesh")
    peering.peer_mesh(ordered_clients)
    print_log("Creating route advertisements")
    ordered_subnets = [client.query_state("subnet") for client in ordered_clients]
    routing.create_route_advertisements(ordered_clients, ordered_subnets)


if __name__ == "__main__":
    parameters = get_env_config()
    print_log("Using config: %s" % parameters)
    root_client, peer_clients = create_clients(**parameters)
    print_log("Using VNS3 @ %s as root controller" % root_client.host_uri)
    build_mesh(root_client, peer_clients, parameters)
