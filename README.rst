========
PySO8601
========

PySO8601 aims to be a better Python module to parse ISO 8601 dates. It is inspired 
by the `iso8601`_ currently available in the `pypi repository`_, however this module is 
designed to accept any valid ISO8601 formatted string:

 - `Date`_, including:
   - `Week Dates`_
   - `Ordinal Dates`_
 - `Time`_ including `Time zone designations`_
 - `Combined Date & Time`_
 - `Durations`_
 - `Intervals`_

Truncated representations (``YYYYMM``, ``YYMMDD``, ``hhmmss``, etc) are also accepted.

For full examples on usage please review the `specs`_ in the source.

---------
Durations
---------

Due to the nature of working with calendars, years specified in the duration format are set to 365 days and months are set to 30 days.

.. _iso8601: http://code.google.com/p/pyiso8601
.. _pypi repository: http://pypi.python.org/pypi/iso8601
.. _Date: http://en.wikipedia.org/wiki/ISO_8601#Dates
.. _Week Dates: http://en.wikipedia.org/wiki/ISO_8601#Week_dates
.. _Ordinal Dates: http://en.wikipedia.org/wiki/ISO_8601#Ordinal_dates
.. _Time: http://en.wikipedia.org/wiki/ISO_8601#Times
.. _Time zone designations: http://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators
.. _Combined Date & Time: http://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations
.. _Durations: http://en.wikipedia.org/wiki/ISO_8601#Durations 
.. _Intervals: http://en.wikipedia.org/wiki/ISO_8601#Time_intervals
.. _specs: https://github.com/unpluggd/PySO8601/tree/master/specs
