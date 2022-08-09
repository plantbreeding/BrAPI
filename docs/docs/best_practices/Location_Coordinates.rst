Location Coordinates
====================

GeoJSON
-------

To encode locations as coordinates, BrAPI follows the `GeoJSON <https://geojson.org/>`__ standard `RFC 7946 <https://tools.ietf.org/html/rfc7946>`__.
`WGS84 <https://en.wikipedia.org/wiki/World_Geodetic_System>`__ is used as the geodetic datum spatial reference system and is the default used
by most GPS tools. The BrAPI spec for `GeoJSON <https://geojson.org/>`__ only supports two of the possible geometries: **Points** and **Polygons**.

A **Point** is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, precisely in that
order and using decimal numbers. Altitude or elevation MAY be included as an optional third element, and is recorded in meters above the
`WGS84 <https://en.wikipedia.org/wiki/World_Geodetic_System>`__ reference ellipsoid.

Point Example:

.. code-block:: json

    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [ 42.444230, -76.463130, 123.00 ]
        }
    }


A **Polygon** is an array of Linear Rings, with each Linear Ring defined
as an array of Points. In this structure, a Polygon can include one or
many geometric shapes which might be overlapping or separate.

Polygon Example: 

.. code-block:: json

  {
    "type": "Feature",
    "geometry": {
      "type": "Polygon",
      "coordinates": [
                     [
                       [ -77.456654, 42.241133, 123.00 ],
                       [ -75.414133, 41.508282, 123.00 ],
                       [ -76.506042, 42.417373, 123.00 ],
                       [ -77.456654, 42.241133, 123.00 ]
                     ]
                   ]
    }
  }



**Note for Image Locations**

-  With most images, the **Point** geometry should be used, and it
   should indicate the longitude and latitude of the camera.
-  For top down images (ie from drones, cranes, etc), the **Point**
   geometry may be used to indicate the longitude and latitude of the
   centroid of the image content, and the **Polygon** geometry may be
   used to indicate the border of the image content.

BrAPI V1 Location Encoding
--------------------------

Simple coordinate system with GPS values only, no structure.

