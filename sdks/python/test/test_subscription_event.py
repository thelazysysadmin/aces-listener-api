# coding: utf-8

"""
    ACES Listener API

    API Specification for ACES Listeners that read data on a blockchain and forward transaction events to registered subscribers. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import com.arkaces.aces_listener_api
from com.arkaces.aces_listener_api.rest import ApiException
from com.arkaces.aces_listener_api.models.subscription_event import SubscriptionEvent


class TestSubscriptionEvent(unittest.TestCase):
    """ SubscriptionEvent unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscriptionEvent(self):
        """
        Test SubscriptionEvent
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = com.arkaces.aces_listener_api.models.subscription_event.SubscriptionEvent()
        pass


if __name__ == '__main__':
    unittest.main()
