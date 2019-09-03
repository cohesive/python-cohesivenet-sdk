# cohesivenet.SnapshotsApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **DELETE** /snapshots/{name} | 
[**get_download_snapshot**](SnapshotsApi.md#get_download_snapshot) | **GET** /snapshots/{name} | 
[**get_snapshots**](SnapshotsApi.md#get_snapshots) | **GET** /snapshots | 
[**post_create_snapshot**](SnapshotsApi.md#post_create_snapshot) | **POST** /snapshots | 
[**put_import_snapshot**](SnapshotsApi.md#put_import_snapshot) | **PUT** /snapshots/running_config | 


# **delete_snapshot**
> object delete_snapshot()



Delete named snapshot

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
api_instance = cohesivenet.SnapshotsApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_snapshot()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->delete_snapshot: %s\n" % e)
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
**403** | Request Forbidden - operation not allowed |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_snapshot**
> file get_download_snapshot()



Download snapshot file

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
api_instance = cohesivenet.SnapshotsApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_download_snapshot()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_download_snapshot: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> SnapshotsListResponse get_snapshots()



get list of snapshots

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
api_instance = cohesivenet.SnapshotsApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_snapshots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotsListResponse**](SnapshotsListResponse.md)

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

# **post_create_snapshot**
> SnapshotsDetailResponse post_create_snapshot(create_snapshot_request=create_snapshot_request)



Create a new snapshot

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
api_instance = cohesivenet.SnapshotsApi(cohesivenet.VNS3Client(configuration))
create_snapshot_request = cohesivenet.CreateSnapshotRequest() # CreateSnapshotRequest |  (optional)

try:
    api_response = api_instance.post_create_snapshot(create_snapshot_request=create_snapshot_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->post_create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_snapshot_request** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | [optional] 

### Return type

[**SnapshotsDetailResponse**](SnapshotsDetailResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_snapshot**
> SnapshotImportStatusResponse put_import_snapshot(body)



Import snapshot into the manager and triggers a reboot for the Configuration to take effect.

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
api_instance = cohesivenet.SnapshotsApi(cohesivenet.VNS3Client(configuration))
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

[**SnapshotImportStatusResponse**](SnapshotImportStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

