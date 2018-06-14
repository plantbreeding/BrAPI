
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
        "abbreviation": "IB",
        "locationType": "Breeding Location",
        "name": "Ibadan",
        "instituteName": "INRA - GDEC",
        "altitude": 12,
        "countryName": "Nigeria",
        "countryCode": "NGA",
        "additionalInfo": {
            "soilDescription": "23",
            "annualMeanRain": "value"
        },
        "latitude": -21.5,
        "abreviation": "IB -- DEPRECATED -- see abbreviation",
        "instituteAddress": "road foo, nigeria",
        "locationDbId": "abc123",
        "longitude": 165.5
    },
    "metadata": {
        "pagination": {
            "totalCount": 0,
            "currentPage": 0,
            "totalPages": 0,
            "pageSize": 0
        },
        "datafiles": [],
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
                "abbreviation": "IB",
                "locationType": "Breeding Location",
                "name": "Ibadan",
                "instituteName": "INRA - GDEC",
                "altitude": 12,
                "countryName": "Nigeria",
                "countryCode": "NGA",
                "additionalInfo": {
                    "soilDescription": "23",
                    "annualMeanRain": "value"
                },
                "latitude": -21.5,
                "longitude": 165.5,
                "instituteAddress": "route foo, Clermont Ferrand, France",
                "locationDbId": "abc123"
            },
            {
                "abbreviation": "GO",
                "name": "Goa",
                "locationType": "Storage Location",
                "altitude": 10,
                "countryName": "India",
                "countryCode": "IND",
                "additionalInfo": {
                    "name1": "value1",
                    "name2": "value2"
                },
                "latitude": 28.36,
                "longitude": 77.12,
                "locationDbId": "def456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```