# cohesivenet.SystemAdministrationApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_access_url**](SystemAdministrationApi.md#delete_access_url) | **DELETE** /access/url | 
[**delete_access_url_by_id**](SystemAdministrationApi.md#delete_access_url_by_id) | **DELETE** /access/url/{access_url_id} | 
[**delete_api_access_token**](SystemAdministrationApi.md#delete_api_access_token) | **DELETE** /access/token/{token_id} | 
[**get_access_urls**](SystemAdministrationApi.md#get_access_urls) | **GET** /access/urls | 
[**get_access_url**](SystemAdministrationApi.md#get_access_url) | **GET** /access/url/{access_url_id} | 
[**get_api_access_token**](SystemAdministrationApi.md#get_api_access_token) | **GET** /access/token/{token_id} | 
[**get_api_access_tokens**](SystemAdministrationApi.md#get_api_access_tokens) | **GET** /access/tokens | 
[**get_cloud_data**](SystemAdministrationApi.md#get_cloud_data) | **GET** /cloud_data | 
[**get_ping_system**](SystemAdministrationApi.md#get_ping_system) | **GET** /system/ping | 
[**get_status**](SystemAdministrationApi.md#get_status) | **GET** /status | 
[**get_system_status**](SystemAdministrationApi.md#get_system_status) | **GET** /status/system | 
[**get_task_status**](SystemAdministrationApi.md#get_task_status) | **GET** /status/task | 
[**post_create_access_url**](SystemAdministrationApi.md#post_create_access_url) | **POST** /access/url | 
[**post_create_api_access_token**](SystemAdministrationApi.md#post_create_api_access_token) | **POST** /access/token | 
[**post_generate_keypair**](SystemAdministrationApi.md#post_generate_keypair) | **POST** /remote_support/keypair | 
[**put_expire_access_url**](SystemAdministrationApi.md#put_expire_access_url) | **PUT** /access/url/{access_url_id} | 
[**put_expire_api_access_token**](SystemAdministrationApi.md#put_expire_api_access_token) | **PUT** /access/token/{token_id} | 
[**put_remote_support**](SystemAdministrationApi.md#put_remote_support) | **PUT** /remote_support | 
[**put_server_action**](SystemAdministrationApi.md#put_server_action) | **PUT** /server | 


# **delete_access_url**
> object delete_access_url(delete_access_url_request=delete_access_url_request)



Delete access URL by ID or URL

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
delete_access_url_request = cohesivenet.DeleteAccessUrlRequest()

try:
    api_response = api_instance.delete_access_url(delete_access_url_request=delete_access_url_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->delete_access_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_access_url_request** | [**DeleteAccessUrlRequest**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

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
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_url_by_id**
> object delete_access_url_by_id()



Delete access url by ID

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_access_url_by_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->delete_access_url_by_id: %s\n" % e)
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
**200** | OK |  -  |
**401** |  |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_access_token**
> SimpleStringResponse delete_api_access_token()



Delete api token by ID

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_api_access_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->delete_api_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SimpleStringResponse**](SimpleStringResponse.md)

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
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_urls**
> AccessUrlListResponse get_access_urls()



Retrieve list of users' access urls, including expired ones

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_access_urls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_access_urls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessUrlListResponse**](AccessUrlListResponse.md)

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

# **get_access_url**
> object get_access_url(access_url_id)



Retrieve details for specific access url (including expired ones)

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
access_url_id = 56 # int | Access URL ID

try:
    api_response = api_instance.get_access_url(access_url_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_access_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_url_id** | **int**| Access URL ID | 

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
**401** |  |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_access_token**
> object get_api_access_token(token_id)



Retrieve details for specific access token (including expired ones)

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
token_id = 56 # int | Token ID

try:
    api_response = api_instance.get_api_access_token(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_api_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**| Token ID | 

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
**401** |  |  -  |
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_access_tokens**
> AccessTokenListResponse get_api_access_tokens()



Retrieve list of api tokens

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_api_access_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_api_access_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessTokenListResponse**](AccessTokenListResponse.md)

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

# **get_cloud_data**
> CloudInfoDetail get_cloud_data()



Returns cloud-specific data depending upon cloud type. Supports EC2 and GCE. More clouds coming soon.

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_cloud_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_cloud_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudInfoDetail**](CloudInfoDetail.md)

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

# **get_ping_system**
> SystemPingDetail get_ping_system()



Return an echo to a ping - does not require authentication

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_ping_system()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_ping_system: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemPingDetail**](SystemPingDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> RuntimeStatusDetail get_status()



Describe Runtime status details

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RuntimeStatusDetail**](RuntimeStatusDetail.md)

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

# **get_system_status**
> SystemStatusDetail get_system_status(timestamp=timestamp)



Provides information about the underlying appliance; memory, cpu, disk space, etc

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
timestamp = 56 # int | Unix timestamp (optional)

try:
    api_response = api_instance.get_system_status(timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_system_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| Unix timestamp | [optional] 

### Return type

[**SystemStatusDetail**](SystemStatusDetail.md)

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

# **get_task_status**
> TaskStatusDetail get_task_status(body)



Describe task status details

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
body = None # object | 

try:
    api_response = api_instance.get_task_status(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**TaskStatusDetail**](TaskStatusDetail.md)

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

# **post_create_access_url**
> AccessUrlDetail post_create_access_url(create_access_url_request=create_access_url_request)



Create access URL

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
create_access_url_request = cohesivenet.CreateAccessURLRequest() # CreateAccessURLRequest |  (optional)

try:
    api_response = api_instance.post_create_access_url(create_access_url_request=create_access_url_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->post_create_access_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_access_url_request** | [**CreateAccessURLRequest**](CreateAccessURLRequest.md)|  | [optional] 

### Return type

[**AccessUrlDetail**](AccessUrlDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_api_access_token**
> AccessTokenDetail post_create_api_access_token(create_api_token_request=create_api_token_request)



Create api token

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
create_api_token_request = cohesivenet.CreateAPITokenRequest() # CreateAPITokenRequest |  (optional)

try:
    api_response = api_instance.post_create_api_access_token(create_api_token_request=create_api_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->post_create_api_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_token_request** | [**CreateAPITokenRequest**](CreateAPITokenRequest.md)|  | [optional] 

### Return type

[**AccessTokenDetail**](AccessTokenDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_keypair**
> file post_generate_keypair(body)



Generating a remote support key which can be shared with Cohesive to provide  access to the internal of the VNS3 Manager remotely as a \"one time key\".  Once Cohesive has used the key it can be revoked and access terminated. 

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
body = '/path/to/file' # file | Encrypted passphrase file which will be used to generate an X509 key for  accessing the VNS3 Manager in support mode. These are generated and owned by Cohesive.  Contact support@cohesive.net for an encrypted passphrase file. 

try:
    api_response = api_instance.post_generate_keypair(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->post_generate_keypair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file**| Encrypted passphrase file which will be used to generate an X509 key for  accessing the VNS3 Manager in support mode. These are generated and owned by Cohesive.  Contact support@cohesive.net for an encrypted passphrase file.  | 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SSH key .pem file |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_expire_access_url**
> object put_expire_access_url(body=body)



Expire access URL

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
body = None # object |  (optional)

try:
    api_response = api_instance.put_expire_access_url(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_expire_access_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

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
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_expire_api_access_token**
> object put_expire_api_access_token(expire_request=expire_request)



Expire api token

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
expire_request = cohesivenet.ExpireRequest() # ExpireRequest |  (optional)

try:
    api_response = api_instance.put_expire_api_access_token(expire_request=expire_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_expire_api_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expire_request** | [**ExpireRequest**](ExpireRequest.md)|  | [optional] 

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
**404** | Not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_remote_support**
> RemoteSupportStatusResponse put_remote_support(update_remote_support_config_request=update_remote_support_config_request)



Enables and disables remote support. Revokes the validity of a remote support  keypair generated with postGenerateKeypair 

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
update_remote_support_config_request = cohesivenet.UpdateRemoteSupportConfigRequest() # UpdateRemoteSupportConfigRequest |  (optional)

try:
    api_response = api_instance.put_remote_support(update_remote_support_config_request=update_remote_support_config_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_remote_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_remote_support_config_request** | [**UpdateRemoteSupportConfigRequest**](UpdateRemoteSupportConfigRequest.md)|  | [optional] 

### Return type

[**RemoteSupportStatusResponse**](RemoteSupportStatusResponse.md)

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_server_action**
> SimpleStatusResponse put_server_action(reboot_request=reboot_request)



Server action for VNS3 controller. Currently only reboot supported.

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
api_instance = cohesivenet.SystemAdministrationApi(cohesivenet.VNS3Client(configuration))
reboot_request = cohesivenet.RebootRequest() # RebootRequest |  (optional)

try:
    api_response = api_instance.put_server_action(reboot_request=reboot_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_server_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reboot_request** | [**RebootRequest**](RebootRequest.md)|  | [optional] 

### Return type

[**SimpleStatusResponse**](SimpleStatusResponse.md)

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

