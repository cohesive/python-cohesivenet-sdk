# openapi_client.PeeringApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_peer**](PeeringApi.md#delete_peer) | **DELETE** /peering/peers/{peer_id} | 
[**get_peering_status**](PeeringApi.md#get_peering_status) | **GET** /peering | 
[**post_peer**](PeeringApi.md#post_peer) | **POST** /peering/peers | 
[**put_peer**](PeeringApi.md#put_peer) | **PUT** /peering/peers | 
[**put_reconfigure_peers**](PeeringApi.md#put_reconfigure_peers) | **PUT** /peering | 
[**put_self_peering_id**](PeeringApi.md#put_self_peering_id) | **PUT** /peering/self | 


# **delete_peer**
> InlineResponse20039 delete_peer(peer_id)



Breaks a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to  fully break the peer relationship. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = openapi_client.PeeringApi(openapi_client.ApiClient(configuration))
peer_id = 56 # int | Peer ID for controller peer

try:
    api_response = api_instance.delete_peer(peer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->delete_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_id** | **int**| Peer ID for controller peer | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete Accepted |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peering_status**
> InlineResponse20039 get_peering_status()



Provides the status of whether a Controller is peered to other Controllers

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = openapi_client.PeeringApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_peering_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->get_peering_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_peer**
> InlineResponse20039 post_peer(inline_object25)



Creates a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = openapi_client.PeeringApi(openapi_client.ApiClient(configuration))
inline_object25 = openapi_client.InlineObject25() # InlineObject25 | 

try:
    api_response = api_instance.post_peer(inline_object25)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->post_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object25** | [**InlineObject25**](InlineObject25.md)|  | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

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

# **put_peer**
> InlineResponse20039 put_peer(inline_object24)



Edits a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = openapi_client.PeeringApi(openapi_client.ApiClient(configuration))
inline_object24 = openapi_client.InlineObject24() # InlineObject24 | 

try:
    api_response = api_instance.put_peer(inline_object24)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object24** | [**InlineObject24**](InlineObject24.md)|  | 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reconfigure_peers**
> InlineResponse20040 put_reconfigure_peers(inline_object22)



Reconfigure peered controllers

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = openapi_client.PeeringApi(openapi_client.ApiClient(configuration))
inline_object22 = openapi_client.InlineObject22() # InlineObject22 | 

try:
    api_response = api_instance.put_reconfigure_peers(inline_object22)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_reconfigure_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object22** | [**InlineObject22**](InlineObject22.md)|  | 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_self_peering_id**
> InlineResponse20041 put_self_peering_id(inline_object23)



Sets the Controller ID of a controller so that it can be peered within a topology

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://vns3-host:8000/api
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
api_instance = openapi_client.PeeringApi(openapi_client.ApiClient(configuration))
inline_object23 = openapi_client.InlineObject23() # InlineObject23 | 

try:
    api_response = api_instance.put_self_peering_id(inline_object23)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_self_peering_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object23** | [**InlineObject23**](InlineObject23.md)|  | 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

