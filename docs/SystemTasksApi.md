# vns3api.SystemTasksApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_status**](SystemTasksApi.md#get_task_status) | **GET** /status/task | 


# **get_task_status**
> InlineResponse20023 get_task_status(task_token)



Describe task status details

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
api_instance = vns3api.SystemTasksApi(vns3api.ApiClient(configuration))
task_token = vns3api.TaskToken() # TaskToken | 

try:
    api_response = api_instance.get_task_status(task_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemTasksApi->get_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_token** | [**TaskToken**](TaskToken.md)|  | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

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
**403** | Operation not allowed |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

