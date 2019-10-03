import os
import logging
import sys
import urllib3
import pprint
from itertools import combinations

from cohesivenet import constants, ApiException, CohesiveSDKException, VNS3Client
from cohesivenet.clouds import networkmath
from cohesivenet.macros import connect, config, routes, ipsec, admin

urllib3.disable_warnings()
Logger = logging.getLogger()
Logger.handlers = []
Logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
Logger.addHandler(ch)


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
    assert type(host_password_dicts) in list, 'setup_clients expects list as input.'

    return connect.get_clients([
        dict(connect_args, verify=False, username'api')
        for connect_args in host_password_dicts
    ])

def update_client_passwords(clients, master_password):
    """[summary]
    
    Arguments:
        clients {List[VNS3Client]}
        master_password {str}
    
    Returns:
        List[VNS3Client]
    """
    admin.roll_api_password(master_password, clients)
    admin.roll_ui_credentials({
        'username': 'vnscubed',
        'password': master_password
    }, clients, enable_ui=True)
    return clients

def peer_controllers(client_1,  client_2):
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
    missing_kwargs = [a for a in required_kwargs if a not in bridge_kwargs]
    if len(missing_kwargs) > 0:
        return CohesiveSDKException('Missing args for bridge %s' % missing_kwargs)

    try:
        target_client = bridge_kwargs['target_client']
        topology_name = bridge_kwargs['target_topology_name']
        Logger.info('Setup for %s...' % topology_name)
        config.setup_controller(
            target_client, 
            topology_name,
            bridge_kwargs['license_file'],
            license_parameters={'default': True},
            keyset_parameters={'token': bridge_kwargs['keyset_token']},
            reboot_timeout=240,
            keyset_timeout=240)

        target_cidr = bridge_kwargs['target_cidr']
        Logger.info('Creating local gateway routes for %s' % target_cidr)
        routes.create_local_gateway_route(target_client, target_cidr)

        endpoint_name = bridge_kwargs['endpoint_name']
        Logger.info('Creating tunnel: %s' % endpoint_name)
        return ipsec.create_tunnel_endpoint(
            target_client, endpoint_name, bridge_kwargs['tunnel_psk'],
            bridge_kwargs['peer_endpoint'], bridge_kwargs['peer_cidr'], 
            bridge_kwargs['tunnel_vti'])
    except (ApiException, CohesiveSDKException) as e:
        return e


# configure origin controller
# configure rest of 
#
# for each controller
#    configure controller
# for each combination:
#    peer controllers


def setup_root_controller(client, license_file, keyset_token, topology_name):
    """setup_root_controller Configure root controller
    
    Arguments:
        client {[type]} -- [description]
        license_file {[type]} -- [description]
        keyset_token {[type]} -- [description]
        topology_name {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    try:
        return config.setup_controller(
            client, 
            topology_name,
            license_file,
            license_parameters={'default': True},
            keyset_parameters={'token': keyset_token},
            reboot_timeout=240,
            keyset_timeout=240)
    except (ApiException, CohesiveSDKException) as e:
        return e
    pass

def peer_controllers(controller1, controller2):
    pass

def run_configure_peered_topology(**parameters):
    root_controller_data = parameters.get('root_controller')
    root_client = update_client_passwords(
        setup_clients(root_controller_data),
        parameters.get('master_password'))[0]
    peer_clients = update_client_passwords(
        setup_clients(parameters.get('controllers')),
        parameters.get('master_password'))

    try:
        config_resp = config.setup_controller(
            root_client, 
            topology_name,
            license_file,
            license_parameters={'default': True},
            keyset_parameters={'token': keyset_token},
            reboot_timeout=240,
            keyset_timeout=240)


    except (ApiException, CohesiveSDKException) as e:
        return e






def get_env():
    controller_hosts = os.getenv('CONTROLLER_HOSTS_CSV').split(',')
    controller_passwords = os.getenv('CONTROLLER_PASSWORDS_CSV').split(',')
    root_controller_host = os.getenv('ROOT_CONTROLLER')
    root_controller_password = os.getenv('ROOT_CONTROLLER_PASSWORD')
    if root_controller_host and not root_controller_password:
        raise Exception('ROOT_CONTROLLER_PASSWORD is required if ROOT_CONTROLLER is provided')

    if not root_controller_host:
        root_controller_host = controller_hosts.pop()
        root_controller_password = controller_passwords.pop()

    controller_hosts.discard(root_controller_host)
    license_file = os.getenv('LICENSE')
    keyset_token = os.getenv('KEYSET_TOKEN')
    return {
        'controllers': [{
            'host': host,
            'password': controller_passwords[i]
        } for i, host in enumerate(controller_hosts)],
        'master_password': os.getenv('MASTER_PASSWORD'),
        'root_controller': {
            'host': root_controller_host,
            'password': root_controller_password
        },
        'license': license_file,
        'keyset_token': keyset_token
    }




if __name__ == "__main__":
    response = run_configure_peered_topology(**get_env())
    pprint(responses)