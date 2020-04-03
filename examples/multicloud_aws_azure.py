import os
import urllib3
import pprint

from cohesivenet import constants, ApiException, CohesiveSDKException, network_math
from cohesivenet.macros import connect, config, routing, ipsec, admin

urllib3.disable_warnings()


def setup_clients(update_passwords=False):
    """Setup clients for AWS and Azure VNS3 Controllers.
       Reset password to master password and enable Admin UI

    Returns:
        Tuple[VNS3Client, VNS3Client]
    """
    azure_host = os.getenv("AZURE_HOST")
    aws_host = os.getenv("AWS_HOST")
    azure_def_password = os.getenv("AZURE_DEFAULT_PASSWORD")
    aws_def_password = os.getenv("AWS_DEFAULT_PASSWORD")
    master_password = os.getenv("MASTER_PASSWORD")

    azure_client_data = {
        "host": azure_host + ":8000",
        "username": "api",
        "password": master_password if not update_passwords else azure_def_password,
        "verify": False,
    }

    aws_client_data = {
        "host": aws_host + ":8000",
        "username": "api",
        "password": master_password if not update_passwords else aws_def_password,
        "verify": False,
    }

    aws_client, azure_client = connect.get_clients(aws_client_data, azure_client_data)
    if not update_passwords:
        return aws_client, azure_client

    admin.roll_api_password(master_password, [aws_client, azure_client])
    admin.roll_ui_credentials(
        {"username": "vnscubed", "password": master_password},
        [aws_client, azure_client],
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
        routing.create_local_gateway_route(target_client, target_cidr)

        endpoint_name = bridge_kwargs["endpoint_name"]
        print("Creating tunnel: %s" % endpoint_name)
        return ipsec.create_tunnel_endpoint(
            target_client,
            endpoint_name,
            bridge_kwargs["tunnel_psk"],
            bridge_kwargs["peer_endpoint"],
            bridge_kwargs["peer_cidr"],
            bridge_kwargs["tunnel_vti"],
        )
    except (ApiException, CohesiveSDKException) as e:
        return e


def run(license_file, keyset_token, aws_cidr, azure_cidr, ipsec_psk):
    """Fetch variables from environment for clients, configure controllers
       and build IPsec endpoint

    Returns:
        [List[Dict]]
    """
    ipsec_endpoint_name = "aws_azure_vns3_tunnel"
    vti_blocks = network_math.calculate_next_subnets(
        prefix_length=30, take=2, cidr=constants.VTI_RANGE_LINK_LOCAL
    )

    aws_client, azure_client = setup_clients(update_passwords=True)
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
    license_file = os.getenv("LICENSE")
    keyset_token = os.getenv("KEYSET_TOKEN")
    aws_cidr = os.getenv("AWS_CIDR")
    azure_cidr = os.getenv("AZURE_CIDR")
    ipsec_shared_secret = os.getenv("IPSEC_PSK")

    responses = run(
        license_file, keyset_token, aws_cidr, azure_cidr, ipsec_shared_secret
    )

    pprint(responses)
