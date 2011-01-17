from exceptions import *
from datetimestamps import parse_date, parse_time
from durations import parse_duration
from intervals import parse_interval
from timezones import Timezone
from __version__ import __version__

__all__ = ['parse',
           'parse_date',
           'parse_time',
           'parse_duration',
           'parse_interval',
           'Timezone',
           'ParseError',
           '__version__']


def parse(representation):
    representation = str(representation).upper().strip()

    if '/' in representation:
        return parse_interval(representation)

    if representation[0] is 'P':
        return parse_duration(representation)

    return parse_date(representation)
        
