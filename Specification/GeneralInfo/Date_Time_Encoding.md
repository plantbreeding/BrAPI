
### Date and timestamp fields

Date and timestamp fields are coded in the ISO 8601 standard, extended format. If the field name ends in "Date", only the date portion should be provided, for example "2017-06-16". If a field ends in "Timestamp", the date, time and time zone information needs to be provided, as in this example: "2017-06-16T14:47:23-0600". In version 1, milliseconds are not supported.

-- | Format | Example
--|--|--
Date | yyyy-MM-dd | 2017-06-16
Timestamp | yyyy-MM-ddThh:mm:ssz | 2017-06-16T14:47:23-0600
Timestamp UTC | yyyy-MM-ddThh:mm:ssZ | 2017-06-16T20:47:23Z
