# coding: utf-8

"""
    Aces Encoded Listener API

    API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "arkaces-encoded-listener-client"
VERSION = "0.1.1"
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
    description="Aces Encoded Listener API",
    author_email="",
    url="",
    keywords=["Swagger", "Aces Encoded Listener API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 
    """
)
