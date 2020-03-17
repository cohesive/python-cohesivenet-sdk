# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from cohesivenet import Logger
from cohesivenet.api_builder import validate_call, VersionRouter


class RouteConstants(object):
    RouteComparisonKeys = ["cidr", "interface", "gateway", "advertise"]


@validate_call(path_params=["route_id"])
def delete_route(api_client, route_id, **kwargs):  # noqa: E501
    """delete_route  # noqa: E501

    Delete Route  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_route(route_id, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int route_id: ID for Route (required)
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    collection_formats = {}

    path_params = {"route_id": route_id}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/routes/{route_id}",
        "DELETE",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def get_routes(api_client, **kwargs):  # noqa: E501
    """get_routes  # noqa: E501

    Describes routes that this manager has access to via its network interfaces (virtual or otherwise).
    If advertized, other VNS3 Controllers will receive the route instantly. Network clients will
    receive it when they get their next route push, which is normally on a re-connect or in neartime
    if they use the VNS3 Routing agent on their cloud servers. Remote endpoints  (other data centers)
    would not receive the route unless specified as part of  their IPsec Configuration AND the
    Configuration of such a tunnel on the VNS3 controller.   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_routes(async_req=True)

    :param async_req bool: execute request asynchronously
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/routes",
        "GET",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


@validate_call(body_params=["cidr"])
def post_create_route(
    api_client,
    cidr=None,
    description=None,
    interface=None,
    gateway=None,
    tunnel=None,
    advertise=None,
    metric=None,
    **kwargs
):  # noqa: E501
    """post_create_route  # noqa: E501

    Pushes routes that this manager has access to via its network interfaces (virtual or otherwise)   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_route(create_route_request, async_req=True)

    :param cidr str: CIDR of a route that the VNS3 Controller has access  to that it wants to
                     publish throughout the  Routing tables of the overlay network
    :param description str:
    :param interface str: Sets the interface where this route will be advertised.
    :param gateway str: If interface is set, a specific gateway address reachable from that interface
    :param tunnel int: numerical reference for the GRE endpoint id (must provide either tunnel OR interface)
    :param advertise bool: Advertise route to overlay network
    :param metric int: Weight for route
    :param async_req bool: execute request asynchronously
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    request_params = [
        "cidr",
        "description",
        "interface",
        "gateway",
        "tunnel",
        "advertise",
        "metric",
    ]

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []

    local_var_files = {}

    body_params = {}
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        body_params[param] = local_var_params[param]

    gateway = body_params.get("gateway")
    if not gateway:
        body_params["gateway"] = "_notset"
    interface = body_params.get("interface")
    if not interface:
        body_params["interface"] = "_notset"

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # HTTP header `Content-Type`
    header_params["Content-Type"] = api_client.select_header_content_type(  # noqa: E501
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/routes",
        "POST",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def post_create_route_if_not_exists(
    api_client, route_request, comparison_keys=RouteConstants.RouteComparisonKeys
):
    """Create route if it doesn not exist for client. Compare based on keys.

    Arguments:
        client {VNS3Client}
        route {dict} - Route dictionary

    Keyword Arguments:
        comparison_keys {List[str]} - list of Route attributes to compare when checking for existence.
                                        default: ["cidr", "interface", "gateway"]

    Returns:
        [RoutesListResponse] -  dictionary of routes keyed by route Ids (ints). id -> dict
    """

    def __to_route_tuple(route, keys):
        t = ()
        for key in keys:
            _val = route.get(key)
            if _val is not None:
                t += (_val,)
            elif key in ("interface", "gateway"):
                t += ("_notset",)
            else:
                t += (None,)
        return t

    routes_response = api_client.routing.get_routes().response
    route_tuples = {
        __to_route_tuple(
            current_route, comparison_keys
        ): current_route
        for current_route in routes_response.values()
    } if routes_response else {}
    new_route_tuple = __to_route_tuple(route_request, comparison_keys)
    if new_route_tuple in route_tuples:
        Logger.debug(
            "Route already exists. Skipping creation.", host=api_client.host_uri,
        )
        return routes_response

    return api_client.routing.post_create_route(**route_request).response


class RoutingApiRouter(VersionRouter):

    function_library = {
        "delete_route": {"4.8.4": delete_route},
        "get_routes": {"4.8.4": get_routes},
        "post_create_route": {"4.8.4": post_create_route},
        "post_create_route_if_not_exists": {"4.8.4": post_create_route_if_not_exists},
    }
