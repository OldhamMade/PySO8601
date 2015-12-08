import os
import sys
import unittest

BASE_PATH = '/'.join(os.path.dirname(
    os.path.abspath(__file__)).split('/')[0:-1])

if BASE_PATH not in sys.path:
    sys.path.insert(1, BASE_PATH)

from PySO8601.utility import (
    _year_month_delta_from_elements
)


class UtilSpec(unittest.TestCase):
    """Util Spec"""
    def it_should_calculate_year_month_deltas_correctly(self):
        result = _year_month_delta_from_elements({'years': 2, 'months': 14})
        self.assertEqual(result, (3, 2))
