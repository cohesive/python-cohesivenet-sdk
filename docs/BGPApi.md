# vns3api.BGPApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ipsec_endpoint_bgp_peer**](BGPApi.md#delete_ipsec_endpoint_bgp_peer) | **DELETE** /ipsec/endpoints/{endpoint_id}/ebgp_peers/{bgp_peer_id} | 
[**post_create_ipsec_endpoint_bgp_peer**](BGPApi.md#post_create_ipsec_endpoint_bgp_peer) | **POST** /ipsec/endpoints/{endpoint_id}/ebgp_peers | 
[**put_edit_ipsec_endpoint_bgp_peer**](BGPApi.md#put_edit_ipsec_endpoint_bgp_peer) | **PUT** /ipsec/endpoints/{endpoint_id}/ebgp_peers/{bgp_peer_id} | 


# **delete_ipsec_endpoint_bgp_peer**
> InlineResponse20045 delete_ipsec_endpoint_bgp_peer(endpoint_id, bgp_peer_id)



Delete BGP Peer connection

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vns3api
from vns3api.rest import ApiException
from pprint import pprint
configuration = vns3api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = vns3api.BGPApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | numerical ID for IPsec endpoint
bgp_peer_id = 56 # int | numerical ID for BGP peer

try:
    api_response = api_instance.delete_ipsec_endpoint_bgp_peer(endpoint_id, bgp_peer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BGPApi->delete_ipsec_endpoint_bgp_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| numerical ID for IPsec endpoint | 
 **bgp_peer_id** | **int**| numerical ID for BGP peer | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_ipsec_endpoint_bgp_peer**
> InlineResponse20045 post_create_ipsec_endpoint_bgp_peer(endpoint_id, inline_object32)



Create BGP peer connection

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vns3api
from vns3api.rest import ApiException
from pprint import pprint
configuration = vns3api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = vns3api.BGPApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID for IPsec endpoint
inline_object32 = vns3api.InlineObject32() # InlineObject32 | 

try:
    api_response = api_instance.post_create_ipsec_endpoint_bgp_peer(endpoint_id, inline_object32)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BGPApi->post_create_ipsec_endpoint_bgp_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID for IPsec endpoint | 
 **inline_object32** | [**InlineObject32**](InlineObject32.md)|  | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_edit_ipsec_endpoint_bgp_peer**
> InlineResponse20045 put_edit_ipsec_endpoint_bgp_peer(endpoint_id, bgp_peer_id, inline_object33)



Edit BGP peer connection parameters

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import vns3api
from vns3api.rest import ApiException
from pprint import pprint
configuration = vns3api.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = vns3api.BGPApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID for IPsec endpoint
bgp_peer_id = 56 # int | ID for BGP peer
inline_object33 = vns3api.InlineObject33() # InlineObject33 | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint_bgp_peer(endpoint_id, bgp_peer_id, inline_object33)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BGPApi->put_edit_ipsec_endpoint_bgp_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID for IPsec endpoint | 
 **bgp_peer_id** | **int**| ID for BGP peer | 
 **inline_object33** | [**InlineObject33**](InlineObject33.md)|  | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

