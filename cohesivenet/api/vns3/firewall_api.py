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


def get_firewall_fw_sets(api_client, name=None, verbose=None, **kwargs):  # noqa: E501
    """get_firewall_fw_sets  # noqa: E501

    Get a list of current firewall rule sets. These are IPsets that allow for faster matching of rules against IPs.
    See http://ipset.netfilter.org for more details.   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_firewall_fw_sets(async_req=True)

    :param str name: name of resource
    :param bool verbose: True for verbose output
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

    request_params = ["name", "verbose"]  # noqa: E501

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
        "/firewall/fwsets",
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


def post_create_firewall_fw_set(
    api_client, rules=None, name=None, flush=None, **kwargs
):  # noqa: E501
    """post_create_firewall_fw_set  # noqa: E501

    Create a new firewall FW set rules (Binary index list of IPs for fast lookup)  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_firewall_fw_set(name="NETS_cloud_dev", async_req=True)

    :param async_req bool: execute request asynchronously
    :param rules str: Chained fwsets seperated by \\n e.g. NETS_cloud_dev 10.96.20.0/24\\nNETS_cloud_dev 10.97.20.0/24
    :param name str: name of the fw_set
    :param flush bool: whether or not to reload all fwsets (default=True)

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

    request_params = ["rules", "name", "flush"]

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
        "/firewall/fwsets",
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


def delete_firewall_fw_set(api_client, name=None, rules=None, **kwargs):  # noqa: E501
    """delete_firewall_fw_set  # noqa: E501

    Delete Firewall FWSet by name or rules  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_firewall_fw_set(name="FWSetName", async_req=True)

    :param async_req bool: execute request asynchronously
    :param name str: name of the FWset
    :param rules str: Rules in the FWset
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

    request_params = ["name", "rules"]

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
        "/firewall/fwsets",
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


def put_reinitialize_fw_sets(api_client, reinitialize=True, **kwargs):  # noqa: E501
    """put_reinitialize_fw_sets  # noqa: E501

    Reinitialize all Firewall FWSet  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_reinitialize_fw_sets(reinitialize=True, async_req=True)

    :param async_req bool: execute request asynchronously
    :param reinitialize bool: whether or not to reload FW sets
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

    request_params = ["reinitialize"]

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
        "/firewall/fwsets",
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


def delete_firewall_rule_by_position(api_client, position, **kwargs):  # noqa: E501
    """delete_firewall_rule_by_position  # noqa: E501

    Delete Firewall Rule  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_firewall_rule_by_position(position, async_req=True)

    :param async_req bool: execute request asynchronously
    :param int position: index position for firewall rule, 0 is first (required)
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

    path_params = {"position": position}

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
        "/firewall/rules/{position}",
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


def delete_firewall_rule_by_rule(api_client, rule=None, **kwargs):  # noqa: E501
    """delete_firewall_rule_by_rule  # noqa: E501

    Delete firewall rule  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_firewall_rule_by_rule(rule="My Firewall RULE", async_req=True)

    :param async_req bool: execute request asynchronously
    :param rule str: (required)
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

    request_params = ["rule"]

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
        "/firewall/rules",
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


def get_firewall_rules(api_client, **kwargs):  # noqa: E501
    """get_firewall_rules  # noqa: E501

    Get a list of current firewall rules  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_firewall_rules(async_req=True)

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
        "/firewall/rules",
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


def post_create_firewall_rule(
    api_client, rule=None, position=None, **kwargs
):  # noqa: E501
    """post_create_firewall_rule  # noqa: E501

    Adds a firewall rule to the VNS3 Controller's firewall  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_firewall_rule(rule="My Firewall Rule", position=0, async_req=True)

    :param rule str: Firewall Rule (required)
    :param position int: order of rule in firewall, defaults to appending
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

    request_params = ["rule", "position"]

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
        "/firewall/rules",
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


def post_create_firewall_subgroup(
    api_client, rules=None, name=None, position=None, flush=None, **kwargs
):  # noqa: E501
    """post_create_firewall_subgroup  # noqa: E501

    Create a new firewall subgroup rules (rule chain)  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_firewall_subgroup(rules="", async_req=True)

    :param async_req bool: execute request asynchronously
    :param rules str: Chained firewall rules seperated by \\n
    :param name str: name of the subgroup. Must be valid chain that begins with one of the following: PRE_C_, PST_C_, FWD_C_, INP_C_, OUT_C_.
    :param position int: Position which the chain will be inserted in the list of Firewall rules.  Default is 1-, which is first in the ruleset
    :param flush bool: whether or not to reload all rules (default=True)

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

    request_params = ["rules", "name", "position", "flush"]

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
        "/firewall/rules/subgroup",
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


def delete_firewall_subgroup(api_client, rules=None, name=None, **kwargs):  # noqa: E501
    """delete_firewall_subgroup  # noqa: E501

    Delete Firewall subgroup by name or rules  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_firewall_subgroup(firewall_fw_set, async_req=True)

    :param async_req bool: execute request asynchronously
    :param name str: name of the Subgroup
    :param rules str: Rules in the Subgroup
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

    request_params = ["name", "rules"]

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
        "/firewall/rules/subgroup",
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


def get_firewall_rule_subgroups(
    api_client, name=None, verbose=None, **kwargs
):  # noqa: E501
    """get_firewall_rule_subgroups  # noqa: E501

    Get a list of current firewall rules at subgroup (chained rules)  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_firewall_rule_subgroups(async_req=True)

    :param async_req bool: execute request asynchronously
    :param str name: name of resource
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

    request_params = ["name", "verbose"]  # noqa: E501

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
        "/firewall/rules/subgroup",
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


def put_reinitialize_subgroups(api_client, reinitialize=True, **kwargs):  # noqa: E501
    """put_reinitialize_subgroups  # noqa: E501

    Reinitialize Firewall subgroups  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_reinitialize_subgroups(reinit_request, async_req=True)

    :param async_req bool: execute request asynchronously
    :param reinitialize bool: whether or not to reload subgroups
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

    request_params = ["reinitialize"]

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
        "/firewall/rules/subgroup",
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


class FirewallApiRouter(VersionRouter):
    """Manage VNS3 Firewall"""

    function_library = {
        "delete_firewall_fw_set": {"4.8.4-4.11.1": delete_firewall_fw_set},
        "delete_firewall_rule_by_position": {
            "4.8.4-4.11.1": delete_firewall_rule_by_position
        },
        "delete_firewall_rule_by_rule": {"4.8.4-4.11.1": delete_firewall_rule_by_rule},
        "delete_firewall_subgroup": {"4.8.4-4.11.1": delete_firewall_subgroup},
        "get_firewall_fw_sets": {"4.8.4-4.11.1": get_firewall_fw_sets},
        "post_create_firewall_fw_set": {"4.8.4-4.11.1": post_create_firewall_fw_set},
        "get_firewall_rule_subgroups": {"4.8.4-4.11.1": get_firewall_rule_subgroups},
        "get_firewall_rules": {"4.8.4-4.11.1": get_firewall_rules},
        "post_create_firewall_rule": {"4.8.4-4.11.1": post_create_firewall_rule},
        "post_create_firewall_subgroup": {
            "4.8.4-4.11.1": post_create_firewall_subgroup
        },
        "put_reinitialize_fw_sets": {"4.8.4-4.11.1": put_reinitialize_fw_sets},
        "put_reinitialize_firewall_subgroups": {
            "4.8.4-4.11.1": put_reinitialize_subgroups
        },
    }
