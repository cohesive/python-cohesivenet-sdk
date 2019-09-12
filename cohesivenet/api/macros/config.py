import logging
import os

from typing import Dict
from cohesivenet import VNS3Client, data_types, ApiException, ApiValueError
from cohesivenet.api.macros import api_operations

Logger = logging.getLogger('cohesivenet.api.macros')


def license_clients(clients, license_file_path) -> data_types.BulkOperationResult:
    """Upload license file to all clients. These will have DIFFERENT keysets. See keyset operations
       if all controllers are to be in the same clientpack topology 
    
    Arguments:
        clients {List[VNS3Client]}
        license_file_path {str} - full path to license file
    
    Returns:
        BulkOperationResult
    """
    license_file = open(license_file_path).read().strip()
    def  _upload_license(_client):
        return _client.licensing.upload_license(license_file)

    return api_operations.__bulk_call_api(clients, _upload_license)


def accept_clients_license(clients, license_parameters) -> data_types.BulkOperationResult:
    """Accept licenses for all. These will have DIFFERENT keysets. See keyset operations
       if all controllers are to be in the same clientpack topology. Assumes same license
       parameters will be accepted for all clients
    
    Arguments:
        clients {List[VNS3Client]}
        license_parameters {UpdateLicenseParametersRequest} - dict {
            'subnet': 'str',
            'managers': 'str',
            'asns': 'str',
            'clients': 'str',
            'my_manager_vip': 'str',
            'default': 'bool'
        }
    
    Returns:
        BulkOperationResult
    """
    license_file = open(license_file_path).read().strip()
    def _accept_license(_client):
        return _client.licensing.put_set_license_parameters(license_parameters)
    return api_operations.__bulk_call_api(clients, _accept_license)


def setup_controller(client: VNS3Client, topology_name: str, license_file: str,
                     license_parameters: Dict, keyset_parameters: Dict, peering_id: int = 1):
    """setup_controller Set the topology name, set up controller license, keyset and peering ID if provided

    Arguments:
        client {VNS3Client} -- [description]
        topology_name {str} -- [description]
        keyset_parameters {Dict} -- UpdateKeysetRequest {
            'source': 'str',
            'token': 'str',
            'topology_name': 'str',
            'sealed_network': 'bool'
        }
        peering_id {int} -- ID for this controller in peering mesh

    Returns:
        OperationResult
    """
    setup_response = {
        'topology_name': None,
        'keyset': None,
        'license': None,
        'peering': None,
        'error': None
    }
    try:
        topology_response = client.config.put_config({
            'topology_name': topology_name
        })
        setup_response.update(topology_response=topology_response['response']['topology_name'])
        Logger.info('Topology Name updated')

        if not os.path.isfile(license_file):
            Logger.info('License file does not exist')
            setup_response.update(error=ApiValueError('License File %s does not exist' % license_file))
            return setup_response

        license_file = open(license_file).read().strip()
        upload_response = client.licensing.upload_license(license_file)
        setup_response.update(license=upload_response.response)
        Logger.info('License uploaded')

        accept_license_response = client.licensing.put_set_license_parameters(license_parameters)
        Logger.info('License accepted. Controller rebooting. Waiting for api availability.')
        setup_response.update(license_parameters=accept_license_response.response.parameters)
        client.sys_admin.wait_for_api(timeout=90)

        generate_keyset_response = client.config.put_keyset(keyset_parameters)
        Logger.info('Keyset generating. Waiting for keyset availability.')
        keyset_detail = client.config.wait_for_keyset(timeout=90)
        setup_response.update(keyset=keyset_detail)

        if peering_id:
            peering_response = client.peering.put_self_peering_id({'id': peering_id})
            setup_response.update(peering=peering_response.response)
            Logger.info('Peering ID set.')

        return data_types.OperationResult(client, setup_response)
    except ApiException as e:
        setup_response.update(error=e)
        return setup_response