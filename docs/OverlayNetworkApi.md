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
> InlineResponse20038 delete_clientpack_tag(name, inline_object21)



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
inline_object21 = vns3api.InlineObject21() # InlineObject21 | 

try:
    api_response = api_instance.delete_clientpack_tag(name, inline_object21)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->delete_clientpack_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of clientpack, typically IP address snake cased | 
 **inline_object21** | [**InlineObject21**](InlineObject21.md)|  | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

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
> InlineResponse20032 get_clientpack(name)



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

[**InlineResponse20032**](InlineResponse20032.md)

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
> InlineResponse20029 get_clientpacks(sorted=sorted)



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

[**InlineResponse20029**](InlineResponse20029.md)

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
> InlineResponse20025 get_clients_status()



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

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Operation not allowed |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_subnets**
> InlineResponse20028 get_connected_subnets(extended_output=extended_output)



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

[**InlineResponse20028**](InlineResponse20028.md)

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
> file get_download_clientpack(inline_object16)



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
inline_object16 = vns3api.InlineObject16() # InlineObject16 | 

try:
    api_response = api_instance.get_download_clientpack(inline_object16)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_download_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object16** | [**InlineObject16**](InlineObject16.md)|  | 

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
> InlineResponse20033 post_calc_next_clientpack(inline_object17=inline_object17)



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
inline_object17 = vns3api.InlineObject17() # InlineObject17 |  (optional)

try:
    api_response = api_instance.post_calc_next_clientpack(inline_object17=inline_object17)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_calc_next_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object17** | [**InlineObject17**](InlineObject17.md)|  | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

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
> InlineResponse20037 post_clientpack_tag(name, inline_object20)



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
inline_object20 = vns3api.InlineObject20() # InlineObject20 | 

try:
    api_response = api_instance.post_clientpack_tag(name, inline_object20)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_clientpack_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of clientpack, typically IP address snake cased | 
 **inline_object20** | [**InlineObject20**](InlineObject20.md)|  | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

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
> InlineResponse20035 post_reset_all_clients()



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

[**InlineResponse20035**](InlineResponse20035.md)

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
> InlineResponse20034 post_reset_client(inline_object18)



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
inline_object18 = vns3api.InlineObject18() # InlineObject18 | 

try:
    api_response = api_instance.post_reset_client(inline_object18)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_reset_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object18** | [**InlineObject18**](InlineObject18.md)|  | 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

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
> InlineResponse20031 put_add_clientpacks(inline_object15)



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
inline_object15 = vns3api.InlineObject15() # InlineObject15 | 

try:
    api_response = api_instance.put_add_clientpacks(inline_object15)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_add_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object15** | [**InlineObject15**](InlineObject15.md)|  | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

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
> InlineResponse20036 put_disconnect_clientpack(name, inline_object19)



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
inline_object19 = vns3api.InlineObject19() # InlineObject19 | 

try:
    api_response = api_instance.put_disconnect_clientpack(name, inline_object19)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_disconnect_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of clientpack, typically IP address snake cased | 
 **inline_object19** | [**InlineObject19**](InlineObject19.md)|  | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

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
> InlineResponse20030 put_update_clientpacks(inline_object14)



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
inline_object14 = vns3api.InlineObject14() # InlineObject14 | 

try:
    api_response = api_instance.put_update_clientpacks(inline_object14)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_update_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object14** | [**InlineObject14**](InlineObject14.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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

