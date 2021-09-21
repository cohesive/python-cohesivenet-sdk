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


def get_interfaces(api_client, **kwargs):  # noqa: E501
    """get_interfaces  # noqa: E501

    (BETA) Describe all physical and virtual interfaces, both system and edge GRE interfaces  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_interfaces(async_req=True)

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
        "/interfaces",
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


def get_system_interface_details(api_client, interface_id, **kwargs):  # noqa: E501
    """get_system_interface_details  # noqa: E501

    Get interface details by name  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_system_interface_details(async_req=True)

    :param interface_id int: ID of interface
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

    path_params = {"interface_id": interface_id}

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
        "/interfaces/system/{interface_id}",
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


def get_system_interfaces(api_client, **kwargs):  # noqa: E501
    """get_system_interfaces  # noqa: E501

    Describe system interfaces  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_system_interfaces(async_req=True)

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
        "/interfaces/system",
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


def delete_system_interface(api_client, interface_id, **kwargs):  # noqa: E501
    """delete_system_interface  # noqa: E501

    Delete System Interface  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_system_interface(interface_id, async_req=True)

    :param str interface_id: ID for system interface (required)
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

    path_params = {"interface_id": interface_id}

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
        "/interfaces/system/{interface_id}",
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


def delete_gre_interface(api_client, interface_id, **kwargs):  # noqa: E501
    """delete_gre_interface  # noqa: E501

    Delete GRE Interface  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_gre_interface(async_req=True)

    :param str interface_id: ID for system interface (required)
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

    path_params = {"interface_id": interface_id}

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
        "/interfaces/edge_gre/{interface_id}",
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


def get_gre_interfaces(api_client, **kwargs):  # noqa: E501
    """get_gre_interfaces  # noqa: E501

    Describe system edge GRE interfaces  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_gre_interfaces(async_req=True)

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
        "/interfaces/edge_gre",
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


def get_gre_interface_details(api_client, interface_id, **kwargs):  # noqa: E501
    """get_gre_interface_details  # noqa: E501

    Get GRE interface details by id or name  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_gre_interface_details(interface_id, async_req=True)

    :param str interface_id: ID for Edge GRE interface (required)
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

    path_params = {"interface_id": interface_id}

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
        "/interfaces/edge_gre/{interface_id}",
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


def post_interfaces_action(
    api_client,
    discover_new_primary_adapters=None,
    discover_ips=None,
    manage_overlay_interfaces=None,
    **kwargs
):  # noqa: E501
    """post_interfaces_action  # noqa: E501

    Take action on interfaces. Only one action can be taken per request.  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_interfaces_action(interface_action_request, async_req=True)

     Run discovery for new primary adapters

    :param discover_new_primary_adapters bool: execute request asynchronously
    :param discover_ips bool: execute request asynchronously
    :param manage_overlay_interfaces bool: execute request asynchronously
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
        "discover_new_primary_adapters",
        "discover_ips",
        "manage_overlay_interfaces",
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
        "/interfaces/action",
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


def post_create_gre_interface(
    api_client,
    endpoint_name=None,
    description=None,
    ip_internal=None,
    mtu=None,
    enabled=None,
    mask_bits=None,
    system_default=None,
    local_connection_ip=None,
    remote_connection_ip=None,
    ttl=None,
    **kwargs
):  # noqa: E501
    """post_create_gre_interface  # noqa: E501

    Create new edge GRE interface  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_gre_interface(body, async_req=True)

    :param endpoint_name str: (required)
    :param description str:
    :param ip_internal str:
    :param mtu int:
    :param enabled bool:
    :param mask_bits str:
    :param system_default bool:
    :param local_connection_ip str:
    :param remote_connection_ip str:
    :param ttl int:
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
        "endpoint_name",
        "description",
        "ip_internal",
        "mtu",
        "enabled",
        "mask_bits",
        "system_default",
        "local_connection_ip",
        "remote_connection_ip",
        "ttl",
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
        "/interfaces/edge_gre",
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


def post_create_system_interface(
    api_client,
    name=None,
    description=None,
    ip_internal=None,
    ip_external=None,
    mtu=None,
    enabled=None,
    mask_bits=None,
    gateway=None,
    system_default=None,
    **kwargs
):  # noqa: E501
    """post_create_system_interface  # noqa: E501

    Create new system interface  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_system_interface(body, async_req=True)

    :param name str: (required)
    :param description str:
    :param ip_internal str:
    :param ip_external str:
    :param mtu int:
    :param enabled bool:
    :param mask_bits str:
    :param gateway str:
    :param system_default bool:
    :param async_req bool: execute request asynchronously
    :param object body: (required)
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
        "description",
        "ip_internal",
        "ip_external",
        "mtu",
        "enabled",
        "mask_bits",
        "gateway",
        "system_default",
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
        "/interfaces/system",
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


def put_update_gre_interface(
    api_client,
    interface_id,
    endpoint_name=None,
    description=None,
    ip_internal=None,
    mtu=None,
    enabled=None,
    mask_bits=None,
    system_default=None,
    local_connection_ip=None,
    remote_connection_ip=None,
    ttl=None,
    **kwargs
):  # noqa: E501
    """put_update_gre_interface  # noqa: E501

    Update GRE interface  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_update_gre_interface(10, endpoint_name="name", async_req=True)

    :param str interface_id: ID for edge GRE interface (required)
    :param endpoint_name str:
    :param description str:
    :param ip_internal str:
    :param mtu int:
    :param enabled bool:
    :param mask_bits str:
    :param system_default bool:
    :param local_connection_ip str:
    :param remote_connection_ip str:
    :param ttl int:
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
        "endpoint_name",
        "description",
        "ip_internal",
        "mtu",
        "enabled",
        "mask_bits",
        "system_default",
        "local_connection_ip",
        "remote_connection_ip",
        "ttl",
    ]

    collection_formats = {}

    path_params = {"interface_id": interface_id}

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
        "/interfaces/edge_gre/{interface_id}",
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


def put_update_system_interface(
    api_client,
    interface_id,
    name=None,
    description=None,
    ip_internal=None,
    ip_external=None,
    mtu=None,
    enabled=None,
    mask_bits=None,
    gateway=None,
    system_default=None,
    **kwargs
):  # noqa: E501
    """put_update_system_interface  # noqa: E501

    Update system interface  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_update_system_interface(body, async_req=True)

    :param str interface_id: ID for system interface (required)
    :param name str:
    :param description str:
    :param ip_internal str:
    :param ip_external str:
    :param mtu int:
    :param enabled bool:
    :param mask_bits str:
    :param gateway str:
    :param system_default bool:

    :param async_req bool: execute request asynchronously
    :param object body: (required)
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
        "description",
        "ip_internal",
        "ip_external",
        "mtu",
        "enabled",
        "mask_bits",
        "gateway",
        "system_default",
    ]

    collection_formats = {}

    path_params = {"interface_id": interface_id}

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
        "/interfaces/system/{interface_id}",
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


class InterfacesApiRouter(VersionRouter):
    """(Beta) Manage your VNS3 controllers interfaces"""

    function_library = {
        "get_interfaces": {"4.8.4-5.0.8": get_interfaces},
        "get_system_interface_details": {"4.8.4-5.0.8": get_system_interface_details},
        "get_system_interfaces": {"4.8.4-5.0.8": get_system_interfaces},
        "put_update_system_interface": {"4.8.4-5.0.8": put_update_system_interface},
        "post_create_system_interface": {"4.8.4-5.0.8": post_create_system_interface},
        "delete_gre_interface": {"4.8.4-5.0.8": delete_gre_interface},
        "get_gre_interfaces": {"4.8.4-5.0.8": get_gre_interfaces},
        "put_update_gre_interface": {"4.8.4-5.0.8": put_update_gre_interface},
        "get_gre_interface_details": {"4.8.4-5.0.8": get_gre_interface_details},
        "post_create_gre_interface": {"4.8.4-5.0.8": post_create_gre_interface},
        "delete_system_interface": {"4.8.4-5.0.8": delete_system_interface},
        "post_interfaces_action": {"4.8.4-5.0.8": post_interfaces_action},
    }
