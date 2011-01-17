import datetime
import re

from exceptions import *

WEEK_DURATION = re.compile(r'''# start
^P # duration designator
(\d+) # capture the number of weeks
W$ # week designator
''', re.VERBOSE)

SIMPLE_DURATION = re.compile(r"""# start
^P                               # duration designator
(?P<years>(\d*[\.,]?\d+)Y)?      # year designator
(?P<months>(\d*[\.,]?\d+)M)?     # month designator
(?P<days>(\d*[\.,]?\d+)D)?       # day designator
(?P<time>T)?                     # time designator
(?(time)                         # time designator lookup;
                                 #   skip next section if
                                 #   reference doesn't exist
  (?P<hours>(\d*[\.,]?\d+)H)?    # hour designator
  (?P<minutes>(\d*[\.,]?\d+)M)?  # minute designator
  (?P<seconds>(\d*[\.,]?\d+)S)?  # second designator
)
""", re.VERBOSE)

COMBINED_DURATION = re.compile(r"""# start
^P                                 # duration designator
(?P<years>\d{4})?                  # year designator
-?                                 # separator
(?P<months>\d{2})?                 # month designator
-?                                 # separator
(?P<days>\d{2}??                   # day designator
(?P<time>[T|\s])?                  # time designator
(?(time)                           # time designator lookup;
                                   #   skip next section if
                                   #   reference doesn't exist
  (?P<hours>\d{2})?                # hour designator
  :?                               # separator
  (?P<minutes>\d{2})?              # minute designator
  :?                               # separator
  (?P<seconds>\d{2})?              # second designator
)
""", re.VERBOSE)

ELEMENTS = {
    'years': 0,
    'months': 0,
    'days': 0,
    'hours': 0,
    'minutes': 0,
    'seconds': 0,
    }


def parse_duration(duration):
    try:
        return _parse_simple_duration(duration)
    except ParseError:
        pass

    try:
        return _parse_combined_duration(duration)
    except:
        pass

    try:
        return _parse_week_duration(duration)
    except:
        pass

    return ParseError()

def _parse_simple_duration(duration):
    elements = ELEMENTS.copy()

    elements.update(dict((k, int(v[:-1] or 0)) for k,v in SIMPLE_DURATION.match(duration).groupdict().iteritems()))

    return datetime.timedelta(days=(elements['days'] +
                                    _months_to_days(elements['months']) +
                                    _years_to_days(elements['years'])),
                              hours=elements['hours'],
                              minutes=elements['minutes'],
                              seconds=elements['seconds'])

def _parse_combined_duration(duration):
    pass

def _parse_week_duration(duration):
    pass


DAYS_IN_YEAR = 365
MONTHS_IN_YEAR = 12

def _years_to_days(years):
    return years * DAYS_IN_YEAR

def _months_to_days(months):
    return (months * DAYS_IN_YEAR) / MONTHS_IN_YEAR
