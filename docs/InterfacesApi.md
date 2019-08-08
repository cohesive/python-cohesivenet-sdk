# openapi_client.InterfacesApi

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
> InlineResponse20066 delete_gre_endpoint(id)



Delete GRE Interface

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | name or id of GRE interface

try:
    api_response = api_instance.delete_gre_endpoint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->delete_gre_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name or id of GRE interface | 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_interface**
> InlineResponse20063 delete_system_interface(id)



Delete System Interface

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | name or id of system interface

try:
    api_response = api_instance.delete_system_interface(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->delete_system_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name or id of system interface | 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_gre_endpoints**
> InlineResponse20064 get_edge_gre_endpoints()



Describe system edge GRE endpoints

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_edge_gre_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_edge_gre_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gre_endpoint_details**
> InlineResponse20065 get_gre_endpoint_details(id)



Get GRE interface details by id or name

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | name or id of interface

try:
    api_response = api_instance.get_gre_endpoint_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_gre_endpoint_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name or id of interface | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_interfaces**
> InlineResponse20057 get_interfaces()



(BETA) Describe all physical and virtual interfaces, both system and edge GRE interfaces

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_interfaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_interfaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_interface_details**
> InlineResponse20061 get_system_interface_details(id)



Get interface details by name

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | name or id of interface

try:
    api_response = api_instance.get_system_interface_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_system_interface_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name or id of interface | 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_interfaces**
> InlineResponse20059 get_system_interfaces()



Describe system interfaces

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_system_interfaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->get_system_interfaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | Created |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action_interfaces**
> InlineResponse20058 post_action_interfaces(inline_object43)



Take action on interfaces. Only one action can be taken per request.

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
inline_object43 = openapi_client.InlineObject43() # InlineObject43 | 

try:
    api_response = api_instance.post_action_interfaces(inline_object43)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->post_action_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object43** | [**InlineObject43**](InlineObject43.md)|  | 

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
**200** | Accepted |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_gre_endpoint**
> InlineResponse20065 post_create_gre_endpoint(gre_endpoint_params)



Create new edge GRE interface

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
gre_endpoint_params = openapi_client.GREEndpointParams() # GREEndpointParams | 

try:
    api_response = api_instance.post_create_gre_endpoint(gre_endpoint_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->post_create_gre_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gre_endpoint_params** | [**GREEndpointParams**](GREEndpointParams.md)|  | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

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

# **post_create_system_interface**
> InlineResponse20060 post_create_system_interface(system_interface)



Create new system interface

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
system_interface = openapi_client.SystemInterface() # SystemInterface | 

try:
    api_response = api_instance.post_create_system_interface(system_interface)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->post_create_system_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_interface** | [**SystemInterface**](SystemInterface.md)|  | 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

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

# **put_update_gre_endpoint**
> InlineResponse20065 put_update_gre_endpoint(id, gre_endpoint_params)



Update GRE interface

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | name or id of interface
gre_endpoint_params = openapi_client.GREEndpointParams() # GREEndpointParams | 

try:
    api_response = api_instance.put_update_gre_endpoint(id, gre_endpoint_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->put_update_gre_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name or id of interface | 
 **gre_endpoint_params** | [**GREEndpointParams**](GREEndpointParams.md)|  | 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

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

# **put_update_system_interface**
> InlineResponse20062 put_update_system_interface(id, system_interface)



Update system interface

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
api_instance = openapi_client.InterfacesApi(openapi_client.ApiClient(configuration))
id = 'id_example' # str | name or id of interface
system_interface = openapi_client.SystemInterface() # SystemInterface | 

try:
    api_response = api_instance.put_update_system_interface(id, system_interface)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterfacesApi->put_update_system_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| name or id of interface | 
 **system_interface** | [**SystemInterface**](SystemInterface.md)|  | 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

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

