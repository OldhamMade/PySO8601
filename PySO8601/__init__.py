"""
Years:
    YYYY
Calendar Dates:
    YYYY-MM-DD
    YYYY-MM
    YYYYMMDD
    YYMMDD
Week Dates:
    YYYY-Www-D
    YYYY-Www
    YYYYWwwD
    YYYYWww
Ordinal Dates:
    YYYY-DDD
    YYYYDDD
Times:
    hh:mm:ss
    hh:mm
    hhmmss
    hhmm
    <time>Z
    <time>+|-hh:mm
    <time>+|-hhmm
    <time>+|-hh
"""

import datetime

__all__ = ['parse']

EXTENDED_DATE_FORMATS = {
    10: ['%Y-%m-%d', '%Y-W%U%w'],
    9: ['%YW%U%w', '%Y-W%U'],
    8: [],
}

BASIC_DATE_FORMATS = {
    8: ['%Y%m%d', '%YW%U']
}

PERIOD_FORMATS = {
}

class ParseError(Exception):
    pass

def parse_date(datestring):
    datestring = str(datestring).strip()

    if not datestring[0].isdigit():
        raise ParseError
        
    if 'W' in datestring.upper() and '-' in datestring:
        try:
            datestring = datestring[:-1] + str(int(datestring[-1:]) -1)
        except:
            pass
        
    for pattern in EXTENDED_DATE_FORMATS[len(datestring)]:
        return datetime.datetime.strptime(datestring, pattern)
        
        
def parse_extended_date(datestring):
    pass
    
    
def parse_basic_date(datestring):
    pass


def parse_time(timestring):
    pass


def parse_extended_time(timestring):
    pass
    

def parse_basic_time(timestring):


def parse_timezone(tz):
    pass


def parse_duration(datestring):
    pass


def parse_interval(datestring):
    pass
        
