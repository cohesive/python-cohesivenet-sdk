# vns3api.RoutingApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_route**](RoutingApi.md#delete_route) | **DELETE** /routes/{id} | 
[**get_routes**](RoutingApi.md#get_routes) | **GET** /routes | 
[**post_create_route**](RoutingApi.md#post_create_route) | **POST** /routes | 


# **delete_route**
> InlineResponse20067 delete_route(id)



Delete Route

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
api_instance = vns3api.RoutingApi(vns3api.ApiClient(configuration))
id = 56 # int | numerical ID for route

try:
    api_response = api_instance.delete_route(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->delete_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| numerical ID for route | 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes**
> InlineResponse20055 get_routes()



Describes routes that this manager has access to via its network interfaces (virtual or otherwise).  If advertized, other VNS3 Controllers will receive the route instantly. Network clients will  receive it when they get their next route push, which is normally on a re-connect or in neartime  if they use the VNS3 Routing agent on their cloud servers. Remote endpoints  (other data centers) would not receive the route unless specified as part of  their IPsec Configuration AND the Configuration of such a tunnel on the VNS3 controller. 

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
api_instance = vns3api.RoutingApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_routes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->get_routes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

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

# **post_create_route**
> InlineResponse20056 post_create_route(inline_object42)



Pushes routes that this manager has access to via its network interfaces (virtual or otherwise) 

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
api_instance = vns3api.RoutingApi(vns3api.ApiClient(configuration))
inline_object42 = vns3api.InlineObject42() # InlineObject42 | 

try:
    api_response = api_instance.post_create_route(inline_object42)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->post_create_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object42** | [**InlineObject42**](InlineObject42.md)|  | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

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

