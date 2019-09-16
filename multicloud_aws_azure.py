import os
import logging
import sys

from cohesivenet import constants, ApiException, CohesiveSDKException
from cohesivenet.clouds import networkmath
from cohesivenet.macros import connect, config, routes, ipsec, admin

Logger = logging.getLogger()
Logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
Logger.addHandler(ch)

def setup_clients():
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
        'password': master_password,
        'verify': False
    }

    aws_client_data = {
        'host': aws_host + ':8000',
        'username': 'api',
        'password': master_password,
        'verify': False
    }

    return connect.get_clients(aws_client_data, azure_client_data)
    reset_ps_response = admin.roll_api_password(master_password, [aws_client, azure_client])
    enable_ui_response = admin.roll_ui_credentials(
        {'username': 'vnscubed', 'password': master_password},
        [aws_client, azure_client], 
        enable_ui=True)
    return aws_client, azure_client

def configure_multicloud_bridge(aws_client=None, azure_client=None):
    license_file = os.getenv('LICENSE')
    keyset_token = os.getenv('KEYSET_TOKEN')
    aws_cidr = os.getenv('AWS_CIDR')
    azure_cidr = os.getenv('AZURE_CIDR')
    ipsec_shared_secret = os.getenv('IPSEC_PSK')

    if not all([aws_client, azure_client]):
        aws_client, azure_client = setup_clients()

    assert license_file, 'License must be provided. [env=LICENSE]'
    assert keyset_token, 'Keyset token must be provided. [env=KEYSET_TOKEN]'
    assert aws_cidr, 'AWS network CIDR must be provided. [env=AWS_CIDR]'
    assert azure_cidr, 'Azure network CIDR must be provided. [env=AZURE_CIDR]'
    assert ipsec_shared_secret, 'Ipsec tunnel shared key must be provided. [env=IPSEC_PSK]'
    
    try:
        Logger.info('Setup on AZURE....')
        config.setup_controller(
            azure_client, 
            'MultiCloud - Azure',
            license_file,
            license_parameters={'default': True},
            keyset_parameters={'token': keyset_token})
        # Logger.info(azure_controller_setup_response)

        Logger.info('Setup on AWS....')
        config.setup_controller(
            aws_client, 
            'MultiCloud - AWS',
            license_file,
            license_parameters={'default': True},
            keyset_parameters={'token': keyset_token})
        # Logger.info(aws_controller_setup_response)

        Logger.info('Creating local gateway routes')
        routes.create_local_gateway_route(aws_client, aws_cidr)
        routes.create_local_gateway_route(azure_client, azure_cidr)

        vti_blocks = networkmath.calculate_next_subnets(
            prefix_length=30, take=2, cidr=constants.VTI_RANGE_LINK_LOCAL)
        ipsec_tunnel_name = 'aws_azure_vns3_tunnel'

        Logger.info('Creating tunnel: AWS')
        aws_response = ipsec.create_tunnel_endpoint(
            aws_client, ipsec_tunnel_name, ipsec_shared_secret, 
            azure_client.configuration.host_ip, azure_cidr, 
            vti_blocks[0], target_network_name='Azure')
        Logger.info(aws_response)

        Logger.info('Creating tunnel: Azure')
        azure_resp = ipsec.create_tunnel_endpoint(
            azure_client, ipsec_tunnel_name, ipsec_shared_secret, 
            aws_client.configuration.host_ip, aws_cidr, 
            vti_blocks[1], target_network_name='AWS')
        Logger.info(azure_resp)
    except (ApiException, CohesiveSDKException)as e:
        return e