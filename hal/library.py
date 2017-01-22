# -*- coding: utf-8 -*-

import abc
import re
import six


@six.add_metaclass(abc.ABCMeta)
class HalLibrary():

    SUCCESS = 1
    FAILURE = 2
    ERROR = 3
    INCOMPLETE = 4

    def __init__(self, command):
        self.orig_command = command
        self.command = command
        self.init()

        # Status is failure by default
        self.status = self.FAILURE
        self.response_list = []
        self.error = ""

    def init(self):
        pass

    def command_empty(self, ignore_punctuations=False):
        if(ignore_punctuations):
            self.match_and_reduce(self.punctuations)
        return len(self.command) == 0

    @abc.abstractmethod
    def process_input(self):
        """
        Tries to parse the command
        """
        pass

    @abc.abstractmethod
    def process(self):
        """
        Process the parsed command to get the result
        """
        pass

    def add_response(self, response):
        self.response_list.append(response)

    def get_response(self):
        return self.response_list

    def get_error(self):
        return self.error

    def set_error(self, error):
        self.error = error

    def help(cls):
        """
        returns help
        """
        pass

    def match_and_reduce(self, regex):
        """Match command with regex and reduce the command"""
        r_m = regex.match(self.command)
        if r_m:
            self.last_matched = r_m
            self.command = self.command[len(r_m.group(0)):]
            return True
        return False

    def match_and_reduce_list(self, regex_list, exclusive=False):
        """
        Match the regex of the list against the command and reduce the
        command and ignore if match found. Return after first match if
        exclusive
        """
        matched = False
        for regex in regex_list:
            if self.match_and_reduce(regex):
                matched = True
                if exclusive:
                    break
        return matched

    # Generic matches
    wh_question = re.compile(
        "((What\s+(is|was))|(what\'?s)|(I\s+want\s+to\s+know)|((Show|Tell)(\s+me)?))(\s+the)?\s+", re.IGNORECASE)

    tell = re.compile("(say|tell)(\s+me)?\s+", re.IGNORECASE)

    punctuations = re.compile("(\.|\?)*")
