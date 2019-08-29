# vns3api.HighAvailabilityApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ha_id**](HighAvailabilityApi.md#get_ha_id) | **GET** /ha/uuid | 
[**get_ha_status**](HighAvailabilityApi.md#get_ha_status) | **GET** /ha/status | 
[**get_ha_sync_file**](HighAvailabilityApi.md#get_ha_sync_file) | **GET** /ha/pull | 
[**get_ha_sync_status**](HighAvailabilityApi.md#get_ha_sync_status) | **GET** /ha/sync | 
[**post_init_ha**](HighAvailabilityApi.md#post_init_ha) | **POST** /ha/init | 
[**post_sync_ha**](HighAvailabilityApi.md#post_sync_ha) | **POST** /ha/sync | 
[**put_ha_activate**](HighAvailabilityApi.md#put_ha_activate) | **PUT** /ha/activate | 
[**put_ha_push_file**](HighAvailabilityApi.md#put_ha_push_file) | **PUT** /ha/push | 


# **get_ha_id**
> InlineResponse20088 get_ha_id()



Get the unique ID this controller in HA configuration

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_ha_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->get_ha_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ha_status**
> InlineResponse20092 get_ha_status(uuid)



Get HA status for given ID

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))
uuid = 'uuid_example' # str | ID for controller in HA configuration

try:
    api_response = api_instance.get_ha_status(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->get_ha_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ID for controller in HA configuration | 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

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

# **get_ha_sync_file**
> file get_ha_sync_file(uuid, sync_uuid)



Download sync file from HA Primary

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))
uuid = 'uuid_example' # str | ID for controller in HA configuration
sync_uuid = 'sync_uuid_example' # str | ID for HA sync

try:
    api_response = api_instance.get_ha_sync_file(uuid, sync_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->get_ha_sync_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ID for controller in HA configuration | 
 **sync_uuid** | **str**| ID for HA sync | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**404** | Bad request |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ha_sync_status**
> InlineResponse20090 get_ha_sync_status(uuid, sync_uuid)



Get HA sync status for given ID

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))
uuid = 'uuid_example' # str | ID for controller in HA configuration
sync_uuid = 'sync_uuid_example' # str | ID for HA sync

try:
    api_response = api_instance.get_ha_sync_status(uuid, sync_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->get_ha_sync_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ID for controller in HA configuration | 
 **sync_uuid** | **str**| ID for HA sync | 

### Return type

[**InlineResponse20090**](InlineResponse20090.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **post_init_ha**
> InlineResponse20089 post_init_ha(inline_object52)



Initialise HA

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))
inline_object52 = vns3api.InlineObject52() # InlineObject52 | 

try:
    api_response = api_instance.post_init_ha(inline_object52)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->post_init_ha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Accepted |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_ha**
> InlineResponse20091 post_sync_ha(inline_object53)



Initiate a sync creation on HA Primary

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))
inline_object53 = vns3api.InlineObject53() # InlineObject53 | 

try:
    api_response = api_instance.post_sync_ha(inline_object53)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->post_sync_ha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object53** | [**InlineObject53**](InlineObject53.md)|  | 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

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

# **put_ha_activate**
> InlineResponse20093 put_ha_activate(inline_object54)



Activate the HA switchover

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))
inline_object54 = vns3api.InlineObject54() # InlineObject54 | 

try:
    api_response = api_instance.put_ha_activate(inline_object54)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->put_ha_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object54** | [**InlineObject54**](InlineObject54.md)|  | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

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

# **put_ha_push_file**
> InlineResponse20038 put_ha_push_file(body)



Upload a sync file to HA Backup

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
api_instance = vns3api.HighAvailabilityApi(vns3api.ApiClient(configuration))
body = '/path/to/file' # file | Sync file

try:
    api_response = api_instance.put_ha_push_file(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->put_ha_push_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file**| Sync file | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

