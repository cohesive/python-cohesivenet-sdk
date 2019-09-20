import os
import logging
import sys
import urllib3

from cohesivenet import constants, ApiException, CohesiveSDKException
from cohesivenet.clouds import networkmath
from cohesivenet.macros import connect, config, routes, ipsec, admin

urllib3.disable_warnings()
Logger = logging.getLogger()
Logger.handlers = []
Logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
Logger.addHandler(ch)

def update_clients(master_password, aws_client, azure_client):
    reset_ps_response = admin.roll_api_password(master_password, [aws_client, azure_client])
    enable_ui_response = admin.roll_ui_credentials(
        {'username': 'vnscubed', 'password': master_password},
        [aws_client, azure_client], 
        enable_ui=True)
    return aws_client, azure_client



def setup_clients(update_passwords=False):
    """Setup clients for AWS and Azure VNS3 Controllers. 
       Reset password to master password and enable Admin UI
    
    Returns:
        Tuple[VNS3Client, VNS3Client]
    """
    azure_host = os.getenv('AZURE_HOST')
    aws_host = os.getenv('AWS_HOST')
    azure_def_password = os.getenv('AZURE_DEFAULT_PASSWORD')
    aws_def_password = os.getenv('AWS_DEFAULT_PASSWORD')
    master_password = os.getenv('MASTER_PASSWORD')

    azure_client_data = {
        'host': azure_host + ':8000',
        'username': 'api',
        'password': master_password if not update_passwords else azure_def_password,
        'verify': False
    }

    aws_client_data = {
        'host': aws_host + ':8000',
        'username': 'api',
        'password': master_password if not update_passwords else aws_def_password,
        'verify': False
    }

    aws_client, azure_client = connect.get_clients(aws_client_data, azure_client_data)
    if update_passwords:
        return update_clients(master_password, aws_client, azure_client)
    return aws_client, azure_client


def configure_multicloud_bridge_aws(aws_client, tunnel_endpoint, tunnel_name, tunnel_vti):
    license_file = os.getenv('LICENSE')
    keyset_token = os.getenv('KEYSET_TOKEN')
    aws_cidr = os.getenv('AWS_CIDR')
    azure_cidr = os.getenv('AZURE_CIDR')
    ipsec_shared_secret = os.getenv('IPSEC_PSK')

    assert license_file, 'License must be provided. [env=LICENSE]'
    assert keyset_token, 'Keyset token must be provided. [env=KEYSET_TOKEN]'
    assert aws_cidr, 'AWS network CIDR must be provided. [env=AWS_CIDR]'
    assert azure_cidr, 'Azure network CIDR must be provided. [env=AZURE_CIDR]'
    assert ipsec_shared_secret, 'Ipsec tunnel shared key must be provided. [env=IPSEC_PSK]'

    try:
        Logger.info('Setup on AWS....')
        config.setup_controller(
            aws_client, 
            'MultiCloud - AWS Controller',
            license_file,
            license_parameters={'default': True},
            keyset_parameters={'token': keyset_token},
            reboot_timeout=240,
            keyset_timeout=240)

        Logger.info('Creating local gateway routes')
        routes.create_local_gateway_route(aws_client, aws_cidr)

        Logger.info('Creating tunnel: AWS')
        aws_response = ipsec.create_tunnel_endpoint(
            aws_client, tunnel_name, ipsec_shared_secret, 
            tunnel_endpoint, azure_cidr, 
            tunnel_vti, target_network_name='Azure')
        Logger.info(aws_response)
    except (ApiException, CohesiveSDKException)as e:
        return e


def configure_multicloud_bridge_azure(azure_client, tunnel_endpoint, tunnel_name, tunnel_vti):
    license_file = os.getenv('LICENSE')
    keyset_token = os.getenv('KEYSET_TOKEN')
    aws_cidr = os.getenv('AWS_CIDR')
    azure_cidr = os.getenv('AZURE_CIDR')
    ipsec_shared_secret = os.getenv('IPSEC_PSK')

    assert license_file, 'License must be provided. [env=LICENSE]'
    assert keyset_token, 'Keyset token must be provided. [env=KEYSET_TOKEN]'
    assert aws_cidr, 'AWS network CIDR must be provided. [env=AWS_CIDR]'
    assert azure_cidr, 'Azure network CIDR must be provided. [env=AZURE_CIDR]'
    assert ipsec_shared_secret, 'Ipsec tunnel shared key must be provided. [env=IPSEC_PSK]'

    try:
        Logger.info('Setup on AZURE....')
        config.setup_controller(
            azure_client, 
            'MultiCloud - Azure Controller',
            license_file,
            license_parameters={'default': True},
            keyset_parameters={'token': keyset_token},
            reboot_timeout=240,
            keyset_timeout=240)

        Logger.info('Creating local gateway routes')
        # routes.create_local_gateway_route(azure_client, azure_cidr)

        Logger.info('Creating tunnel: Azure')
        azure_resp = ipsec.create_tunnel_endpoint(
            azure_client, tunnel_name, ipsec_shared_secret, 
            tunnel_endpoint, aws_cidr, 
            tunnel_vti, target_network_name='AWS')
        Logger.info(azure_resp)
    except (ApiException, CohesiveSDKException) as e:
        return e

def run():
    ipsec_tunnel_name = 'aws_azure_vns3_tunnel'
    vti_blocks = networkmath.calculate_next_subnets(
        prefix_length=30, take=2, cidr=constants.VTI_RANGE_LINK_LOCAL)
    return ipsec_tunnel_name, vti_blocks