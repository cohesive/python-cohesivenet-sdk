# Python cohesivenet
Cohesive Networks SDK is a wrapper around our product APIs providing complete control of your network's addresses, routes, rules and edge

[![contact][contact-image]][contact-url]


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 4.8
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/cohesive/python-cohesivenet-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/cohesive/python-cohesivenet-sdk.git`)

Then import the package:
```python
import cohesivenet 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cohesivenet
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
configuration.host = "https://vns3-host:8000/api"
# Create an instance of the API class
vns3_controller = cohesivenet.VNS3Client(configuration)

try:
    api_response = vns3_controller.ipsec.delete_ipsec_endpoint(10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecAPI->delete_ipsec_endpoint: %s\n" % e)

```

## Documentation For Authorization

## basicAuth

- **Type**: HTTP basic authentication

## Author

solutions@cohesive.net

<!-- Markdown links -->

[contact-image]: https://img.shields.io/badge/contact-support-green.svg
[contact-url]: https://support.cohesive.net/support/home