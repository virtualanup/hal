# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.lib.datetime import DateTime
from .libtest import HalLibTest


class DateTimeTestCase(HalLibTest):
    """
    Test case for date and time library
    """

    lib = DateTime

    def test_response(self):
        self.assert_successful_response("whats the time")
        self.assert_successful_response("whats the time in kathmandu")
        self.assert_successful_response("whats the time in new_york")
        self.assert_successful_response("What is the time in new_york?")
