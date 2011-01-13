import datetime
import os
import re
import sys
import unittest

print sys.path

BASE_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)
    
from PySO8601 import parse_interval

class IntervalSpec(unittest.TestCase):
    """ISO8601 Interval Spec"""
    def it_should_parse_intervals(self):
        assert False
