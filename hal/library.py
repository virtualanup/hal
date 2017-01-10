# -*- coding: utf-8 -*-

import abc
import re
import six


@six.add_metaclass(abc.ABCMeta)
class HalLibrary():

    def __init__(self, command):
        self.orig_command = command
        self.command = command
        self.init()
        self.matched = False
        self.match()

    def init(self):
        pass

    def command_empty(self, ignore_punctuations=False):
        if(ignore_punctuations):
            self.match_and_reduce(self.punctuations)
        return len(self.command) == 0

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
        "((What\s+(is|was))|(whats)|(I\s+want\s+to\s+know)|(Show(\s+me)?))(\s+the)?\s+", re.IGNORECASE)

    tell = re.compile("(say|tell)(\s+me)?\s+", re.IGNORECASE)

    punctuations = re.compile("(\.|\?)*")
