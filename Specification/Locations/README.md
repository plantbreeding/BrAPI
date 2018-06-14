
# Group Locations

Location calls.




## Locations/{locationdbid} [Get /brapi/v1/locations/{locationDbId}]

 <strong>Implemented by:</strong>  GnpIS
Get details for a location.
* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.  

+ Parameters
    + locationDbId (Required, string) ... The internal DB id for a location


+ Response 200 (application/json)
```
{
    "result": {
        "countryCode": "NGA",
        "altitude": 12,
        "abreviation": "IB -- DEPRECATED -- see abbreviation",
        "locationType": "Breeding Location",
        "instituteName": "INRA - GDEC",
        "abbreviation": "IB",
        "instituteAddress": "road foo, nigeria",
        "locationDbId": "abc123",
        "longitude": 165.5,
        "name": "Ibadan",
        "latitude": -21.5,
        "countryName": "Nigeria",
        "additionalInfo": {
            "annualMeanRain": "value",
            "soilDescription": "23"
        }
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": []
    }
}
```

## Locations [Get /brapi/v1/locations{?locationType}{?pageSize}{?page}]


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
    "result": {
        "data": [
            {
                "countryCode": "NGA",
                "altitude": 12,
                "locationType": "Breeding Location",
                "instituteName": "INRA - GDEC",
                "abbreviation": "IB",
                "instituteAddress": "route foo, Clermont Ferrand, France",
                "locationDbId": "abc123",
                "longitude": 165.5,
                "name": "Ibadan",
                "latitude": -21.5,
                "countryName": "Nigeria",
                "additionalInfo": {
                    "annualMeanRain": "value",
                    "soilDescription": "23"
                }
            },
            {
                "countryCode": "IND",
                "altitude": 10,
                "locationType": "Storage Location",
                "abbreviation": "GO",
                "locationDbId": "def456",
                "longitude": 77.12,
                "name": "Goa",
                "latitude": 28.36,
                "countryName": "India",
                "additionalInfo": {
                    "name1": "value1",
                    "name2": "value2"
                }
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
    }
}
```