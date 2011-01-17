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

    def it_should_parse_combined_durations(self):
        result = parse_duration('P0003-06-04T12:30:05')
        self.assertEqual(result,
                         datetime.timedelta(days=1281,
                                            hours=12,
                                            minutes=30,
                                            seconds=5))
