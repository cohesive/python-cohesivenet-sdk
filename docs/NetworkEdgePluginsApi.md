# cohesivenet.NetworkEdgePluginsApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_container**](NetworkEdgePluginsApi.md#delete_container) | **DELETE** /container_system/containers/{uuid} | 
[**delete_container_image**](NetworkEdgePluginsApi.md#delete_container_image) | **DELETE** /container_system/images/{uuid} | 
[**get_container_logs**](NetworkEdgePluginsApi.md#get_container_logs) | **GET** /container_system/containers/{uuid}/logs | 
[**get_container_system_i_ps**](NetworkEdgePluginsApi.md#get_container_system_i_ps) | **GET** /container_system/ip_addresses | 
[**get_container_system_images**](NetworkEdgePluginsApi.md#get_container_system_images) | **GET** /container_system/images | 
[**get_container_system_running_containers**](NetworkEdgePluginsApi.md#get_container_system_running_containers) | **GET** /container_system/containers | 
[**get_container_system_status**](NetworkEdgePluginsApi.md#get_container_system_status) | **GET** /container_system | 
[**post_action_container_system**](NetworkEdgePluginsApi.md#post_action_container_system) | **POST** /container_system | 
[**post_commit_container**](NetworkEdgePluginsApi.md#post_commit_container) | **POST** /container_system/containers/{uuid}/commit | 
[**post_create_container_image**](NetworkEdgePluginsApi.md#post_create_container_image) | **POST** /container_system/images | 
[**post_start_container**](NetworkEdgePluginsApi.md#post_start_container) | **POST** /container_system/containers | 
[**put_configure_container_system**](NetworkEdgePluginsApi.md#put_configure_container_system) | **PUT** /container_system | 
[**put_edit_container_image**](NetworkEdgePluginsApi.md#put_edit_container_image) | **PUT** /container_system/images/{uuid} | 
[**put_stop_container**](NetworkEdgePluginsApi.md#put_stop_container) | **PUT** /container_system/containers/{uuid} | 


# **delete_container**
> DeleteContainerDetailResponse delete_container()



Delete a container

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_container()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->delete_container: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeleteContainerDetailResponse**](DeleteContainerDetailResponse.md)

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

# **delete_container_image**
> DeleteContainerImageDetailResponse delete_container_image(force=force)



Delete container image

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
force = False # bool | force operation with cleanup (optional) (default to False)

try:
    api_response = api_instance.delete_container_image(force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->delete_container_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force** | **bool**| force operation with cleanup | [optional] [default to False]

### Return type

[**DeleteContainerImageDetailResponse**](DeleteContainerImageDetailResponse.md)

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_logs**
> ContainerLogsResponse get_container_logs(lines)



Fetch containers log messages

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
lines = 56 # int | Number of log lines to fetch

try:
    api_response = api_instance.get_container_logs(lines)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->get_container_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lines** | **int**| Number of log lines to fetch | 

### Return type

[**ContainerLogsResponse**](ContainerLogsResponse.md)

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

# **get_container_system_i_ps**
> ContainerSystemIPListResponse get_container_system_i_ps()



Retrieve IP address list for current container network configuration

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_container_system_i_ps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->get_container_system_i_ps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContainerSystemIPListResponse**](ContainerSystemIPListResponse.md)

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

# **get_container_system_images**
> ContainerImageListResponse get_container_system_images(uuid=uuid)



Get list of existing container system images

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
uuid = 'uuid_example' # str | UUID for resource (optional)

try:
    api_response = api_instance.get_container_system_images(uuid=uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->get_container_system_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID for resource | [optional] 

### Return type

[**ContainerImageListResponse**](ContainerImageListResponse.md)

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
**500** | Invalid server state |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_system_running_containers**
> RunningContainersDetailResponse get_container_system_running_containers(show_all=show_all)



Provides description information for one or all allocated containers

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
show_all = True # bool | Boolean for full list output (optional) (default to True)

try:
    api_response = api_instance.get_container_system_running_containers(show_all=show_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->get_container_system_running_containers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **bool**| Boolean for full list output | [optional] [default to True]

### Return type

[**RunningContainersDetailResponse**](RunningContainersDetailResponse.md)

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

# **get_container_system_status**
> ContainerSystemStatusDetailResponse get_container_system_status()



Retrieve status of container system

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_container_system_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->get_container_system_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContainerSystemStatusDetailResponse**](ContainerSystemStatusDetailResponse.md)

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

# **post_action_container_system**
> object post_action_container_system(container_system_action_request)



Take action on container system

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
container_system_action_request = cohesivenet.ContainerSystemActionRequest() # ContainerSystemActionRequest | 

try:
    api_response = api_instance.post_action_container_system(container_system_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->post_action_container_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_system_action_request** | [**ContainerSystemActionRequest**](ContainerSystemActionRequest.md)|  | 

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

# **post_commit_container**
> CreateContainerImageResponse post_commit_container(commit_container_request)



Creates a new container image from a running container

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
commit_container_request = cohesivenet.CommitContainerRequest() # CommitContainerRequest | 

try:
    api_response = api_instance.post_commit_container(commit_container_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->post_commit_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commit_container_request** | [**CommitContainerRequest**](CommitContainerRequest.md)|  | 

### Return type

[**CreateContainerImageResponse**](CreateContainerImageResponse.md)

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

# **post_create_container_image**
> CreateImageDetailResponse post_create_container_image(create_container_image_request)



Create new container image

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
image_request = cohesivenet.CreateContainerImageRequest()

try:
    api_response = api_instance.post_create_container_image(image_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->post_create_container_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_container_image_request** | [**CreateContainerImageRequest**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**CreateImageDetailResponse**](CreateImageDetailResponse.md)

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

# **post_start_container**
> RunContainerDetailResponse post_start_container(start_container_request)


Create (allocate) a new container or start an existing one

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
start_container_requet = cohesivenet.StartContainerRequest()

try:
    api_response = api_instance.post_start_container(start_container_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->post_start_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_container_request** | [**StartContainerRequest**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**RunContainerDetailResponse**](RunContainerDetailResponse.md)

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_configure_container_system**
> object put_configure_container_system(update_configure_container_system_request)



Configures the container network.

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
update_configure_container_system_request = cohesivenet.UpdateConfigureContainerSystemRequest() # UpdateConfigureContainerSystemRequest | 

try:
    api_response = api_instance.put_configure_container_system(update_configure_container_system_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->put_configure_container_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_configure_container_system_request** | [**UpdateConfigureContainerSystemRequest**](UpdateConfigureContainerSystemRequest.md)|  | 

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_edit_container_image**
> UpdateContainerImageDetailResponse put_edit_container_image(update_container_image_request)



Edits container image

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))
update_container_image_request = cohesivenet.UpdateContainerImageRequest() # UpdateContainerImageRequest | 

try:
    api_response = api_instance.put_edit_container_image(update_container_image_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->put_edit_container_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_container_image_request** | [**UpdateContainerImageRequest**](UpdateContainerImageRequest.md)|  | 

### Return type

[**UpdateContainerImageDetailResponse**](UpdateContainerImageDetailResponse.md)

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

# **put_stop_container**
> StopContainerDetailResponse put_stop_container()



Stops a running container

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
api_instance = cohesivenet.NetworkEdgePluginsApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.put_stop_container()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkEdgePluginsApi->put_stop_container: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StopContainerDetailResponse**](StopContainerDetailResponse.md)

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

