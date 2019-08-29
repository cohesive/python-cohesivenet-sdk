# Python VNS3 API Client
The Python vns3api client is a client sdk for interfacing with the VNS3 API on Python 3.6 and above, proving programatic control your network's addresses, routes, rules and edge.

## Requirements.

Python 3.6+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import vns3api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import vns3api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = vns3api.BGPApi(vns3api.ApiClient(configuration))
endpoint_id = 56 # int | numerical ID for IPsec endpoint
bgp_peer_id = 56 # int | numerical ID for BGP peer

try:
    api_response = api_instance.delete_ipsec_endpoint_bgp_peer(endpoint_id, bgp_peer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BGPApi->delete_ipsec_endpoint_bgp_peer: %s\n" % e)

```
## [Endpoints](./endpoints.md)

## Documentation For Authorization

## basicAuth

- **Type**: HTTP basic authentication


## Author

solutions@cohesive.net


