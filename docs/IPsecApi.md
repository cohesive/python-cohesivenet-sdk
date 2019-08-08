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
> InlineResponse20043 delete_ipsec_endpoint(endpoint_id)



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

[**InlineResponse20043**](InlineResponse20043.md)

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
> InlineResponse20045 delete_ipsec_endpoint_tunnel(endpoint_id, tunnel_id)



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

[**InlineResponse20045**](InlineResponse20045.md)

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
> InlineResponse20042 get_ipsec()



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

[**InlineResponse20042**](InlineResponse20042.md)

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
> InlineResponse20045 get_ipsec_endpoint(endpoint_id)



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

[**InlineResponse20045**](InlineResponse20045.md)

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
> InlineResponse20024 get_ipsec_status()



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

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Operation not allowed |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_history**
> InlineResponse20027 get_link_history(inline_object13=inline_object13)



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
inline_object13 = vns3api.InlineObject13() # InlineObject13 |  (optional)

try:
    api_response = api_instance.get_link_history(inline_object13=inline_object13)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_link_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object13** | [**InlineObject13**](InlineObject13.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

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

# **post_create_ipsec_endpoint**
> InlineResponse20045 post_create_ipsec_endpoint(inline_object28)



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
inline_object28 = vns3api.InlineObject28() # InlineObject28 | 

try:
    api_response = api_instance.post_create_ipsec_endpoint(inline_object28)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_create_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object28** | [**InlineObject28**](InlineObject28.md)|  | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

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
> InlineResponse20045 post_create_ipsec_endpoint_tunnel(endpoint_id, inline_object30)



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
inline_object30 = vns3api.InlineObject30() # InlineObject30 | 

try:
    api_response = api_instance.post_create_ipsec_endpoint_tunnel(endpoint_id, inline_object30)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_create_ipsec_endpoint_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID of ipsec endpoint | 
 **inline_object30** | [**InlineObject30**](InlineObject30.md)|  | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

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
**403** | Permission denied. Max number of tunnels reach |  -  |
**401** | Authentication information missing or invalid |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_restart_ipsec_action**
> InlineResponse20044 post_restart_ipsec_action(inline_object27)



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
inline_object27 = vns3api.InlineObject27() # InlineObject27 | 

try:
    api_response = api_instance.post_restart_ipsec_action(inline_object27)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_restart_ipsec_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object27** | [**InlineObject27**](InlineObject27.md)|  | 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

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
> InlineResponse20045 put_edit_ipsec_endpoint(endpoint_id, inline_object29)



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
inline_object29 = vns3api.InlineObject29() # InlineObject29 | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint(endpoint_id, inline_object29)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_edit_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID of the IPsec endpoint | 
 **inline_object29** | [**InlineObject29**](InlineObject29.md)|  | 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

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
> InlineResponse20046 put_edit_ipsec_endpoint_tunnel(endpoint_id, tunnel_id, inline_object31)



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
inline_object31 = vns3api.InlineObject31() # InlineObject31 | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint_tunnel(endpoint_id, tunnel_id, inline_object31)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_edit_ipsec_endpoint_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID for IPsec endpoint | 
 **tunnel_id** | **int**| ID for tunnel | 
 **inline_object31** | [**InlineObject31**](InlineObject31.md)|  | 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

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
> InlineResponse20043 put_ipsec_config(inline_object26)



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
inline_object26 = vns3api.InlineObject26() # InlineObject26 | 

try:
    api_response = api_instance.put_ipsec_config(inline_object26)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_ipsec_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object26** | [**InlineObject26**](InlineObject26.md)|  | 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

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

