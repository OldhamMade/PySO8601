import datetime
import os
import sys
import unittest

BASE_PATH = '/'.join(os.path.dirname(
    os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)

from PySO8601 import parse_date, Timezone


class ExtendedSpec(unittest.TestCase):
    """ISO8601 Extended Spec"""
    def it_should_parse_simple_dates(self):
        result = parse_date('2007-01-02')
        self.assertEqual(result,
                         datetime.datetime(2007, 1, 2))

    def it_should_parse_combined_date_full_time_z(self):
        result = parse_date('2011-01-13T16:44:00Z')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone()))

    def it_should_parse_combined_date_full_time_full_tz(self):
        result = parse_date('2011-01-13T16:44:00+01:00')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone('+0100')))

    def it_should_parse_combined_date_full_time_basic_tz(self):
        result = parse_date('2011-01-13T16:44:00+0100')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone('+0100')))

    def it_should_parse_combined_date_full_time_short_tz(self):
        result = parse_date('2011-01-13T16:44:00+01')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone('+0100')))

    def it_should_parse_separate_date_time_z(self):
        result = parse_date('2011-01-13T16:44Z')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone()))

    def it_should_parse_separate_date_full_time(self):
        result = parse_date('2011-01-13T16:44:00')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))

    def it_should_parse_separate_date_full_time_with_fragment(self):
        result = parse_date('2011-01-01T14:32:11.12345')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 1, 14, 32, 11, 12345))

    def it_should_parse_separate_date_time(self):
        result = parse_date('2011-01-13T16:44')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))

    def it_should_parse_date_with_week_number(self):
        result = parse_date('2010-W05-2')
        self.assertEqual(result,
                         datetime.datetime(2010, 2, 1))

    def it_should_parse_date_with_week_number_with_time(self):
        result = parse_date('2010-W05-2T09:10:30')
        self.assertEqual(result,
                         datetime.datetime(2010, 2, 1, 9, 10, 30))

    def it_should_parse_date_with_week_number_with_time_and_fragment(self):
        result = parse_date('2010-W05-2T09:10:30.91')
        self.assertEqual(result,
                         datetime.datetime(2010, 2, 1, 9, 10, 30, 91))

    def it_should_parse_ordinal_date(self):
        result = parse_date('2000-234')
        self.assertEqual(result,
                         datetime.datetime(2000, 8, 21))

    def it_should_parse_ordinal_date_with_time(self):
        result = parse_date('2000-234 04:44:40')
        self.assertEqual(result,
                         datetime.datetime(2000, 8, 21, 4, 44, 40))

    def it_should_parse_ordinal_date_with_time_and_fragment(self):
        result = parse_date('2000-234 04:44:40.444')
        self.assertEqual(result,
                         datetime.datetime(2000, 8, 21, 4, 44, 40, 444))
