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

    calcregex = re.compile("(calc|eval|calculate)\s+((the\s+)?value\s+of\s+)?(.*)")

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

    def help_text(self, text):
        pass
