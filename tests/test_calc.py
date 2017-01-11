# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.lib.calc import CalcLib
from .libtest import HalLibTest


class CalcTestCase(HalLibTest):
    """
    Test case for joke library
    """

    lib = CalcLib

    def test_response(self):
        self.assert_successful_response("eval 12+12-33")
        self.assert_successful_response("calculate 12  - 12")
        self.assert_successful_response("eval 12-32")
