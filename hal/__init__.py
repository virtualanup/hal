# -*- coding: utf-8 -*-

from .hal import Hal
from .libraries import *

from .version import __version__, __VERSION__

import sys
import socket

__version__ = '0.0.1'

__VERSION__ = __version__


class ConsoleHal(Hal):
    """
    Console interface to hal
    """

    def __init__(self, configpath):
        super(ConsoleHal, self).__init__(configpath)

    def process(self, command):
        # First of all, try to query the server. If it fails, then
        # Run locally
        try:
            serversocket = socket.socket()
            host = 'localhost'
            port = 3423

            serversocket.connect((host, port))
            serversocket.send(command.encode())
            response = serversocket.recv(1024).decode()
            serversocket.close()
            return response
        except:
            return super(ConsoleHal, self).process(command)

    def say_all(self):
        response = "\n".join(self.responses)
        return response

    def display_help(self, help_content):
        print()
        print(help_content["name"])
        print("=" * len(help_content["name"]))
        print(help_content["description"])
        print()
        print("Samples:")
        print("--------")
        for s in help_content["samples"]:
            print(s)
        print()
        print()


def main():
    # Interpret the given command
    hal = ConsoleHal("~/")
    # Get user command from command line
    command = " ".join(sys.argv[1:])

    response = hal.process(command)
    print(response)
    return 0


if __name__ == "__main__":
    sys.exit(main())
