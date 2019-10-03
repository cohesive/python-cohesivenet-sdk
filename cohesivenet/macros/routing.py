from functools import partial as bind

from cohesivenet import data_types, log_util
from cohesivenet.clouds import networkmath
from cohesivenet.macros import api_operations


def create_route_advertisements(clients, local_subnets) -> data_types.BulkOperationResult:
    """create_route_advertisements Create a route advertisement for controllers network
    
    Arguments:
        clients {List[VNS3Client]}
        local_subnets {List[str]} - order should correspond with clients list
    
    Returns:
        data_types.BulkOperationResult
    """
    assert len(clients) == len(local_subnets), 'clients list length must equal local_subnets list length'

    invalid = []
    for index, client in enumerate(clients):
        if not networkmath.subnet_contains_ipv4(client.private_ip, local_subnets[index]):
            invalid.append('%s not in %s' % (client.private_ip, local_subnets[index]))

    if len(invalid):
        raise AssertionError('Invalid subnets provided for clients: %s.' % ','.join(invalid))

    def _create_route(_client, subnet):
        return _client.routing.post_create_route({
            'cidr': subnet,
            'description': 'Local subnet advertisement',
            'advertise': True,
            'gateway': ''
        })

    bound_api_calls = [
        bind(_create_route, client, local_subnets[index])
        for index, client in enumerate(clients)
    ]

    return api_operations.__bulk_call_api(bound_api_calls)


def test_logging(data):
    log_util.log_debug('debug heres the fucking gist', **data)
    log_util.log_info('info heres the fucking gist', **data)
    log_util.log_error('error heres the fucking gist', **data)
