import datetime
import os
import sys
import unittest

BASE_PATH = '/'.join(os.path.dirname(
    os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)

from PySO8601 import (
    parse_duration,
    parse_duration_with_start,
    parse_duration_with_end
)


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

    def it_should_parse_durations_with_start(self):
        start = datetime.datetime(2000, 1, 1)
        result = parse_duration_with_start(start, 'P3Y')
        self.assertEqual(result,
                         (start, datetime.timedelta(days=1096)))
        result = parse_duration('P3Y', start=start)
        self.assertEqual(result,
                         (start, datetime.timedelta(days=1096)))


    def it_should_parse_complex_durations_with_start(self):
        start = datetime.datetime(2000, 1, 1)
        result = parse_duration_with_start(start, 'P3Y2M3DT1H1M1S')
        self.assertEqual(result,
                         (start, datetime.timedelta(days=1158, seconds=3661)))
        result = parse_duration('P3Y2M3DT1H1M1S', start=start)
        self.assertEqual(result,
                         (start, datetime.timedelta(days=1158, seconds=3661)))


    def it_should_parse_durations_with_end(self):
        end = datetime.datetime(2003, 1, 1)
        result = parse_duration_with_end('P3Y', end)
        self.assertEqual(result,
                         (datetime.timedelta(days=1096), end))
        result = parse_duration('P3Y', end=end)
        self.assertEqual(result,
                         (datetime.timedelta(days=1096), end))


    def it_should_parse_complex_durations_with_end(self):
        end = datetime.datetime(2003, 3, 4, 1, 1, 1)
        result = parse_duration_with_end('P3Y2M3DT1H1M1S', end)
        self.assertEqual(result,
                         (datetime.timedelta(days=1158, seconds=3661), end))
        result = parse_duration('P3Y2M3DT1H1M1S', end=end)
        self.assertEqual(result,
                         (datetime.timedelta(days=1158, seconds=3661), end))
