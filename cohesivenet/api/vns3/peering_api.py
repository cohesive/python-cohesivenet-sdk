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

# python 2 and python 3 compatibility library
import six

from cohesivenet.exceptions import ApiTypeError, ApiValueError


class PeeringApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            from cohesivenet.vns3_client import VNS3Client

            api_client = VNS3Client()
        self.api_client = api_client

    def delete_peer(self, peer_id, **kwargs):  # noqa: E501
        """delete_peer  # noqa: E501

        Breaks a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to  fully break the peer relationship.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_peer(peer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int peer_id: Peer ID for controller peer (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.delete_peer_with_http_info(peer_id, **kwargs)  # noqa: E501

    def delete_peer_with_http_info(self, peer_id, **kwargs):  # noqa: E501
        """delete_peer  # noqa: E501

        Breaks a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to  fully break the peer relationship.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_peer_with_http_info(peer_id, async_req=True)
        >>> result = thread.get()

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
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["peer_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_peer" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'peer_id' is set
        if "peer_id" not in local_var_params or local_var_params["peer_id"] is None:
            raise ApiValueError(
                "Missing the required parameter `peer_id` when calling `delete_peer`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "peer_id" in local_var_params:
            path_params["peer_id"] = local_var_params["peer_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
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

    def get_peering_status(self, **kwargs):  # noqa: E501
        """get_peering_status  # noqa: E501

        Provides the status of whether a Controller is peered to other Controllers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_peering_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PeersDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_peering_status_with_http_info(**kwargs)  # noqa: E501

    def get_peering_status_with_http_info(self, **kwargs):  # noqa: E501
        """get_peering_status  # noqa: E501

        Provides the status of whether a Controller is peered to other Controllers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_peering_status_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :return: tuple(PeersDetailResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_peering_status" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/peering",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PeersDetailResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_peer(self, create_peer_request, **kwargs):  # noqa: E501
        """post_peer  # noqa: E501

        Creates a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_peer(create_peer_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePeerRequest create_peer_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PeersDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.post_peer_with_http_info(
            create_peer_request, **kwargs
        )  # noqa: E501

    def post_peer_with_http_info(self, create_peer_request, **kwargs):  # noqa: E501
        """post_peer  # noqa: E501

        Creates a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_peer_with_http_info(create_peer_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePeerRequest create_peer_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PeersDetailResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["create_peer_request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_peer" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'create_peer_request' is set
        if (
            "create_peer_request" not in local_var_params
            or local_var_params["create_peer_request"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `create_peer_request` when calling `post_peer`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "create_peer_request" in local_var_params:
            body_params = local_var_params["create_peer_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/peering/peers",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PeersDetailResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_peer(self, peer_id, update_peer_request, **kwargs):  # noqa: E501
        """put_peer  # noqa: E501

        Edits a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_peer(update_peer_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int peer_id: ID for Peer (required)
        :param UpdatePeerRequest update_peer_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PeersDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.put_peer_with_http_info(
            peer_id, update_peer_request, **kwargs
        )  # noqa: E501

    def put_peer_with_http_info(
        self, peer_id, update_peer_request, **kwargs
    ):  # noqa: E501
        """put_peer  # noqa: E501

        Edits a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_peer_with_http_info(update_peer_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int peer_id: ID for Peer (required)
        :param UpdatePeerRequest update_peer_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PeersDetailResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["peer_id", "update_peer_request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        # verify the required parameter 'peer_id' is set
        if self.api_client.client_side_validation and (
            "peer_id" not in local_var_params
            or local_var_params["peer_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `peer_id` when calling `put_peer`"
            )  # noqa: E501

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_peer" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'update_peer_request' is set
        if (
            "update_peer_request" not in local_var_params
            or local_var_params["update_peer_request"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `update_peer_request` when calling `put_peer`"
            )  # noqa: E501

        if (
            self.api_client.client_side_validation
            and "peer_id" in local_var_params
            and local_var_params["peer_id"] < 0
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `peer_id` when calling `put_peer`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "peer_id" in local_var_params:
            path_params["peer_id"] = local_var_params["peer_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "update_peer_request" in local_var_params:
            body_params = local_var_params["update_peer_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/peering/peers/{peer_id}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PeersDetailResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_reconfigure_peers(self, configure_peer_request, **kwargs):  # noqa: E501
        """put_reconfigure_peers  # noqa: E501

        Reconfigure peered controllers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_reconfigure_peers(configure_peer_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ConfigurePeerRequest configure_peer_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.put_reconfigure_peers_with_http_info(
            configure_peer_request, **kwargs
        )  # noqa: E501

    def put_reconfigure_peers_with_http_info(
        self, configure_peer_request, **kwargs
    ):  # noqa: E501
        """put_reconfigure_peers  # noqa: E501

        Reconfigure peered controllers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_reconfigure_peers_with_http_info(configure_peer_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ConfigurePeerRequest configure_peer_request: (required)
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

        all_params = ["configure_peer_request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_reconfigure_peers" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'configure_peer_request' is set
        if (
            "configure_peer_request" not in local_var_params
            or local_var_params["configure_peer_request"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `configure_peer_request` when calling `put_reconfigure_peers`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "configure_peer_request" in local_var_params:
            body_params = local_var_params["configure_peer_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/peering",
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

    def put_self_peering_id(self, peer_self_request, **kwargs):  # noqa: E501
        """put_self_peering_id  # noqa: E501

        Sets the Controller ID of a controller so that it can be peered within a topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_self_peering_id(peer_self_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PeerSelfRequest peer_self_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PeersDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.put_self_peering_id_with_http_info(
            peer_self_request, **kwargs
        )  # noqa: E501

    def put_self_peering_id_with_http_info(
        self, peer_self_request, **kwargs
    ):  # noqa: E501
        """put_self_peering_id  # noqa: E501

        Sets the Controller ID of a controller so that it can be peered within a topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_self_peering_id_with_http_info(peer_self_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param PeerSelfRequest peer_self_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PeersDetailResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["peer_self_request"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_self_peering_id" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'peer_self_request' is set
        if (
            "peer_self_request" not in local_var_params
            or local_var_params["peer_self_request"] is None
        ):
            raise ApiValueError(
                "Missing the required parameter `peer_self_request` when calling `put_self_peering_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "peer_self_request" in local_var_params:
            body_params = local_var_params["peer_self_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["basicAuth"]  # noqa: E501

        return self.api_client.call_api(
            "/peering/self",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PeersDetailResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
