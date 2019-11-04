# coding: utf-8
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

"""
    Cohesive Networks SDK

    Cohesive Networks SDK is a thin wrapper around our product APIs providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""

import os
import sys
from setuptools import setup, find_packages  # noqa: H301
from setuptools.command.test import test as TestCommand

NAME = "cohesivenet"
DEPENDENDIES = [
    "urllib3 >= 1.15",
    "certifi >=  14.05.14",
    "python-dateutil >= 2.5.3",
    "paramiko >= 2.4.3",
]

DIR = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex

        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


os.chdir(DIR)

version_contents = {}
with open(os.path.join(DIR, "cohesivenet", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)


def load_long_description():
    with open(os.path.join(DIR, "README.md"), "r") as fh:
        return fh.read()


setup(
    name=NAME,
    version=version_contents["VERSION"],
    description="Cohesive Networks SDK",
    author="Cohesive Networks, Inc.",
    long_description=load_long_description(),
    long_description_content_type="text/markdown",
    author_email="solutions@cohesive.net",
    python_requires=">=3.5.0",
    url="https://github.com/cohesive/python-cohesivenet-sdk",
    keywords=[
        "Cohesive Networks SDK",
        "Cohesive Networks",
        "Secops",
        "SDN",
        "Software Defined Networking",
        "Networkops",
        "networking",
        "Openapi",
    ],
    install_requires=DEPENDENDIES,
    tests_require=["pytest >= 4.6.2"],
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    include_package_data=True,
    package_data={NAME: ["version"]},
    cmdclass={"test": PyTest},
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
