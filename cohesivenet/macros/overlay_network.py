from cohesivenet import util, VNS3Client


def add_clientpack_tags(client: VNS3Client, clientpack_tags):
    """Add tags to clientpacks.

    Arguments:
        client {VNS3Client} - The client to use for API calls.
        clientpack_tags {List[dict]} - List of tags to add to clientpacks. Each tag should be a dictionary with
                                        'clientpack_name', 'key', and 'value' keys.

    Returns:
        dict: A dictionary with clientpack names as keys and the result of the tag addition operation as values.
    """
    results = {}
    for tag_info in clientpack_tags:
        clientpack_name = tag_info['clientpack_name']
        key = tag_info['key']
        value = tag_info['value']

        try:
            response = client.overlay_network.post_create_clientpack_tag(clientpack_name, key, value)
            results[clientpack_name] = {'success': True, 'response': response}
        except Exception as e:
            results[clientpack_name] = {'success': False, 'error': str(e)}

    return results


def segment_overlay_clients(
    client: VNS3Client, groups=None, number_groups=None, group_ratios=None
):
    """segment_overlay_clients Segment clientpacks into sets

    Arguments:
        client {VNS3Client}

    Keyword Arguments:
        groups {List[str]} - Segment into len(groups) groups, each element being the name of group (default: {None})
        number_groups {int} - Segment into number_groups, names being 'group_x' (default: {None})
        group_ratios {Dict[str, float]} - segment by ratio of overlay size, key being the name of the group (default: {None})

    Returns:
        dict - {
            group_name<str>: clientpacks<List[str]>,
        }
    """
    assert (
        groups or number_groups or group_ratios
    ), "groups (List[str]) or number_groups (int) or group_ratios (Dict[str, flaot]) must be provided"
    clients = list(client.overlay_network.get_clientpacks().response.keys())

    if groups:
        partitions = util.partition_list_groups(clients, len(groups))
        return {group_name: partitions[i] for i, group_name in enumerate(groups)}
    elif number_groups:
        partitions = util.partition_list_groups(clients, number_groups)
        return {
            "group_%d" % (i + 1): partitions[i]
            for i, partition in enumerate(partitions)
        }
    else:
        ratios = list(group_ratios.values())
        partitions = util.partition_list_ratios(clients, ratios)
        return {group: partitions[str(ratio)] for group, ratio in group_ratios.items()}
