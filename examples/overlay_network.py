import os

from cohesivenet import Logger
from cohesivenet.macros import connect, config, admin, peering, routing

Logger.silence_urllib3()


def take_keys(keys, data_dict):
    """Take keys from dict

    Arguments:
        keys {List[str]} -- Keys it include in output dict
        data_dict {Dict}

    Returns:
        [Dict]
    """
    return {k: v for k, v in data_dict.items() if k in keys}


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
                take_keys(["host", "password"], connect_args),
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
    LICENSE: path to license file
    KEYSET_TOKEN: secret token to be used for keyset

    Raises:
        RuntimeError: Raise runtime error if environment is not properly configured

    Returns:
        Dict -- Parsed data for configuring a mesh network
    """
    license_file = os.getenv("LICENSE")
    keyset_token = os.getenv("KEYSET_TOKEN")
    master_password = os.getenv("MASTER_PASSWORD")
    master_set = os.getenv("MASTER_SET", "False").lower() not in ("0", "false")

    controller_hosts = os.getenv("CONTROLLER_HOSTS_CSV").split(",")
    controller_passwords = os.getenv("CONTROLLER_PASSWORDS_CSV").split(",")
    controller_subnets = os.getenv("CONTROLLER_SUBNETS").split(",")
    assert (
        len(controller_hosts) == len(controller_passwords) == len(controller_subnets)
    ), (
        "CONTROLLER_HOSTS_CSV, CONTROLLER_PASSWORDS_CSV "
        "and CONTROLLER_SUBNETS must have same number of elements"
    )

    return {
        "controllers": [
            {
                "host": host + ":8000",
                "password": controller_passwords[i]
                if not master_set
                else master_password,
                "subnet": controller_subnets[i],
            }
            for i, host in enumerate(controller_hosts)
        ],
        "master_password": master_password,
        "topology_name": "VNS3 Overlay Net Example",
        "license": license_file,
        "keyset_token": keyset_token,
    }


def create_clients(**parameters):
    clients = setup_clients(parameters["controllers"])

    if not parameters.get("master_set"):
        print("Setting master")
        [_, api_failures], [_, ui_failures] = update_client_passwords(
            clients, parameters.get("master_password")
        )
        if len(ui_failures) or len(api_failures):
            print("Failure updating master passwords:")
            print("UI: %s" % ".".join([str(e) for e in ui_failures]))
            print("API: %s" % ".".join([str(e) for e in api_failures]))
    else:
        for client in clients:
            client.configuration.password = parameters.get("master_password")

    return clients


def setup_overlay(client, parameters):
    return config.setup_controller(
        client,
        parameters["topology_name"],
        parameters["license"],
        license_parameters={"default": True},
        keyset_parameters={"token": parameters["keyset_token"]},
        reboot_timeout=240,
        keyset_timeout=240,
    )


def peer_controllers(root_client, peer_client, parameters):
    """Run configure and create peering mesh and route advertisements

    Arguments:
        root_client {VNS3Client}
        peer_client {VNS3Client}
        parameters {Dict} - values from get_env
    """
    print("Setting peer Id")
    peer_client.peering.put_self_peering_id({"id": 2})
    print("Creating peering mesh")
    peering.peer_mesh([root_client, peer_client])
    print("Creating route advertisements")
    ordered_subnets = [parameters["root_controller"]["subnet"]] + [
        c["subnet"] for c in parameters["controllers"]
    ]
    routing.create_route_advertisements([root_client, peer_client], ordered_subnets)


def run():
    """Run create peering mesh.
    """
    parameters = get_env()
    clients = create_clients(**parameters)

    # only building a simple overlay topology with 2 controllers
    assert (
        len(clients) == 2
    ), "More controllers provided by env than expected. Expected 2 in overlay."
    root, peer = clients
    setup_overlay(root, parameters)
    return config.fetch_keysets([peer], root.host_uri, parameters["keyset_token"])
