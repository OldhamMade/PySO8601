import datetime
import os
import re
import sys
import unittest

print sys.path

BASE_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)
    
from PySO8601 import parse_duration

class DurationSpec(unittest.TestCase):
    """ISO8601 Duration Spec"""
    def it_should_parse_simple_durations(self):
        result = parse_duration('P3Y6M4DT12H30M5S')
        self.assertEqual(result,
                         datetime.timedelta(days=1281,
                                            hours=12,
                                            minutes=30,
                                            seconds=5))


    def it_should_parse_simple_short_durations(self):
        result = parse_duration('P6M4DT12H15M')
        self.assertEqual(result,
                         datetime.timedelta(days=186,
                                            hours=12,
                                            minutes=15))
                                        

    def it_should_understand_minutes_and_months(self):
        result = parse_duration('P2M')
        self.assertEqual(result,
                         datetime.timedelta(days=60))

        result = parse_duration('PT2M')
        self.assertEqual(result,
                         datetime.timedelta(minutes=2))


    def it_should_parse_combined_durations(self):
        result = parse_duration('P0003-06-04T12:30:05')
        self.assertEqual(result,
                         datetime.timedelta(days=1281,
                                            hours=12,
                                            minutes=30,
                                            seconds=5))


    def it_should_parse_short_combined_durations(self):
        result = parse_duration('P00030604T123005')
        self.assertEqual(result,
                         datetime.timedelta(days=1281,
                                            hours=12,
                                            minutes=30,
                                            seconds=5))
