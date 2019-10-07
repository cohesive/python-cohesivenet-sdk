# UpdateIpsecTunnelRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounce** | **bool** | Resets the IPsec connection for this specific tunnel | [optional] [default to False]
**description** | **str** |  | [optional] 
**remote_subnet** | **str** | Remote subnet for tunnel in CIDR notation | [optional] 
**local_subnet** | **str** | Local subnet for tunnel in CIDR notation | [optional] 
**ping_ipaddress** | **str** | Exo Ping feature - remote IP destination of ping | [optional] 
**ping_interval** | **int** | Exo Ping feature - periodicy of the ping in seconds | [optional] 
**ping_interface** | **str** | Exo Ping feature - what network interface IP of the VNS3 controller to use as the source of ping | [optional] 
**enabled** | **bool** | Disables tunnel if set to false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

