# coding: utf-8

"""
    VNS3:ms API

    Cohesive networks VNS3 provides complete control of your network's addresses, routes, rules and edge. Networking does  # noqa: E501

    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from cohesivenet.api_builder import VersionRouter


def get_backups(api_client, **kwargs):  # noqa: E501
    """Return a list of available database backup files  # noqa: E501

    Return a list of available database backup files  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_backups(async_req=True)

    :param VNS3Client api_client: (required)
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
    request_params = []

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {}

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/backups",
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


def delete_backup(api_client, backup_name=None, **kwargs):  # noqa: E501
    """Delete a backup file  # noqa: E501

    Delete a backup file  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_backup(async_req=True)

    :param VNS3Client api_client: (required)
    :param backup_name str: Name of backup (required)
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
    request_params = ["backup_name"]

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
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/backups",
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


def get_download_backup(api_client, backup_name=None, **kwargs):  # noqa: E501
    """Download a named backup file  # noqa: E501

    Download latest named backup file   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_download_backup(client, async_req=True)

    :param async_req bool: execute request asynchronously
    :param backup_name str: Optional name of backup file to download
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

    request_params = ["backup_name"]  # noqa: E501

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
        ["text/plain", "application/octet-stream"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/backups/download",
        "GET",
        path_params,
        query_params,
        header_params,
        body={},
        post_params=form_params,
        files=local_var_files,
        response_type="file",
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def post_upload_backup(api_client, body=None, **kwargs):  # noqa: E501
    """Upload a backup file  # noqa: E501

    Upload a backup file. Restoring VNS3:ms state  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_upload_backup(client, body, async_req=True)

    :param body str: License file (required)
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

    body_params = body

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # HTTP header `Content-Type`
    header_params["Content-Type"] = api_client.select_header_content_type(  # noqa: E501
        ["text/plain"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/backups/upload",
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


def post_create_backup(api_client, **kwargs):  # noqa: E501
    """Schedule a backup creation job  # noqa: E501

    Schedule a backup creation job  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_backup(async_req=True)

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

    request_params = []

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []

    local_var_files = {}

    body_params = {}

    # parse protected keyword param from kwargs if exists.
    for param in [
        p for p in request_params if local_var_params["kwargs"].get(p) is not None
    ]:
        body_params[param] = local_var_params["kwargs"][param]

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/backups/create_backup",
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


def get_backup_job(api_client, job_id, **kwargs):  # noqa: E501
    """Retrieve backup job status (DEPRECATED)  # noqa: E501

    Retrieve backup job status (DEPRECATED)   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_backup_job(async_req=True)

    :param uuid str: Job ID (required)
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

    request_params = []  # noqa: E501

    collection_formats = {}

    path_params = {"uuid": job_id}

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
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/backups/create_backup/{uuid}",
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


def post_restore_backup(api_client, backup_name=None, **kwargs):  # noqa: E501
    """Restore a backup file, resetting the state of VNS3:ms  # noqa: E501

    Restore a backup file, resetting the state of VNS3:ms   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_restore_backup(async_req=True)

    :param VNS3Client api_client: (required)
    :param backup_name str: Name of backup (required)
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
    request_params = ["backup_name"]

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
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/backups/restore_backup",
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


def get_snapshots_backup(api_client, **kwargs):  # noqa: E501
    """Return details of snapshots backup  # noqa: E501

    Return details of snapshots backup  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_snapshots_backup(async_req=True)

    :param VNS3Client api_client: (required)
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
    request_params = []

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {}

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup",
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


def delete_snapshots_backup(api_client, **kwargs):  # noqa: E501
    """Delete a backup file  # noqa: E501

    Delete a backup file  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.delete_snapshots_backup(async_req=True)

    :param VNS3Client api_client: (required)
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
    request_params = []

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

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup",
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


def get_download_snapshots_backup(api_client, **kwargs):  # noqa: E501
    """Download a snapshots backup file  # noqa: E501

    Download latest snapshots backup file   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_download_snapshots_backup(client, async_req=True)

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

    request_params = []  # noqa: E501

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["text/plain", "application/octet-stream"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup/download",
        "GET",
        path_params,
        query_params,
        header_params,
        body={},
        post_params=form_params,
        files=local_var_files,
        response_type="file",
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def post_upload_snapshots_backup(api_client, url=None, **kwargs):  # noqa: E501
    """post_upload_snapshots_backup  # noqa: E501

    Schedule a "pull" to retrieve a snapshots backup file from a specified URI  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_upload_snapshots_backup(client, url, async_req=True)

    :param url str: URL to download snapshot backup from (required)
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

    request_params = ["url"]

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
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup/upload_backup",
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


def get_snapshots_upload_status(api_client, job_id, **kwargs):  # noqa: E501
    """Retrieve snapshots backup retrieval job status (DEPRECATED)  # noqa: E501

    Retrieve snapshots backup retrieval job status (DEPRECATED)   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_snapshots_upload_status(async_req=True)

    :param uuid str: Job ID (required)
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

    request_params = []  # noqa: E501

    collection_formats = {}

    path_params = {"uuid": job_id}

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
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup/upload_backup/{uuid}",
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


def post_create_snapshots_backup(api_client, **kwargs):  # noqa: E501
    """Schedule a snapshot backup creation  # noqa: E501

    Schedule a snapshot backup creation  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_create_snapshots_backup(async_req=True)

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

    request_params = []

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []

    local_var_files = {}

    body_params = {}

    # parse protected keyword param from kwargs if exists.
    for param in [
        p for p in request_params if local_var_params["kwargs"].get(p) is not None
    ]:
        body_params[param] = local_var_params["kwargs"][param]

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup/create_backup",
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


def get_snapshots_backup_status(api_client, job_id, **kwargs):  # noqa: E501
    """Retrieve snapshot backup job status (DEPRECATED)  # noqa: E501

    Retrieve snapshot backup job status (DEPRECATED)   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_snapshots_backup_status(async_req=True)

    :param uuid str: Job ID (required)
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

    request_params = []  # noqa: E501

    collection_formats = {}

    path_params = {"uuid": job_id}

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
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup/create_backup/{uuid}",
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


def post_restore_snapshots_backup(api_client, backup_name=None, **kwargs):  # noqa: E501
    """Restore a snapshots backup file  # noqa: E501

    Restore a snapshots backup file   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_restore_snapshots_backup(async_req=True)

    :param VNS3Client api_client: (required)
    :param backup_name str: Name of backup (required)
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
    request_params = ["backup_name"]

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
    auth_settings = ["ApiTokenAuth"]  # noqa: E501

    return api_client.call_api(
        "/snapshots_backup/restore_backup",
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


class BackupsApiRouter(VersionRouter):
    """Configure backups for VNS3:ms and your controller snapshots"""

    function_library = {
        "get_backups": {"2.1.1-2.3.5": get_backups},
        "delete_backup": {"2.1.1-2.3.5": delete_backup},
        "get_download_backup": {"2.1.1-2.3.5": get_download_backup},
        "post_upload_backup": {"2.1.1-2.3.5": post_upload_backup},
        "post_create_backup": {"2.1.1-2.3.5": post_create_backup},
        "get_backup_job": {"2.1.1-2.3.5": get_backup_job},
        "post_restore_backup": {"2.1.1-2.3.5": post_restore_backup},
        "get_snapshots_backup": {"2.1.1-2.3.5": get_snapshots_backup},
        "delete_snapshots_backup": {"2.1.1-2.3.5": delete_snapshots_backup},
        "get_download_snapshots_backup": {"2.1.1-2.3.5": get_download_snapshots_backup},
        "post_upload_snapshots_backup": {"2.1.1-2.3.5": post_upload_snapshots_backup},
        "get_snapshots_upload_status": {"2.1.1-2.3.5": get_snapshots_upload_status},
        "post_create_snapshots_backup": {"2.1.1-2.3.5": post_create_snapshots_backup},
        "get_snapshots_backup_status": {"2.1.1-2.3.5": get_snapshots_backup_status},
        "post_restore_snapshots_backup": {"2.1.1-2.3.5": post_restore_snapshots_backup},
    }