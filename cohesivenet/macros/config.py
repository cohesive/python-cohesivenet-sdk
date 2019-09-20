import logging
import os
from typing import Dict

from cohesivenet import VNS3Client, data_types, CohesiveSDKException, ApiValueError, ApiException
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
                     license_parameters: Dict, keyset_parameters: Dict, peering_id: int = 1,
                     reboot_timeout=120, keyset_timeout=120):
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

    if not current_config.licensed:
        if not os.path.isfile(license_file):
            raise CohesiveSDKException('License file does not exist')

        license_file = open(license_file).read().strip()
        upload_response = client.licensing.upload_license(license_file)

    accept_license = False
    try:
        current_license = client.licensing.get_license().response
        accept_license = not current_license or not current_license.finalized
    except ApiException as e:
        if e.get_error_message() == 'Must be licensed first.':
            accept_license = True
        else:
            raise e

    if accept_license:
        accept_license_response = client.licensing.put_set_license_parameters(license_parameters)
        client.sys_admin.wait_for_api(timeout=reboot_timeout, wait_for_reboot=True)

    current_keyset = client.config.get_keyset().response
    if not current_keyset:
        # API not up yet. Really this shouldnt happen
        client.sys_admin.wait_for_api(timeout=reboot_timeout, wait_for_reboot=True)

    current_keyset = client.config.get_keyset().response
    if not current_keyset.keyset_present and not current_keyset.in_progress:
        generate_keyset_response = client.config.put_keyset(keyset_parameters)
        client.config.wait_for_keyset(timeout=keyset_timeout)
    elif current_keyset.in_progress:
        client.config.wait_for_keyset(timeout=keyset_timeout)

    current_peering_status = client.peering.get_peering_status().response
    if not current_peering_status.id and peering_id:
        peering_response = client.peering.put_self_peering_id({'id': peering_id})
    return client