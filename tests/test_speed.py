# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.library import HalLibrary

import unittest

class SpeedTestCase(unittest.TestCase):
    """
    Do testing multiple times to test speed
    """

    def test_speed(self):
        for j in range(1,1000):
            pass
