# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.libraries.fun import FunLib
from .libtest import HalLibTest


class FunTestCase(HalLibTest):
    """
    Test case for fun library
    """

    lib = FunLib

    def test_response(self):
        self.assert_successful_response("whats the meaning of life?")
        self.assert_successful_response("Tell me the meaning of life")

        self.assert_in_response("You're awesome", "betcha")


        self.assert_in_response("Hodor hodor", "hodor")

        self.assert_in_response("open the pod bay door", "sorry, dave")


        self.assert_in_response("roll a dice", "dice 1")
        self.assert_in_response("roll two dices", "dice 2")
        self.assert_in_response("roll two dices of three faces", "dice 2")
        self.assert_in_response("roll ten dices of one thousand faces", "dice 9")

        self.assert_response_count("roll ten dices of one thousand faces", 10)

        self.assert_error_response("roll eighteen dices")

        self.assert_in_response("flip a coin", "coin 1")
        self.assert_in_response("toss two coins", "coin 2")
        self.assert_in_response("flip two coins", "coin 2")
        self.assert_response_count("flip ten coins", 10)
        self.assert_error_response("flip eleven coins", "Can't roll that number of coins")
