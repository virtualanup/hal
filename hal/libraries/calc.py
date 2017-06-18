# -*- coding: utf-8 -*-

import re
import random
import math

from simpleeval import simple_eval
from hal.library import HalLibrary


class CalcLib(HalLibrary):
    """
    Calculator library
    """

    name = "Calculator"
    keywords = ["calc", "calculate", "eval"]

    functions = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "ceil": math.ceil,
        "floor": math.floor,
        "factorial": math.factorial,
        "log": math.log,
        "log10": math.log10,
        "sqrt": math.sqrt,
        "square": lambda x: x*x,
        "sqrt": lambda x: x**0.5,

    }

    calcregex = re.compile(
        "(value\s+of\s+)?(.*)", re.IGNORECASE
    )

    function_regex = re.compile(
        "([a-zA-Z0-9]+)\s+of\s+(.*)", re.IGNORECASE
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

        calc_command = self.command

        if self.match_and_reduce(self.calcregex):
            expression = self.last_matched.groups()[-1].strip()
            if expression:
                try:
                    # Try to parse the expression here.
                    result = simple_eval(
                        expression,
                        functions=self.functions
                    )
                    self.status = self.SUCCESS
                    self.result = result
                    return
                except:
                    # Fail silently
                    pass
        # restore the calc command to interpret it in other way
        self.command = calc_command
        if self.match_and_reduce(self.function_regex):
            function_name = self.last_matched.groups()[-2].strip()
            expression = self.last_matched.groups()[-1].strip()

            created_expression = "{}({})".format(function_name.lower(), expression)
            try:
                # Try to parse the expression here.
                result = simple_eval(
                    created_expression,
                    functions=self.functions
                )
                self.status = self.SUCCESS
                self.result = result
                return
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
