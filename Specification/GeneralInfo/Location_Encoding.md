
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
 

#### Image Locations with GeoJSON

The `/images` calls support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
 + With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
 + For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 