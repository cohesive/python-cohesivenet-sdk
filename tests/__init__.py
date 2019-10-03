import collections

TypeInfo = collections.namedtuple('TypeSchema', 'type allow_none required')

def example():
    expected_types = {
        'asn': TypeInfo(type=int, allow_none=True, required=True),
        'topology_name': TypeInfo(type=str, allow_none=True, required=True),
        'topology_checksum': TypeInfo(type=str, allow_none=False, required=True),
        'manager_id': TypeInfo(type=int, allow_none=True, required=True),
        'ntp_hosts': TypeInfo(type=str, allow_none=False, required=True),
        'vns3_version': TypeInfo(type=str, allow_none=False, required=True),
        'licensed': TypeInfo(type=bool, allow_none=False, required=True),
        'overlay_ipaddress': TypeInfo(type=str, allow_none=True, required=True),
        'peered': TypeInfo(type=bool, allow_none=True, required=True),
        'public_ipaddress': TypeInfo(type=str, allow_none=True, required=True),
        'private_ipaddress': TypeInfo(type=str, allow_none=False, required=True),
        'security_token': TypeInfo(type=str, allow_none=True, required=True),
    }


def assert_types(response_dict, types_dict):
    """Assert on types for dictionary or raise Assertion error
    
    Arguments:
        response_dict {dict}
        types_dict {dict} -- str -> TypeInfo
    
    Returns:
        [bool|Exception]
    """
    required_keys = set([k for k, type_info in types_dict.items() if type_info.required])
    response_keys = set(response_dict.keys())
    missing_keys = required_keys.difference(response_keys)
    assert not missing_keys, 'Missing required keys: %s' % ','.join([str(k) for k in missing_keys])
    # assert on each type
    type_errors = []
    for key, val in response_dict.items():
        val_type_info = types_dict[key]
        if val is None:
            if not val_type_info.allow_none:
                type_errors.append('Invalid None value for "%s"' % key)
            continue
        if not isinstance(val, val_type_info.type):
            type_errors.append(
                'Invalid type for "%s". Must be "%s" but was "%s"' % (key, val_type_info.type, type(val)))
        
    assert not type_errors, 'Type Errors: %s' % ','.join(type_errors)
    return True
