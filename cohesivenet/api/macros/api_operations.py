import functools

import cohesivenet
import cohesivenet.pipe as pipe
import cohesivenet.data_types as data_types

from cohesivenet import VNS3Client, Configuration


def try_api_call(api_call, *args, **kwargs):
    """try_api_call Wrapper for api call to catch errors
    
    Arguments:
        api_call {callable}
    
    Returns:
        [OperationResult or ClientExceptionResult]
    """
    try:
        response = api_call(*args, **kwargs)
        return data_types.OperationResult(client, response)
    except cohesivenet.ApiException as e:
        return data_types.ClientExceptionResult(client, e)


async def try_api_call_async(api_call, *args, **kwargs):
    """try_api_call_async Async Wrapper for api call to catch errors
    
    Arguments:
        api_call {callable}
    
    Returns:
        [Coroutine -> [OperationResult or ClientExceptionResult]]
    """
    try:
        response = api_call(*args, **kwargs)
        return data_types.OperationResult(client, response)
    except cohesivenet.ApiException as e:
        return data_types.ClientExceptionResult(client, e)


def __bulk_call_api_sync(clients, call_client_func) -> data_types.BulkOperationResult:
    """Bulk operation for clients, call same method for all clients
    
    Arguments:
        clients {List[VNS3Client]}
        call_client_func {callable} - func: VNS3Client -> response
    
    Returns:
        data_types.BulkOperationResult -- [description]
    """
    succeeded = []
    failed = []
    for client in clients:
        call_client = functools.partial(call_client_func, client)
        result = try_api_call(call_client)
        if isinstance(result, data_types.ClientExceptionResult):
            failed.append(result)
        else:
            succeeded.append(result)
    return succeeded, failed


def __bulk_call_api_parallel(clients, call_client_func) -> data_types.BulkOperationResult:
    """Bulk operation for clients, call same method for all clients
    
    Arguments:
        clients {List[VNS3Client]}
        call_client_func {callable} - func: VNS3Client -> response
    
    Returns:
        data_types.BulkOperationResult
    """
    results = pipe.run_parallel(*(
        try_api_call_async(functools.partial(call_client_func, client)) for client in clients
    ))

    succeeded = []
    failed = []
    for result in results:
        if isinstance(result, data_types.ClientExceptionResult):
            failed.append(result)
        else:
            succeeded.append(result)

    return succeeded, failed


def __bulk_call_api(clients, call_client_func, parallelize=False) -> data_types.BulkOperationResult:
    """Bulk operation for clients, call same method for all clients
    
    Arguments:
        clients {List[VNS3Client]}
        call_client_func {callable} - func: VNS3Client -> response
    
    Returns:
        data_types.BulkOperationResult
    """
    if parallelize:
        return __bulk_call_api_parallel(clients, call_client_func)
    else:
        return __bulk_call_api_sync(clients, call_client_func)