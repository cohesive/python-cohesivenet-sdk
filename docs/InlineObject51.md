# InlineObject51

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipaddress** | **str** | IP address of the desired BGP peer. | 
**asn** | **int** | Autonomous system number assigned to device at ipaddress | 
**access_list** | **str** | List of \&quot;in permit CIDR\&quot; and/or \&quot;out permit CIDR\&quot; statements in a string delimited by \&quot;\\n\&quot; | [optional] 
**bgp_password** | **str** | String to be agreed upon by both peers as a simple password. | [optional] 
**add_network_distance** | **bool** | Enable network distance for BGP peer | [optional] 
**add_network_distance_direction** | **str** | Add distance direction for BGP peer | [optional] 
**add_network_distance_hops** | **int** | Distance metric weight indicating distance in hops for BGP peer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


