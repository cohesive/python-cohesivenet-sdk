from typing import Tuple, List, Dict
from collections import namedtuple

from cohesivenet import VNS3Client


ClientExceptionResult = namedtuple('ClientExceptionResult', 'client exception')
OperationResult = namedtuple('OperationResult', 'client result')
BulkOperationResult = Tuple[List[OperationResult], List[ClientExceptionResult]]