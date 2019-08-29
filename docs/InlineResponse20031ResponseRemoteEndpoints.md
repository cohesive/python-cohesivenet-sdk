# InlineResponse20031ResponseRemoteEndpoints

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**ipaddress** | **str** |  | [optional] 
**nat_t_enabled** | **bool** |  | [optional] 
**ike_version** | **str** |  | [optional] 
**pfs** | **bool** | Perfect forward secrecy enabled | [optional] 
**private_ipaddress** | **str** |  | [optional] 
**extra_config** | **list[str]** |  | [optional] 
**tunnels** | [**dict(str, InlineResponse2008ResponseIpsec)**](InlineResponse2008ResponseIpsec.md) |  | [optional] 
**bgp_peers** | [**dict(str, InlineResponse20031ResponseBgpPeers)**](InlineResponse20031ResponseBgpPeers.md) |  | [optional] 
**type** | **str** | Indicating Ipsec or GRE over ipsec | [optional] 
**vpn_type** | **str** |  | [optional] 
**gre_interface_address** | **str** |  | [optional] 
**route_based_int_address** | **str** |  | [optional] 
**route_based_local** | **str** |  | [optional] 
**route_based_remote** | **str** |  | [optional] 
**psk** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


