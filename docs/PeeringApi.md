# vns3api.PeeringApi

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
> InlineResponse20059 delete_peer(peer_id)



Breaks a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to  fully break the peer relationship. 

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
api_instance = vns3api.PeeringApi(vns3api.ApiClient(configuration))
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

[**InlineResponse20059**](InlineResponse20059.md)

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
> InlineResponse20056 get_peering_status()



Provides the status of whether a Controller is peered to other Controllers

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
api_instance = vns3api.PeeringApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_peering_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->get_peering_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

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
> InlineResponse20059 post_peer(inline_object41)



Creates a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process. 

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
api_instance = vns3api.PeeringApi(vns3api.ApiClient(configuration))
inline_object41 = vns3api.InlineObject41() # InlineObject41 | 

try:
    api_response = api_instance.post_peer(inline_object41)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->post_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object41** | [**InlineObject41**](InlineObject41.md)|  | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

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
> InlineResponse20059 put_peer(inline_object40)



Edits a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process. 

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
api_instance = vns3api.PeeringApi(vns3api.ApiClient(configuration))
inline_object40 = vns3api.InlineObject40() # InlineObject40 | 

try:
    api_response = api_instance.put_peer(inline_object40)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object40** | [**InlineObject40**](InlineObject40.md)|  | 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

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
> InlineResponse20057 put_reconfigure_peers(inline_object38)



Reconfigure peered controllers

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
api_instance = vns3api.PeeringApi(vns3api.ApiClient(configuration))
inline_object38 = vns3api.InlineObject38() # InlineObject38 | 

try:
    api_response = api_instance.put_reconfigure_peers(inline_object38)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_reconfigure_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object38** | [**InlineObject38**](InlineObject38.md)|  | 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

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
> InlineResponse20058 put_self_peering_id(inline_object39)



Sets the Controller ID of a controller so that it can be peered within a topology

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
api_instance = vns3api.PeeringApi(vns3api.ApiClient(configuration))
inline_object39 = vns3api.InlineObject39() # InlineObject39 | 

try:
    api_response = api_instance.put_self_peering_id(inline_object39)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_self_peering_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object39** | [**InlineObject39**](InlineObject39.md)|  | 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

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

