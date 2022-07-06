Alternative Standards
=====================

MIAPPE
------

Here is the complete list of `MIAPPE to BrAPI Field Mappings <MIAPPE>`__

BrAPI V2 endpoints required to fully support MIAPPE data:

-  GET /trials
-  GET /studies
-  GET /locations
-  GET /germplasm
-  GET /observationunits
-  GET /events
-  GET /samples
-  GET /variables

ICASA
-----

In BrAPI V2.1, the `/events` endpoint was made compatible with the International Consortium for Agricultural Systems Applications (ICASA) controlled vocabulary. 

MCPD
----

Multi-Crop Passport Descriptors (MCPD) "is a widely used international
standard to facilitate germplasm passport information exchange" (
`bioversityinternational.org <https://www.bioversityinternational.org/e-library/publications/detail/faobioversity-multi-crop-passport-descriptors-v21-mcpd-v21/>`__
). In BrAPI, the primary way to share Germplasm data is through the "GET
/germplasm" endpoint. This endpoint has 24 fields out of the available
41 MCPD fields

GeoJSON
-------

GeoJSON is a standard format for defining GPS coordinates and areas. Please see best practices document :doc:`"Location Coordinates" </best_practices/Location_Coordinates>` for more information. 

GA4GH Variants Schema
---------------------

The Global Alliance for Genomics and Health (GA4GH) developed an API schema for managing genotyping data. This schema forms the basis for the BrAPI-Genotyping module, with additions based on community input.
