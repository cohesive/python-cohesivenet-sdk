from cohesivenet.clouds import networkmath
from cohesivenet.macros import api_operations


def create_local_gateway_route(client, local_cidr, **route_kwargs):
    """[summary]

    Arguments:
        client {[type]} -- [description]
        local_cidr {[type]} -- [description]

    Keyword Arguments:
        gateway {[type]} -- [description] (default: {None})

    Returns:
        OperationResult
    """
    route = dict(
        **{
            "cidr": local_cidr,
            "description": "Local Underlay Network Routing",
            "interface": "eth0",
            "gateway": networkmath.get_default_gateway(local_cidr),
            "advertise": "False",
            "metric": 0,
        },
        **route_kwargs
    )
    return api_operations.try_api_call(
        client.routing.post_create_route, route, should_raise=True
    )
