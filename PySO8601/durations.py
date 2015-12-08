from .regexs import (SIMPLE_DURATION, COMBINED_DURATION, ELEMENTS)
from .utility import (
    ParseError,
    MONTHS_IN_YEAR,
    _years_to_days,
    _months_to_days,
    _clean,
    _timedelta_from_elements,
    _year_month_delta_from_elements,
)

def parse_duration(duration, start=None, end=None):
    """
    Attepmt to parse an ISO8601 formatted duration.

    Accepts a ``duration`` and optionally a start or end ``datetime``.
    ``duration`` must be an ISO8601 formatted string.

    Returns a ``datetime.timedelta`` object.
    """
    if not start and not end:
        return parse_simple_duration(duration)

    if start:
        return parse_duration_with_start(start, duration)

    if end:
        return parse_duration_with_end(duration, end)


def parse_simple_duration(duration):
    """
    Attepmt to parse an ISO8601 formatted duration, using a naive calculation.

    Accepts a ``duration`` which must be an ISO8601 formatted string, and
    assumes 365 days in a year and 30 days in a month for the calculation.

    Returns a ``datetime.timedelta`` object.
    """
    elements = _parse_duration_string(_clean(duration))

    if not elements:
        raise ParseError()

    return _timedelta_from_elements(elements)


def _parse_duration_string(duration):
    elements = ELEMENTS.copy()

    for pattern in (SIMPLE_DURATION, COMBINED_DURATION):
        if pattern.match(duration):
            found = pattern.match(duration).groupdict()
            del found['time']

            elements.update(dict((k, int(v or 0))
                                 for k, v
                                 in found.items()))

            return elements


def parse_duration_with_start(start, duration):
    """
    Attepmt to parse an ISO8601 formatted duration based on a start datetime.

    Accepts a ``duration`` and a start ``datetime``. ``duration`` must be
    an ISO8601 formatted string.

    Returns a ``datetime.timedelta`` object.
    """
    elements = _parse_duration_string(_clean(duration))
    year, month = _year_month_delta_from_elements(elements)

    end = start.replace(
        year=start.year + year,
        month=start.month + month
    )

    del elements['years']
    del elements['months']

    end += _timedelta_from_elements(elements)

    return start, end - start


def parse_duration_with_end(duration, end):
    """
    Attepmt to parse an ISO8601 formatted duration based on an end datetime.

    Accepts a ``duration`` and an end ``datetime``. ``duration`` must be
    an ISO8601 formatted string.

    Returns a ``datetime.timedelta`` object.
    """
    elements = _parse_duration_string(_clean(duration))
    year, month = _year_month_delta_from_elements(elements)

    start = end.replace(
        year=end.year - year,
        month=end.month - month
    )

    del elements['years']
    del elements['months']

    start -= _timedelta_from_elements(elements)

    return end - start, end
