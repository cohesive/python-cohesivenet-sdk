# vns3api.MonitoringAndAlertingApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alert**](MonitoringAndAlertingApi.md#delete_alert) | **DELETE** /alert/{id} | 
[**get_alert**](MonitoringAndAlertingApi.md#get_alert) | **GET** /alert/{id} | 
[**get_alerts**](MonitoringAndAlertingApi.md#get_alerts) | **GET** /alerts | 
[**post_define_new_alert**](MonitoringAndAlertingApi.md#post_define_new_alert) | **POST** /alert | 
[**post_test_alert**](MonitoringAndAlertingApi.md#post_test_alert) | **POST** /alert/{id}/test | 
[**post_toggle_enabled_alert**](MonitoringAndAlertingApi.md#post_toggle_enabled_alert) | **POST** /alert/{id}/toggle_enabled | 
[**put_update_alert**](MonitoringAndAlertingApi.md#put_update_alert) | **PUT** /alert/{id} | 


# **delete_alert**
> InlineResponse20031 delete_alert(id)



Delete defined alert

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
api_instance = vns3api.MonitoringAndAlertingApi(vns3api.ApiClient(configuration))
id = 56 # int | ID of alert

try:
    api_response = api_instance.delete_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAndAlertingApi->delete_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of alert | 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> InlineResponse20075 get_alert(id)



Retrieve details for single alert

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
api_instance = vns3api.MonitoringAndAlertingApi(vns3api.ApiClient(configuration))
id = 56 # int | ID of alert

try:
    api_response = api_instance.get_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAndAlertingApi->get_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of alert | 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> InlineResponse20074 get_alerts()



Retrieve all alerts

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
api_instance = vns3api.MonitoringAndAlertingApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAndAlertingApi->get_alerts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20074**](InlineResponse20074.md)

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

# **post_define_new_alert**
> InlineResponse20075 post_define_new_alert(inline_object47)



Define new alert

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
api_instance = vns3api.MonitoringAndAlertingApi(vns3api.ApiClient(configuration))
inline_object47 = vns3api.InlineObject47() # InlineObject47 | 

try:
    api_response = api_instance.post_define_new_alert(inline_object47)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAndAlertingApi->post_define_new_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object47** | [**InlineObject47**](InlineObject47.md)|  | 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

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

# **post_test_alert**
> InlineResponse20076 post_test_alert(id)



Send test alert for this defined alert

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
api_instance = vns3api.MonitoringAndAlertingApi(vns3api.ApiClient(configuration))
id = 56 # int | ID of alert

try:
    api_response = api_instance.post_test_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAndAlertingApi->post_test_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of alert | 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_toggle_enabled_alert**
> InlineResponse20075 post_toggle_enabled_alert(id)



Toggle enabled property on alert

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
api_instance = vns3api.MonitoringAndAlertingApi(vns3api.ApiClient(configuration))
id = 56 # int | ID of alert

try:
    api_response = api_instance.post_toggle_enabled_alert(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAndAlertingApi->post_toggle_enabled_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of alert | 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

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
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_alert**
> InlineResponse20075 put_update_alert(id, inline_object48)



Edit defined alert

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
api_instance = vns3api.MonitoringAndAlertingApi(vns3api.ApiClient(configuration))
id = 56 # int | ID of alert
inline_object48 = vns3api.InlineObject48() # InlineObject48 | 

try:
    api_response = api_instance.put_update_alert(id, inline_object48)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAndAlertingApi->put_update_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of alert | 
 **inline_object48** | [**InlineObject48**](InlineObject48.md)|  | 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

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

