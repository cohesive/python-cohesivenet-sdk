# cohesivenet.PeeringApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_peer**](PeeringApi.md#delete_peer) | **DELETE** /peering/peers/{peer_id} | 
[**get_peering_status**](PeeringApi.md#get_peering_status) | **GET** /peering | 
[**post_peer**](PeeringApi.md#post_peer) | **POST** /peering/peers | 
[**put_peer**](PeeringApi.md#put_peer) | **PUT** /peering/peers | 
[**put_reconfigure_peers**](PeeringApi.md#put_reconfigure_peers) | **PUT** /peering | 
[**put_self_peering_id**](PeeringApi.md#put_self_peering_id) | **PUT** /peering/self | 


# **delete_peer**
> object delete_peer(peer_id)



Breaks a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to  fully break the peer relationship. 

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
api_instance = cohesivenet.PeeringApi(cohesivenet.VNS3Client(configuration))
peer_id = 56 # int | Peer ID for controller peer

try:
    api_response = api_instance.delete_peer(peer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->delete_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_id** | **int**| Peer ID for controller peer | 

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
**200** | Delete Accepted |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peering_status**
> PeersDetailResponse get_peering_status()



Provides the status of whether a Controller is peered to other Controllers

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
api_instance = cohesivenet.PeeringApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_peering_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->get_peering_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PeersDetailResponse**](PeersDetailResponse.md)

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

# **post_peer**
> object post_peer(create_peer_request)



Creates a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process. 

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
api_instance = cohesivenet.PeeringApi(cohesivenet.VNS3Client(configuration))
create_peer_request = cohesivenet.CreatePeerRequest() # CreatePeerRequest | 

try:
    api_response = api_instance.post_peer(create_peer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->post_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_peer_request** | [**CreatePeerRequest**](CreatePeerRequest.md)|  | 

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
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_peer**
> object put_peer(update_peer_request)



Edits a peering relationship from a manager to another manager.  The peering call is unidirectional. Reciprocal calls must be made to peer two controllers  together and complete the peering process. 

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
api_instance = cohesivenet.PeeringApi(cohesivenet.VNS3Client(configuration))
update_peer_request = cohesivenet.UpdatePeerRequest() # UpdatePeerRequest | 

try:
    api_response = api_instance.put_peer(update_peer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_peer_request** | [**UpdatePeerRequest**](UpdatePeerRequest.md)|  | 

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
**200** | Updated |  -  |
**400** | Bad request |  -  |
**401** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reconfigure_peers**
> object put_reconfigure_peers(configure_peer_request)



Reconfigure peered controllers

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
api_instance = cohesivenet.PeeringApi(cohesivenet.VNS3Client(configuration))
configure_peer_request = cohesivenet.ConfigurePeerRequest() # ConfigurePeerRequest | 

try:
    api_response = api_instance.put_reconfigure_peers(configure_peer_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_reconfigure_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_peer_request** | [**ConfigurePeerRequest**](ConfigurePeerRequest.md)|  | 

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

# **put_self_peering_id**
> object put_self_peering_id(peer_self_request)



Sets the Controller ID of a controller so that it can be peered within a topology

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
api_instance = cohesivenet.PeeringApi(cohesivenet.VNS3Client(configuration))
peer_self_request = cohesivenet.PeerSelfRequest() # PeerSelfRequest | 

try:
    api_response = api_instance.put_self_peering_id(peer_self_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeeringApi->put_self_peering_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_self_request** | [**PeerSelfRequest**](PeerSelfRequest.md)|  | 

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

