# vns3api.OverlayNetworkApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_clientpack_tag**](OverlayNetworkApi.md#delete_clientpack_tag) | **DELETE** /clientpack/{name} | 
[**get_clientpack**](OverlayNetworkApi.md#get_clientpack) | **GET** /clientpacks/{name} | 
[**get_clientpacks**](OverlayNetworkApi.md#get_clientpacks) | **GET** /clientpacks | 
[**get_clients_status**](OverlayNetworkApi.md#get_clients_status) | **GET** /status/clients | 
[**get_connected_subnets**](OverlayNetworkApi.md#get_connected_subnets) | **GET** /status/connected_subnets | 
[**get_download_clientpack**](OverlayNetworkApi.md#get_download_clientpack) | **GET** /clientpack | 
[**post_calc_next_clientpack**](OverlayNetworkApi.md#post_calc_next_clientpack) | **POST** /clientpacks/next_available | 
[**post_clientpack_tag**](OverlayNetworkApi.md#post_clientpack_tag) | **POST** /clientpack/{name} | 
[**post_reset_all_clients**](OverlayNetworkApi.md#post_reset_all_clients) | **POST** /clients/reset_all | 
[**post_reset_client**](OverlayNetworkApi.md#post_reset_client) | **POST** /client/reset | 
[**put_add_clientpacks**](OverlayNetworkApi.md#put_add_clientpacks) | **PUT** /clientpacks/add_clientpacks | 
[**put_clientpack**](OverlayNetworkApi.md#put_clientpack) | **PUT** /clientpack | 
[**put_disconnect_clientpack**](OverlayNetworkApi.md#put_disconnect_clientpack) | **PUT** /clientpack/{name} | 
[**put_update_clientpacks**](OverlayNetworkApi.md#put_update_clientpacks) | **PUT** /clientpacks | 


# **delete_clientpack_tag**
> InlineResponse20055 delete_clientpack_tag(name, inline_object37)



For deleting individual clientpack tags

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
name = 'name_example' # str | name of clientpack, typically IP address snake cased
inline_object37 = vns3api.InlineObject37() # InlineObject37 | 

try:
    api_response = api_instance.delete_clientpack_tag(name, inline_object37)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->delete_clientpack_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of clientpack, typically IP address snake cased | 
 **inline_object37** | [**InlineObject37**](InlineObject37.md)|  | 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clientpack**
> InlineResponse20049 get_clientpack(name)



Returns detailed information about all of the clientpacks in the topology.  If manager's are properly peered, this information can come from any of the controllers. 

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
name = 'name_example' # str | Filter client packs by name

try:
    api_response = api_instance.get_clientpack(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter client packs by name | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

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

# **get_clientpacks**
> InlineResponse20046 get_clientpacks(sorted=sorted)



Returns detailed information about all of the clientpacks in the topology. If manager's are properly peered, this information can come from any of the controllers.

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
sorted = False # bool | Sort by IP address (optional) (default to False)

try:
    api_response = api_instance.get_clientpacks(sorted=sorted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sorted** | **bool**| Sort by IP address | [optional] [default to False]

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

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

# **get_clients_status**
> InlineResponse20044 get_clients_status()



Describe overlay clients

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_clients_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_clients_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

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

# **get_connected_subnets**
> InlineResponse20045 get_connected_subnets(extended_output=extended_output)



Provides information about any connected subnets.

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
extended_output = False # bool | Receive verbose information about the connected subnets. (optional) (default to False)

try:
    api_response = api_instance.get_connected_subnets(extended_output=extended_output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_connected_subnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_output** | **bool**| Receive verbose information about the connected subnets. | [optional] [default to False]

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
**200** | OK |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_clientpack**
> file get_download_clientpack(inline_object32)



Returns clientpack file. Clientpacks are files with the necessary information and credentials  for an overlay client to be connected to the VNS3 topology 

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
inline_object32 = vns3api.InlineObject32() # InlineObject32 | 

try:
    api_response = api_instance.get_download_clientpack(inline_object32)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_download_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object32** | [**InlineObject32**](InlineObject32.md)|  | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Clientpack file |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_calc_next_clientpack**
> InlineResponse20050 post_calc_next_clientpack(inline_object33=inline_object33)



Get next sequential client pack. Provides sufficient information to call GET /clientpack.  Note, Using this resource against multiple controllers in the same topology could cause distribution of the  same clientpack to multiple overlay devices which is not allowed. 

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
inline_object33 = vns3api.InlineObject33() # InlineObject33 |  (optional)

try:
    api_response = api_instance.post_calc_next_clientpack(inline_object33=inline_object33)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_calc_next_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object33** | [**InlineObject33**](InlineObject33.md)|  | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_clientpack_tag**
> InlineResponse20054 post_clientpack_tag(name, inline_object36)



For tagging individual clientpacks.

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
name = 'name_example' # str | name of clientpack, typically IP address snake cased
inline_object36 = vns3api.InlineObject36() # InlineObject36 | 

try:
    api_response = api_instance.post_clientpack_tag(name, inline_object36)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_clientpack_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of clientpack, typically IP address snake cased | 
 **inline_object36** | [**InlineObject36**](InlineObject36.md)|  | 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reset_all_clients**
> InlineResponse20052 post_reset_all_clients()



For resetting all of the connections of clients connected to the VNS3 Controller

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.post_reset_all_clients()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_reset_all_clients: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

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

# **post_reset_client**
> InlineResponse20051 post_reset_client(inline_object34)



For resetting the connection of a client to a VNS3 Controller

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
inline_object34 = vns3api.InlineObject34() # InlineObject34 | 

try:
    api_response = api_instance.post_reset_client(inline_object34)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_reset_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object34** | [**InlineObject34**](InlineObject34.md)|  | 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_add_clientpacks**
> InlineResponse20048 put_add_clientpacks(inline_object31)



Incrementally add new clientpacks for use

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
inline_object31 = vns3api.InlineObject31() # InlineObject31 | 

try:
    api_response = api_instance.put_add_clientpacks(inline_object31)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_add_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object31** | [**InlineObject31**](InlineObject31.md)|  | 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_clientpack**
> OneOfobjectobject put_clientpack(unknown_base_type)



Change properties of clientpacks; enabling or disabling, checking in or out, or regenerating

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
unknown_base_type = vns3api.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.put_clientpack(unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**OneOfobjectobject**](OneOfobjectobject.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_disconnect_clientpack**
> InlineResponse20053 put_disconnect_clientpack(name, inline_object35)



Force disconnect client for named clientpack

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
name = 'name_example' # str | name of clientpack, typically IP address snake cased
inline_object35 = vns3api.InlineObject35() # InlineObject35 | 

try:
    api_response = api_instance.put_disconnect_clientpack(name, inline_object35)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_disconnect_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of clientpack, typically IP address snake cased | 
 **inline_object35** | [**InlineObject35**](InlineObject35.md)|  | 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_clientpacks**
> InlineResponse20047 put_update_clientpacks(inline_object30)



For bulk set of the enabled (true/false) state for all clientpacks and the checked_out (true/false) state for all clientpacks.  This enables a variety of work flows by calling these functions after key generation,  but before general provisioning of addresses to devivces 

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
api_instance = vns3api.OverlayNetworkApi(vns3api.ApiClient(configuration))
inline_object30 = vns3api.InlineObject30() # InlineObject30 | 

try:
    api_response = api_instance.put_update_clientpacks(inline_object30)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_update_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object30** | [**InlineObject30**](InlineObject30.md)|  | 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

