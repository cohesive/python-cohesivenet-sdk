import asyncio
import json
import logging

from copy import deepcopy
from typing import Dict, Tuple, List, Callable, Union, Awaitable

Logger = logging.getLogger(__name__)


def run_parallel(*coroutines):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*coroutines))
    loop.close()
    return results


def run_pipe(init_data, steps: List[Tuple[str, Callable]]):
    data = deepcopy(init_data)
    total_steps = len(steps)
    Logger.debug('Running pipe [steps=%s] [inputs=%s]' % (total_steps, clean_data(init_data)))

    for step_i, (step_name, func) in enumerate(steps):
        step_num = step_i + 1
        Logger.info('Running step [step=%s/%s] [name=%s]' % (step_num, total_steps, step_name))
        response = func(data)
        outputs = response.get('outputs', {})
        data.update(outputs)
        Logger.debug('Step %s/%s finished. Outputs: %s' % (step_num, total_steps, outputs))
    return data


def run_pipe_async(init_data, steps: List[Tuple[str, Union[Callable, List[Awaitable]]]]):
    """Run pipeline of step functions, running in parallel if 

    Arguments:
        init_data {[type]} -- [description]
        steps {List[Tuple[str, Union[Callable, List[Awaitable]]]]} -- [description]

    Returns:
        [type] -- [description]
    """
    data = deepcopy(init_data)
    total_steps = len(steps)
    Logger.info('Running pipe [steps=%s] [inputs=%s]' % (total_steps, clean_data(init_data)))
    for step_i, (step_name, step_func) in enumerate(steps):
        step_num = step_i + 1
        Logger.info('Running pipe step [step=%s/%s] [name=%s]' % (step_num, total_steps, step_name))
        if type(step_func) is list:
            Logger.info('Running async substeps')
            step_responses = run_parallel(*(func(data) for func in step_func))
            Logger.debug('Substeps finished. Outputs: %s' % step_responses)
            for response in step_responses:
                data.update(response.get('outputs', {}))
        else:
            response = step_func(data)
            outputs = response.get('outputs', {})
            data.update(outputs)
            Logger.debug('Step %s/%s finished. Outputs: %s' % (step_num, total_steps, outputs))
    return data


def take_keys(keys: List[str], data_dict):
    """Take keys from dict
    
    Arguments:
        keys {List[str]} -- Keys it include in output dict
        data_dict {Dict}
    
    Returns:
        [Dict]
    """
    return {k: v for k, v in data_dict.items() if k in keys}


def flatten_dict(d, prefix=None, joinchar='__'):
    """flatten_dict Flatten nested dictionary, joining paths into single string key
    
    Arguments:
        d {[type]} -- [description]
    
    Keyword Arguments:
        prefix {str} -- Prefix string for joining keys (default: {None})
        joinchar {str} -- String for joining nested keys (default: {'__'})
    
    Returns:
        [Dict] -- Dict of depth 1
    """
    key_value_pairs = {}
    _prefix = lambda k: k if not prefix else '%s%s%s' % (prefix, joinchar, k)
    for k, v in d.items():
        if type(v) is dict:
            key_value_pairs.update(flatten_dict(v, prefix=_prefix(k), joinchar=joinchar))
        else:
            key_value_pairs[_prefix(k)] = v
    return key_value_pairs


def unflatten_dict(d, splitchar='__'):
    """unflatten_dict Build nested dictionary based on keys
    
    Arguments:
        d {Dict}
    
    Keyword Arguments:
        splitchar {str} -- str marking nested dictionary (default: {'__'})
    
    Returns:
        [Dict]
    """
    resp = {}
    for flatkey, v in d.items():
        keyparts = flatkey.split(splitchar)
        _target = resp
        final_key = keyparts[-1]
        for key in keyparts[:-1]:
            if key not in _target:
                _target[key] = {}
            _target = _target[key]
        _target[final_key] = v
    return resp


def map_type(s, expected_type, strict=True):
    _def_return_val = s
    try:
        if type(s) is list:
            return s
        elif 'list' in str(expected_type).lower():
            _def_return_val = []
            return json.loads(s)
        elif not s or s.lower() in ('none', ''):
            return None
        elif expected_type is bool:
            return s.lower() == 'true'

        return expected_type(s)
    except ValueError:
        if not strict:
            return _def_return_val
        raise


def duck_type_dict(datacls, data: dict, strict_types=True):
    if not data:
        return None

    fields = {f.name: f.type for f in get_fields(datacls)}
    return datacls(**{
        k: (
            map_type(data.get(k), value_type, strict=strict_types)
            if not is_dataclass(value_type)
            else duck_type_dict(value_type, data.get(k), strict_types=strict_types)
        ) for k, value_type in fields.items()
    })


def get_path(data_dict, key_path, fail=False):
    """get_path
    
    Arguments:
        data_dict {dict} -- [description]
        key_path {str or List of strings} -- a.b.c or ['a', 'b', 'c']
    
    Keyword Arguments:
        fail {bool} -- Raise exception if does not exist (default: {False})
    
    Raises:
        Exception: Generic not found exception
    
    Returns:
        [any] -- value at key path
    """
    _target = data_dict
    steps = key_path if type(key_path) is list else key_path.split('.')
    for step in steps:
        if type(_target) is not dict or step not in _target:
            if fail:
                raise Exception('Path "%s" does not exist' % key_path)
            return None
        _target = _target.get(step)
    return _target


def map_dict_values(func_map, data_dict):
    return {
        k: func_map.get(k, lambda x: x)(v)
        for k, v in data_dict.items()
    }


def map_dict_keypaths(key_map, data_dict):
    updates = {
        new_key: get_path(data_dict, key_path)
        for key_path, new_key in key_map.items()
    }
    return {**data_dict, **updates}

