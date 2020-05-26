import os
import pprint

from cohesivenet import (
    constants,
    ApiException,
    CohesiveSDKException,
    network_math,
    Logger
)

from cohesivenet.macros import (
    connect,
    config,
    routing,
    ipsec,
    admin
)

Logger.silence_urllib3()


def assert_on_values(config_dict):
    missing_vals = []
    for key, val in config_dict.items():
        if val in ("", None):
            missing_vals.append(key)
    assert len(missing_vals) == 0, "Missing config: %s" % ",".join(missing_vals)


def get_env_config():
    return {
        "azure_controller": os.getenv("AZURE_CONTROLLER"),
        "aws_controller": os.getenv("AWS_CONTROLLER"),
        "azure_password": os.getenv("AZURE_CONTROLLER_PASSWORD"),
        "aws_password": os.getenv("AWS_CONTROLLER_PASSWORD"),
        "master_password": os.getenv("MASTER_CONTROLLER_PASSWORD"),
        "license": os.getenv("LICENSE"),
        "keyset_token": os.getenv("KEYSET_TOKEN"),
        "aws_cidr": os.getenv("AWS_CIDR"),
        "azure_cidr": os.getenv("AZURE_CIDR"),
        "ipsec_shared_secret": os.getenv("IPSEC_PSK")
    }


def setup_clients(client_data):
    """Setup clients for AWS and Azure VNS3 Controllers.
       Reset password to master password and enable Admin UI

    Returns:
        Tuple[VNS3Client (AWS), VNS3Client (Azure)]
    """
    azure_vns3 = client_data.get("azure_controller")
    azure_current_ps = client_data.get("azure_password")
    aws_vns3 = client_data.get("aws_controller")
    aws_current_ps = client_data.get("aws_password")

    assert all([azure_vns3, aws_vns3, azure_current_ps, aws_current_ps]), (
        "Configuration must contain the following: "
        "azure_controller, aws_controller, azure_password, aws_password"
    )

    azure_client_data = {
        "host": azure_vns3 + ":8000",
        "username": "api",
        "password": azure_current_ps,
        "verify": False,
    }

    aws_client_data = {
        "host": aws_vns3 + ":8000",
        "username": "api",
        "password": aws_current_ps,
        "verify": False,
    }

    master_password = client_data.get("master_password")
    aws_client, azure_client = connect.get_clients(aws_client_data, azure_client_data)
    if not master_password:
        return aws_client, azure_client

    clients_to_update = []
    if aws_client_data["password"] != master_password:
        clients_to_update.append(aws_client)
    if azure_client_data["password"] != master_password:
        clients_to_update.append(azure_client)

    if len(clients_to_update) > 0:
        # Automatically updates password used by client
        admin.roll_api_password(master_password, clients_to_update)
        admin.roll_ui_credentials(
            {"username": "vnscubed", "password": master_password},
            clients_to_update,
            enable_ui=True,
        )

    return aws_client, azure_client


def configure_multicloud_bridge_client(**bridge_kwargs):
    """Configure client for multicloud IPsec bridge

    Arguments:
        target_client {VNS3Client} - client to be configured
        target_topology_name {str}
        peer_endpoint {str} - controller endpoint on otherside of bridge
        endpoint_name {str} - name for the IPsec endpoint
        tunnel_vti {str} - CIDR to be used for VTI interface

        license_file {str} - full path to license file
        target_cidr {str} - cidr for this clients network
        peer_cidr {str} - cidr accessible on other side of bridge
        tunnel_psk {str} -- Preshared key for IPsec tunnel

    Returns:
        Dict - {
            endpoint: IpsecRemoteEndpoint,
            routes: Dict
        } OR Exception
    """
    required_kwargs = [
        "target_client",
        "target_topology_name",
        "peer_endpoint",
        "endpoint_name",
        "tunnel_vti",
        "license_file",
        "keyset_token",
        "target_cidr",
        "peer_cidr",
        "tunnel_psk",
    ]

    missing_kwargs = [a for a in required_kwargs if a not in bridge_kwargs]
    if len(missing_kwargs) > 0:
        return CohesiveSDKException("Missing args for bridge %s" % missing_kwargs)

    try:
        target_client = bridge_kwargs["target_client"]
        topology_name = bridge_kwargs["target_topology_name"]
        print("Setup for %s..." % topology_name)
        config.setup_controller(
            target_client,
            topology_name,
            bridge_kwargs["license_file"],
            license_parameters={"default": True},
            keyset_parameters={"token": bridge_kwargs["keyset_token"]},
            reboot_timeout=240,
            keyset_timeout=240,
        )

        target_cidr = bridge_kwargs["target_cidr"]
        print("Creating local gateway routes for %s" % target_cidr)
        routing.create_local_gateway_route(target_client, target_cidr, should_raise=False)

        endpoint_name = bridge_kwargs["endpoint_name"]
        print("Creating tunnel: %s" % endpoint_name)
        return ipsec.create_tunnel_endpoint(
            target_client,
            endpoint_name,
            bridge_kwargs["tunnel_psk"],
            bridge_kwargs["peer_endpoint"],
            bridge_kwargs["peer_cidr"],
            bridge_kwargs["tunnel_vti"]
        )
    except (ApiException, CohesiveSDKException) as e:
        return e


def run(config):
    """Fetch variables from environment for clients, configure controllers
       and build IPsec endpoint

    Returns:
        [List[Dict]]
    """
    ipsec_endpoint_name = "aws_azure_vns3_tunnel"
    vti_blocks = network_math.calculate_next_subnets(
        prefix_length=30, take=2, cidr=constants.VTI_RANGE_LINK_LOCAL
    )

    print("Setting up clients")
    aws_client, azure_client = setup_clients(config)
    license_file = config.get("license")
    keyset_token = config.get("keyset_token")
    aws_cidr = config.get("aws_cidr")
    azure_cidr = config.get("azure_cidr")
    ipsec_shared_secret = config.get("ipsec_shared_secret")

    print("Setting up AWS controller")
    aws_response = configure_multicloud_bridge_client(
        target_client=aws_client,
        target_topology_name="MultiCloud - AWS Controller",
        peer_endpoint=azure_client.configuration.host_uri,
        endpoint_name=ipsec_endpoint_name,
        tunnel_vti=vti_blocks[0],
        license_file=license_file,
        keyset_token=keyset_token,
        target_cidr=aws_cidr,
        peer_cidr=azure_cidr,
        tunnel_psk=ipsec_shared_secret,
    )

    print("Setting up Azure controller")
    azure_response = configure_multicloud_bridge_client(
        target_client=azure_client,
        target_topology_name="MultiCloud - Azure Controller",
        peer_endpoint=aws_client.configuration.host_uri,
        endpoint_name=ipsec_endpoint_name,
        tunnel_vti=vti_blocks[1],  # Non-overlapping VTI blocks
        license_file=license_file,
        keyset_token=keyset_token,
        target_cidr=azure_cidr,
        peer_cidr=aws_cidr,
        tunnel_psk=ipsec_shared_secret,
    )

    return [aws_response, azure_response]


if __name__ == "__main__":
    env = get_env_config()
    assert_on_values(env)
    responses = run(env)
    pprint.pprint(responses)
