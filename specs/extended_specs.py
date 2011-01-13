import datetime
import os
import re
import sys
import unittest

print sys.path

BASE_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)
    
from PySO8601 import parse_date

class ExtendedSpec(unittest.TestCase):
    """ISO8601 Extended Spec"""
    def it_should_parse_dates(self):
        result = parse_date('2007-01-02')
        self.assertEqual(result,
                         datetime.datetime(2007, 1, 2))

    def it_should_parse_combined_date_full_time_z(self):
        result = parse_date('2011-01-13T16:44:00Z')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))
        
    def it_should_parse_separate_date_time_z(self):
        result = parse_date('2011-01-13T16:44Z')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))

    def it_should_parse_separate_date_full_time(self):
        result = parse_date('2011-01-13T16:44:00')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))

    def it_should_parse_separate_date_time(self):
        result = parse_date('2011-01-13T16:44')
        self.assertEqual(result,
                         datetime.datetime(2011, 1, 13, 16, 44, 00))

    def it_should_parse_date_with_week_number(self):
        assert False
        
    def it_should_parse_ordinal_date(self):
        assert False
