from PySO8601.utility import ParseError
from PySO8601.datetimestamps import parse_date, parse_time
from PySO8601.durations import parse_duration
from PySO8601.intervals import parse_interval
from PySO8601.timezones import Timezone
from PySO8601.__version__ import __version__

__all__ = ['parse',
           'parse_date',
           'parse_time',
           'parse_duration',
           'parse_interval',
           'Timezone',
           'ParseError',
           '__version__']


def parse(representation):
    """Attempts to parse an ISO8601 formatted ``representation`` string,
    which could be of any valid ISO8601 format (date, time, duration,
    interval).

    Return value is specific to ``representation``.
    """
    representation = str(representation).upper().strip()

    if '/' in representation:
        return parse_interval(representation)

    if representation[0] is 'P':
        return parse_duration(representation)

    return parse_date(representation)
