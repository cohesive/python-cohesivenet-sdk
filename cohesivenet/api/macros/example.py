import os

from cohesivenet import constants as cohesive_constants
from cohesivenet.clouds import networkmath
from cohesivenet.api.macros import connect, config, routes, ipsec, admin

Logger = logging.getLogger(__name__)

def setup_clients(with_defaults=False):
    azure_host = os.getenv('AZURE_HOST')
    aws_host = os.getenv('AWS_HOST')
    azure_def_password = os.getenv('AZURE_DEFAULT_PASSWORD')
    aws_def_password = os.getenv('AWS_DEFAULT_PASSWORD')
    master_password = os.getenv('MASTER_PASSWORD')

    azure_host_data = {
        'host': azure_host + ':8000',
        'username': 'api',
        'password': azure_def_password if with_defaults else master_password,
        'verify': False
    }

    aws_host_data = {
        'host': aws_host + ':8000',
        'username': 'api',
        'password': aws_def_password if with_defaults else master_password,
        'verify': False
    }

    aws_client, azure_client = connect.get_clients(aws_host_data, azure_host_data)

    if not with_defaults:
        return aws_client, azure_client

    reset_ps_response = admin.roll_api_password(master_password, [azure_client])
    enable_ui_response = admin.roll_ui_credentials(
        {'username': 'vnscubed', 'password': master_password},
        [aws_client, azure_client], 
        enable_ui=True)
    return aws_client, azure_client

def run(aws_client=None, azure_client=None):
    import os

    license_file = os.getenv('LICENSE')
    keyset_token = os.getenv('KEYSET_TOKEN')
    aws_cidr = os.getenv('AWS_CIDR')
    azure_cidr = os.getenv('AZURE_CIDR')

    if not all([aws_client, azure_client]):
        aws_client, azure_client = setup_clients()
    
    Logger.info('Setup on AZURE....')
    azure_controller_setup_response = config.setup_controller(
        azure_client, 
        'MultiCloud - Azure',
        license_file,
        license_parameters={'default': True},
        keyset_parameters={'token': keyset_token})
    # Logger.info(azure_controller_setup_response)
    if azure_controller_setup_response.get('error'):
        return azure_controller_setup_response

    Logger.info('Setup on AWS....')
    aws_controller_setup_response = config.setup_controller(
        aws_client, 
        'MultiCloud - AWS',
        license_file,
        license_parameters={'default': True},
        keyset_parameters={'token': keyset_token})
    # Logger.info(aws_controller_setup_response)
    if aws_controller_setup_response.get('error'):
        return aws_controller_setup_response

    # Logger.info('Creating local gateway routes')
    # routes.create_local_gateway_route(aws_client, aws_cidr)
    # routes.create_local_gateway_route(azure_client, azure_cidr)

    vti_blocks = networkmath.calculate_next_subnets(
        prefix_length=30, take=2, cidr=cohesive_constants.VTI_RANGE_LINK_LOCAL)
    ipsec_tunnel_name = 'aws_azure_vns3_tunnel'
    shared_secret = 'thisisatestsharedsecret'

    Logger.info('Creating tunnel: AWS')
    aws_response = ipsec.create_tunnel_endpoint(
        aws_client, ipsec_tunnel_name, shared_secret, 
        azure_client.configuration.host_ip, azure_cidr, 
        vti_blocks[0], target_network_name='Azure')
    Logger.info(aws_response)

    Logger.info('Creating tunnel: Azure')
    azure_resp = ipsec.create_tunnel_endpoint(
        azure_client, ipsec_tunnel_name, shared_secret, 
        aws_client.configuration.host_ip, aws_cidr, 
        vti_blocks[1], target_network_name='AWS')
    Logger.info(azure_resp)