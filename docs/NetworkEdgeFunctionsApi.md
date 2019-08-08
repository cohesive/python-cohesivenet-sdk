# openapi_client.NetworkEdgeFunctionsApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_container**](NetworkEdgeFunctionsApi.md#delete_container) | **DELETE** /container_system/containers/{uuid} | 
[**delete_container_image**](NetworkEdgeFunctionsApi.md#delete_container_image) | **DELETE** /container_system/images/{uuid} | 
[**get_container_logs**](NetworkEdgeFunctionsApi.md#get_container_logs) | **GET** /container_system/containers/{uuid}/logs | 
[**get_container_system_i_ps**](NetworkEdgeFunctionsApi.md#get_container_system_i_ps) | **GET** /container_system/ip_addresses | 
[**get_container_system_images**](NetworkEdgeFunctionsApi.md#get_container_system_images) | **GET** /container_system/images | 
[**get_container_system_running_containers**](NetworkEdgeFunctionsApi.md#get_container_system_running_containers) | **GET** /container_system/containers | 
[**get_container_system_status**](NetworkEdgeFunctionsApi.md#get_container_system_status) | **GET** /container_system | 
[**post_action_container_system**](NetworkEdgeFunctionsApi.md#post_action_container_system) | **POST** /container_system | 
[**post_commit_container**](NetworkEdgeFunctionsApi.md#post_commit_container) | **POST** /container_system/containers/{uuid}/commit | 
[**post_create_container_image**](NetworkEdgeFunctionsApi.md#post_create_container_image) | **POST** /container_system/images | 
[**post_start_container**](NetworkEdgeFunctionsApi.md#post_start_container) | **POST** /container_system/containers | 
[**put_configure_container_system**](NetworkEdgeFunctionsApi.md#put_configure_container_system) | **PUT** /container_system | 
[**put_edit_container_image**](NetworkEdgeFunctionsApi.md#put_edit_container_image) | **PUT** /container_system/images/{uuid} | 
[**put_stop_container**](NetworkEdgeFunctionsApi.md#put_stop_container) | **PUT** /container_system/containers/{uuid} | 


# **delete_container**
> InlineResponse20088 delete_container(uuid)



Delete a container

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID for allocated container

try:
    api_response = api_instance.delete_container(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->delete_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID for allocated container | 

### Return type

[**InlineResponse20088**](InlineResponse20088.md)

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
**403** | Controller must be licensed first |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_container_image**
> InlineResponse20084 delete_container_image(uuid, force=force)



Delete container image

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID for container image
force = False # bool | force delete image by removing running containers (optional) (default to False)

try:
    api_response = api_instance.delete_container_image(uuid, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->delete_container_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID for container image | 
 **force** | **bool**| force delete image by removing running containers | [optional] [default to False]

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_logs**
> InlineResponse20090 get_container_logs(uuid, inline_object53)



Fetch containers log messages

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID for allocated container
inline_object53 = openapi_client.InlineObject53() # InlineObject53 | 

try:
    api_response = api_instance.get_container_logs(uuid, inline_object53)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->get_container_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID for allocated container | 
 **inline_object53** | [**InlineObject53**](InlineObject53.md)|  | 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_system_i_ps**
> InlineResponse20080 get_container_system_i_ps()



Retrieve IP address list for current container network configuration

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_container_system_i_ps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->get_container_system_i_ps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_system_images**
> InlineResponse20081 get_container_system_images(uuid=uuid)



Get list of existing container system images

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | ID of image (optional)

try:
    api_response = api_instance.get_container_system_images(uuid=uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->get_container_system_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ID of image | [optional] 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

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
**403** | Operation not allowed |  -  |
**500** | Invalid server state |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_system_running_containers**
> InlineResponse20085 get_container_system_running_containers(show_all=show_all, uuid=uuid)



Provides description information for one or all allocated containers

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
show_all = True # bool | Displays all allocated containers when true (optional) (default to True)
uuid = 'uuid_example' # str | Container id for filtering (optional)

try:
    api_response = api_instance.get_container_system_running_containers(show_all=show_all, uuid=uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->get_container_system_running_containers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **bool**| Displays all allocated containers when true | [optional] [default to True]
 **uuid** | **str**| Container id for filtering | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_system_status**
> InlineResponse20077 get_container_system_status()



Retrieve status of container system

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_container_system_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->get_container_system_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action_container_system**
> InlineResponse20079 post_action_container_system(inline_object50)



Take action on container system

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
inline_object50 = openapi_client.InlineObject50() # InlineObject50 | 

try:
    api_response = api_instance.post_action_container_system(inline_object50)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->post_action_container_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object50** | [**InlineObject50**](InlineObject50.md)|  | 

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_commit_container**
> InlineResponse20089 post_commit_container(uuid, inline_object52)



Creates a new container image from a running container

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID for allocated container
inline_object52 = openapi_client.InlineObject52() # InlineObject52 | 

try:
    api_response = api_instance.post_commit_container(uuid, inline_object52)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->post_commit_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID for allocated container | 
 **inline_object52** | [**InlineObject52**](InlineObject52.md)|  | 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_container_image**
> InlineResponse20082 post_create_container_image(unknown_base_type)



Create new container image

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
unknown_base_type = openapi_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.post_create_container_image(unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->post_create_container_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**InlineResponse20082**](InlineResponse20082.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**400** | Bad request |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_start_container**
> InlineResponse20086 post_start_container(unknown_base_type)



Create (allocate) a new container or start an existing one

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
unknown_base_type = openapi_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.post_start_container(unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->post_start_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_configure_container_system**
> InlineResponse20078 put_configure_container_system(inline_object49)



Configures the container network.

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
inline_object49 = openapi_client.InlineObject49() # InlineObject49 | 

try:
    api_response = api_instance.put_configure_container_system(inline_object49)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->put_configure_container_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object49** | [**InlineObject49**](InlineObject49.md)|  | 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_edit_container_image**
> InlineResponse20083 put_edit_container_image(uuid, inline_object51)



Edits container image

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID for container image
inline_object51 = openapi_client.InlineObject51() # InlineObject51 | 

try:
    api_response = api_instance.put_edit_container_image(uuid, inline_object51)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->put_edit_container_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID for container image | 
 **inline_object51** | [**InlineObject51**](InlineObject51.md)|  | 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**400** | Bad request |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_stop_container**
> InlineResponse20087 put_stop_container(uuid)



Stops a running container

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
api_instance = openapi_client.NetworkEdgeFunctionsApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | UUID for allocated container

try:
    api_response = api_instance.put_stop_container(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgeFunctionsApi->put_stop_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID for allocated container | 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

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
**403** | Controller must be licensed first |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

