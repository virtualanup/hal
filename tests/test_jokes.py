# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from hal.lib.joke import JokeLib
from .libtest import HalLibTest


class JokesTestCase(HalLibTest):
    """
    Test case for joke library
    """

    lib = JokeLib

    def test_response(self):
        self.assert_successful_response("Tell me a joke")
        self.assert_successful_response("say a joke")
        self.assert_successful_response("joke")
        self.assert_successful_response("jokes")
