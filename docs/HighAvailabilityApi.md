# cohesivenet.HighAvailabilityApi

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
> HaUUID get_ha_id()



Get the unique ID this controller in HA configuration

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_ha_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->get_ha_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HaUUID**](HaUUID.md)

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

# **get_ha_status**
> HaDetail get_ha_status()



Get HA status for given ID

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_ha_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->get_ha_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HaDetail**](HaDetail.md)

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
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ha_sync_file**
> file get_ha_sync_file()



Download sync file from HA Primary

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_ha_sync_file()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->get_ha_sync_file: %s\n" % e)
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

# **get_ha_sync_status**
> object get_ha_sync_status(uuid, sync_uuid)



Get HA sync status for given ID

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))
uuid = 'uuid_example' # str | UUID for resource
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
 **uuid** | **str**| UUID for resource | 
 **sync_uuid** | **str**| ID for HA sync | 

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
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_init_ha**
> object post_init_ha(init_ha_request)



Initialise HA

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))
init_ha_request = cohesivenet.InitHaRequest() # InitHaRequest | 

try:
    api_response = api_instance.post_init_ha(init_ha_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->post_init_ha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **init_ha_request** | [**InitHaRequest**](InitHaRequest.md)|  | 

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
**200** | Accepted |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sync_ha**
> HaSyncStatusResponse post_sync_ha(body)



Initiate a sync creation on HA Primary

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))
body = None # object | 

try:
    api_response = api_instance.post_sync_ha(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->post_sync_ha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**HaSyncStatusResponse**](HaSyncStatusResponse.md)

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ha_activate**
> object put_ha_activate(activate_ha_request)



Activate the HA switchover

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))
activate_ha_request = cohesivenet.ActivateHaRequest() # ActivateHaRequest | 

try:
    api_response = api_instance.put_ha_activate(activate_ha_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HighAvailabilityApi->put_ha_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_ha_request** | [**ActivateHaRequest**](ActivateHaRequest.md)|  | 

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

# **put_ha_push_file**
> object put_ha_push_file(body)



Upload a sync file to HA Backup

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
api_instance = cohesivenet.HighAvailabilityApi(cohesivenet.VNS3Client(configuration))
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

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

