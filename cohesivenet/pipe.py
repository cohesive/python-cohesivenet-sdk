import asyncio
import logging
from copy import deepcopy
from typing import Dict, Tuple, List, Callable, Union, Awaitable

Logger = logging.getLogger('cohesivenet')


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


async def await_concurrent_steps(*funcs):
    return await asyncio.gather(*funcs)


def run_pipe_async(init_data, steps: List[Tuple[str, Union[Callable, List[Awaitable]]]]):
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
