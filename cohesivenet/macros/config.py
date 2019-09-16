import logging
import os
from typing import Dict

from cohesivenet import VNS3Client, data_types, CohesiveSDKException, ApiValueError
from cohesivenet.macros import api_operations


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
    """setup_controller Set the topology name, controller license, keyset and peering ID if provided

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
    logger = logging.getLogger(__name__)
    current_config = client.config.get_config().response
    if current_config.topology_name != topology_name:
        topology_response = client.config.put_config({
            'topology_name': topology_name
        })
        logger.info('Topology Name updated')
    else:
        logger.info('Controller already has topology name. Skipping.')

    if not current_config.licensed:
        if not os.path.isfile(license_file):
            logger.info('License file does not exist')
            raise CohesiveSDKException('License file does not exist')

        license_file = open(license_file).read().strip()
        upload_response = client.licensing.upload_license(license_file)
        logger.info('License uploaded')
    else:
        logger.info('Controller is already licensed. Skipping.')

    current_license = client.licensing.get_license().response
    if not current_license.finalized:
        accept_license_response = client.licensing.put_set_license_parameters(license_parameters)
        logger.info('License accepted. Controller rebooting. Waiting for api availability.')
        client.sys_admin.wait_for_api(timeout=90)
    else:
        logger.info('License is already accepted. Skipping.')

    current_keyset = client.config.get_keyset().response
    if not current_keyset.keyset_present and not current_keyset.in_progress:
        generate_keyset_response = client.config.put_keyset(keyset_parameters)
        logger.info('Keyset generating. Waiting for keyset availability.')
        keyset_detail = client.config.wait_for_keyset(timeout=90)
    else:
        logger.info('Keyset is already present [in_progress=%s]. Skipping.' % current_keyset.in_progress)

    current_peering_status = client.peering.get_peering_status().response
    if not current_peering_status.id and peering_id:
        peering_response = client.peering.put_self_peering_id({'id': peering_id})
        logger.info('Peering ID set.')
    return client