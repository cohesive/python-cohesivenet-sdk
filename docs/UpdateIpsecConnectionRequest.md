# UpdateIpsecConnectionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the connection. | [optional] 
**ipaddress** | **str** | IP of the remote gateway | [optional] 
**secret** | **str** | Pre-shared key | [optional] 
**pfs** | **bool** | Perfect Forward Secrecy if true, disables if false. | [optional] 
**ike_version** | **int** | Version for IKE algorithm | [optional] 
**nat_t_enabled** | **bool** | True if you want encapsulated IPsec protocol to this gateway | [optional] 
**extra_config** | **str** | Additional optionals for connection such as &#39;phase1&#x3D;aes256_gcm-sha2_256-dh14 phase2&#x3D;aes256_gcm&#39; | [optional] 
**private_ipaddress** | **str** | Internal NAT address of the remote gateway | [optional] 
**gre** | **bool** | True if GRE is being used for the specific endpoint | [optional] 
**gre_interface_address** | **str** | Interface address for GRE | [optional] 
**vpn_type** | **str** | policy, gre, vti | [optional] 
**route_based_int_address** | **str** |  | [optional] 
**route_based_local** | **str** |  | [optional] 
**route_based_remote** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


