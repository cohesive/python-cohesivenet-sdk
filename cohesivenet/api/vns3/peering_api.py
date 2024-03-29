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


def delete_peer(api_client, peer_id, **kwargs):  # noqa: E501
    """delete_peer  # noqa: E501

    Breaks a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to  fully break the peer relationship.   # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_peer(peer_id, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int peer_id: Peer ID for controller peer (required)
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

    local_var_params = dict(locals(), **kwargs)

    collection_formats = {}

    path_params = {"peer_id": peer_id}

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
        "/peering/peers/{peer_id}",
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


def get_peering_status(api_client, **kwargs):  # noqa: E501
    """get_peering_status  # noqa: E501

    Provides the status of whether a Controller is peered to other Controllers  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_peering_status(async_req=True)

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

    local_var_params = dict(locals(), **kwargs)

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
        "/peering",
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


def post_create_peer(
    api_client, id=None, name=None, overlay_mtu=None, **kwargs
):  # noqa: E501
    """post_peer  # noqa: E501

    Creates a peering relationship from a manager to another manager.  The peering call is unidirectional.
    Reciprocal calls must be made to peer two controllers  together and complete the peering process.   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_peer(create_peer_request, async_req=True)

    :param id int: Controller ID as an integer of the controller you are peering with,  NOT the id of the one you are calling from
    :param name str: Hostname or IP address of the one you are peering with.
    :param overlay_mtu str: Link MTU between 500 and 4800. Defaults to 1500
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

    local_var_params = dict(locals(), **kwargs)

    request_params = ["id", "name", "overlay_mtu"]

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {"force": kwargs.pop("force", True)}
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
        "/peering/peers",
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


def put_update_peer(
    api_client, peer_id, name=None, overlay_mtu=None, force=None, **kwargs
):  # noqa: E501
    """put_peer  # noqa: E501

    Edits a peering relationship from a manager to another manager. The peering call is unidirectional.
    Reciprocal calls must be made to peer two controllers  together and complete the peering process.   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_peer(update_peer_request, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int peer_id: ID for Peer (required)
    :param name str: Hostname or IP address of the one you are peering with.
    :param overlay_mtu str: Link MTU between 500 and 4800. Defaults to 1500
    :param force bool: Setting false will NOT finalize the peering operation.
        A peer \"reconfigure\" call would then be required. Default is true
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

    local_var_params = dict(locals(), **kwargs)

    request_params = ["name", "overlay_mtu", "force"]

    collection_formats = {}

    path_params = {"peer_id": peer_id}

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
        "/peering/peers/{peer_id}",
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


def put_self_peering_id(api_client, id=None, **kwargs):  # noqa: E501
    """put_self_peering_id  # noqa: E501

    Sets the Controller ID of a controller so that it can be peered within a topology  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_self_peering_id(peer_self_request, async_req=True)

    :param async_req bool: execute request asynchronously
    :param id int: ID to set this controller Peer ID to(required)
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

    local_var_params = dict(locals(), **kwargs)

    request_params = ["id"]

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {"force": kwargs.pop("force", True)}
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
        "/peering/self",
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


class PeeringApiRouter(VersionRouter):
    function_library = {
        "delete_peer": {"4.8.4-6.x.x": delete_peer},
        "get_peering_status": {"4.8.4-6.x.x": get_peering_status},
        "post_create_peer": {"4.8.4-6.x.x": post_create_peer},
        "put_update_peer": {"4.8.4-6.x.x": put_update_peer},
        "put_self_peering_id": {"4.8.4-6.x.x": put_self_peering_id},
    }
