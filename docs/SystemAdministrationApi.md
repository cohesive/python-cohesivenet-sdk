# openapi_client.SystemAdministrationApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_access_url**](SystemAdministrationApi.md#delete_access_url) | **DELETE** /access/url | 
[**delete_access_url_by_id**](SystemAdministrationApi.md#delete_access_url_by_id) | **DELETE** /access/url/{access_url_id} | 
[**delete_api_access_token**](SystemAdministrationApi.md#delete_api_access_token) | **DELETE** /access/token/{token_id} | 
[**get_access_ur_ls**](SystemAdministrationApi.md#get_access_ur_ls) | **GET** /access/urls | 
[**get_access_url**](SystemAdministrationApi.md#get_access_url) | **GET** /access/url/{access_url_id} | 
[**get_api_access_token**](SystemAdministrationApi.md#get_api_access_token) | **GET** /access/token/{token_id} | 
[**get_api_access_tokens**](SystemAdministrationApi.md#get_api_access_tokens) | **GET** /access/tokens | 
[**get_cloud_data**](SystemAdministrationApi.md#get_cloud_data) | **GET** /cloud_data | 
[**get_ping_system**](SystemAdministrationApi.md#get_ping_system) | **GET** /system/ping | 
[**get_remote_support_details**](SystemAdministrationApi.md#get_remote_support_details) | **GET** /remote_support | 
[**get_status**](SystemAdministrationApi.md#get_status) | **GET** /status | 
[**get_system_status**](SystemAdministrationApi.md#get_system_status) | **GET** /status/system | 
[**post_create_access_url**](SystemAdministrationApi.md#post_create_access_url) | **POST** /access/url | 
[**post_create_api_access_token**](SystemAdministrationApi.md#post_create_api_access_token) | **POST** /access/token | 
[**post_generate_keypair**](SystemAdministrationApi.md#post_generate_keypair) | **POST** /remote_support/keypair | 
[**put_expire_access_url**](SystemAdministrationApi.md#put_expire_access_url) | **PUT** /access/url/{access_url_id} | 
[**put_expire_api_access_token**](SystemAdministrationApi.md#put_expire_api_access_token) | **PUT** /access/token/{token_id} | 
[**put_remote_support**](SystemAdministrationApi.md#put_remote_support) | **PUT** /remote_support | 
[**put_server_action**](SystemAdministrationApi.md#put_server_action) | **PUT** /server | 


# **delete_access_url**
> InlineResponse2006 delete_access_url(unknown_base_type=unknown_base_type)



Delete access URL by ID or URL

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
unknown_base_type = openapi_client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    api_response = api_instance.delete_access_url(unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->delete_access_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_url_by_id**
> InlineResponse2006 delete_access_url_by_id(access_url_id)



Delete access url by ID

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
access_url_id = 56 # int | Access URL ID

try:
    api_response = api_instance.delete_access_url_by_id(access_url_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->delete_access_url_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_url_id** | **int**| Access URL ID | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

# **delete_api_access_token**
> InlineResponse2004 delete_api_access_token(token_id)



Delete api token by ID

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
token_id = 56 # int | Token ID

try:
    api_response = api_instance.delete_api_access_token(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->delete_api_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**| Token ID | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **get_access_ur_ls**
> InlineResponse2005 get_access_ur_ls()



Retrieve list of users' access urls, including expired ones

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_access_ur_ls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_access_ur_ls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **get_access_url**
> InlineResponse2011 get_access_url(access_url_id)



Retrieve details for specific access url (including expired ones)

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
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

[**InlineResponse2011**](InlineResponse2011.md)

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

# **get_api_access_token**
> InlineResponse201 get_api_access_token(token_id)



Retrieve details for specific access token (including expired ones)

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
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

[**InlineResponse201**](InlineResponse201.md)

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

# **get_api_access_tokens**
> InlineResponse2003 get_api_access_tokens()



Retrieve list of api tokens

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_api_access_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_api_access_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **get_cloud_data**
> InlineResponse2007 get_cloud_data()



Returns cloud-specific data depending upon cloud type. Supports EC2 and GCE. More clouds coming soon.

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_cloud_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_cloud_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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

# **get_ping_system**
> InlineResponse200 get_ping_system()



Return an echo to a ping - does not require authentication

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_ping_system()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_ping_system: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_support_details**
> InlineResponse2001 get_remote_support_details()



Get remote support information

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_remote_support_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_remote_support_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> InlineResponse20022 get_status()



Describe Runtime status details

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_status**
> InlineResponse20026 get_system_status(inline_object12=inline_object12)



Provides information about the underlying appliance; memory, cpu, disk space, etc

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
inline_object12 = openapi_client.InlineObject12() # InlineObject12 |  (optional)

try:
    api_response = api_instance.get_system_status(inline_object12=inline_object12)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->get_system_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Operation not allowed |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_access_url**
> InlineResponse2011 post_create_access_url(inline_object3=inline_object3)



Create access URL

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
inline_object3 = openapi_client.InlineObject3() # InlineObject3 |  (optional)

try:
    api_response = api_instance.post_create_access_url(inline_object3=inline_object3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->post_create_access_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_api_access_token**
> InlineResponse201 post_create_api_access_token(inline_object1=inline_object1)



Create api token

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
inline_object1 = openapi_client.InlineObject1() # InlineObject1 |  (optional)

try:
    api_response = api_instance.post_create_api_access_token(inline_object1=inline_object1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->post_create_api_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_generate_keypair**
> file post_generate_keypair(body)



Generating a remote support key which can be shared with Cohesive to provide  access to the internal of the VNS3 Manager remotely as a \"one time key\".  Once Cohesive has used the key it can be revoked and access terminated. 

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_expire_access_url**
> InlineResponse2011 put_expire_access_url(access_url_id, inline_object4=inline_object4)



Expire access URL

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
access_url_id = 56 # int | Access URL ID
inline_object4 = openapi_client.InlineObject4() # InlineObject4 |  (optional)

try:
    api_response = api_instance.put_expire_access_url(access_url_id, inline_object4=inline_object4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_expire_access_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_url_id** | **int**| Access URL ID | 
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_expire_api_access_token**
> InlineResponse201 put_expire_api_access_token(token_id, inline_object2=inline_object2)



Expire api token

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
token_id = 56 # int | Token ID
inline_object2 = openapi_client.InlineObject2() # InlineObject2 |  (optional)

try:
    api_response = api_instance.put_expire_api_access_token(token_id, inline_object2=inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_expire_api_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**| Token ID | 
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_remote_support**
> InlineResponse2002 put_remote_support(inline_object=inline_object)



Enables and disables remote support. Revokes the validity of a remote support  keypair generated with postGenerateKeypair 

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
inline_object = openapi_client.InlineObject() # InlineObject |  (optional)

try:
    api_response = api_instance.put_remote_support(inline_object=inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_remote_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **put_server_action**
> InlineResponse2009 put_server_action(inline_object6=inline_object6)



Server action for VNS3 controller. Currently only reboot supported.

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
api_instance = openapi_client.SystemAdministrationApi(openapi_client.ApiClient(configuration))
inline_object6 = openapi_client.InlineObject6() # InlineObject6 |  (optional)

try:
    api_response = api_instance.put_server_action(inline_object6=inline_object6)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationApi->put_server_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

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

