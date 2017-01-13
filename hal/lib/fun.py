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
        "roll\s+(.*)\s+dice(s)?(\s+(?:of|with)\s+(.*)\s+face(s)?)?")

    coin_regex = re.compile("(?:toss|flip)\s+(.*)\s+coin(s)?")

    def init(self):
        self.fun_response = ""

    def process_input(self):

        # Meaning of life
        self.match_and_reduce(self.wh_question)
        if self.match_and_reduce(self.mol_regex):
            if self.command_empty(True):
                self.fun_response = "42."
                self.status = self.SUCCESS
                return
        # Rewind and try another fun thing
        self.command = self.orig_command

        if self.match_and_reduce(self.open_pod_regex):
            if self.command_empty(True):
                self.fun_response = "I'm sorry, Dave. I'm afraid I can't do that."
                self.status = self.SUCCESS
                return

        self.command = self.orig_command
        if self.match_and_reduce(self.appreciate_regex):
            if self.command_empty(True):
                self.fun_response = "You betcha."
                self.status = self.SUCCESS
                return

        self.command = self.orig_command
        if self.match_and_reduce(self.dice_regex):

            service = NumberService()
            num_of_dice = self.last_matched.group(1)

            try:
                self.num_of_dice = int(service.parse(num_of_dice))
                # If faces is also passed
                self.faces = 6
                try:
                    faces = self.last_matched.group(4)
                    if faces:
                        self.faces = service.parse(faces)
                except:
                    pass

                if self.command_empty(True):
                    if self.num_of_dice < 0 or self.num_of_dice > 10:
                        self.status = self.ERROR
                        self.set_error("Can't roll that number of dices")
                    elif self.faces < 1:
                        self.status = self.ERROR
                        self.set_error("Can't roll dice of that faces")
                    else:
                        self.response = []
                        for j in range(1, self.num_of_dice + 1):
                            self.response.append(
                                "Dice {} : {}".format(
                                    j, random.randint(1, self.faces))
                            )
                        self.status = self.SUCCESS
            except:
                pass

        self.command = self.orig_command
        if self.match_and_reduce(self.coin_regex):

            service = NumberService()
            num_of_coins = self.last_matched.group(1)

            try:
                self.num_of_coins = int(service.parse(num_of_coins))
                if self.command_empty(True):
                    if self.num_of_coins < 0 or self.num_of_coins > 10:
                        self.status = self.ERROR
                        self.set_error("Can't roll that number of coins")
                    else:
                        self.response = []
                        for j in range(1, self.num_of_coins + 1):
                            self.response.append(
                                "Coin {} : {}".format(
                                    j, random.choice(["Head", "Tail"])
                                ))
                    self.status = self.SUCCESS
            except:
                pass

    def process(self):
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
