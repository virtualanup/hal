# -*- coding: utf-8 -*-

import re
import random

from yahoo_finance import Share
from hal.library import HalLibrary


class StocksLib(HalLibrary):
    """
    Stocks library
    """

    name = "Stocks"
    keywords = ["stock", "share"]

    stock_regex = re.compile(
        "(.*)(stock|share)s?\s(detail)s?", re.IGNORECASE)
    stock_short_regex = re.compile(
        "(.*)(stock|share)s?", re.IGNORECASE)

    def init(self):
        pass

    def process_input(self):
        if self.match_and_reduce(self.stock_regex):
            expressions = self.last_matched.groups()[0].split()
            for expression in expressions:
                if expression:
                    try:
                        # Try getting Stock data
                        service = Share(expression)
                        stock_name = service.get_name()
                        stock_change = service.get_change()
                        stock_change = stock_change[0] + "$" + stock_change[1:]
                        self.add_response("{}".format(stock_name))
                        self.add_response("=" * len(stock_name))
                        self.add_response(
                            "Price: ${} ({}) ({})".format(
                                service.get_price(),
                                stock_change,
                                service.get_percent_change()
                            )
                        )
                        self.add_response(
                            "Open: ${}".format(
                                service.get_open())
                        )
                        self.add_response(
                            "Today's High: ${}".format(
                                service.get_days_high())
                        )
                        self.add_response(
                            "Today's Low: ${}".format(
                                service.get_days_low())
                        )
                        self.add_response(
                            "Market Cap: ${}".format(
                                service.get_market_cap())
                        )
                        self.add_response(
                            "P/E Ratio: {}".format(
                                service.get_price_earnings_ratio())
                        )
                        self.add_response("=" * len(stock_name))
                        self.status = self.SUCCESS
                    except:
                        # Stock Not Found, Fail Silently
                        pass

        if self.match_and_reduce(self.stock_short_regex):
            expressions = self.last_matched.groups()[0].split()
            for expression in expressions:
                if expression:
                    try:
                        # Try getting Stock data
                        service = Share(expression)
                        stock_name = service.get_name()
                        stock_change = service.get_change()
                        stock_change = stock_change[0] + "$" + stock_change[1:]
                        self.add_response(
                            "{}:\t${}\t({}) ({})".format(
                                expression.upper(),
                                service.get_price(),
                                stock_change,
                                service.get_percent_change()
                            )
                        )
                        self.status = self.SUCCESS
                    except:
                        # Stock Not Found, Fail Silently
                        pass

    def process(self):
        pass

    @classmethod
    def help(cls):
        return {
            "name": "Stocks",
            "description": "Stock prices",
            "samples": [
                    "tsla stock",
                    "goog spy aapl stock detail",
                    "goog spy aapl stocks",
            ]
        }
