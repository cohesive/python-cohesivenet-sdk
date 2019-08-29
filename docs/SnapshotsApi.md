# vns3api.SnapshotsApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **DELETE** /snapshots/{name} | 
[**get_download_snapshot**](SnapshotsApi.md#get_download_snapshot) | **GET** /snapshots/{name} | 
[**get_snapshots**](SnapshotsApi.md#get_snapshots) | **GET** /snapshots | 
[**post_create_snapshot**](SnapshotsApi.md#post_create_snapshot) | **POST** /snapshots | 
[**put_import_snapshot**](SnapshotsApi.md#put_import_snapshot) | **PUT** /snapshots/running_config | 


# **delete_snapshot**
> InlineResponse20072 delete_snapshot(name)



Delete named snapshot

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
api_instance = vns3api.SnapshotsApi(vns3api.ApiClient(configuration))
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

[**InlineResponse20072**](InlineResponse20072.md)

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
**404** | Not found |  -  |
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
api_instance = vns3api.SnapshotsApi(vns3api.ApiClient(configuration))
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
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**404** | Not found |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> InlineResponse20070 get_snapshots()



get list of snapshots

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
api_instance = vns3api.SnapshotsApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_snapshots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

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

# **post_create_snapshot**
> InlineResponse20071 post_create_snapshot(inline_object44=inline_object44)



Create a new snapshot

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
api_instance = vns3api.SnapshotsApi(vns3api.ApiClient(configuration))
inline_object44 = vns3api.InlineObject44() # InlineObject44 |  (optional)

try:
    api_response = api_instance.post_create_snapshot(inline_object44=inline_object44)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->post_create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object44** | [**InlineObject44**](InlineObject44.md)|  | [optional] 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

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

# **put_import_snapshot**
> InlineResponse20073 put_import_snapshot(body)



Import snapshot into the manager and triggers a reboot for the Configuration to take effect.

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
api_instance = vns3api.SnapshotsApi(vns3api.ApiClient(configuration))
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

[**InlineResponse20073**](InlineResponse20073.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

