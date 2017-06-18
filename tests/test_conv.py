# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.libraries.convert import ConvLib
from .libtest import HalLibTest


class ConvTestCase(HalLibTest):
    """
    Test case for Conversion library
    """

    lib = ConvLib

    def test_response(self):
        self.assert_successful_response("convert 12 kg to lb")
        self.assert_in_response("convert 12 kg to lb", "26.45")
