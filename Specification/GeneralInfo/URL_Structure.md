### URL structure

API requests are structured as 

"https://_\<server\>_/brapi/v1/_\<call\>_"

where "v1" is the major version number of the API, followed by the desired REST call.
  
Example: https://test-server.brapi.org/brapi/v1/markerprofiles/2939 

To distinguish between multiple databases available from the same server, include the database name as part of the "\<server\>" identifier. An arbitrary number of levels can be inserted between the domain name and the brapi level, if needed.

Example: test-server.brapi.org/maize\_db\_01/brapi/v1/markerprofiles/2939
Example: test-server.brapi.org/cornell/cips/wheat_db/brapi/v1/markerprofiles/2939