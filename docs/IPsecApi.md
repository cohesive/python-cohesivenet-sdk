# cohesivenet.IPsecApi

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
> object delete_ipsec_endpoint()



Delete IPsec endpoint

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_ipsec_endpoint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->delete_ipsec_endpoint: %s\n" % e)
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
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ipsec_endpoint_tunnel**
> object delete_ipsec_endpoint_tunnel()



Delete IPsec tunnel

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.delete_ipsec_endpoint_tunnel()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->delete_ipsec_endpoint_tunnel: %s\n" % e)
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
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipsec**
> IpsecSystemDetail get_ipsec()



Get details for all IPsec endpoints/subnets

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_ipsec()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_ipsec: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpsecSystemDetail**](IpsecSystemDetail.md)

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

# **get_ipsec_endpoint**
> object get_ipsec_endpoint(endpoint_id)



Get IPsec endpoint information

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
endpoint_id = 56 # int | ID for IPsec endpoint

try:
    api_response = api_instance.get_ipsec_endpoint(endpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| ID for IPsec endpoint | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ipsec_status**
> IpsecTunnelListResponseKeyValue get_ipsec_status()



Describe ipsec tunnels status

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_ipsec_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_ipsec_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpsecTunnelListResponseKeyValue**](IpsecTunnelListResponseKeyValue.md)

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

# **get_link_history**
> LinkHistoryDetail get_link_history(remote=remote, local=local, tunnelid=tunnelid)



Provides information about the connection history of the subnet or tunnel

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
remote = 'remote_example' # str | Address string in CIDR format to display link history to a remote endpoint. (optional)
local = 'local_example' # str | Address string in CIDR format which will display status of the local route (optional)
tunnelid = 56 # int | Will display link history of just the tunnel specified, which may be only one tunnel to a remote endpoint. (optional)

try:
    api_response = api_instance.get_link_history(remote=remote, local=local, tunnelid=tunnelid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->get_link_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote** | **str**| Address string in CIDR format to display link history to a remote endpoint. | [optional] 
 **local** | **str**| Address string in CIDR format which will display status of the local route | [optional] 
 **tunnelid** | **int**| Will display link history of just the tunnel specified, which may be only one tunnel to a remote endpoint. | [optional] 

### Return type

[**LinkHistoryDetail**](LinkHistoryDetail.md)

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_ipsec_endpoint**
> IpsecRemoteEndpointDetail post_create_ipsec_endpoint(create_ipsec_endpoint_request)



Create IPsec connection to the defined remote gateway

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
create_ipsec_endpoint_request = cohesivenet.CreateIpsecEndpointRequest() # CreateIpsecEndpointRequest | 

try:
    api_response = api_instance.post_create_ipsec_endpoint(create_ipsec_endpoint_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_create_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ipsec_endpoint_request** | [**CreateIpsecEndpointRequest**](CreateIpsecEndpointRequest.md)|  | 

### Return type

[**IpsecRemoteEndpointDetail**](IpsecRemoteEndpointDetail.md)

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
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_ipsec_endpoint_tunnel**
> object post_create_ipsec_endpoint_tunnel(create_ipsec_tunnel_request)



Create IPsec endpoint tunnel

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
create_ipsec_tunnel_request = cohesivenet.CreateIpsecTunnelRequest() # CreateIpsecTunnelRequest | 

try:
    api_response = api_instance.post_create_ipsec_endpoint_tunnel(create_ipsec_tunnel_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_create_ipsec_endpoint_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ipsec_tunnel_request** | [**CreateIpsecTunnelRequest**](CreateIpsecTunnelRequest.md)|  | 

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
**200** | Created |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**403** | Permission denied. Max number of tunnels reach |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_restart_ipsec_action**
> RestartStatus post_restart_ipsec_action(restart_request)



Restart ipsec subystem

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
restart_request = cohesivenet.RestartRequest() # RestartRequest | 

try:
    api_response = api_instance.post_restart_ipsec_action(restart_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->post_restart_ipsec_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restart_request** | [**RestartRequest**](RestartRequest.md)|  | 

### Return type

[**RestartStatus**](RestartStatus.md)

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

# **put_edit_ipsec_endpoint**
> object put_edit_ipsec_endpoint(update_ipsec_connection_request)



Edit IPsec connection

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
update_ipsec_connection_request = cohesivenet.UpdateIpsecConnectionRequest() # UpdateIpsecConnectionRequest | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint(update_ipsec_connection_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_edit_ipsec_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_ipsec_connection_request** | [**UpdateIpsecConnectionRequest**](UpdateIpsecConnectionRequest.md)|  | 

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

# **put_edit_ipsec_endpoint_tunnel**
> IpsecTunnelDetail put_edit_ipsec_endpoint_tunnel(tunnel_id, update_ipsec_tunnel_request)



Edit IPsec endpoint tunnel

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
tunnel_id = 56 # int | ID for tunnel
update_ipsec_tunnel_request = cohesivenet.UpdateIpsecTunnelRequest() # UpdateIpsecTunnelRequest | 

try:
    api_response = api_instance.put_edit_ipsec_endpoint_tunnel(tunnel_id, update_ipsec_tunnel_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_edit_ipsec_endpoint_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tunnel_id** | **int**| ID for tunnel | 
 **update_ipsec_tunnel_request** | [**UpdateIpsecTunnelRequest**](UpdateIpsecTunnelRequest.md)|  | 

### Return type

[**IpsecTunnelDetail**](IpsecTunnelDetail.md)

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

# **put_ipsec_config**
> object put_ipsec_config(update_ipsec_address_request)



Edit Ipsec Configuration on device. Note, This is device wide and must be set before  any remote endpoint definitions are created. If it needs to be changed, all remote endpoint  information and tunnel information must be deleted first. 

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
api_instance = cohesivenet.IPsecApi(cohesivenet.VNS3Client(configuration))
update_ipsec_address_request = cohesivenet.UpdateIpsecAddressRequest() # UpdateIpsecAddressRequest | 

try:
    api_response = api_instance.put_ipsec_config(update_ipsec_address_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecApi->put_ipsec_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_ipsec_address_request** | [**UpdateIpsecAddressRequest**](UpdateIpsecAddressRequest.md)|  | 

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

