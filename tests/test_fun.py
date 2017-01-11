# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.lib.fun import FunLib
from .libtest import HalLibTest


class FunTestCase(HalLibTest):
    """
    Test case for fun library
    """

    lib = FunLib

    def test_response(self):
        self.assert_successful_response("whats the meaning of life?")
        self.assert_successful_response("open the pod bay door.")
