import datetime
import math

DAYS_IN_YEAR = 365
MONTHS_IN_YEAR = 12


class ParseError(Exception):
    """Raised when there is a formatting error with the argument(s)"""
    pass


def _years_to_days(years):
    """Return a naive calculation of 365 * years."""
    return years * DAYS_IN_YEAR


def _months_to_days(months):
    """Return a naive calculation of (months * 365) / 12."""
    return math.floor((months * DAYS_IN_YEAR) / MONTHS_IN_YEAR)


def _clean(item):
    """Return a stripped, uppercase string."""
    return str(item).upper().strip()


def _timedelta_from_elements(elements):
    """
    Return a timedelta from a dict of date elements.

    Accepts a dict containing any of the following:
      - years
      - months
      - days
      - hours
      - minutes
      - seconds

    If years and/or months are provided, it will use a naive calcuation
    of 365 days in a year and 30 days in a month.
    """
    days = sum((
        elements['days'],
        _months_to_days(elements.get('months', 0)),
        _years_to_days(elements.get('years', 0))
    ))

    return datetime.timedelta(days=days,
                              hours=elements.get('hours', 0),
                              minutes=elements.get('minutes', 0),
                              seconds=elements.get('seconds', 0))


def _year_month_delta_from_elements(elements):
    """
    Return a tuple of (years, months) from a dict of date elements.

    Accepts a dict containing any of the following:
      - years
      - months

    Example:

    >>> _year_month_delta_from_elements({'years': 2, 'months': 14})
    (3, 2)
    """
    return divmod(
        (int(elements.get('years', 0)) * MONTHS_IN_YEAR) +
        elements.get('months', 0),
        MONTHS_IN_YEAR
    )
