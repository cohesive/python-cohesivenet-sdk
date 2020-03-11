# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 provides complete control of your network's addresses, routes, rules and edge. Networking does  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cohesivenet.api_builder import VersionRouter, validate_call


# @validate_call()
def create_access_url(api_client, expires=3600, description=None, **kwargs):  # noqa: E501
    """Create access URL  # noqa: E501

    Create access URL  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.create_access_url(async_req=True)

    :param VNS3Client api_client: (required)
    :param expires int: Number of seconds before expiration
    :param description str: Optional description of access URL
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
    request_params = [
        "expires",
        "description"
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
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/url', 'POST',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


def create_api_token(api_client, expires=3600, token_name=None, refreshes=None, **kwargs):  # noqa: E501
    """Create API token  # noqa: E501

    Create api token  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.create_api_token_with_http_info(async_req=True)

    :param VNS3Client api_client: (required)
    :param expires int: Number of seconds before expiration
    :param token_name str: Optional name of token
    :param refreshes bool: Token lifetime refreshes when used
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
        "expires",
        "token_name",
        "refreshes"
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
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/token', 'POST',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


@validate_call(path_params=["access_url_id"])
def delete_access_url(api_client, access_url_id, **kwargs):  # noqa: E501
    """Delete access URL  # noqa: E501

    Delete access URL by ID  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_access_url_with_http_info(access_url_id, async_req=True)

    :param VNS3Client api_client: (required)
    :param int access_url_id: Access URL ID (required)
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

    path_params = {
        "access_url_id": access_url_id
    }

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/url/{access_url_id}', 'DELETE',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


def delete_access_url_by_search(api_client, access_url_id=None, access_url=None, **kwargs):  # noqa: E501
    """Find and delete access URL  # noqa: E501

    Delete access URL by ID or URL  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_access_url_by_search_with_http_info(async_req=True)

    :param VNS3Client api_client: (required)
    :param access_url_id int: ID of access URL
    :param access_url str: URL
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
        "access_url_id",
        "access_url"
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
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/url', 'DELETE',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


@validate_call(path_params=["token_id"])
def delete_api_token(api_client, token_id, **kwargs):  # noqa: E501
    """Delete API token  # noqa: E501

    Delete API token by ID  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_api_token_with_http_info(token_id, async_req=True)

    :param VNS3Client api_client: (required)
    :param int token_id: Token ID (required)
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

    path_params = {
        "token_id": token_id
    }

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/token/{token_id}', 'DELETE',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


def get_access_urls(api_client, **kwargs):  # noqa: E501
    """Get access URLs  # noqa: E501

    Retrieve list of users' access urls, including expired ones  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_access_ur_ls_with_http_info(async_req=True)

    :param VNS3Client api_client: (required)
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
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/urls', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


@validate_call(path_params=["access_url_id"])
def get_access_url(api_client, access_url_id, **kwargs):  # noqa: E501
    """Get access URL  # noqa: E501

    Retrieve details for specific access url (including expired ones)  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_access_url_with_http_info(access_url_id, async_req=True)

    :param VNS3Client api_client: (required)
    :param int access_url_id: Access URL ID (required)
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

    path_params = {
        "access_url_id": access_url_id
    }

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/url/{access_url_id}', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


@validate_call(path_params=["token_id"])
def get_api_token(api_client, token_id, **kwargs):  # noqa: E501
    """Get API access token  # noqa: E501

    Retrieve details for specific access token (including expired ones)  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_api_token_with_http_info(token_id, async_req=True)

    :param VNS3Client api_client: (required)
    :param int token_id: Token ID (required)
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

    path_params = {
        "token_id": token_id
    }

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/token/{token_id}', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


def get_api_tokens(api_client, **kwargs):  # noqa: E501
    """Get API access tokens  # noqa: E501

    Retrieve list of api tokens  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_api_tokens_with_http_info(async_req=True)

    :param VNS3Client api_client: (required)
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
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/tokens', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


@validate_call(path_params=["access_url_id"])
def put_expire_access_url(api_client, access_url_id, expired=True, **kwargs):  # noqa: E501
    """Expire access URL  # noqa: E501

    Expire access URL  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_expire_access_url_with_http_info(access_url_id, async_req=True)

    :param VNS3Client api_client: (required)
    :param access_url_id int: Access URL ID (required)
    :param expired bool: Indicates whether to expire
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

    request_params = ['expired']

    collection_formats = {}

    path_params = {
        "access_url_id": access_url_id
    }

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {}
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        body_params[param] = local_var_params[param]

    # HTTP header `Accept`
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/url/{access_url_id}', 'PUT',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


@validate_call(path_params=["token_id"])
def put_expire_api_token(api_client, token_id, expired=True, **kwargs):  # noqa: E501
    """Expire API token  # noqa: E501

    Expire API token  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_expire_api_token_with_http_info(token_id, async_req=True)

    :param VNS3Client api_client: (required)
    :param int token_id: Token ID (required)
    :param expired bool: Indicates whether to expire
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

    request_params = ['expired']
 
    collection_formats = {}

    path_params = {
        "token_id": token_id
    }

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {}
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        body_params[param] = local_var_params[param]

    # HTTP header `Accept`
    header_params['Accept'] = api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = api_client.select_header_content_type(  # noqa: E501
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['basicAuth']  # noqa: E501

    return api_client.call_api(
        '/access/token/{token_id}', 'PUT',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='object',  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get('async_req'),
        _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
        _preload_content=local_var_params.get('_preload_content', True),
        _request_timeout=local_var_params.get('_request_timeout'),
        collection_formats=collection_formats)


class AccessApiRouter(VersionRouter):
    """Manage access to VNS3 with API tokens and admin access URLs"""

    function_library = {
        'create_access_url': {
            '4.8.4': create_access_url
        },
        'create_api_token': {
            '4.8.4': create_api_token
        },
        'delete_access_url': {
            '4.8.4': delete_access_url
        },
        'delete_access_url_by_search': {
            '4.8.4': delete_access_url_by_search
        },
        'delete_api_token': {
            '4.8.4': delete_api_token
        },
        'get_access_urls': {
            '4.8.4': get_access_urls
        },
        'get_access_url': {
            '4.8.4': get_access_url
        },
        'get_api_token': {
            '4.8.4': get_api_token
        },
        'get_api_tokens': {
            '4.8.4': get_api_tokens
        },
        'put_expire_access_url': {
            '4.8.4': put_expire_access_url
        },
        'put_expire_api_token': {
            '4.8.4': put_expire_api_token
        }
    }
