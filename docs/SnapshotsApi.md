# openapi_client.SnapshotsApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **DELETE** /snapshots/{name} | 
[**get_download_snapshot**](SnapshotsApi.md#get_download_snapshot) | **GET** /snapshots/{name} | 
[**get_snapshots**](SnapshotsApi.md#get_snapshots) | **GET** /snapshots | 
[**post_create_snapshot**](SnapshotsApi.md#post_create_snapshot) | **POST** /snapshots | 
[**put_import_snapshot**](SnapshotsApi.md#put_import_snapshot) | **PUT** /snapshots/running_config | 


# **delete_snapshot**
> InlineResponse20093 delete_snapshot(name)



Delete named snapshot

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
api_instance = openapi_client.SnapshotsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | Unique name for snapshot

try:
    api_response = api_instance.delete_snapshot(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->delete_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Unique name for snapshot | 

### Return type

[**InlineResponse20093**](InlineResponse20093.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_snapshot**
> file get_download_snapshot(name)



Download snapshot file

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
api_instance = openapi_client.SnapshotsApi(openapi_client.ApiClient(configuration))
name = 'name_example' # str | Unique name for snapshot

try:
    api_response = api_instance.get_download_snapshot(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_download_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Unique name for snapshot | 

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
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> InlineResponse20091 get_snapshots()



get list of snapshots

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
api_instance = openapi_client.SnapshotsApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_snapshots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Controller must be licensed first |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_snapshot**
> InlineResponse20092 post_create_snapshot(inline_object54=inline_object54)



Create a new snapshot

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
api_instance = openapi_client.SnapshotsApi(openapi_client.ApiClient(configuration))
inline_object54 = openapi_client.InlineObject54() # InlineObject54 |  (optional)

try:
    api_response = api_instance.post_create_snapshot(inline_object54=inline_object54)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->post_create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object54** | [**InlineObject54**](InlineObject54.md)|  | [optional] 

### Return type

[**InlineResponse20092**](InlineResponse20092.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**403** | Operation not allowed |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_snapshot**
> InlineResponse20094 put_import_snapshot(body)



Import snapshot into the manager and triggers a reboot for the Configuration to take effect.

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
api_instance = openapi_client.SnapshotsApi(openapi_client.ApiClient(configuration))
body = '/path/to/file' # file | Snapshot file

try:
    api_response = api_instance.put_import_snapshot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->put_import_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file**| Snapshot file | 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**403** | Operation not allowed |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

