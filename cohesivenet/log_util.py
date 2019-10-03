import logging
import os
import re
import six
import sys
from collections import OrderedDict
from typing import Dict, List


logger = logging.getLogger('cohesivenet')
DEFAULT_LOG_FORMAT = '[%(asctime)s] [%(name)s] [%(levelname)s] [%(message)s]'
# Log handler is configured if provided in ENV. Configured end of file (EOF)
COHESIVE_LOG_LEVEL = os.environ.get('COHESIVE_LOG_LEVEL', '').lower()

DEBUG = 'debug'
INFO = 'info'
ERROR = 'error'

def add_handler(_logger, level):
    _logger.handlers = []
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
    console.setLevel(level)
    _logger.addHandler(console)


def set_default_log_handler(log_level):
    print('SETTING DEFAULT HANDLER')
    valid_level = None
    if log_level == 'debug':
        valid_level = logging.DEBUG
    elif log_level == 'info':
        valid_level = logging.INFO
    elif log_level == 'error':
        valid_level = logging.ERROR

    if valid_level:
        add_handler(logger, valid_level)
    else:
        print('!!! LOG SETUP ERROR - Level must be one of debug,info or error. No logging configured.')


def logfmt(props):
    def fmt(key, val):
        # Handle case where val is a bytes or bytesarray
        if six.PY3 and hasattr(val, "decode"):
            val = val.decode("utf-8")
        # Check if val is already a string to avoid re-encoding into
        # ascii. Since the code is sent through 2to3, we can't just
        # use unicode(val, encoding='utf8') since it will be
        # translated incorrectly.
        if not isinstance(val, six.string_types):
            val = six.text_type(val)
        if re.search(r"\s", val):
            val = repr(val)
        # key should already be a string
        if re.search(r"\s", key):
            key = repr(key)
        return u"{key}={val}".format(key=key, val=val)

    return u" ".join([fmt(key, val) for key, val in props.items()])

def __format_msg(message, **params):
    props = OrderedDict(message=message)
    props.update(params)
    return logfmt(props)


def log_debug(message, **params):
    logger.debug(__format_msg(message, **params))


def log_info(message, **params):
    logger.info(__format_msg(message, **params))


def log_error(message, **params):
    logger.error(__format_msg(message, **params))


def scrub_sensitive(data: Dict, secrets: List[str]):
    return {
        k: v if k not in secrets else '****'
        for k, v in data.items()
    }


if COHESIVE_LOG_LEVEL:
    set_default_log_handler(COHESIVE_LOG_LEVEL)