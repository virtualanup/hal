# -*- coding: utf-8 -*-

import re
from datetime import datetime
from pytz import country_timezones, timezone

from hal.library import HalLibrary


class DateTime(HalLibrary):

    name = "Date and Time"
    keywords = ["date", "time", "today"]

    date_regex = re.compile("(date)", re.IGNORECASE)
    time_regex = re.compile("(time)", re.IGNORECASE)
    datetime_regex = re.compile(
        "(((date\s+and\s+time)|(time\s+and\s+date)))", re.IGNORECASE)
    dayofweek_regex = re.compile("day(\s+of\s+week)?(\s+)?")

    pointofref_regex = re.compile("\s*((today)|(now))", re.IGNORECASE)

    timezone_regex = re.compile("\s+(in\s+)?(\w+(\/\w+)?)", re.IGNORECASE)

    SHOWDATE = 1
    SHOWTIME = 2
    SHOWDATETIME = 3
    SHOWDAY = 4

    def init(self):
        self.timezones = []

    def match(self):
        self.show = 0

        # Trim if it starts with WH question or tell
        self.match_and_reduce_list([self.wh_question, self.tell], True)

        # remove the "current" if it exists
        self.match_and_reduce(re.compile("current\s+"))

        # Try to match with one of the regex
        if(self.match_and_reduce(self.datetime_regex)):
            self.show = self.SHOWDATETIME
        elif(self.match_and_reduce(self.date_regex)):
            self.show = self.SHOWDATE
        elif(self.match_and_reduce(self.time_regex)):
            self.show = self.SHOWTIME
        elif(self.match_and_reduce(self.dayofweek_regex)):
            self.show = self.SHOWDAY
        else:
            # this match is mandatory
            return

        pointofref = self.match_and_reduce(self.pointofref_regex)

        # Get city name if possible
        if(self.match_and_reduce(self.timezone_regex)):

            # Get the city (or continent) name
            city_info = self.last_matched.group(2).strip().lower()

            for tz in country_timezones.items():
                symbol = tz[0].lower()

                for location in tz[1]:
                    llocation = location.lower()
                    if city_info == symbol or city_info == llocation or \
                            city_info in llocation.split("/"):
                        self.timezones.append(location)

            if not self.timezones:
                # TODO: Show city not found error here?
                print("Timezone not found")
                return

        if not pointofref:
            # If not specified earlier, try again
            pointofref = self.match_and_reduce(self.pointofref_regex)

        self.match_and_reduce(self.punctuations)

        if len(self.command) == 0:
            self.matched = True

    def get_response_timezone(self, cur_timezone=None):
        """
        Get response for certain timezone or system timezone if
        cur_timezone is not passed
        """

        ref_time = datetime.now()
        ref_text = ""

        if cur_timezone:
            # generate text like "New York in America"
            ref_time = datetime.now(timezone(cur_timezone))
            loc = cur_timezone.replace("_", " ").split("/")
            ref_text = " in {} in {}".format(loc[1], loc[0])

        # Suffix for date
        suffix = 'th' if 11 <= ref_time.day <= 13 else {
            1: 'st', 2: 'nd', 3: 'rd'}.get(ref_time.day % 10, 'th')

        c_date = ref_time.strftime("%A, %-d{} %B, %Y".format(suffix))
        c_time = ref_time.strftime("%I:%M %p")
        c_day = ref_time.strftime("%A")

        output = ""
        if(self.show == self.SHOWDATETIME):
            output = "The date is {} and time is {}".format(c_date, c_time)
        elif(self.show == self.SHOWDATE):
            output = "The date is {}".format(c_date)
        elif (self.show == self.SHOWTIME):
            output = "The time is {}".format(c_time)
        elif (self.show == self.SHOWDAY):
            output = "The day of week is {}".format(c_day)

        return output + ref_text

    def get_response(self):
        response = []
        if self.timezones:
            for timezone in self.timezones[:10]:
                response.append(self.get_response_timezone(timezone))
        else:
            response.append(self.get_response_timezone())
        return response

    @classmethod
    def help(cls):
        return {
                "name": "Date and Time",
                "description": "Show date and time information",
                "samples": [
                    "hal show time in london",
                    "hal show date and time",
                    "hal whats today"
                    ]
                }
