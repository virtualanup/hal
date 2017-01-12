# -*- coding: utf-8 -*-

import re
import random
from semantic.numbers import NumberService
from hal.library import HalLibrary


class FunLib(HalLibrary):
    """
    Most of these are directly influenced by betty
    """
    name = "fun"
    keywords = ["life", "fun"]

    mol_regex = re.compile("meaning\s+of\s+life", re.IGNORECASE)
    open_pod_regex = re.compile(
        "(please\s+)?open\s+(the\s+)?pod\s+bay\s+door(s)?", re.IGNORECASE)
    appreciate_regex = re.compile(
        "you\'?(re)?\s+(are\s+)?(cool|awesome|amazing|fun(ny)?|rock\s+my\s+world|rule)")

    dice_regex = re.compile(
        "roll\s+(.*)\s+dice(s)?(\s+of\s+(.*)\s+face(s)?)?")

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

        self.command = self.orig_command
        if self.match_and_reduce(self.dice_regex):

            service = NumberService()
            num_of_dice = self.last_matched.group(1)

            try:
                self.num_of_dice = service.parse(num_of_dice )
               # If faces is also passed
                self.faces = 1
                try:
                    faces = self.last_matched.group(4)
                    self.faces = service.parse(faces)
                except:
                    raise

                if self.command_empty(True):
                    if self.num_of_dice < 0 or self.num_of_dice > 10:
                        self.response["Can't roll that number of dices"]
                    elif self.faces < 1:
                        self.response = ["Can't roll dice of that faces"]
                    else:
                        self.response = []
                        for j in range(1, self.num_of_dice+1):
                            self.response.append(
                                    "Dice {} : {}".format(j, random.randint(1, self.faces))
                                )
                    self.matched = True
            except:
                pass

    def get_response(self):
        return self.response

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
