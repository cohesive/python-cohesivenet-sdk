# cohesivenet.FirewallApi

All URIs are relative to *https://vns3-host:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_firewall_fw_set**](FirewallApi.md#delete_firewall_fw_set) | **DELETE** /firewall/fwsets | 
[**delete_firewall_rule_by_position**](FirewallApi.md#delete_firewall_rule_by_position) | **DELETE** /firewall/rules/{position} | 
[**delete_firewall_rule_by_rule**](FirewallApi.md#delete_firewall_rule_by_rule) | **DELETE** /firewall/rules | 
[**delete_firewall_subgroup**](FirewallApi.md#delete_firewall_subgroup) | **DELETE** /firewall/rules/subgroup | 
[**get_firewall_fw_sets**](FirewallApi.md#get_firewall_fw_sets) | **GET** /firewall/fwsets | 
[**get_firewall_rule_subgroups**](FirewallApi.md#get_firewall_rule_subgroups) | **GET** /firewall/rules/subgroup | 
[**get_firewall_rules**](FirewallApi.md#get_firewall_rules) | **GET** /firewall/rules | 
[**post_create_firewall_rule**](FirewallApi.md#post_create_firewall_rule) | **POST** /firewall/rules | 
[**post_create_firewall_subgroup_rule**](FirewallApi.md#post_create_firewall_subgroup_rule) | **POST** /firewall/rules/subgroup | 
[**put_reinitialize_fw_sets**](FirewallApi.md#put_reinitialize_fw_sets) | **PUT** /firewall/fwsets | 
[**put_reinitialize_subgroups**](FirewallApi.md#put_reinitialize_subgroups) | **PUT** /firewall/rules/subgroup | 


# **delete_firewall_fw_set**
> object delete_firewall_fw_set(body)



Delete Firewall FWSet by name or rules

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
body = None # object | 

try:
    api_response = api_instance.delete_firewall_fw_set(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_fw_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_rule_by_position**
> object delete_firewall_rule_by_position(position)



Delete Firewall Rule

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
position = 56 # int | index position for firewall rule, 0 is first

try:
    api_response = api_instance.delete_firewall_rule_by_position(position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_rule_by_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **int**| index position for firewall rule, 0 is first | 

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_rule_by_rule**
> object delete_firewall_rule_by_rule(delete_firewall_rule_request)



Delete firewall rule

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
delete_firewall_rule_request = cohesivenet.DeleteFirewallRuleRequest() # DeleteFirewallRuleRequest | 

try:
    api_response = api_instance.delete_firewall_rule_by_rule(delete_firewall_rule_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_rule_by_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_firewall_rule_request** | [**DeleteFirewallRuleRequest**](DeleteFirewallRuleRequest.md)|  | 

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_subgroup**
> object delete_firewall_subgroup(firewall_fw_set)



Delete Firewall subgroup by name or rules

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
firewall_fw_set = cohesivenet.FirewallFWSet() # FirewallFWSet | 

try:
    api_response = api_instance.delete_firewall_subgroup(firewall_fw_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_subgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_fw_set** | [**FirewallFWSet**](FirewallFWSet.md)|  | 

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
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**404** | Not found |  -  |
**410** | Resource gone |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_fw_sets**
> FirewallFWSetListResponse get_firewall_fw_sets()



Get a list of current firewall rule sets. These are IPsets that allow for faster matching of rules against IPs.  See http://ipset.netfilter.org for more details. 

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_firewall_fw_sets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_fw_sets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FirewallFWSetListResponse**](FirewallFWSetListResponse.md)

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

# **get_firewall_rule_subgroups**
> FirewallSubgroupListResponse get_firewall_rule_subgroups(name=name, verbose=verbose)



Get a list of current firewall rules at subgroup (chained rules)

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
name = 'name_example' # str | name of resource (optional)
verbose = True # bool | True for verbose output (optional) (default to True)

try:
    api_response = api_instance.get_firewall_rule_subgroups(name=name, verbose=verbose)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_rule_subgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of resource | [optional] 
 **verbose** | **bool**| True for verbose output | [optional] [default to True]

### Return type

[**FirewallSubgroupListResponse**](FirewallSubgroupListResponse.md)

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

# **get_firewall_rules**
> FirewallRuleListResponse get_firewall_rules()



Get a list of current firewall rules

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))

try:
    api_response = api_instance.get_firewall_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FirewallRuleListResponse**](FirewallRuleListResponse.md)

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

# **post_create_firewall_rule**
> FirewallRuleOperationResponse post_create_firewall_rule(create_firewall_rule_request)



Adds a firewall rule to the VNS3 Controller's firewall

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
create_firewall_rule_request = cohesivenet.CreateFirewallRuleRequest() # CreateFirewallRuleRequest | 

try:
    api_response = api_instance.post_create_firewall_rule(create_firewall_rule_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_firewall_rule_request** | [**CreateFirewallRuleRequest**](CreateFirewallRuleRequest.md)|  | 

### Return type

[**FirewallRuleOperationResponse**](FirewallRuleOperationResponse.md)

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_firewall_subgroup_rule**
> OneOfobjectobject post_create_firewall_subgroup_rule(create_fw_subgroup_request)



Create a new firewall subgroup rules (rule chain)

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
create_fw_subgroup_request = cohesivenet.CreateFWSubgroupRequest() # CreateFWSubgroupRequest | 

try:
    api_response = api_instance.post_create_firewall_subgroup_rule(create_fw_subgroup_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_subgroup_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_fw_subgroup_request** | [**CreateFWSubgroupRequest**](CreateFWSubgroupRequest.md)|  | 

### Return type

[**OneOfobjectobject**](OneOfobjectobject.md)

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
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reinitialize_fw_sets**
> put_reinitialize_fw_sets(reinit_firewall_request)



Reinitialize all Firewall FWSet

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
reinit_firewall_request = cohesivenet.ReinitFirewallRequest() # ReinitFirewallRequest | 

try:
    api_instance.put_reinitialize_fw_sets(reinit_firewall_request)
except ApiException as e:
    print("Exception when calling FirewallApi->put_reinitialize_fw_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reinit_firewall_request** | [**ReinitFirewallRequest**](ReinitFirewallRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reinitialize_subgroups**
> put_reinitialize_subgroups(reinit_request)



Reinitialize Firewall subgroups

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
api_instance = cohesivenet.FirewallApi(cohesivenet.VNS3Client(configuration))
reinit_request = cohesivenet.ReinitRequest() # ReinitRequest | 

try:
    api_instance.put_reinitialize_subgroups(reinit_request)
except ApiException as e:
    print("Exception when calling FirewallApi->put_reinitialize_subgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reinit_request** | [**ReinitRequest**](ReinitRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** |  |  -  |
**403** | Request Forbidden - operation not allowed |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

