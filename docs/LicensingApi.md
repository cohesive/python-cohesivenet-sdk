# openapi_client.LicensingApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_license**](LicensingApi.md#get_license) | **GET** /license | 
[**put_license_upgrade**](LicensingApi.md#put_license_upgrade) | **PUT** /license/upgrade | 
[**put_set_license_parameters**](LicensingApi.md#put_set_license_parameters) | **PUT** /license/parameters | 
[**upload_license**](LicensingApi.md#upload_license) | **PUT** /license | 


# **get_license**
> InlineResponse20013 get_license()



Get license details

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
api_instance = openapi_client.LicensingApi(openapi_client.ApiClient(configuration))

try:
    api_response = api_instance.get_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->get_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get license topology details |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_license_upgrade**
> InlineResponse20016 put_license_upgrade(body)



Upload new license to controller

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
api_instance = openapi_client.LicensingApi(openapi_client.ApiClient(configuration))
body = '/path/to/file' # file | License file

try:
    api_response = api_instance.put_license_upgrade(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->put_license_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file**| License file | 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New license parameters |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_set_license_parameters**
> InlineResponse20015 put_set_license_parameters(inline_object9)



Set and accept license parameters. Triggers reboot. Irreversible operation.

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
api_instance = openapi_client.LicensingApi(openapi_client.ApiClient(configuration))
inline_object9 = openapi_client.InlineObject9() # InlineObject9 | 

try:
    api_response = api_instance.put_set_license_parameters(inline_object9)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->put_set_license_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object9** | [**InlineObject9**](InlineObject9.md)|  | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Put new license parameters for topology |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_license**
> InlineResponse20014 upload_license(body)



License a VNS3 Controller to be a part of a specific topology. Must not be licensed already.

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
api_instance = openapi_client.LicensingApi(openapi_client.ApiClient(configuration))
body = '/path/to/file' # file | License file

try:
    api_response = api_instance.upload_license(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicensingApi->upload_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **file**| License file | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload license response |  -  |
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

