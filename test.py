# coding: utf-8


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

class Test(object):
    """Manage access to VNS3 with API tokens and admin access URLs"""

    def __init__(self, =None):
        if api_client is None:
            from cohesivenet.vns3_client import VNS3Client

            api_client = VNS3Client()
        self.api_client = api_client

    def __getattribute__(self, name):
        print('Getting %s' % name)
        attr = super().__getattribute__(name)
        if callable(attr):


    def method_1(self, a, b):
        return a

