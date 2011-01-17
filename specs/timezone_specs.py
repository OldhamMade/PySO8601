import datetime
import os
import re
import sys
import unittest

print sys.path

BASE_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)
    
from PySO8601 import Timezone

class TimezoneSpec(unittest.TestCase):
    def it_should_init_correctly(self):
        self.assertEqual(str(Timezone()),
                         'UTC')

    def it_should_parse_z(self):
        self.assertEqual(str(Timezone('Z')),
                         'UTC')

    def it_should_parse_plus_hours_mins(self):
        self.assertEqual(str(Timezone('+01:30')),
                         'UTC+01:30')

    def it_should_parse_plus_hours_mins_short(self):
        self.assertEqual(str(Timezone('+0130')),
                         'UTC+01:30')

    def it_should_parse_plus_hours(self):
        self.assertEqual(str(Timezone('+01')),
                         'UTC+01:00')

    def it_should_parse_minus_hours_mins(self):
        self.assertEqual(str(Timezone('-01:30')),
                         'UTC-01:30')

    def it_should_parse_minus_hours_mins_short(self):
        self.assertEqual(str(Timezone('-0130')),
                         'UTC-01:30')

    def it_should_parse_minus_hours(self):
        self.assertEqual(str(Timezone('-01')),
                         'UTC-01:00')
