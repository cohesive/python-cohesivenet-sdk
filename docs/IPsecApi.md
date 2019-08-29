# vns3api.IPsecApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ipsec_endpoint**](IPsecApi.md#delete_ipsec_endpoint) | **DELETE** /ipsec/endpoints/{endpoint_id} | 
[**delete_ipsec_endpoint_tunnel**](IPsecApi.md#delete_ipsec_endpoint_tunnel) | **DELETE** /ipsec/endpoints/{endpoint_id}/tunnels/{tunnel_id} | 
[**get_ipsec**](IPsecApi.md#get_ipsec) | **GET** /ipsec | 
[**get_ipsec_endpoint**](IPsecApi.md#get_ipsec_endpoint) | **GET** /ipsec/endpoints/{endpoint_id} | 
[**get_ipsec_status**](IPsecApi.md#get_ipsec_status) | **GET** /status/ipsec | 
[**get_link_history**](IPsecApi.md#get_link_history) | **GET** /status/link_history | 
[**post_create_ipsec_endpoint**](IPsecApi.md#post_create_ipsec_endpoint) | **POST** /ipsec/endpoints | 
[**post_create_ipsec_endpoint_tunnel**](IPsecApi.md#post_create_ipsec_endpoint_tunnel) | **POST** /ipsec/endpoints/{endpoint_id}/tunnels | 
[**post_restart_ipsec_action**](IPsecApi.md#post_restart_ipsec_action) | **POST** /ipsec | 
[**put_edit_ipsec_endpoint**](IPsecApi.md#put_edit_ipsec_endpoint) | **PUT** /ipsec/endpoints/{endpoint_id} | 
[**put_edit_ipsec_endpoint_tunnel**](IPsecApi.md#put_edit_ipsec_endpoint_tunnel) | **PUT** /ipsec/endpoints/{endpoint_id}/tunnels/{tunnel_id} | 
[**put_ipsec_config**](IPsecApi.md#put_ipsec_config) | **PUT** /ipsec | 


# **delete_ipsec_endpoint**
> InlineResponse20031 delete_ipsec_endpoint(endpoint_id)



Delete IPsec endpoint

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID of the IPsec endpoint

try:
    api_response = api_instance.delete_ipsec_endpoint(endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->delete_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID of the IPsec endpoint | 

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
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipsec_endpoint_tunnel**
> InlineResponse20030 delete_ipsec_endpoint_tunnel(endpoint_id, tunnel_id)



Delete IPsec tunnel

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID for IPsec endpoint
tunnel_id = 56 # int | numerical ID for tunnel

try:
    api_response = api_instance.delete_ipsec_endpoint_tunnel(endpoint_id, tunnel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->delete_ipsec_endpoint_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID for IPsec endpoint | 
 **tunnel_id** | **int**| numerical ID for tunnel | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipsec**
> InlineResponse20027 get_ipsec()



Get details for all IPsec endpoints/subnets

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_ipsec()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_ipsec: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

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

# **get_ipsec_endpoint**
> InlineResponse20030 get_ipsec_endpoint(endpoint_id)



Get IPsec endpoint information

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID of the IPsec endpoint

try:
    api_response = api_instance.get_ipsec_endpoint(endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID of the IPsec endpoint | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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

# **get_ipsec_status**
> InlineResponse20025 get_ipsec_status()



Describe ipsec tunnels status

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_ipsec_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_ipsec_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

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

# **get_link_history**
> InlineResponse20026 get_link_history(inline_object14=inline_object14)



Provides information about the connection history of the subnet or tunnel

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
inline_object14 = vns3api.InlineObject14() # InlineObject14 |  (optional)

try:
    api_response = api_instance.get_link_history(inline_object14=inline_object14)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_link_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object14** | [**InlineObject14**](InlineObject14.md)|  | [optional] 

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
**400** | Bad request |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_ipsec_endpoint**
> InlineResponse20030 post_create_ipsec_endpoint(inline_object17)



Create IPsec connection to the defined remote gateway

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
inline_object17 = vns3api.InlineObject17() # InlineObject17 | 

try:
    api_response = api_instance.post_create_ipsec_endpoint(inline_object17)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_create_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object17** | [**InlineObject17**](InlineObject17.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_ipsec_endpoint_tunnel**
> InlineResponse20030 post_create_ipsec_endpoint_tunnel(endpoint_id, inline_object19)



Create IPsec endpoint tunnel

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID of ipsec endpoint
inline_object19 = vns3api.InlineObject19() # InlineObject19 | 

try:
    api_response = api_instance.post_create_ipsec_endpoint_tunnel(endpoint_id, inline_object19)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_create_ipsec_endpoint_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID of ipsec endpoint | 
 **inline_object19** | [**InlineObject19**](InlineObject19.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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
**401** | Authentication information missing or invalid |  -  |
**403** | Permission denied. Max number of tunnels reach |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_restart_ipsec_action**
> InlineResponse20029 post_restart_ipsec_action(inline_object16)



Restart ipsec subystem

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
inline_object16 = vns3api.InlineObject16() # InlineObject16 | 

try:
    api_response = api_instance.post_restart_ipsec_action(inline_object16)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_restart_ipsec_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object16** | [**InlineObject16**](InlineObject16.md)|  | 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

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

# **put_edit_ipsec_endpoint**
> InlineResponse20030 put_edit_ipsec_endpoint(endpoint_id, inline_object18)



Edit IPsec connection

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID of the IPsec endpoint
inline_object18 = vns3api.InlineObject18() # InlineObject18 | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint(endpoint_id, inline_object18)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_edit_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID of the IPsec endpoint | 
 **inline_object18** | [**InlineObject18**](InlineObject18.md)|  | 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

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

# **put_edit_ipsec_endpoint_tunnel**
> InlineResponse20032 put_edit_ipsec_endpoint_tunnel(endpoint_id, tunnel_id, inline_object20)



Edit IPsec endpoint tunnel

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | ID for IPsec endpoint
tunnel_id = 56 # int | ID for tunnel
inline_object20 = vns3api.InlineObject20() # InlineObject20 | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint_tunnel(endpoint_id, tunnel_id, inline_object20)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_edit_ipsec_endpoint_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID for IPsec endpoint | 
 **tunnel_id** | **int**| ID for tunnel | 
 **inline_object20** | [**InlineObject20**](InlineObject20.md)|  | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

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

# **put_ipsec_config**
> InlineResponse20028 put_ipsec_config(inline_object15)



Edit Ipsec Configuration on device. Note, This is device wide and must be set before  any remote endpoint definitions are created. If it needs to be changed, all remote endpoint  information and tunnel information must be deleted first. 

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
api_instance = vns3api.IPsecApi(vns3api.ApiClient(configuration))
inline_object15 = vns3api.InlineObject15() # InlineObject15 | 

try:
    api_response = api_instance.put_ipsec_config(inline_object15)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_ipsec_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object15** | [**InlineObject15**](InlineObject15.md)|  | 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

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

