# -*- coding: utf-8 -*-

import abc

import re


class HalLibrary(metaclass=abc.ABCMeta):

    def __init__(self, command):
        self.orig_command = command
        self.command = command
        self.init()
        self.matched = False
        self.match()

    def init(self):
        pass

    @abc.abstractmethod
    def match(self):
        """
        returns true if the command is matched
        """
        pass

    @abc.abstractmethod
    def get_response(self):
        """
        Gets response for the command
        """
        pass

    @abc.abstractmethod
    def help_text(self):
        """
        returns help text
        """
        pass

    def match_and_reduce(self, regex):
        """Match command with regex and reduce"""
        r_m = regex.match(self.command)
        if r_m:
            self.command = self.command[len(r_m.group(0)):]
    # Generic matches
    wh_question = re.compile(
        "((What\s+is)|(whats)|(I\s+want\s+to\s+know)|(Show(\s+me)?))(\s+the)?\s+", re.IGNORECASE)

    tell = re.compile("(say|tell)(\s+me)?\s+", re.IGNORECASE)

    punctuations = re.compile("(\.|\?)*")
