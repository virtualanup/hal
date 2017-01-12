# -*- coding: utf-8 -*-

import re
import random

from simpleeval import simple_eval
from hal.library import HalLibrary


class CalcLib(HalLibrary):
    """
    Calculator library
    """

    name = "Calculator"
    keywords = ["calc", "calculate", "eval"]

    calcregex = re.compile(
        "(what(s|\s+is)?|calc|eval|calculate)\s+((the\s+)?value\s+of\s+)?(.*)", re.IGNORECASE)

    def init(self):
        pass

    def match(self):
        if self.match_and_reduce(self.calcregex):
            expression = self.last_matched.groups()[-1].strip()
            if expression:
                try:
                    # Try to parse the expression
                    result = simple_eval(expression)
                    self.matched = True
                    self.result = result
                except:
                    # Fail silently
                    pass

    def get_response(self):
        return ["Result : " + str(self.result)]

    @classmethod
    def help(cls):
        return {
            "name": "Calculator",
            "description": "Evaluate mathematical expressions",
            "samples": [
                    "hal what is 12+12",
                    "hal calculate the value of sin(90)",
                    "hal calc \"12*(12+12*7)\"",
            ]
        }
