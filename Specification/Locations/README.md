
# Group Locations

Location calls.




## Get Locations  [GET /brapi/v1/locations{?locationType}{?pageSize}{?page}]


Implemented by: Germinate
Get a list of locations.
* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.
**Note**: Consider revising to describe polygon lat/lan points and check if adopting http://geojson.org/ is worth doing for v1.  

+ Parameters
    + locationType (Optional, string) ... Filter by location type specified.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "abbreviation": "IB",
                "additionalInfo": {
                    "annualMeanRain": "value",
                    "soilDescription": "23"
                },
                "altitude": 12,
                "countryCode": "NGA",
                "countryName": "Nigeria",
                "instituteAddress": "route foo, Clermont Ferrand, France",
                "instituteName": "INRA - GDEC",
                "latitude": -21.5,
                "locationDbId": "abc123",
                "locationType": "Breeding Location",
                "longitude": 165.5,
                "name": "Ibadan"
            },
            {
                "abbreviation": "GO",
                "additionalInfo": {
                    "name1": "value1",
                    "name2": "value2"
                },
                "altitude": 10,
                "countryCode": "IND",
                "countryName": "India",
                "latitude": 28.36,
                "locationDbId": "def456",
                "locationType": "Storage Location",
                "longitude": 77.12,
                "name": "Goa"
            }
        ]
    }
}
```

## Get Locations by locationDbId  [GET /brapi/v1/locations/{locationDbId}]

 <strong>Implemented by:</strong>  GnpIS
Get details for a location.
* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.  

+ Parameters
    + locationDbId (Required, string) ... The internal DB id for a location


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "abbreviation": "IB",
        "abreviation": "IB -- DEPRECATED -- see abbreviation",
        "additionalInfo": {
            "annualMeanRain": "value",
            "soilDescription": "23"
        },
        "altitude": 12,
        "countryCode": "NGA",
        "countryName": "Nigeria",
        "instituteAddress": "road foo, nigeria",
        "instituteName": "INRA - GDEC",
        "latitude": -21.5,
        "locationDbId": "abc123",
        "locationType": "Breeding Location",
        "longitude": 165.5,
        "name": "Ibadan"
    }
}
```