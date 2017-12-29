# coding: utf-8

"""
    ExaVault API

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="ExaVault API",
    author_email="",
    url="",
    keywords=["Swagger", "ExaVault API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)