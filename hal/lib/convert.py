# -*- coding: utf-8 -*-

import re
import random


from semantic.units import ConversionService
from hal.library import HalLibrary


class ConvLib(HalLibrary):
    """
    Conversion library
    """

    name = "Converter"
    keywords = ["convert", "converter", "conversion"]

    convregex = re.compile(
        "(convert|change)(.*)", re.IGNORECASE)

    def init(self):
        pass

    def match(self):
        if self.match_and_reduce(self.convregex):
            expression = self.last_matched.groups()[-1].strip()
            if expression:
                try:
                    # Try conversion
                    service = ConversionService()
                    self.result = service.convert(expression)
                    self.matched = True
                except:
                    # Fail silently
                    raise
    def get_response(self):
        return ["Result : " + str(self.result)]

    @classmethod
    def help(cls):
        return {
            "name": "Conversion",
            "description": "Conversion between units",
            "samples": [
                    "convert a pound to kg",
                    "change Seven and a half kilograms to pounds",
                    "convert Seven and a half pounds per square foot to kilograms per meter squared",
            ]
        }
