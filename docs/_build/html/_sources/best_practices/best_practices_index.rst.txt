
Best Practices
==============


General Concepts
----------------
.. toctree::
   :maxdepth: 2
   :hidden:
   
   Alternative_Standards
   Authentication
   CORS
   Required_and_Additional_Fields
   RESTfulness
   Versioning
   
The :doc:`BrAPI Community </community/BrAPI_Community>` has developed a set of Best Practices when working with :doc:`BrAPI </community/BrAPI>` implementations.

-  :doc:`Alternative Standards </best_practices/Alternative_Standards>` - Notes on conversions and mappings to other existing standards including MIAPPE, ICASA, MCPD, GeoJSON, and GA4GH Variants Schema
-  :doc:`Authentication </best_practices/Authentication>` - Notes on Authentication and Authorization, focusing on OAuth2
-  :doc:`Cross-Origin Resource Sharing (CORS) </best_practices/CORS>` - Notes on common :doc:`CORS <CORS>` errors and how to deal with them
-  :doc:`Required and Additional Fields </best_practices/Required_and_Additional_Fields>` - Notes on Fields and Parameters when they are Required, Added, and Deprecated
-  :doc:`RESTfulness </best_practices/RESTfulness>` - General REST best practices, including notes on HTTP verbs, HTTP status codes, and URL construction.
-  :doc:`Versioning </best_practices/Versioning>` - Notes on BrAPI Versioning Scheme

Implementation Notes
--------------------

.. toctree::
   :maxdepth: 2
   :hidden:
   
   Dates_and_Times
   Object_Identifiers
   Error_Handling
   Location_Coordinates
   Observation_Levels
   Pagination
   Search_Services
   
These are notes on how to correctly implement certain specific concepts in BrAPI.

-  :doc:`Dates and Times </best_practices/Dates_and_Times>` - Notes on encoding Dates and Times
-  :doc:`Object Identifiers </best_practices/Object_Identifiers>` - Notes on DbIds, Names, PUIs, DOIs, and External References
-  :doc:`Error Handling </best_practices/Error_Handling>` - Notes on handling Errors
-  :doc:`Location Coordinates </best_practices/Location_Coordinates>` - Notes on use GPS Coordinates and GeoJSON
-  :doc:`Observation Levels </best_practices/Observation_Levels>` - Notes on how to represent different types of Observation Units (ie, field, plot, plant, etc)
-  :doc:`Pagination </best_practices/Pagination>` - Notes on Pagination
-  :doc:`Search Services </best_practices/Search_Services>` - Notes on Search implementations