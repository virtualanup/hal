# -*- coding: utf-8 -*-

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

if __name__ == "__main__":
    # Interpret the given command
    hal = ConsoleHal("~/")
    # Get user command from command line
    command = " ".join(sys.argv[1:])

    hal.process(command)
