# Python Cohesive Networks SDK
[![contact][contact-image]][contact-url]

Cohesive Networks SDK is Python tool providing access to the VNS3 API from applications written in Python. It also includes common pipelines and macro functions
for building network topologies.

## API Versions supported
The SDK will make best efforts to always be backwards compatible. All SDK releases will support all VNS3 versions starting with VNS3 v4.8.4 up to the latest VNS3 version.

| cohesivenet==X |    VNS3 API    |     MS API     |
|----------------|:--------------:|:--------------:|
|     0.1.0-31   |      4.8.4     |       N/A      |    # MS SDK not implemented
    

View [VNS3 API specifications](docs.cohesivenet.)
[VNS3 API specs](https://github.com/cohesive/cohesive-api-specs/blob/master/vns3/vns3-v48-api/spec.yaml)

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

### Configuring a Client

```python
import cohesivenet
from pprint import pprint

configuration = cohesivenet.Configuration(
    host='https://[vns3-host]:8000',
    username='api',         
    password='YOUR_PASSWORD',
    verify_ssl=False) # Local cert is used by default. Can add your own cert.
# Configure HTTP basic authorization: basicAuth
configuration.username = 'api'
configuration.password = 'YOUR_PASSWORD'
configuration.host = "https://[vns3-host]:8000"
# Create an instance of the API class
vns3_controller = cohesivenet.VNS3Client(configuration)

try:
    api_response = vns3_controller.config.get_config()
    pprint(api_response)
except cohesivenet.ApiException as e:
    print("Exception fetching VNS3 Configuration get_config(): %s\n" % e)

# OR
from cohesivenet.macros import connect as vns3_connect

vns3_host = "55.55.55.55:8000"
api_user = "api"
api_ps = "test1234"
vns3 = vns3_connect.get_client(vns3_host, api_user, api_ps)
config = vns3.config.get_config()
print(config.response)
```

### Methods
All endpoints are documented [here](https://github.com/cohesive/python-cohesivenet-sdk/blob/master/endpoints.md). Each sub-api is available from the VNS3Client instance as follows:

```python

vns3_client.access                # Manage access urls and api tokens
vns3_client.bgp                   # BGPApi for Border Gateway Protocol methods
vns3_client.config                # ConfigurationApi provides VNS3 config methods
vns3_client.firewall              # FirewallApi for configuring VNS3 policies
vns3_client.ipsec                 # IPsecApi for IPsec tunnel methods
vns3_client.interfaces            # InterfacesApi for viewing VNS3 interfaces
vns3_client.monitoring            # MonitoringAlertingApi
vns3_client.network_edge_plugins  # NetworkEdgePluginsApi
vns3_client.overlay_network       # OverlayNetworkApi for managing the overlay network
vns3_client.peering               # PeeringApi for peering VNS3 controllers
vns3_client.routing               # RoutingApi for configuring routing
vns3_client.snapshots             # SnapshotsApi for managing backups
vns3_client.sys_admin             # SystemAdministrationApi for access and sys admin tasks
vns3_client.licensing             # LicensingApi for controller licensing 
```

### Common API patterns: `cohesivenet.macros`
Many API calls are called together to configure a topology or update a network configuration. More macros will be added to 
increasingly simplify VNS3 topology creation and configuration. More documentation to come.

```python
macros.admin                  # Admin operations typically applied to multiple controllers at once
macros.config                 # configuring multiple clients
macros.connect                # connecting to clients
macros.firewall               # firewall operations like idempotently creating full firewall
macros.ipsec                  # ipsec operations like creating a tunnel and then a route
macros.network_edge_plugins   # Manage container system network, images and running containers
macros.overlay_network        # overlay network functions like calculating network segments of the overlay
macros.peering                # topology peering operations like creating a peering mesh between controllers
macros.routing                # Operations for updating routing in your topology
macros.state                  # Methods for fetching the state of your controller(s)
```

### Logging
The SDK can be configured to emit logs for better visibility into what it's doing. The SDK supports INFO, DEBUG, and ERROR logging.

There are two ways to enable it:

1. Set the environment variable `COHESIVE_LOG_LEVEL` to the value `debug`, `info` or `error`

   ```sh
   $ export COHESIVE_LOG_LEVEL=debug
   ```

2. Enable it through Python's logging module:

   ```python
   import logging
   logging.basicConfig()
   logging.getLogger('cohesivenet').setLevel(logging.DEBUG)
   ```

## Author

solutions@cohesive.net

<!-- Markdown links -->

[contact-image]: https://img.shields.io/badge/contact-support-blue.svg?style=flat-square
[contact-url]: https://support.cohesive.net/support/home
