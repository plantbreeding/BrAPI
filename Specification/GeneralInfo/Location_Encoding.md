
### Location coordinate encoding

To encode locations as coordinates, the ISO 6709 standard is used, degree notation only. WGS84 is used as the geodetic datum spatial reference system.

||Unit|Format|Example|
|---|---|---|---|
|latitude|degrees|±DD.D|"+40.20361"|
|longitude|degrees|±DDD.D|"-075.00417"|
|altitude|meters|±M|"+127"|

Note:
 + Plus and minus signs are always required
 + Latitude has two digits before the decimal separator (with leading zeros when necessary)
 + Longitude has three digits before the decimal separator (with leading zeros when necessary)
 + Altitude is recorded in meters above the WGS84 reference ellipsoid (no leading zeros) 
