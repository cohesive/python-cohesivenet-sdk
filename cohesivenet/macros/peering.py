from itertools import combinations, permutations
from functools import partial as bind

from cohesivenet import data_types, VNS3Client, ApiException, log_util
from cohesivenet.clouds import networkmath
from cohesivenet.macros import api_operations


def set_peer_ids(clients) -> data_types.BulkOperationResult:
    """Set peer ids for all clients. Assume order of clients passed as ids
    
    Arguments:
        clients {List[VNS3Client]}
    
    Returns:
        BulkOperationResult
    """
    def _set_peer_id(_client, i):
        return _client.peering.put_self_peering_id({
            'id': i
        })

    bound_api_calls = [
        bind(_set_peer_id, client, index + 1)
        for index, client in enumerate(clients)
    ]

    return api_operations.__bulk_call_api(bound_api_calls)


def peer_mesh(clients, use_private_ip=False, delay_configure=False, mtu=None):
    """peer_mesh Create a peering mesh by adding each client as peer for other clients.
       The order of the list of clients is the assumed peering id, i.e. client at clients[0] 
       has peering id of 1, clients[1] has peering id of 2. Each TLS connection between peers
       is then automatically negotiated.
    
    Arguments:
        clients {List[VNS3Client]}
    
    Keyword Arguments:
        use_private_ip {bool} -- use private ip of client for peering name (default: False)
        delay_configure {bool} -- delay automatic negotiation of peer (default: False)
        mtu {int} -- Override MTU for the peering TLS connection (default: {None})
    
    Returns:
        [type] -- [description]
    """
    common_peer_kwargs = {}
    if delay_configure:
        common_peer_kwargs.update(force=False)
    if mtu:
        common_peer_kwargs.update(overlay_mtu=mtu)

    client_indexes = set(range(len(clients)))
    client_peering_ips = (
        [c.private_ip for c in clients]
        if use_private_ip 
        else [c.configuration.host_ip for c in clients])

    print(client_peering_ips)
    def create_all_peers_for_client(client, post_peer_args):
        return [
            client.peering.post_peer(dict(peering_request, **common_peer_kwargs))
            for peering_request in post_peer_args
        ]

    run_peering_funcs = []
    for i, vns3 in enumerate(clients):
        other_client_indexes = client_indexes - {i}
        peering_requests = [{
            'id': index + 1,
            'name': client_peering_ips[index]
        } for index in other_client_indexes]
        run_peering_funcs.append(bind(create_all_peers_for_client, vns3, peering_requests))

    return api_operations.__bulk_call_api(run_peering_funcs)