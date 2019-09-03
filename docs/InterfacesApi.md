# cohesivenet.InterfacesApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_gre_endpoint**](InterfacesApi.md#delete_gre_endpoint) | **DELETE** /interfaces/edge_gre/{id} | 
[**delete_system_interface**](InterfacesApi.md#delete_system_interface) | **DELETE** /interfaces/system/{id} | 
[**get_edge_gre_endpoints**](InterfacesApi.md#get_edge_gre_endpoints) | **GET** /interfaces/edge_gre | 
[**get_gre_endpoint_details**](InterfacesApi.md#get_gre_endpoint_details) | **GET** /interfaces/edge_gre/{id} | 
[**get_interfaces**](InterfacesApi.md#get_interfaces) | **GET** /interfaces | 
[**get_system_interface_details**](InterfacesApi.md#get_system_interface_details) | **GET** /interfaces/system/{id} | 
[**get_system_interfaces**](InterfacesApi.md#get_system_interfaces) | **GET** /interfaces/system | 
[**post_action_interfaces**](InterfacesApi.md#post_action_interfaces) | **POST** /interfaces/action | 
[**post_create_gre_endpoint**](InterfacesApi.md#post_create_gre_endpoint) | **POST** /interfaces/edge_gre | 
[**post_create_system_interface**](InterfacesApi.md#post_create_system_interface) | **POST** /interfaces/system | 
[**put_update_gre_endpoint**](InterfacesApi.md#put_update_gre_endpoint) | **PUT** /interfaces/edge_gre/{id} | 
[**put_update_system_interface**](InterfacesApi.md#put_update_system_interface) | **PUT** /interfaces/system/{id} | 


# **delete_gre_endpoint**
> object delete_gre_endpoint()



Delete GRE Interface

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_gre_endpoint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->delete_gre_endpoint: %s\n" % e)
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
**401** |  |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_interface**
> object delete_system_interface()



Delete System Interface

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_system_interface()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->delete_system_interface: %s\n" % e)
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
**401** |  |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_gre_endpoints**
> GREEndpointListResponse get_edge_gre_endpoints()



Describe system edge GRE endpoints

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_edge_gre_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_edge_gre_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GREEndpointListResponse**](GREEndpointListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gre_endpoint_details**
> GREEndpointDetail get_gre_endpoint_details()



Get GRE interface details by id or name

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_gre_endpoint_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_gre_endpoint_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GREEndpointDetail**](GREEndpointDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**401** |  |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interfaces**
> SystemInterfaceListResponse get_interfaces()



(BETA) Describe all physical and virtual interfaces, both system and edge GRE interfaces

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_interfaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_interfaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInterfaceListResponse**](SystemInterfaceListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_interface_details**
> object get_system_interface_details(id)



Get interface details by name

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))
id = 'id_example' # str | Resource ID or unique Name

try:
    api_response = api_instance.get_system_interface_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_system_interface_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Resource ID or unique Name | 

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
**401** |  |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_interfaces**
> object get_system_interfaces()



Describe system interfaces

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_system_interfaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_system_interfaces: %s\n" % e)
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
**200** | Created |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action_interfaces**
> list[str] post_action_interfaces(interface_action_request)



Take action on interfaces. Only one action can be taken per request.

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))
interface_action_request = cohesivenet.InterfaceActionRequest() # InterfaceActionRequest | 

try:
    api_response = api_instance.post_action_interfaces(interface_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->post_action_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_action_request** | [**InterfaceActionRequest**](InterfaceActionRequest.md)|  | 

### Return type

**list[str]**

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

# **post_create_gre_endpoint**
> object post_create_gre_endpoint(body)



Create new edge GRE interface

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))
body = None # object | 

try:
    api_response = api_instance.post_create_gre_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->post_create_gre_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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

# **post_create_system_interface**
> SystemInterfaceDetail post_create_system_interface(body)



Create new system interface

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))
body = None # object | 

try:
    api_response = api_instance.post_create_system_interface(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->post_create_system_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**SystemInterfaceDetail**](SystemInterfaceDetail.md)

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

# **put_update_gre_endpoint**
> object put_update_gre_endpoint(body)



Update GRE interface

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))
body = None # object | 

try:
    api_response = api_instance.put_update_gre_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->put_update_gre_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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
**200** | Updated |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_system_interface**
> object put_update_system_interface(body)



Update system interface

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
api_instance = cohesivenet.InterfacesApi(cohesivenet.VNS3Client(configuration))
body = None # object | 

try:
    api_response = api_instance.put_update_system_interface(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->put_update_system_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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
**200** | Updated |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

