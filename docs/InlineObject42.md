# InlineObject42

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | CIDR of a route that the VNS3 Controller has access  to that it wants to publish throughout the  Routing tables of the overlay network  | 
**description** | **str** |  | [optional] 
**interface** | **str** | Sets the interface where this route will be advertised. | [optional] 
**gateway** | **str** | If interface is set, a specific gateway address reachable from that interface | [optional] 
**tunnel** | **int** | numerical reference for the GRE endpoint id (must provide either tunnel OR interface) | [optional] 
**advertise** | **bool** | advertise route to overlay network | [optional] 
**metric** | **int** | weight for route | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


