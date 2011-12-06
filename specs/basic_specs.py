import datetime
import os
import re
import sys
import unittest

print sys.path

BASE_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)

from PySO8601 import parse_date, Timezone

class BasicSpec(unittest.TestCase):
    """ISO8601 Basic Spec"""
    def it_should_parse_combined_date_full_time_z(self):
        result = parse_date('20110113T164400Z')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone()))

    def it_should_parse_separate_date_time_z(self):
        result = parse_date('20110113T1644Z')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone()))

    def it_should_parse_separate_date_full_time(self):
        result = parse_date('20110113T164400')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))

    def it_should_parse_separate_date_time(self):
        result = parse_date('20110113T1644')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))

    def it_should_parse_date_with_week_number(self):
        result = parse_date('2010W052')
        self.assertEqual(result,
                         datetime.datetime(2010, 2, 1))

    def it_should_parse_ordinal_date(self):
        result = parse_date('2000234')
        self.assertEqual(result,
                         datetime.datetime(2000, 8, 21))

    def it_should_parse_simple_dates(self):
        result = parse_date('20070102')
        self.assertEqual(result,
                         datetime.datetime(2007, 1, 2))

    def it_should_parse_simple_short_dates(self):
        result = parse_date('070101')
        self.assertEqual(result,
                         datetime.datetime(2007, 1, 1))

    def it_should_parse_simple_year(self):
        result = parse_date('2006')
        self.assertEqual(result,
                         datetime.datetime(2006, 1, 1))
