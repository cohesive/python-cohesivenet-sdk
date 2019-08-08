# vns3api.FirewallApi

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
[**post_create_firewall_fw_set**](FirewallApi.md#post_create_firewall_fw_set) | **POST** /firewall/fwsets | 
[**post_create_firewall_rule**](FirewallApi.md#post_create_firewall_rule) | **POST** /firewall/rules | 
[**post_create_firewall_subgroup_rule**](FirewallApi.md#post_create_firewall_subgroup_rule) | **POST** /firewall/rules/subgroup | 
[**put_reinitialize_fw_sets**](FirewallApi.md#put_reinitialize_fw_sets) | **PUT** /firewall/fwsets | 
[**put_reinitialize_subgroups**](FirewallApi.md#put_reinitialize_subgroups) | **PUT** /firewall/rules/subgroup | 


# **delete_firewall_fw_set**
> InlineResponse20054 delete_firewall_fw_set(inline_object41)



Delete Firewall FWSet by name or rules

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object41 = vns3api.InlineObject41() # InlineObject41 | 

try:
    api_response = api_instance.delete_firewall_fw_set(inline_object41)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_fw_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object41** | [**InlineObject41**](InlineObject41.md)|  | 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

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

# **delete_firewall_rule_by_position**
> InlineResponse20050 delete_firewall_rule_by_position(position)



Delete Firewall Rule

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
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

[**InlineResponse20050**](InlineResponse20050.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_rule_by_rule**
> InlineResponse20049 delete_firewall_rule_by_rule(inline_object35)



Delete firewall rule

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object35 = vns3api.InlineObject35() # InlineObject35 | 

try:
    api_response = api_instance.delete_firewall_rule_by_rule(inline_object35)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_rule_by_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object35** | [**InlineObject35**](InlineObject35.md)|  | 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_subgroup**
> InlineResponse20052 delete_firewall_subgroup(inline_object38)



Delete Firewall subgroup by name or rules

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object38 = vns3api.InlineObject38() # InlineObject38 | 

try:
    api_response = api_instance.delete_firewall_subgroup(inline_object38)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_subgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object38** | [**InlineObject38**](InlineObject38.md)|  | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

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
**410** | Resource gone |  -  |
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_fw_sets**
> InlineResponse20053 get_firewall_fw_sets(name=name, verbose=verbose)



Get a list of current firewall rule sets. These are IPsets that allow for faster matching of rules against IPs.  See http://ipset.netfilter.org for more details. 

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
name = 'name_example' # str | name of subgroup (optional)
verbose = True # bool | True for verbose output on firewall fwsets (optional) (default to True)

try:
    api_response = api_instance.get_firewall_fw_sets(name=name, verbose=verbose)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_fw_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of subgroup | [optional] 
 **verbose** | **bool**| True for verbose output on firewall fwsets | [optional] [default to True]

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

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

# **get_firewall_rule_subgroups**
> InlineResponse20051 get_firewall_rule_subgroups(name=name, verbose=verbose)



Get a list of current firewall rules at subgroup (chained rules)

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
name = 'name_example' # str | name of subgroup (optional)
verbose = True # bool | True for verbose output on firewall rules subgroup (optional) (default to True)

try:
    api_response = api_instance.get_firewall_rule_subgroups(name=name, verbose=verbose)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_rule_subgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of subgroup | [optional] 
 **verbose** | **bool**| True for verbose output on firewall rules subgroup | [optional] [default to True]

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

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

# **get_firewall_rules**
> InlineResponse20047 get_firewall_rules()



Get a list of current firewall rules

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))

try:
    api_response = api_instance.get_firewall_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->get_firewall_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

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

# **post_create_firewall_fw_set**
> OneOfarrayobject post_create_firewall_fw_set(inline_object40)



Create a new firewall FWSet for fast rule matching

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object40 = vns3api.InlineObject40() # InlineObject40 | 

try:
    api_response = api_instance.post_create_firewall_fw_set(inline_object40)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_fw_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object40** | [**InlineObject40**](InlineObject40.md)|  | 

### Return type

[**OneOfarrayobject**](OneOfarrayobject.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_firewall_rule**
> InlineResponse20048 post_create_firewall_rule(inline_object34)



Adds a firewall rule to the VNS3 Controller's firewall

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object34 = vns3api.InlineObject34() # InlineObject34 | 

try:
    api_response = api_instance.post_create_firewall_rule(inline_object34)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object34** | [**InlineObject34**](InlineObject34.md)|  | 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_firewall_subgroup_rule**
> OneOfarrayobject post_create_firewall_subgroup_rule(inline_object37)



Create a new firewall subgroup rules (rule chain)

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object37 = vns3api.InlineObject37() # InlineObject37 | 

try:
    api_response = api_instance.post_create_firewall_subgroup_rule(inline_object37)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_subgroup_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object37** | [**InlineObject37**](InlineObject37.md)|  | 

### Return type

[**OneOfarrayobject**](OneOfarrayobject.md)

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
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reinitialize_fw_sets**
> put_reinitialize_fw_sets(inline_object39)



Reinitialize all Firewall FWSet

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object39 = vns3api.InlineObject39() # InlineObject39 | 

try:
    api_instance.put_reinitialize_fw_sets(inline_object39)
except ApiException as e:
    print("Exception when calling FirewallApi->put_reinitialize_fw_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object39** | [**InlineObject39**](InlineObject39.md)|  | 

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
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reinitialize_subgroups**
> put_reinitialize_subgroups(inline_object36)



Reinitialize Firewall subgroups

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
api_instance = vns3api.FirewallApi(vns3api.ApiClient(configuration))
inline_object36 = vns3api.InlineObject36() # InlineObject36 | 

try:
    api_instance.put_reinitialize_subgroups(inline_object36)
except ApiException as e:
    print("Exception when calling FirewallApi->put_reinitialize_subgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object36** | [**InlineObject36**](InlineObject36.md)|  | 

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
**401** | Authentication information missing or invalid |  -  |
**403** | Operation not allowed |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

