# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


import unittest


class HalLibTest(unittest.TestCase):
    """
    Base class for testing hal libraries
    """

    def assert_successful_response(self, command):
        a = self.lib(command)
        self.assertTrue(a.matched)
