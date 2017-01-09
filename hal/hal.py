# -*- coding: utf-8 -*-
import datetime
import abc
import os
import inspect
import importlib
from .library import HalLibrary


class Hal(metaclass=abc.ABCMeta):

    def __init__(self, configpath):
        # Find libraries inside the lib directory

        dir_path = os.path.join(os.path.dirname(__file__), "lib")
        lib_files = [f for f in os.listdir(dir_path) if
                     os.path.isfile(os.path.join(dir_path, f)) and
                     f.upper().endswith(".PY")
                     ]

        self.libraries = []
        for f in lib_files:
            # Try to load the module
            try:
                module_name = "hal.lib." + f[:-3]
                module = importlib.import_module(module_name)
                for name, obj in inspect.getmembers(module):
                    # Find classes that inherit from HalLibrary
                    if inspect.isclass(obj) and issubclass(obj, HalLibrary) and \
                            name != "HalLibrary" and not inspect.isabstract(obj):
                        self.libraries.append(obj)
            except:
                self.say("Error loading library {}".format(f))
                raise

    @abc.abstractmethod
    def say(self, text):
        """ Present some information to the user """
        pass

    def greet(self):
        hour = datetime.datetime.now().hour

        greeting = "Good Evening"
        if hour < 12:
            greeting = 'Good morning'
        elif 12 <= hour < 18:
            greeting = 'Good afternoon'

        self.say("{}. Whet can I help you with?".format(greeting))

    def process(self, command):
        """
        Process the command and get response by querying each plugin if required.
        """
        if(len(command) == 0):
            self.greet()
            return

        # prepare the command
        command = command.strip()
        command_words = command.split()
        command_lower = command.lower()
        command_upper = command.upper()

        # Some hard coded patterns: If first word is help, activate help
        # moudule
        if command_lower.startswith("help"):
            self.say("Help mode activated")
            return

        matched = False

        for lib in self.libraries:

            lib_obj = lib(command)

            if lib_obj.matched:

                matched = True
                resp = lib_obj.get_response()

                for r in resp:
                    self.say(r)

        if not matched:
            self.say("I don't understand what you're saying.")
