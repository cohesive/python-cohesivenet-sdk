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
from cohesivenet.api_builder import VersionRouter
from cohesivenet.exceptions import CohesiveSDKException


def delete_ipsec_endpoint(api_client, endpoint_id, **kwargs):  # noqa: E501
    """delete_ipsec_endpoint  # noqa: E501

    Delete IPsec endpoint  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_ipsec_endpoint(endpoint_id, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int endpoint_id: ID for IPsec endpoint (required)
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

    path_params = {"endpoint_id": endpoint_id}

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
        "/ipsec/endpoints/{endpoint_id}",
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


def delete_ipsec_endpoint_tunnel(
    api_client, endpoint_id, tunnel_id, **kwargs
):  # noqa: E501
    """delete_ipsec_endpoint_tunnel  # noqa: E501

    Delete IPsec tunnel  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_ipsec_endpoint_tunnel(endpoint_id, tunnel_id, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int endpoint_id: ID for IPsec endpoint (required)
    :param int tunnel_id: ID for tunnel (required)
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

    path_params = {"endpoint_id": endpoint_id, "tunnel_id": tunnel_id}

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
        "/ipsec/endpoints/{endpoint_id}/tunnels/{tunnel_id}",
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


def get_ipsec_details(api_client, **kwargs):  # noqa: E501
    """get_ipsec_details  # noqa: E501

    Get details for all IPsec endpoints/subnets  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_ipsec_details(async_req=True)

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
    auth_settings = ["ApiTokenAuth", "basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/ipsec",
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


def get_ipsec_endpoint(api_client, endpoint_id, **kwargs):  # noqa: E501
    """get_ipsec_endpoint  # noqa: E501

    Get IPsec endpoint information  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_ipsec_endpoint(endpoint_id, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int endpoint_id: ID for IPsec endpoint (required)
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

    path_params = {"endpoint_id": endpoint_id}

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
        "/ipsec/endpoints/{endpoint_id}",
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


def get_ipsec_status(api_client, **kwargs):  # noqa: E501
    """get_ipsec_status  # noqa: E501

    Describe ipsec tunnels status  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_ipsec_status(async_req=True)

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
    auth_settings = ["ApiTokenAuth", "basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/status/ipsec",
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


def get_connected_subnets(api_client):
    # TODO:
    pass


def get_ipsec_link_history(
    api_client, remote=None, local=None, tunnelid=None, **kwargs
):  # noqa: E501
    """get_ipsec_link_history  # noqa: E501

    Provides information about the connection history of the subnet or tunnel  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_ipsec_link_history(async_req=True)

    :param str remote: Address string in CIDR format to display link history to a remote endpoint.
    :param str local: Address string in CIDR format which will display status of the local route
    :param int tunnelid: Will display link history of just the tunnel specified, which may be only one tunnel to a remote endpoint.
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

    request_params = ["remote", "local", "tunnelid"]  # noqa: E501

    collection_formats = {}

    path_params = {}

    query_params = []
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        query_params.append((param, local_var_params[param]))  # noqa: E501

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
        "/status/link_history",
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


def post_create_ipsec_endpoint(
    api_client,
    name=None,
    ipaddress=None,
    secret=None,
    description=None,
    pfs=True,
    ike_version=1,
    nat_t_enabled=True,
    extra_config=None,
    private_ipaddress=None,
    gre=None,
    gre_interface_address=None,
    vpn_type=None,
    route_based_int_address=None,
    route_based_local=None,
    route_based_remote=None,
    **kwargs
):  # noqa: E501
    """post_create_ipsec_endpoint  # noqa: E501

    Create IPsec connection to the defined remote gateway  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_ipsec_endpoint(create_ipsec_endpoint_request, async_req=True)

    :param name str: Name for the connection. (required)
    :param ipaddress str: IP of the remote gateway (required)
    :param secret str:  Pre-shared key (required)
    :param description str: Description of this IPsec endpoint
    :param pfs bool: Perfect Forward Secrecy if true, disables if false. defaults to true.
    :param ike_version int: Version for IKE algorithm. default 1
    :param nat_t_enabled bool: True if you want encapsulated IPsec protocol to this gateway. default true
    :param extra_config str: Additional optionals for connection such as 'phase1=aes256_gcm-sha2_256-dh14 phase2=aes256_gcm'
    :param private_ipaddress str: Internal NAT address of the remote gateway
    :param gre bool: True if GRE is being used for the specific endpoint
    :param gre_interface_address str: Interface for GRE in /30 format
    :param vpn_type str: policy, gre, vti. defaults to policy
    :param route_based_int_address str:
    :param route_based_local str:
    :param route_based_local str:
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
        "name",
        "ipaddress",
        "secret",
        "description",
        "pfs",
        "ike_version",
        "nat_t_enabled",
        "extra_config",
        "private_ipaddress",
        "gre",
        "gre_interface_address",
        "vpn_type",
        "route_based_int_address",
        "route_based_local",
        "route_based_remote",
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
        "/ipsec/endpoints",
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


def post_create_ipsec_endpoint_tunnel(
    api_client,
    endpoint_id,
    remote_subnet=None,
    local_subnet=None,
    enabled=None,
    ping_ipaddress=None,
    ping_interface=None,
    ping_interval=None,
    description=None,
    **kwargs
):  # noqa: E501
    """post_create_ipsec_endpoint_tunnel  # noqa: E501

    Create IPsec endpoint tunnel  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_ipsec_endpoint_tunnel(endpoint_id, remote_subnet=remote_subnet, , async_req=True)

    :param int endpoint_id: ID for IPsec endpoint (required)
    :param remote_subnet str:
    :param local_subnet str:
    :param enabled str:
    :param ping_ipaddress str:
    :param ping_interface str:
    :param ping_interval int:
    :param description str:
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
        "remote_subnet",
        "local_subnet",
        "enabled",
        "ping_ipaddress",
        "ping_interface",
        "ping_interval",
        "description",
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
        "/ipsec/endpoints/{endpoint_id}/tunnels",
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


def post_restart_ipsec_action(api_client, restart=True, **kwargs):  # noqa: E501
    """post_restart_ipsec_action  # noqa: E501

    Restart ipsec subystem  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_restart_ipsec_action(client, True, async_req=True)

    :param restart bool:
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

    request_params = ["restart"]

    collection_formats = {}

    path_params = {}

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
        "/ipsec",
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


def put_update_ipsec_endpoint(
    api_client,
    endpoint_id,
    name=None,
    ipaddress=None,
    secret=None,
    description=None,
    pfs=True,
    ike_version=1,
    nat_t_enabled=True,
    extra_config=None,
    private_ipaddress=None,
    gre=None,
    gre_interface_address=None,
    vpn_type=None,
    route_based_int_address=None,
    route_based_local=None,
    route_based_remote=None,
    **kwargs
):  # noqa: E501
    """put_update_ipsec_endpoint  # noqa: E501

    update IPsec connection  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_update_ipsec_endpoint(endpoint_id, update_ipsec_connection_request, async_req=True)

    :param int endpoint_id: ID for IPsec endpoint (required)
    :param name str: Name for the connection.
    :param ipaddress str: IP of the remote gateway
    :param secret str:  Pre-shared key
    :param description str: Description of this IPsec endpoint
    :param pfs bool: Perfect Forward Secrecy if true, disables if false.
    :param ike_version int: Version for IKE algorithm.
    :param nat_t_enabled bool: True if you want encapsulated IPsec protocol to this gateway.
    :param extra_config str: Additional optionals for connection such as 'phase1=aes256_gcm-sha2_256-dh14 phase2=aes256_gcm'
    :param private_ipaddress str: Internal NAT address of the remote gateway
    :param gre bool: True if GRE is being used for the specific endpoint
    :param gre_interface_address str: Interface for GRE in /30 format
    :param vpn_type str: policy, gre, vti. defaults to policy
    :param route_based_int_address str:
    :param route_based_local str:
    :param route_based_local str:
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
        "name",
        "ipaddress",
        "secret",
        "description",
        "pfs",
        "ike_version",
        "nat_t_enabled",
        "extra_config",
        "private_ipaddress",
        "gre",
        "gre_interface_address",
        "vpn_type",
        "route_based_int_address",
        "route_based_local",
        "route_based_remote",
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
        "/ipsec/endpoints/{endpoint_id}",
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


def put_update_ipsec_endpoint_tunnel(
    api_client,
    endpoint_id,
    tunnel_id,
    remote_subnet=None,
    local_subnet=None,
    enabled=None,
    bounce=None,
    ping_ipaddress=None,
    ping_interface=None,
    ping_interval=None,
    description=None,
    **kwargs
):  # noqa: E501
    """put_update_ipsec_endpoint_tunnel  # noqa: E501

    update IPsec endpoint tunnel  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_update_ipsec_endpoint_tunnel(endpoint_id, tunnel_id, update_ipsec_tunnel_request, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int endpoint_id: ID for IPsec endpoint (required)
    :param int tunnel_id: ID for tunnel (required)
    :param remote_subnet str:
    :param local_subnet str:
    :param enabled str:
    :param bounce bool: restart tunnel
    :param ping_ipaddress str:
    :param ping_interface str:
    :param ping_interval int:
    :param description str:
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
        "remote_subnet",
        "local_subnet",
        "enabled",
        "bounce",
        "ping_ipaddress",
        "ping_interface",
        "ping_interval",
        "description",
    ]

    collection_formats = {}

    path_params = {"endpoint_id": endpoint_id, "tunnel_id": tunnel_id}

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
        "/ipsec/endpoints/{endpoint_id}/tunnels/{tunnel_id}",
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


def put_update_ipsec_config(
    api_client, ipsec_local_ipaddress=None, **kwargs
):  # noqa: E501
    """put_update_ipsec_config  # noqa: E501

    update Ipsec Configuration on device. Note, This is device wide and must be set before
    any remote endpoint definitions are created. If it needs to be changed, all remote endpoint
    information and tunnel information must be deleted first.   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_update_ipsec_config(ipsec_local_ipaddress, async_req=True)

    :param ipsec_local_ipaddress str: This is effectively a \"cloud NAT\" address, since you don't
           know what your LAN address will be between invocations in a cloud, this address can be
           used by remote endpoints  as your \"behind a NAT\" address, sometimes referred to Peer
           or IKE ID, if needed (e.g. Watchguard or Juniper). It can ALSO be thought of even
           more simply as an IPsec \"loopback\" interface that you can use to terminate traffic.
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

    request_params = ["ipsec_local_ipaddress"]

    collection_formats = {}

    path_params = {}

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
        "/ipsec",
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


def wait_for_tunnel_connected(
    api_client,
    endpoint_id=None,
    tunnel_id=None,
    retry_timeout=2,
    timeout=60,
    sleep_time=1.0,
    **kwargs
):
    """Wait for tunnel to have status connected. If ONLY endpoint id provided, assumes only 1 tunnel exists.

    Arguments:
        api_client {VNS3Client} -- [description]

    Keyword Arguments:
        endpoint_id {int} - endpoint to check tunnel status for
        tunnel_id {int} - Tunnel for status
        retry_timeout {int}
        timeout {int}
        sleep_time {float}

    Returns:
        [dict] - tunnel status dict
    """
    import time

    if not (tunnel_id or endpoint_id):
        raise RuntimeError("tunnel_id or endpoint_id must be provided")

    if not tunnel_id:
        endpoint = get_ipsec_endpoint(api_client, endpoint_id).response
        endpoint_tunnels = endpoint["tunnels"]
        total_tunnels = len(endpoint_tunnels)
        if total_tunnels != 1:
            raise RuntimeError(
                "Can't determine tunnel for endpoint. Expected 1 tunnel, found %s"
                % str(total_tunnels)
            )
        tunnel_id = next(iter(endpoint_tunnels.values()))["id"]

    tunnel_id = str(tunnel_id)
    start_time = time.time()
    while time.time() - start_time < timeout:
        ipsec_status = get_ipsec_status(api_client, _request_timeout=retry_timeout)
        if tunnel_id not in ipsec_status.response:
            raise CohesiveSDKException("Tunnel ID %s does not exist." % tunnel_id)

        tunnel = ipsec_status.response[tunnel_id]
        if tunnel.get("connected") is True:
            Logger.debug(
                "Tunnel connected", host=api_client.host_uri, tunnel_id=tunnel_id
            )
            return tunnel

        Logger.debug(
            "Tunnel not up yet. Waiting.", host=api_client.host_uri, tunnel_id=tunnel_id
        )
        time.sleep(sleep_time)
    raise CohesiveSDKException("Polling timeout [timeout=%sseconds]" % timeout)


class IPsecApiRouter(VersionRouter):

    function_library = {
        "delete_ipsec_endpoint": {"4.8.4-5.0.8": delete_ipsec_endpoint},
        "delete_ipsec_endpoint_tunnel": {"4.8.4-5.0.8": delete_ipsec_endpoint_tunnel},
        "get_ipsec_details": {"4.8.4-5.0.8": get_ipsec_details},
        "get_ipsec_endpoint": {"4.8.4-5.0.8": get_ipsec_endpoint},
        "get_ipsec_status": {"4.8.4-5.0.8": get_ipsec_status},
        "get_ipsec_link_history": {"4.8.4-5.0.8": get_ipsec_link_history},
        "get_connected_subnets": {"4.8.4-5.0.8": get_connected_subnets},
        "post_create_ipsec_endpoint": {"4.8.4-5.0.8": post_create_ipsec_endpoint},
        "post_create_ipsec_endpoint_tunnel": {
            "4.8.4-5.0.8": post_create_ipsec_endpoint_tunnel
        },
        "post_restart_ipsec_action": {"4.8.4-5.0.8": post_restart_ipsec_action},
        "put_update_ipsec_endpoint": {"4.8.4-5.0.8": put_update_ipsec_endpoint},
        "put_update_ipsec_endpoint_tunnel": {
            "4.8.4-5.0.8": put_update_ipsec_endpoint_tunnel
        },
        "put_update_ipsec_config": {"4.8.4-5.0.8": put_update_ipsec_config},
        "wait_for_tunnel_connected": {"4.8.4-5.0.8": wait_for_tunnel_connected},
    }
