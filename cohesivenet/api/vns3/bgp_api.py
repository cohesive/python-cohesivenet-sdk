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

from cohesivenet.api_builder import VersionRouter


def get_bgp_peer(
    api_client, endpoint_id, bgp_peer_id, verbose=False, **kwargs
):  # noqa: E501
    """Get eBGP peer  # noqa: E501

    Get eBGP peer details  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = api.get_bgp_peer(client, endpoint_id, bgp_peer_id, async_req=True)

    :param int endpoint_id: ID for IPsec endpoint (required)
    :param int bgp_peer_id: ID for BGP peer (required)
    :param async_req bool: execute request asynchronously
    :param bool verbose: True for verbose output
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

    request_params = ["verbose"]  # noqa: E501

    collection_formats = {}

    query_params = []
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        query_params.append((param, local_var_params[param]))  # noqa: E501

    path_params = {"endpoint_id": endpoint_id, "bgp_peer_id": bgp_peer_id}

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth", "basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/ipsec/endpoints/{endpoint_id}/ebgp_peers/{bgp_peer_id}",
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


def delete_bgp_peer(api_client, endpoint_id, bgp_peer_id, **kwargs):  # noqa: E501
    """delete_bgp_peer  # noqa: E501

    Delete BGP Peer connection  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_bgp_peer(endpoint_id, bgp_peer_id, async_req=True)

    :param VNS3Client api_client: (required)
    :param int endpoint_id: ID for IPsec endpoint (required)
    :param int bgp_peer_id: ID for BGP peer (required)
    :param async_req bool: execute request asynchronously
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

    path_params = {"endpoint_id": endpoint_id, "bgp_peer_id": bgp_peer_id}
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
    auth_settings = ["ApiTokenAuth", "basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/ipsec/endpoints/{endpoint_id}/ebgp_peers/{bgp_peer_id}",
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


def create_bgp_peer(
    api_client,
    endpoint_id,
    ipaddress=None,
    asn=None,
    local_asn_alias=None,
    access_list=None,
    bgp_password=None,
    add_network_distance=None,
    add_network_distance_direction=None,
    add_network_distance_hops=None,
    **kwargs
):  # noqa: E501
    """Create BGP Peer  # noqa: E501

    Create new BGP peer connection for IPsec endpoint  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.create_bgp_peer(endpoint_id, create_bgp_peer_request, async_req=True)

    :param VNS3Client api_client: (required)
    :param int endpoint_id: ID for IPsec endpoint (required)
    :param str ipaddress: IP address of the desired BGP peer. (required)
    :param int asn: Autonomous system number assigned to device at ipaddress (required)
    :param int local_asn_alias: Autonomous system number alias
    :param str access_list: List of \"in permit CIDR\" and/or \"out permit CIDR\" statements in a string delimited by \"\\n\"
    :param str bgp_password: String to be agreed upon by both peers as a simple password.
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
        "ipaddress",
        "asn",
        "local_asn_alias",
        "access_list",
        "bgp_password",
        "add_network_distance",
        "add_network_distance_direction",
        "add_network_distance_hops",
    ]

    collection_formats = {}

    path_params = {"endpoint_id": endpoint_id}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {}
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        body_params[param] = local_var_params[param]

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # HTTP header `Content-Type`
    header_params["Content-Type"] = api_client.select_header_content_type(  # noqa: E501
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth", "basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/ipsec/endpoints/{endpoint_id}/ebgp_peers",
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


def update_bgp_peer(
    api_client,
    endpoint_id,
    bgp_peer_id,
    ipaddress=None,
    asn=None,
    local_asn_alias=None,
    access_list=None,
    bgp_password=None,
    add_network_distance=None,
    add_network_distance_direction=None,
    add_network_distance_hops=None,
    **kwargs
):  # noqa: E501
    """update_bgp_peer  # noqa: E501

    Edit BGP peer connection parameters  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.update_bgp_peer(endpoint_id, bgp_peer_id, update_bgp_peer_connection_request, async_req=True)

    :param VNS3Client api_client: (required)
    :param async_req bool: execute request asynchronously
    :param int endpoint_id: ID for IPsec endpoint (required)
    :param int bgp_peer_id: ID for BGP peer (required)
    :param str ipaddress: IP address of the desired BGP peer. (required)
    :param int asn: Autonomous system number assigned to device at ipaddress (required)
    :param int local_asn_alias: Autonomous system number alias
    :param str access_list: List of \"in permit CIDR\" and/or \"out permit CIDR\" statements in a string delimited by \"\\n\"
    :param str bgp_password: String to be agreed upon by both peers as a simple password.
    :param bool add_network_distance: Enable network distance for BGP peer
    :param str add_network_distance_direction: Add distance direction for BGP peer
    :param int add_network_distance_hops: Distance metric weight indicating distance in hops for BGP peer
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                If the method is called asynchronously,
                returns the request thread.
    """

    local_var_params = locals()

    request_params = [
        "ipaddress",
        "asn",
        "local_asn_alias",
        "access_list",
        "bgp_password",
        "add_network_distance",
        "add_network_distance_direction",
        "add_network_distance_hops",
    ]

    local_var_params = locals()

    collection_formats = {}

    path_params = {"endpoint_id": endpoint_id, "bgp_peer_id": bgp_peer_id}

    query_params = []

    header_params = {}

    form_params = []

    local_var_files = {}

    body_params = {}
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        body_params[param] = local_var_params[param]

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # HTTP header `Content-Type`
    header_params["Content-Type"] = api_client.select_header_content_type(  # noqa: E501
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth", "basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/ipsec/endpoints/{endpoint_id}/ebgp_peers/{bgp_peer_id}",
        "PUT",
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


class BGPApiRouter(VersionRouter):
    """Manage BGP peers"""

    function_library = {
        "get_bgp_peer": {"4.8.4-5.0.0": get_bgp_peer},
        "delete_bgp_peer": {"4.8.4-5.0.0": delete_bgp_peer},
        "create_bgp_peer": {"4.8.4-5.0.0": create_bgp_peer},
        "update_bgp_peer": {"4.8.4-5.0.0": update_bgp_peer},
    }
