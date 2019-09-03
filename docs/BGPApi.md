# cohesivenet.BGPApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ipsec_endpoint_bgp_peer**](BGPApi.md#delete_ipsec_endpoint_bgp_peer) | **DELETE** /ipsec/endpoints/{endpoint_id}/ebgp_peers/{bgp_peer_id} | 
[**post_create_ipsec_endpoint_bgp_peer**](BGPApi.md#post_create_ipsec_endpoint_bgp_peer) | **POST** /ipsec/endpoints/{endpoint_id}/ebgp_peers | 
[**put_edit_ipsec_endpoint_bgp_peer**](BGPApi.md#put_edit_ipsec_endpoint_bgp_peer) | **PUT** /ipsec/endpoints/{endpoint_id}/ebgp_peers/{bgp_peer_id} | 


# **delete_ipsec_endpoint_bgp_peer**
> object delete_ipsec_endpoint_bgp_peer()



Delete BGP Peer connection

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import cohesivenet
from cohesivenet.rest import ApiException
from pprint import pprint
configuration = cohesivenet.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = cohesivenet.BGPApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_ipsec_endpoint_bgp_peer()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BGPApi->delete_ipsec_endpoint_bgp_peer: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**400** | Bad request indicating BGP peer does not exist |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_ipsec_endpoint_bgp_peer**
> object post_create_ipsec_endpoint_bgp_peer(create_bgp_peer_request)



Create BGP peer connection

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import cohesivenet
from cohesivenet.rest import ApiException
from pprint import pprint
configuration = cohesivenet.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = cohesivenet.BGPApi(cohesivenet.VNS3Client(configuration))
create_bgp_peer_request = cohesivenet.CreateBGPPeerRequest() # CreateBGPPeerRequest | 

try:
    api_response = api_instance.post_create_ipsec_endpoint_bgp_peer(create_bgp_peer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BGPApi->post_create_ipsec_endpoint_bgp_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bgp_peer_request** | [**CreateBGPPeerRequest**](CreateBGPPeerRequest.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_edit_ipsec_endpoint_bgp_peer**
> object put_edit_ipsec_endpoint_bgp_peer(bgp_peer_id, update_bgp_peer_connection_request)



Edit BGP peer connection parameters

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import cohesivenet
from cohesivenet.rest import ApiException
from pprint import pprint
configuration = cohesivenet.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = cohesivenet.BGPApi(cohesivenet.VNS3Client(configuration))
bgp_peer_id = 56 # int | ID for BGP peer
update_bgp_peer_connection_request = cohesivenet.UpdateBGPPeerConnectionRequest() # UpdateBGPPeerConnectionRequest | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint_bgp_peer(bgp_peer_id, update_bgp_peer_connection_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BGPApi->put_edit_ipsec_endpoint_bgp_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_peer_id** | **int**| ID for BGP peer | 
 **update_bgp_peer_connection_request** | [**UpdateBGPPeerConnectionRequest**](UpdateBGPPeerConnectionRequest.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

