import functools


def validate(
    path_params=None,
    path_constraints=None,
    body_params=None,
    body_constraints=None,
    query_params=None,
    query_constraints=None,
    supported_versions=None,
    file_upload=None,
    file_kwarg=None
):
    def validate_decorator(api_func):
        @functools.wraps(api_func)
        def api_func_wrapper(self_api, *args, **kwargs):
            call_path_params = list(args)
            call_keyword_params = dict(kwargs)

            if path_params:
                assert len(args) == len(path_params), 'declared path params and args are different lengths'
                call_path_params = dict(zip(path_params, args))
            else:
                call_path_params = list(args)

            if supported_versions:
                vns3_version = vns3_state.get_vns3_version(self_api.api_client)
                is_supported = True
                if not is_supported:
                    raise ApiMethodUnsupportedError(
                        method_name=api_func.__name__,
                        version=vns3_version,
                        supported_versions=supported_versions
                    )

            if path_params:
                for path_param in path_params:
                    if path_param not in call_path_params or call_path_params[path_param] is None:
                        raise ApiValueError(
                            "Missing the required path parameter `%s` when calling `%s`"
                            % (path_param, api_func.__name__)
                        )

            # keyword params can be either body params (POST, PUT, PATCH) or query params (GET)
            keyword_params = kwargs
            if body_params:
                for body_param in body_params:
                    if body_param not in keyword_params or keyword_params[body_param] is None:
                        raise ApiValueError(
                            "Missing the required field `%s` when calling `%s`"
                            % (body_param, api_func.__name__)
                        )

            if query_params:
                for query_param in query_params:
                    if query_param not in keyword_params or keyword_params[query_param] is None:
                        raise ApiValueError(
                            "Missing the required query parameter `%s` when calling `%s`"
                            % (query_param, api_func.__name__)
                        )

            if file_upload:
                assert file_kwarg, "no kwarg key provided for file upload param validation"
                if file_kwarg not in keyword_params or not keyword_params[file_kwarg]:
                     raise ApiValueError(
                            "Missing the file stream kwarg field `%s` when calling `%s`"
                            % (file_kwarg, api_func.__name__)
                        )


            return api_func(*args, **kwargs)
        return api_func_wrapper
    return validate_decorator


def set_api_library(client, api, library):
    """Set the API library functions based on the current clients version
    
    Arguments:
        client {VNS3Client}
        api {Object} -
        library {Dict} - {
            func_name: str -> dict[version:str -> func]
        }

    Returns: None
    """
    vns3_version = client.vns3_dot_version

    def in_range(val, min_v, max_v):
        return val >= min_v and val <= max_v

    def v_to_int(val):
        return int(val.replace('.', ''))

    version_library = {}
    vns3_version_int = v_to_int(vns3_version)
    for function_name, versions_funcs in library.items():
        for version, func in versions_funcs.items():
            if '-' in version:
                min_v, max_v = [v_to_int(i) for i in version.split('-')]
                if in_range(vns3_version_int, min_v, max_v):
                    version_library[function_name] = func
            elif version == vns3_version:
                version_library[function_name] = func

    for name, func in version_library.items():
        setattr(api, name, functools.partial(func, client))