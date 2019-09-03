# RuntimeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_clients** | [**dict(str, OverlayClient)**](OverlayClient.md) | clients keyed by ip address | [optional] 
**connected_subnets** | **list[list[str]]** | Array of arrays with each element of length 2 representing [network, subnet mask] | [optional] 
**ipsec** | [**dict(str, IpsecTunnel)**](IpsecTunnel.md) | IPSEC tunnels keyed by tunnel ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


