# InlineObject13

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet** | **str** | Specifies the CIDR of the virtual network created for use with the VNS3 Manager | [optional] 
**managers** | **str** | Whitespace delimited address string in the subnet to use for the VNS3 Controllers&#39; virtual interfaces. | [optional] 
**asns** | **str** | Whitespace delimited string of ASNs (autonomous system numbers) corresponding to the order of the controllers | [optional] 
**clients** | **str** | Comma delimited, or hyphenated sequence of addresses for use as client addresses in the virtual network. | [optional] 
**my_manager_vip** | **str** | IPAddress that must be allocated from the subnet, and be the same for all controllers | [optional] 
**default** | **bool** | Specifices whether to use defualt topology addressing as specified by the license | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


