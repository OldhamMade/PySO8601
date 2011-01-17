import datetime
import os
import re
import sys
import unittest

print sys.path

BASE_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)
    
from PySO8601 import parse_interval, Timezone

class IntervalSpec(unittest.TestCase):
    """ISO8601 Interval Spec"""
    def it_should_parse_intervals(self):
        a, b = parse_interval('2011-01-13T16:44:00+01:00/P6M4DT12H15M')
        self.assertEqual(a,
                         datetime.datetime(2011, 1, 13, 16, 44, 00,
                                           tzinfo=Timezone('+0100')))
        self.assertEqual(b,
                         datetime.timedelta(days=186,
                                            hours=12,
                                            minutes=15))
