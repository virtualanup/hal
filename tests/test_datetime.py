# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.libraries.datetime import DateTime
from .libtest import HalLibTest


class DateTimeTestCase(HalLibTest):
    """
    Test case for date and time library
    """

    lib = DateTime

    def test_response(self):
        self.assert_successful_response("whats the time")
        self.assert_successful_response("whats the time in kathmandu")

        self.assert_successful_response("whats the date")
        self.assert_successful_response("whats the date in london?")

        self.assert_successful_response("what is the current day")
        self.assert_successful_response("i want to know the date in london?")

        self.assert_successful_response("i want to know the date   and time in london.")
        self.assert_successful_response("i want to know the current date   and time in london.")


        self.assert_successful_response("whats the date and time in New York?")

        self.assert_successful_response("whats the date in kathmandu")
        self.assert_successful_response("whats the date in kathmandu")
        self.assert_successful_response("whats the time in new_york")
        self.assert_successful_response("What is the time in new_york?")

        self.assert_error_response("What is the time in lasjdljaer?", "Timezone not found")
        self.assert_error_response("What is the date in londons?", "Timezone not found")

        self.assert_failure_response("What's the datentime in rochester?")


        self.assert_in_response("Whats the date in kathmandu", "Asia")
        self.assert_in_response("Whats the date in new york", "america")

        self.assert_in_response("I want to know the current day", "The day of week is ")
