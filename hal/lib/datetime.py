# -*- coding: utf-8 -*-

import re
import time

from hal.library import HalLibrary


class DateTime(HalLibrary):

    name = "Date and Time"
    date = re.compile("(date)", re.IGNORECASE)
    time = re.compile("(time)", re.IGNORECASE)
    datetime = re.compile(
        "(((date\s+and\s+time)|(time\s+and\s+date)))", re.IGNORECASE)

    def init(self):
        pass

    def match(self):
        self.show = 0

        # Trim if it starts with WH question or tell
        to_match = [self.wh_question, self.tell]

        for regex in to_match:
            if regex.match(self.command):
                self.match_and_reduce(regex)
                break

        # remove the "current" if it exists
        self.match_and_reduce(re.compile("current\s+"))

        # Try to match with one of the regex
        if(self.datetime.match(self.command)):
            self.show = 1
            self.match_and_reduce(self.datetime)
        elif(self.date.match(self.command)):
            self.match_and_reduce(self.date)
            self.show = 2
        elif(self.time.match(self.command)):
            self.match_and_reduce(self.time)
            self.show = 3

        self.match_and_reduce(self.punctuations)

        if len(self.command) == 0:
            self.matched = True

    def get_response(self):
        c_date = time.strftime("%A, %-d %B, %Y")
        c_time = time.strftime("%I:%M %p")

        if(self.show == 1):
            return "The date is {} and time is {}".format(c_date, c_time)
        elif(self.show == 2):
            return "The date is {}".format(c_date)
        elif (self.show == 3):
            return "The time is {}".format(c_time)

    def help_text(self, text):
        pass
