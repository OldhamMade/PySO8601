PySO8601
========

PySO8601 aims to be a better Python module to parse ISO 8601 dates. It is inspired 
by the [iso8601](http://code.google.com/p/pyiso8601) currently available in the 
[pypi repository](http://pypi.python.org/pypi/iso8601), however this module is 
designed to accept any valid ISO8601 formatted string:

 - [Date](http://en.wikipedia.org/wiki/ISO_8601#Dates), including:
   - [Week Dates](http://en.wikipedia.org/wiki/ISO_8601#Week_dates)
   - [Ordinal Dates](http://en.wikipedia.org/wiki/ISO_8601#Ordinal_dates)
 - [Time](http://en.wikipedia.org/wiki/ISO_8601#Times) including [Time zone designations](http://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators)
 - [Combined Date & Time](http://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations)
 - [Durations](http://en.wikipedia.org/wiki/ISO_8601#Durations)
 - [Intervals](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)

Truncated representations (`YYYYMM`, `YYMMDD`, `hhmmss`, etc) are also accepted.

Durations
---------

Due to the nature of working with calendars, years specified in the duration format are set to 365 days and months are set to 30 days.
