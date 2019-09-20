import cohesivenet
import cohesivenet.pipe as pipe
import cohesivenet.data_types as data_types

from cohesivenet import VNS3Client, Configuration, ApiException


def try_call_client(client, call, *args, **kwargs):
    try:
        response = call(client, *args, **kwargs)
        return data_types.OperationResult(client, response)
    except cohesivenet.ApiException as e:
        return data_types.ClientExceptionResult(client, e)


async def try_call_client_async(client, call, *args, **kwargs):
    return try_call_client(client, call, *args, **kwargs)


def try_api_call(api_call, *args, should_raise=False, **kwargs):
    """try_api_call Wrapper for api call to catch errors
    
    Arguments:
        api_call {callable}
    
    Returns:
        [OperationResult or ClientExceptionResult]
    """

    try:
        return api_call(*args, **kwargs)
    except cohesivenet.ApiException as e:
        if should_raise:
            raise e
        return e


async def try_api_call_async(api_call, *args, **kwargs):
    """try_api_call_async Async Wrapper for api call to catch errors
    
    Arguments:
        api_call {callable}
    
    Returns:
        [Coroutine -> [OperationResult or ClientExceptionResult]]
    """
    return try_api_call(api_call, *args, **kwargs)


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
        result = try_call_client(client, call_client_func)
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
        try_call_client_async(client, call_client_func) for client in clients
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