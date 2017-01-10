# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys

from .hal import Hal


class ConsoleHal(Hal):
    """
    Console interface to hal
    """
    def __init__(self, configpath):
        super(ConsoleHal, self).__init__(configpath)

    def say(self, text):
        print(text)

    def display_help(self, help_content):
        print()
        print(help_content["name"])
        print("="*len(help_content["name"]))
        print(help_content["description"])
        print()
        print("Samples:")
        print("--------")
        for s in help_content["samples"]:
            print(s)
        print()
        print()

if __name__ == "__main__":
    # Interpret the given command
    hal = ConsoleHal("~/")
    # Get user command from command line
    command = " ".join(sys.argv[1:])

    hal.process(command)
