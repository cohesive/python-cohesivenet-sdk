from cohesivenet import util, Logger, VNS3Client, CohesiveSDKException, VNS3Client

def create_firewall_fwsets(clients, fwset_rules):
    results = {}
    for client in clients:
        successes = []
        errors = []
        
        existing_fwsets = client.firewall.get_firewall_fwsets().response
        existing_fwset_names = {fwset['name'] for fwset in existing_fwsets}
        
        for fwset in fwset_rules:
            name = fwset['name']
            fwset_type = fwset['type']
            
            if fwset_type == "clientpack_tag_group":
                target = fwset['target']
                fwset_data = {"target": target}
            else:
                entries = [{"entry": val} for val in fwset['entries']]
                fwset_data = {"entries": entries}
            
            if 'sync' in fwset:
                fwset_data['sync'] = fwset['sync']
            
            if name in existing_fwset_names:
                # Update existing fwset
                try:
                    client.firewall.put_update_firewall_fwset(
                        fwset_name=name,
                        **fwset_data
                    )
                    successes.append(f"Successfully updated fwset '{name}'")
                except Exception as e:
                    errors.append(f"Error updating fwset '{name}': {str(e)}")
            else:
                # Create new fwset
                try:
                    client.firewall.post_create_firewall_fwset(
                        name=name,
                        type=fwset_type,
                        **fwset_data
                    )
                    successes.append(f"Successfully created fwset '{name}'")
                except Exception as e:
                    errors.append(f"Error creating fwset '{name}': {str(e)}")
        
        # Delete fwsets that are not in the input list
        for existing_name in existing_fwset_names:
            if existing_name not in [fwset['name'] for fwset in fwset_rules]:
                try:
                    client.firewall.delete_firewall_fwset(fwset_name=existing_name)
                    successes.append(f"Successfully deleted fwset '{existing_name}'")
                except Exception as e:
                    errors.append(f"Error deleting fwset '{existing_name}': {str(e)}")

        results[client.host_uri] = (successes, errors)

    return results

def create_firewall_policies(clients, firewall_rules, state={}):
    """Create a group of firewall rules for multiple clients.

    Arguments:
        clients {List[VNS3Client]} - List of VNS3Client instances
        firewall_rules {List[dict]} - [{
            'position': int,
            'rule': str
        }, ...]

    Keyword Arguments:
        state {dict} - State to format rules with. (can call client.state for each client)

    Returns:
        dict: A dictionary with client host_uri as keys and tuples of successes and errors lists as values
    """
    results = {}
    for client in clients:
        successes, errors = [], []
        Logger.debug(
            "Checking firewall policy for client.",
            host=client.host_uri,
            rule_count=len(firewall_rules),
        )

        # Fetch current firewall rules from the client
        current_rules_response = client.firewall.get_firewall_rules()
        if hasattr(current_rules_response, 'response') and current_rules_response.response:
            current_rules = [rule['rule'].strip() for rule in current_rules_response.response if 'rule' in rule]
        else:
            current_rules = []
            errors.append(f"Failed to fetch current firewall rules for {client.host_uri}")

        # Format desired rules
        desired_rules = []
        for rule_args in firewall_rules:
            rule, err = util.format_string(rule_args["rule"], state)
            if err:
                errors.append(err)
                continue

            rule_args.update(rule=rule)
            desired_rules.append(rule_args)

        # Compare desired rules with current rules
        rules_to_add = []
        rules_to_delete = []
        for current_rule in current_rules:
            if current_rule not in [r['rule'] for r in desired_rules]:
                rules_to_delete.append(current_rule)

        for desired_rule in desired_rules:
            if desired_rule['rule'] not in current_rules:
                rules_to_add.append(desired_rule)

        # Delete rules that are not defined in firewall_rules
        for rule_to_delete in rules_to_delete:
            response = client.firewall.delete_firewall_rule_by_rule(rule=rule_to_delete)
            if hasattr(response, 'status') and response.status == 200:  # Assuming 'status' attribute and success code 200
                successes.append(f'Rule "{rule_to_delete}" deleted')
            else:
                errors.append(f'Error deleting rule "{rule_to_delete}"')

        # Add only the rules that are not already present
        for rule_args in rules_to_add:
            response = client.firewall.post_create_firewall_rule(rule=rule_args['rule'], position=rule_args['position'])
            if hasattr(response, 'status') and response.status == 200:  # Assuming 'status' attribute and success code 200
                successes.append(f'Rule "{rule_args["rule"]}" inserted at position {rule_args["position"]}')
            else:
                errors.append(f'Error inserting rule "{rule_args["rule"]}" at position {rule_args["position"]}')

        # Identify and delete duplicate rules
        current_rules_response = client.firewall.get_firewall_rules()
        if hasattr(current_rules_response, 'response') and current_rules_response.response:
            current_rules = current_rules_response.response
            seen_rules = set()
            for rule in current_rules:
                if 'rule' in rule:
                    rule_str = rule['rule'].strip()
                    if rule_str in seen_rules:
                        response = client.firewall.delete_firewall_rule_by_position(position=rule['position'])
                        if hasattr(response, 'status') and response.status == 200:  # Assuming 'status' attribute and success code 200
                            successes.append(f'Duplicate rule "{rule_str}" at position {rule["position"]} deleted')
                        else:
                            errors.append(f'Error deleting duplicate rule "{rule_str}" at position {rule["position"]}')
                    else:
                        seen_rules.add(rule_str)

        results[client.host_uri] = (successes, errors)

    return results

def create_firewall_policy(client: VNS3Client, firewall_rules, state={}):
    """Create group of firewall rules

    Arguments:
        client {VNS3Client}
        firewall_rules {List[CreateFirewallRuleRequest]} - [{
            'position': int,
            'rule': str
        }, ...]

    Keyword Arguments:
        state {dict} - State to format rules with. (can call client.state)

    Returns:
        Tuple[List[str], List[str]] - success, errors
    """
    successes = []
    errors = []
    Logger.debug(
        "Creating firewall policy.",
        host=client.host_uri,
        rule_count=len(firewall_rules),
    )
    for i, rule_args in enumerate(firewall_rules):
        rule, err = util.format_string(rule_args["rule"], state)
        if err:
            errors.append(err)
            continue

        rule_args.update(rule=rule)
        client.firewall.post_create_firewall_rule(**rule_args)
        successes.append(
            'Rule "%s" inserted at position %d' % (rule, rule_args["position"])
        )
    return successes, errors


def __construct_proposed_firewall_list(rule_args_list, state=None):
    _state = state or {}
    errors = []
    new_firewall = []
    for rule_args in rule_args_list:
        rule, err = util.format_string(rule_args["rule"], _state)
        if err:
            errors.append(err)
            continue

        position = rule_args.get("position", -1)
        if position == -1:
            new_firewall.append(rule)
        elif type(position) is int:
            new_firewall.insert(position, rule)
        else:
            errors.append("Rule position %s invalid. [RULE='%s']" % (position, rule))

    return new_firewall, errors


def __firewall_resp_to_list(firewall_raw_response):
    return [
        rule_tuple[0].strip()
        for rule_tuple in sorted(
            firewall_raw_response.response, key=lambda r: int(r[1])
        )
    ]


def assert_rule_policy(client: VNS3Client, rules, should_fix=False):
    """Assert rule policy contains expected rules

    Arguments:
        client {VNS3Client}
        rules {List[dict]}

    Keyword Arguments:
        should_fix {bool} - if false, raise Error, else, update firewall

    Raises:
        CohesiveSDKException - raised if invalid firewall rules provided
        AssertionError - raised if should_fix=False and provided rules dont match VNS3

    Returns:
        List[str] - ordered list of firewall rules
    """
    current_firewall = __firewall_resp_to_list(client.firewall.get_firewall_rules())
    new_firewall, errors = __construct_proposed_firewall_list(rules, state=client.state)
    if errors:
        raise CohesiveSDKException(
            "Invalid firewall rules provided. Errors=%s" % (errors)
        )

    if current_firewall == new_firewall:
        Logger.info("Current firewall is correct. No-op.", host=client.host_uri)
        return current_firewall

    Logger.info(
        "Firewall configuration drift. Expected: %s != %s."
        % (new_firewall, current_firewall),
        host=client.host_uri,
    )

    if not should_fix:
        raise AssertionError(
            "Firewalls did not match for VNS3 @ %s. Current firewall %s != %s."
            % (client.host_uri, current_firewall, new_firewall)
        )

    # operations: insert, delete
    OP_INS = "insert"
    OP_DEL = "delete"
    firewall_edits = []
    for i, rule in enumerate(new_firewall):
        if len(current_firewall) <= i:
            operation = OP_INS
        elif current_firewall[i] == rule:
            continue
        else:
            # current firewall rule is incorrect.
            # now, minimize operations to get correct
            # if can insert OR delete, prefer delete
            # ie. if next rule is the correct rule, del this rule
            operation = (
                OP_DEL
                if len(current_firewall) > i + 1 and current_firewall[i + 1] == rule
                else OP_INS
            )

        firewall_edits.append("%s:%s" % (operation, i))
        if operation == OP_INS:
            client.firewall.post_create_firewall_rule(**{"rule": rule, "position": i})
            current_firewall.insert(i, rule)
        else:  # operation == OP_DEL:
            client.firewall.delete_firewall_rule_by_position(i)
            del current_firewall[i]

    Logger.debug(
        "%s network operations required to fix firewall: %s"
        % (len(firewall_edits), firewall_edits),
        host=client.host_uri,
    )

    return __firewall_resp_to_list(client.firewall.get_firewall_rules())
