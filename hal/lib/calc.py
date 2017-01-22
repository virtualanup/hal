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
        "(value\s+of\s+)?(.*)", re.IGNORECASE
    )

    calc_command_regex = re.compile(
        "(calc|eval|calculate|evaluate)\s+(the\s+)?", re.IGNORECASE
    )

    def init(self):
        pass

    def process_input(self):
        if not self.match_and_reduce(self.wh_question):
            if not self.match_and_reduce(self.calc_command_regex):
                # nothing to do
                return

        if self.match_and_reduce(self.calcregex):
            expression = self.last_matched.groups()[-1].strip()
            if expression:
                try:
                    # Try to parse the expression here.
                    result = simple_eval(expression)
                    self.status = self.SUCCESS
                    self.result = result
                except:
                    # Fail silently
                    pass

    def process(self):
        self.add_response("Result : " + str(self.result))

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
