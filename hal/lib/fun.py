# -*- coding: utf-8 -*-

import re
import random

from hal.library import HalLibrary


class FunLib(HalLibrary):
    """
    Most of these are directly influenced by betty
    """
    name = "fun"
    keywords = ["life", "fun"]

    mol_regex = re.compile("meaning\s+of\s+life", re.IGNORECASE)
    open_pod_regex = re.compile(
        "open\s+(the\s+)?pod\s+bay\s+door(s)?", re.IGNORECASE)
    appreciate_regex = re.compile(
        "you\'?(re)?\s+(are\s+)?(cool|awesome|amazing|fun(ny)?|rock\s+my\s+world|rule)")

    def init(self):
        self.fun_response = ""

    def match(self):

        # Meaning of life
        self.match_and_reduce(self.wh_question)
        if self.match_and_reduce(self.mol_regex):
            if self.command_empty(True):
                self.fun_response = "42."
                self.matched = True
                return
        # Rewind and try another fun thing
        self.command = self.orig_command

        if self.match_and_reduce(self.open_pod_regex):
            if self.command_empty(True):
                self.fun_response = "I'm sorry, Dave. I'm afraid I can't do that."
                self.matched = True
                return

        self.command = self.orig_command
        if self.match_and_reduce(self.appreciate_regex):
            if self.command_empty(True):
                self.fun_response = "You betcha."
                self.matched = True
                return

    def get_response(self):
        return [self.fun_response]

    @classmethod
    def help(cls):
        return {
            "name": "Fun Interactions",
            "description": "Some fun interactions with hal",
            "samples": [
                    "hal whats the meaning of life",
                    "hal open the pod bay door",
                    "hal you're funny",
            ]
        }
