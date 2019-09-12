import cohesivenet.constants as cohesive_constants
from cohesivenet.api.macros import connect, config, routes, ipsec


def run():
    import os

    license_file = os.getenv('LICENSE')
    keyset_token = os.getenv('KEYSET_TOKEN')
    aws_cidr = os.getenv('AWS_CIDR')
    azure_cidr = os.getenv('AZURE_CIDR')

    azure_host_data = {
        'host': os.getenv('AZURE_HOST') + ':8000',
        'username': 'api',
        'password': os.getenv('AZURE_DEFAULT_PASSWORD'),
        'verify': False
    }

    aws_host_data = {
        'host': os.getenv('AWS_HOST') + ':8000',
        'username': 'api',
        'password': os.getenv('AWS_DEFAULT_PASSWORD'),
        'verify': False
    }

    aws_client, azure_client = connect.get_clients(aws_host_data, azure_host_data)
    
    azure_controller_setup_response = config.setup_controller(
        azure_client, 
        'MultiCloud - Azure',
        license_file,
        license_parameters={'default': True},
        keyset_parameters={'token': keyset_token})

    aws_controller_setup_response = config.setup_controller(
        aws_client, 
        'MultiCloud - AWS',
        license_file,
        license_parameters={'default': True},
        keyset_parameters={'token': keyset_token})

    # parallizable
    routes.create_local_gateway_route(aws_client, aws_cidr)
    routes.create_local_gateway_route(azure_client, azure_cidr)


    vti_blocks = networkmath.calculate_next_subnets(
        prefix_length=30, take=2, cidr=cohesive_constants.VTI_RANGE_LINK_LOCAL)
    ipsec_tunnel_name = 'aws_azure_vns3_tunnel'
    shared_secret = 'thisisatestsharedsecret'

    ipsec.create_tunnel_endpoint(
        aws_client, ipsec_tunnel_name, shared_secret, 
        azure_client.configuration.host_ip, azure_cidr, 
        vti_blocks[0], target_network_name='Azure')

    ipsec.create_tunnel_endpoint(
        azure_client, ipsec_tunnel_name, shared_secret, 
        aws_client.configuration.host_ip, aws_cidr, 
        vti_blocks[1], target_network_name='AWS')