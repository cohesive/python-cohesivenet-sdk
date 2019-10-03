# Python Cohesive Networks SDK
[![contact][contact-image]][contact-url]
Cohesive Networks SDK is Python tool providing access to the VNS3 API from applications written in Python. It also includes common pipelines and macro functions
for building network topologies.

VNS3 API version: [4.8](https://github.com/cohesive/cohesive-api-specs/blob/master/vns3/vns3-v48-api/spec.yaml)

## Installation

You can PIP install with

```sh
pip install cohesivenet
```
(you may need to run `pip` with root permission: `sudo pip install cohesivenet`)

or Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

## Usage
View all endpoints [documented here](./endpoints.md)

### Configuring a Client

### IPsec Configuration

### Overlay Networking Configuration

### Policy Firewall and Routing

### Alerting
Define and retrieve alerts from VNS3. Alerts can be configured to send to 
Slack, Ops Genie, ... EDIT ME, or any any webhook endpoint for your monitoring systems

### Network Edge Plugins 
Want to run a proxy on your network edge? Or maybe some network intrusion detection? The VNS3 Plugin system allows you to 
easily plug in a container with privileged access to VNS3 runtime and interfaces.

### System Administration

```python
import time
import cohesivenet
from cohesivenet.rest import ApiException
from pprint import pprint

configuration = cohesivenet.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'api'
configuration.password = 'YOUR_PASSWORD'
configuration.host = "https://[vns3-host]:8000"
# Create an instance of the API class
vns3_controller = cohesivenet.VNS3Client(configuration)

try:
    api_response = vns3_controller.ipsec.delete_ipsec_endpoint(10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPsecAPI->delete_ipsec_endpoint: %s\n" % e)

```

## Author

solutions@cohesive.net

<!-- Markdown links -->

[contact-image]: https://img.shields.io/badge/contact-support-blue.svg?style=flat-square
[contact-url]: https://support.cohesive.net/support/home
