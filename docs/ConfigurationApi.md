# openapi_client.ConfigurationApi

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
> InlineResponse20011 get_config()



Describe Runtime Configuration for VNS3 Controller

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get runtime Configuration details |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keyset**
> InlineResponse20020 get_keyset()



Returns status of whether cryptographic credentials, which are used to provide  overlay devices access to the topology, have been generated. 

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_keyset()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_keyset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

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

# **get_runtime**
> InlineResponse20011 get_runtime()



Alias for GET /config

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_runtime()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_runtime: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get runtime Configuration details |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssl_install_status**
> InlineResponse20019 get_ssl_install_status(uuid)



Get status for ssl installation task

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))
uuid = 'uuid_example' # str | uuid of install task

try:
    api_response = api_instance.get_ssl_install_status(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_ssl_install_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| uuid of install task | 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_config**
> InlineResponse20012 put_config(inline_object8)



Provides general information about the manager's topology, license state and  checksums and allows you to set the topology name. 

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))
inline_object8 = openapi_client.InlineObject8() # InlineObject8 | 

try:
    api_response = api_instance.put_config(inline_object8)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_install_ssl_keypair**
> InlineResponse20018 put_install_ssl_keypair()



Install new SSL cert and key pair

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.put_install_ssl_keypair()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_install_ssl_keypair: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_keyset**
> InlineResponse20021 put_keyset(inline_object11)



Generates or fetches cryptographic credentials which are used to provide overlay devices access to the topology.  Keyset generation happens in background. Poll on GET /keyset in_progress value. 

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))
inline_object11 = openapi_client.InlineObject11() # InlineObject11 | 

try:
    api_response = api_instance.put_keyset(inline_object11)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_keyset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_admin_ui**
> InlineResponse2008 put_update_admin_ui(inline_object5)



Update Admin UI settings. Enable/Disable and set credentials. 

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))
inline_object5 = openapi_client.InlineObject5() # InlineObject5 | 

try:
    api_response = api_instance.put_update_admin_ui(inline_object5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_update_admin_ui: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object5** | [**InlineObject5**](InlineObject5.md)|  | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_api_password**
> InlineResponse20010 put_update_api_password(inline_object7)



Allows you to change the API password/secret key.  To change the Web UI password (or username) use PUT admin_ui. 

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))
inline_object7 = openapi_client.InlineObject7() # InlineObject7 | 

try:
    api_response = api_instance.put_update_api_password(inline_object7)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_update_api_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_upload_ssl_keypair**
> InlineResponse20017 put_upload_ssl_keypair(inline_object10)



Upload new SSL cert and key pair

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
api_instance = openapi_client.ConfigurationApi(openapi_client.ApiClient(configuration))
inline_object10 = openapi_client.InlineObject10() # InlineObject10 | 

try:
    api_response = api_instance.put_upload_ssl_keypair(inline_object10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->put_upload_ssl_keypair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

