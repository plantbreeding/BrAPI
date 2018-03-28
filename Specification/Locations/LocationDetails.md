## Location Details [/brapi/v1/locations/{locationDbId}]

Implemented by:  GnpIS

Get details for a location.

* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.


### Retrieve locations details [GET /brapi/v1/locations/{locationDbId}]
+ Parameters
    + locationDbId (required, string, `abc123`) ... the internal DB id for a location
+ Response 200 (application/json)
        
        {
            "metadata": {
                "pagination": { 
                    "totalCount": 0,
                    "pageSize": 0,
                    "totalPages": 0,
                    "currentPage": 0
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "locationDbId": "abc123",
                "locationType" : "Breeding Location",
                "name": "Ibadan",
                "abreviation": "DEPRECATED -- see abbreviation",
                "abbreviation": "IB",
                "countryCode": "NGA",
                "countryName": "Nigeria",
                "latitude": -21.5,
                "longitude": 165.5,
                "altitude": 12,
                "instituteName": "INRA - GDEC",
                "instituteAddress": "road foo, nigeria",
                "additionalInfo": 
                {
                    "annualMeanRain" : "value", 
                    "soilDescription" :"23"
                }
            }
        }

