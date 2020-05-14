

class AccessApiData(object):
    TokenResponse = {
        "api_token": "f76a2cb3ca8107ba0aaa0394ca929cd622580938"
    }

    ExpireTokenResponse = {
        "response_type": "success",
        "response": {
            "message": "Successfully expired token"
        }
    }

    ApiKeysResponse = {
        "response_type": "success",
        "response":[{
            "id":3,
            "name": "default",
            "enabled":True,
            "created_at":"2020-05-06T19:02:40.000Z",
            "default_key":False,
            "active_tokens":1,
            "expired_tokens":7,
            "last_access_time":"2020-05-12T22:43:13.000Z",
            "last_access_ip":"54.236.197.84"
        }]
    }

    ExpireKeyTokens = {
        "response_type":"success",
        "response": {
            "message": "Invalidated 1 tokens",
            "name":"test",
            "id":2,
            "enabled": True,
            "active_tokens": 0
        }
    }

    NewApiKeyResponse = {
        "response_type": "success",
        "response": {
            "message": "Key created",
            "name": "api-created-new-again",
            "api_key": "4f00ac88739f00dbb8fd3b878a96d9e94aeae3b6a0b0048fd8427d5eee722b70c85c72de2f91331c18c90e90befd54e03b600efe1aa9c21e699256be87b9f9ef",
            "id":4,
            "active_tokens":0,
            "enabled": True
        }
    }

    ApiKeyUpdatedResponse = {
        "response_type":"success",
        "response":{
            "message":"Key updated",
            "name":"test-updated",
            "id":2,
            "enabled":True,
            "active_tokens":1
        }
    }


class AdminApiData(object):
    LdapSettingsResponse = {
        "response_type":"success",
        "response":{
            "ldap_host":None,
            "ldap_port":None,
            "ldap_ssl":None,
            "ldap_binddn":None,
            "ldap_bindpw":None
        }
    }

    LdapUserSchemaResponse = {
        "response_type":"success",
        "response": {
            "ldap_user_base":"DN",
            "ldap_user_id_attribute":"1",
            "ldap_user_list_filter":"subtree"
        }
    }

    LdapGroupSchemaResponse = {
        "response_type":"success",
        "response":{
            "ldap_group_required":True,
            "ldap_group_base":"vns3admin",
            "ldap_group_id_attribute":"fact",
            "ldap_group_list_filter":None,
            "ldap_group_member_attribute":"again",
            "ldap_group_member_attr_format":"UserDN",
            "ldap_search_scope": "subtree"
        }
    }


class BackupsApiData(object):
    CreateBackupResponse = {
        "response_type":"success",
        "response":{
            "status":"Backup process queued",
            "uuid":"ce81bb5b-a917-49c7-8efd-d97d158d31fe"
        }
    }

    BackupJobStatusResponse = {
        "response_type":"success",
        "response":{
            "uuid":"ce81bb5b-a917-49c7-8efd-d97d158d31fe",
            "status":"Queued",
            "filename":""
        }
    }


class CloudMonitoringApiData(object):
    CreateVirtualNetworkResponse = {
        "response_type":"success",
        "response":{
            "msg":"Virtual Network created","id":1
        }
    }

    VirtualNetworkDetail = {
        "response":{
            "id":1,
            "name":"dev-env-network",
            "description":"test environment",
            "created_at":"2020-05-13T16:57:09.000Z"
        }
    }

    CreateVns3TopologyResponse = {
        "response_type":"success",
        "response":{
            "msg":"VNS3 Topology created",
            "id":1
        }
    }


class SystemApiData(object):
    SystemStatusResponse = {
        "response_type":"success",
        "response":{
            "system_disk":{
                "type":None,
                "block_size":4096,
                "free_blocks":6029874,
                "available_blocks":5636673,
                "total_blocks":7707903
            },
            "data_disk":{
                "type":"ext4",
                "block_size":4096,
                "free_blocks":6029874,
                "available_blocks":5636673,
                "total_blocks":7707903
            },"cpus":[{
                "num":0,
                "user":17830,
                "system":9350,
                "nice":28,
                "idle":6266562
            },{
                "num":1,
                "user":19990,
                "system":9396,
                "nice":31,
                "idle":6268907
            }],
            "load_average":{
                "one_minute":0.07,
                "five_minutes":0.03,
                "fifteen_minutes":0.01
            },
            "memory":{
                "pagesize":4096,
                "wired":77154,
                "active":285876,
                "inactive":115567,
                "free":23746,
                "pageins":1415297,
                "pageouts":5674892
            },
            "boot_time":"2020-05-12T23:38:54.871Z",
            "system_time":"2020-05-13T17:20:03.431Z",
            "uptime":63668.559935987,
            "virtual_networks":1,
            "vns3_topologies":0,
            "vns3_controllers":0,
            "cloud_vlans":0,
            "cloud_vlan_components":0,
            "ha_snapshot_file_count":0,
            "configuration_snapshot_file_count":0,
            "configuration_snapshot_failed_count":0,
            "system_backup_file_count":0,
            "system_snapshots_backup_file_count":0
        }
    }

    NTPHosts = {
        "response_type": "success",
        "response": {
            "0": "0.ubuntu.pool.ntp.org",
            "1": "1.ubuntu.pool.ntp.org",
            "2": "2.ubuntu.pool.ntp.org",
            "3": "3.ubuntu.pool.ntp.org",
            "4": "ntp.ubuntu.com"
        }
    }


class Vns3ManagementApiData(object):
    CreateVns3ControllerResponse = {
        "response_type":"success",
        "response":{
            "msg":"VNS3 Controller created",
            "id":1
        }
    }