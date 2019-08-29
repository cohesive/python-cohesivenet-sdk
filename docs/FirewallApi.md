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
> InlineResponse20040 delete_firewall_fw_set(inline_object28)



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
inline_object28 = vns3api.InlineObject28() # InlineObject28 | 

try:
    api_response = api_instance.delete_firewall_fw_set(inline_object28)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_fw_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object28** | [**InlineObject28**](InlineObject28.md)|  | 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

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
> InlineResponse20036 delete_firewall_rule_by_position(position)



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

[**InlineResponse20036**](InlineResponse20036.md)

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
> InlineResponse20035 delete_firewall_rule_by_rule(inline_object22)



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
inline_object22 = vns3api.InlineObject22() # InlineObject22 | 

try:
    api_response = api_instance.delete_firewall_rule_by_rule(inline_object22)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_rule_by_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object22** | [**InlineObject22**](InlineObject22.md)|  | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

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
> InlineResponse20038 delete_firewall_subgroup(inline_object25)



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
inline_object25 = vns3api.InlineObject25() # InlineObject25 | 

try:
    api_response = api_instance.delete_firewall_subgroup(inline_object25)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->delete_firewall_subgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object25** | [**InlineObject25**](InlineObject25.md)|  | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

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
**404** | Not found |  -  |
**410** | Resource gone |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_fw_sets**
> InlineResponse20039 get_firewall_fw_sets(name=name, verbose=verbose)



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

[**InlineResponse20039**](InlineResponse20039.md)

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
> InlineResponse20037 get_firewall_rule_subgroups(name=name, verbose=verbose)



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

[**InlineResponse20037**](InlineResponse20037.md)

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
> InlineResponse20033 get_firewall_rules()



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

[**InlineResponse20033**](InlineResponse20033.md)

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
> OneOfarrayobject post_create_firewall_fw_set(inline_object27)



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
inline_object27 = vns3api.InlineObject27() # InlineObject27 | 

try:
    api_response = api_instance.post_create_firewall_fw_set(inline_object27)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_fw_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object27** | [**InlineObject27**](InlineObject27.md)|  | 

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
> InlineResponse20034 post_create_firewall_rule(inline_object21)



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
inline_object21 = vns3api.InlineObject21() # InlineObject21 | 

try:
    api_response = api_instance.post_create_firewall_rule(inline_object21)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object21** | [**InlineObject21**](InlineObject21.md)|  | 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

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
> OneOfarrayobject post_create_firewall_subgroup_rule(inline_object24)



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
inline_object24 = vns3api.InlineObject24() # InlineObject24 | 

try:
    api_response = api_instance.post_create_firewall_subgroup_rule(inline_object24)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirewallApi->post_create_firewall_subgroup_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object24** | [**InlineObject24**](InlineObject24.md)|  | 

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
> put_reinitialize_fw_sets(inline_object26)



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
inline_object26 = vns3api.InlineObject26() # InlineObject26 | 

try:
    api_instance.put_reinitialize_fw_sets(inline_object26)
except ApiException as e:
    print("Exception when calling FirewallApi->put_reinitialize_fw_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object26** | [**InlineObject26**](InlineObject26.md)|  | 

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
> put_reinitialize_subgroups(inline_object23)



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
inline_object23 = vns3api.InlineObject23() # InlineObject23 | 

try:
    api_instance.put_reinitialize_subgroups(inline_object23)
except ApiException as e:
    print("Exception when calling FirewallApi->put_reinitialize_subgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object23** | [**InlineObject23**](InlineObject23.md)|  | 

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

