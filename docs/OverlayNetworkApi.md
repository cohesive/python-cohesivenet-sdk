# cohesivenet.OverlayNetworkApi

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
> object delete_clientpack_tag(clientpack_tag_key_request)



For deleting individual clientpack tags

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
clientpack_tag_key_request = cohesivenet.ClientpackTagKeyRequest() # ClientpackTagKeyRequest | 

try:
    api_response = api_instance.delete_clientpack_tag(clientpack_tag_key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->delete_clientpack_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientpack_tag_key_request** | [**ClientpackTagKeyRequest**](ClientpackTagKeyRequest.md)|  | 

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
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clientpack**
> ClientpackDetailResponse get_clientpack(name)



Returns detailed information about all of the clientpacks in the topology.  If manager's are properly peered, this information can come from any of the controllers. 

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
name = 'name_example' # str | name of resource

try:
    api_response = api_instance.get_clientpack(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of resource | 

### Return type

[**ClientpackDetailResponse**](ClientpackDetailResponse.md)

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** | Error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clientpacks**
> ClientpackListResponse get_clientpacks(sorted=sorted)



Returns detailed information about all of the clientpacks in the topology. If manager's are properly peered, this information can come from any of the controllers.

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
sorted = False # bool | Sort resources (optional) (default to False)

try:
    api_response = api_instance.get_clientpacks(sorted=sorted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sorted** | **bool**| Sort resources | [optional] [default to False]

### Return type

[**ClientpackListResponse**](ClientpackListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients_status**
> OverlayClientsListResponse get_clients_status()



Describe overlay clients

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_clients_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_clients_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OverlayClientsListResponse**](OverlayClientsListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_subnets**
> ConnectedSubnetsDetailResponse get_connected_subnets(extended_output=extended_output)



Provides information about any connected subnets.

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
extended_output = False # bool | Receive verbose information about resources (optional) (default to False)

try:
    api_response = api_instance.get_connected_subnets(extended_output=extended_output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_connected_subnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_output** | **bool**| Receive verbose information about resources | [optional] [default to False]

### Return type

[**ConnectedSubnetsDetailResponse**](ConnectedSubnetsDetailResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_clientpack**
> file get_download_clientpack(download_clientpack_request)



Returns clientpack file. Clientpacks are files with the necessary information and credentials  for an overlay client to be connected to the VNS3 topology 

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
download_clientpack_request = cohesivenet.DownloadClientpackRequest() # DownloadClientpackRequest | 

try:
    api_response = api_instance.get_download_clientpack(download_clientpack_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->get_download_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **download_clientpack_request** | [**DownloadClientpackRequest**](DownloadClientpackRequest.md)|  | 

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_calc_next_clientpack**
> object post_calc_next_clientpack(calculate_next_clientpack_request=calculate_next_clientpack_request)



Get next sequential client pack. Provides sufficient information to call GET /clientpack.  Note, Using this resource against multiple controllers in the same topology could cause distribution of the  same clientpack to multiple overlay devices which is not allowed. 

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
calculate_next_clientpack_request = cohesivenet.CalculateNextClientpackRequest() # CalculateNextClientpackRequest |  (optional)

try:
    api_response = api_instance.post_calc_next_clientpack(calculate_next_clientpack_request=calculate_next_clientpack_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_calc_next_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculate_next_clientpack_request** | [**CalculateNextClientpackRequest**](CalculateNextClientpackRequest.md)|  | [optional] 

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
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_clientpack_tag**
> ClientpackTagsResponse post_clientpack_tag(create_clientpack_tag_request)



For tagging individual clientpacks.

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
create_clientpack_tag_request = cohesivenet.CreateClientpackTagRequest() # CreateClientpackTagRequest | 

try:
    api_response = api_instance.post_clientpack_tag(create_clientpack_tag_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_clientpack_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_clientpack_tag_request** | [**CreateClientpackTagRequest**](CreateClientpackTagRequest.md)|  | 

### Return type

[**ClientpackTagsResponse**](ClientpackTagsResponse.md)

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reset_all_clients**
> BulkClientResetStatusResponse post_reset_all_clients()



For resetting all of the connections of clients connected to the VNS3 Controller

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.post_reset_all_clients()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_reset_all_clients: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BulkClientResetStatusResponse**](BulkClientResetStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reset_client**
> ClientpackStatusResponse post_reset_client(reset_overlay_client_request)



For resetting the connection of a client to a VNS3 Controller

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
reset_overlay_client_request = cohesivenet.ResetOverlayClientRequest() # ResetOverlayClientRequest | 

try:
    api_response = api_instance.post_reset_client(reset_overlay_client_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->post_reset_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_overlay_client_request** | [**ResetOverlayClientRequest**](ResetOverlayClientRequest.md)|  | 

### Return type

[**ClientpackStatusResponse**](ClientpackStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_add_clientpacks**
> object put_add_clientpacks(add_clientpack_request)



Incrementally add new clientpacks for use

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
add_clientpack_request = cohesivenet.AddClientpackRequest() # AddClientpackRequest | 

try:
    api_response = api_instance.put_add_clientpacks(add_clientpack_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_add_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_clientpack_request** | [**AddClientpackRequest**](AddClientpackRequest.md)|  | 

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
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_clientpack**
> OneOfobjectobject put_clientpack(unknown_base_type)



Change properties of clientpacks; enabling or disabling, checking in or out, or regenerating

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
unknown_base_type = cohesivenet.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_disconnect_clientpack**
> object put_disconnect_clientpack(disconnet_client_request)



Force disconnect client for named clientpack

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
disconnet_client_request = cohesivenet.DisconnetClientRequest() # DisconnetClientRequest | 

try:
    api_response = api_instance.put_disconnect_clientpack(disconnet_client_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_disconnect_clientpack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disconnet_client_request** | [**DisconnetClientRequest**](DisconnetClientRequest.md)|  | 

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
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_clientpacks**
> UpdateClientpacksStatusResponse put_update_clientpacks(update_config_clientpack_request)



For bulk set of the enabled (true/false) state for all clientpacks and the checked_out (true/false) state for all clientpacks.  This enables a variety of work flows by calling these functions after key generation,  but before general provisioning of addresses to devivces 

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
api_instance = cohesivenet.OverlayNetworkApi(cohesivenet.VNS3Client(configuration))
update_config_clientpack_request = cohesivenet.UpdateConfigClientpackRequest() # UpdateConfigClientpackRequest | 

try:
    api_response = api_instance.put_update_clientpacks(update_config_clientpack_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OverlayNetworkApi->put_update_clientpacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_config_clientpack_request** | [**UpdateConfigClientpackRequest**](UpdateConfigClientpackRequest.md)|  | 

### Return type

[**UpdateClientpacksStatusResponse**](UpdateClientpacksStatusResponse.md)

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

