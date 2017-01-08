# -*- coding: utf-8 -*-

import re
from datetime import datetime
from pytz import country_timezones, timezone

from hal.library import HalLibrary


class DateTime(HalLibrary):

    name = "Date and Time"
    date = re.compile("(date)", re.IGNORECASE)
    time = re.compile("(time)", re.IGNORECASE)
    datetime = re.compile(
        "(((date\s+and\s+time)|(time\s+and\s+date)))", re.IGNORECASE)
    dayofweek = re.compile("(day(\s+of\s+week)?\s+)")

    pointofref = re.compile("\s*((today)|(now))", re.IGNORECASE)

    def init(self):
        self.timezone = None

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
        if(self.match_and_reduce(self.datetime)):
            self.show = 1
        elif(self.match_and_reduce(self.date)):
            self.show = 2
        elif(self.match_and_reduce(self.time)):
            self.show = 3
        elif(self.match_and_reduce(self.dayofweek)):
            self.show = 4
        else:
            # this match is mandatory
            return

        pointofref = self.match_and_reduce(self.pointofref)

        # Get city name if possible
        if(self.match_and_reduce(re.compile("\s+(in\s+)?(\w+(\/\w+)?)"))):
            city_info = self.last_matched.group(2).strip().lower()
            for tz in country_timezones.items():
                symbol = tz[0].lower()
                for location in tz[1]:
                    llocation = location.lower()
                    if city_info == symbol or city_info == llocation or \
                            city_info in llocation.split("/"):
                        self.timezone = location
                        break
                if self.timezone:
                    break
            else:
                # TODO: Show city not found error here?
                print("Timezone not found")

        if not pointofref:
            # If not specified earlier, try again
            pointofref = self.match_and_reduce(self.pointofref)

        self.match_and_reduce(self.punctuations)

        if len(self.command) == 0:
            self.matched = True

    def get_response(self):
        ref_time = datetime.now()
        ref_text = ""

        if self.timezone:
            ref_time = datetime.now(timezone(self.timezone))
            ref_text = " in " + self.timezone

        suffix = 'th' if 11<=ref_time.day<=13 else {1:'st',2:'nd',3:'rd'}.get(ref_time.day%10, 'th')

        c_date = ref_time.strftime("%A, %-d{} %B, %Y".format(suffix))
        c_time = ref_time.strftime("%I:%M %p")
        c_day = ref_time.strftime("%A")


        output = ""
        if(self.show == 1):
            output =  "The date is {} and time is {}".format(c_date, c_time)
        elif(self.show == 2):
            output =  "The date is {}".format(c_date)
        elif (self.show == 3):
            output =  "The time is {}".format(c_time)
        elif (self.show == 4):
            output =  "The day of week is {}".format(c_day)

        output = output + ref_text
        return output

    def help_text(self, text):
        pass
