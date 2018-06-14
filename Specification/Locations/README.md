
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
    "result": {
        "data": [
            {
                "name": "Ibadan",
                "additionalInfo": {
                    "soilDescription": "23",
                    "annualMeanRain": "value"
                },
                "longitude": 165.5,
                "instituteAddress": "route foo, Clermont Ferrand, France",
                "instituteName": "INRA - GDEC",
                "altitude": 12,
                "locationDbId": "abc123",
                "latitude": -21.5,
                "locationType": "Breeding Location",
                "countryCode": "NGA",
                "abbreviation": "IB",
                "countryName": "Nigeria"
            },
            {
                "name": "Goa",
                "additionalInfo": {
                    "name2": "value2",
                    "name1": "value1"
                },
                "abbreviation": "GO",
                "locationDbId": "def456",
                "locationType": "Storage Location",
                "latitude": 28.36,
                "altitude": 10,
                "countryCode": "IND",
                "longitude": 77.12,
                "countryName": "India"
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
        "status": [],
        "datafiles": []
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
    "result": {
        "name": "Ibadan",
        "additionalInfo": {
            "soilDescription": "23",
            "annualMeanRain": "value"
        },
        "abreviation": "IB -- DEPRECATED -- see abbreviation",
        "locationDbId": "abc123",
        "instituteName": "INRA - GDEC",
        "altitude": 12,
        "longitude": 165.5,
        "instituteAddress": "road foo, nigeria",
        "latitude": -21.5,
        "locationType": "Breeding Location",
        "countryCode": "NGA",
        "abbreviation": "IB",
        "countryName": "Nigeria"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0,
            "currentPage": 0
        },
        "status": [],
        "datafiles": []
    }
}
```