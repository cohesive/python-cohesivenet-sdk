# cohesivenet.MonitoringAlertingApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alert**](MonitoringAlertingApi.md#delete_alert) | **DELETE** /alert/{id} | 
[**get_alert**](MonitoringAlertingApi.md#get_alert) | **GET** /alert/{id} | 
[**get_alerts**](MonitoringAlertingApi.md#get_alerts) | **GET** /alerts | 
[**post_define_new_alert**](MonitoringAlertingApi.md#post_define_new_alert) | **POST** /alert | 
[**post_test_alert**](MonitoringAlertingApi.md#post_test_alert) | **POST** /alert/{id}/test | 
[**post_toggle_enabled_alert**](MonitoringAlertingApi.md#post_toggle_enabled_alert) | **POST** /alert/{id}/toggle_enabled | 
[**put_update_alert**](MonitoringAlertingApi.md#put_update_alert) | **PUT** /alert/{id} | 


# **delete_alert**
> object delete_alert()



Delete defined alert

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
api_instance = cohesivenet.MonitoringAlertingApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_alert()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAlertingApi->delete_alert: %s\n" % e)
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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert**
> object get_alert()



Retrieve details for single alert

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
api_instance = cohesivenet.MonitoringAlertingApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_alert()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAlertingApi->get_alert: %s\n" % e)
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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> AlertsListResponse get_alerts()



Retrieve all alerts

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
api_instance = cohesivenet.MonitoringAlertingApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAlertingApi->get_alerts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertsListResponse**](AlertsListResponse.md)

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

# **post_define_new_alert**
> AlertDetailResponse post_define_new_alert(create_alert_request)



Define new alert

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
api_instance = cohesivenet.MonitoringAlertingApi(cohesivenet.VNS3Client(configuration))
create_alert_request = cohesivenet.CreateAlertRequest() # CreateAlertRequest | 

try:
    api_response = api_instance.post_define_new_alert(create_alert_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAlertingApi->post_define_new_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alert_request** | [**CreateAlertRequest**](CreateAlertRequest.md)|  | 

### Return type

[**AlertDetailResponse**](AlertDetailResponse.md)

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

# **post_test_alert**
> SimpleBooleanResponse post_test_alert()



Send test alert for this defined alert

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
api_instance = cohesivenet.MonitoringAlertingApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.post_test_alert()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAlertingApi->post_test_alert: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SimpleBooleanResponse**](SimpleBooleanResponse.md)

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_toggle_enabled_alert**
> object post_toggle_enabled_alert()



Toggle enabled property on alert

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
api_instance = cohesivenet.MonitoringAlertingApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.post_toggle_enabled_alert()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAlertingApi->post_toggle_enabled_alert: %s\n" % e)
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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_alert**
> object put_update_alert(alert_id, update_alert_request)



Edit defined alert

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
api_instance = cohesivenet.MonitoringAlertingApi(cohesivenet.VNS3Client(configuration))
update_alert_request = cohesivenet.UpdateAlertRequest() # UpdateAlertRequest | 

try:
    api_response = api_instance.put_update_alert(alert_id, update_alert_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAlertingApi->put_update_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | Integer  | 
 **update_alert_request** | [**UpdateAlertRequest**](UpdateAlertRequest.md)|  | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

