
# Group Locations

Location calls.




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
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationDbId": "abc123",
                "locationType": "Breeding Location",
                "name": "Ibadan",
                "abbreviation": "IB",
                "countryCode": "NGA",
                "countryName": "Nigeria",
                "latitude": -21.5,
                "longitude": 165.5,
                "altitude": 12,
                "instituteName": "INRA - GDEC",
                "instituteAddress": "route foo, Clermont Ferrand, France",
                "additionalInfo": {
                    "annualMeanRain": "value",
                    "soilDescription": "23"
                }
            },
            {
                "locationDbId": "def456",
                "locationType": "Storage Location",
                "name": "Goa",
                "abbreviation": "GO",
                "countryCode": "IND",
                "countryName": "India",
                "latitude": 28.36,
                "longitude": 77.12,
                "altitude": 10,
                "additionalInfo": {
                    "name1": "value1",
                    "name2": "value2"
                }
            }
        ]
    }
}
```

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
    "metadata": {
        "pagination": {
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0,
            "currentPage": 0
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "locationDbId": "abc123",
        "locationType": "Breeding Location",
        "name": "Ibadan",
        "abreviation": "IB -- DEPRECATED -- see abbreviation",
        "abbreviation": "IB",
        "countryCode": "NGA",
        "countryName": "Nigeria",
        "latitude": -21.5,
        "longitude": 165.5,
        "altitude": 12,
        "instituteName": "INRA - GDEC",
        "instituteAddress": "road foo, nigeria",
        "additionalInfo": {
            "annualMeanRain": "value",
            "soilDescription": "23"
        }
    }
}
```