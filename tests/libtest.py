# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.library import HalLibrary

import unittest


class HalLibTest(unittest.TestCase):
    """
    Base class for testing hal libraries
    """

    def assert_successful_response(self, command):
        a = self.lib(command)
        a.process_input()
        self.assertEqual(a.status, HalLibrary.SUCCESS)

    def assert_failure_response(self, command):
        a = self.lib(command)
        a.process_input()
        self.assertEqual(a.status, HalLibrary.FAILURE)

    def assert_error_response(self, command, message=None):
        a = self.lib(command)
        a.process_input()
        self.assertEqual(a.status, HalLibrary.ERROR)
        if message:
            self.assertEqual(a.get_error(), message)

    def assert_in_response(self, command, string):
        a = self.lib(command)
        a.process_input()
        a.process()

        for s in a.get_response():
            if string.lower() in s.lower():
                return
        raise Exception(string," not in ", a.get_response())
