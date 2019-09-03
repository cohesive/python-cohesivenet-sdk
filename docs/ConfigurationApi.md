# cohesivenet.ConfigurationApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](ConfigurationApi.md#get_config) | **GET** /config | 
[**get_keyset**](ConfigurationApi.md#get_keyset) | **GET** /keyset | 
[**get_runtime**](ConfigurationApi.md#get_runtime) | **GET** /runtime | 
[**get_ssl_install_status**](ConfigurationApi.md#get_ssl_install_status) | **GET** /system/ssl/install/{uuid} | 
[**put_config**](ConfigurationApi.md#put_config) | **PUT** /config | 
[**put_install_ssl_keypair**](ConfigurationApi.md#put_install_ssl_keypair) | **PUT** /system/ssl/install | 
[**put_keyset**](ConfigurationApi.md#put_keyset) | **PUT** /keyset | 
[**put_update_admin_ui**](ConfigurationApi.md#put_update_admin_ui) | **PUT** /admin_ui | 
[**put_update_api_password**](ConfigurationApi.md#put_update_api_password) | **PUT** /api_password | 
[**put_upload_ssl_keypair**](ConfigurationApi.md#put_upload_ssl_keypair) | **PUT** /system/ssl/keypair | 


# **get_config**
> ConfigDetail get_config()



Describe Runtime Configuration for VNS3 Controller

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigDetail**](ConfigDetail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get runtime Configuration details |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keyset**
> KeysetDetail get_keyset()



Returns status of whether cryptographic credentials, which are used to provide  overlay devices access to the topology, have been generated. 

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_keyset()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_keyset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KeysetDetail**](KeysetDetail.md)

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

# **get_runtime**
> object get_runtime()



Alias for GET /config

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_runtime()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_runtime: %s\n" % e)
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
**200** | Get runtime Configuration details |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssl_install_status**
> object get_ssl_install_status(uuid)



Get status for ssl installation task

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))
uuid = 'uuid_example' # str | uuid of resource

try:
    api_response = api_instance.get_ssl_install_status(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_ssl_install_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| uuid of resource | 

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

# **put_config**
> object put_config(update_config_request)



Provides general information about the manager's topology, license state and  checksums and allows you to set the topology name. 

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))
update_config_request = cohesivenet.UpdateConfigRequest() # UpdateConfigRequest | 

try:
    api_response = api_instance.put_config(update_config_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_config_request** | [**UpdateConfigRequest**](UpdateConfigRequest.md)|  | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_install_ssl_keypair**
> ServerSSLDetailResponse put_install_ssl_keypair()



Install new SSL cert and key pair

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.put_install_ssl_keypair()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_install_ssl_keypair: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerSSLDetailResponse**](ServerSSLDetailResponse.md)

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_keyset**
> object put_keyset(update_keyset_request)



Generates or fetches cryptographic credentials which are used to provide overlay devices access to the topology.  Keyset generation happens in background. Poll on GET /keyset in_progress value. 

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))
update_keyset_request = cohesivenet.UpdateKeysetRequest() # UpdateKeysetRequest | 

try:
    api_response = api_instance.put_keyset(update_keyset_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_keyset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_keyset_request** | [**UpdateKeysetRequest**](UpdateKeysetRequest.md)|  | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_admin_ui**
> AdminUISettingsDetail put_update_admin_ui(update_admin_ui_settings_request)



Update Admin UI settings. Enable/Disable and set credentials. 

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))
update_admin_ui_settings_request = cohesivenet.UpdateAdminUISettingsRequest() # UpdateAdminUISettingsRequest | 

try:
    api_response = api_instance.put_update_admin_ui(update_admin_ui_settings_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_update_admin_ui: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_admin_ui_settings_request** | [**UpdateAdminUISettingsRequest**](UpdateAdminUISettingsRequest.md)|  | 

### Return type

[**AdminUISettingsDetail**](AdminUISettingsDetail.md)

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

# **put_update_api_password**
> PasswordResetResponse put_update_api_password(update_password_request)



Allows you to change the API password/secret key.  To change the Web UI password (or username) use PUT admin_ui. 

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))
update_password_request = cohesivenet.UpdatePasswordRequest() # UpdatePasswordRequest | 

try:
    api_response = api_instance.put_update_api_password(update_password_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_update_api_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_password_request** | [**UpdatePasswordRequest**](UpdatePasswordRequest.md)|  | 

### Return type

[**PasswordResetResponse**](PasswordResetResponse.md)

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

# **put_upload_ssl_keypair**
> object put_upload_ssl_keypair(update_server_ssl_request)



Upload new SSL cert and key pair

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
api_instance = cohesivenet.ConfigurationApi(cohesivenet.VNS3Client(configuration))
update_server_ssl_request = cohesivenet.UpdateServerSSLRequest() # UpdateServerSSLRequest | 

try:
    api_response = api_instance.put_upload_ssl_keypair(update_server_ssl_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_upload_ssl_keypair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_server_ssl_request** | [**UpdateServerSSLRequest**](UpdateServerSSLRequest.md)|  | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

