
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
        "locationType": "Breeding Location",
        "latitude": -21.5,
        "instituteAddress": "road foo, nigeria",
        "additionalInfo": {
            "annualMeanRain": "value",
            "soilDescription": "23"
        },
        "abbreviation": "IB",
        "countryCode": "NGA",
        "locationDbId": "abc123",
        "altitude": 12,
        "name": "Ibadan",
        "countryName": "Nigeria",
        "abreviation": "IB -- DEPRECATED -- see abbreviation",
        "longitude": 165.5,
        "instituteName": "INRA - GDEC"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
                "locationType": "Breeding Location",
                "latitude": -21.5,
                "instituteAddress": "route foo, Clermont Ferrand, France",
                "additionalInfo": {
                    "annualMeanRain": "value",
                    "soilDescription": "23"
                },
                "abbreviation": "IB",
                "countryCode": "NGA",
                "locationDbId": "abc123",
                "altitude": 12,
                "name": "Ibadan",
                "countryName": "Nigeria",
                "longitude": 165.5,
                "instituteName": "INRA - GDEC"
            },
            {
                "locationType": "Storage Location",
                "latitude": 28.36,
                "additionalInfo": {
                    "name2": "value2",
                    "name1": "value1"
                },
                "abbreviation": "GO",
                "altitude": 10,
                "locationDbId": "def456",
                "countryCode": "IND",
                "name": "Goa",
                "countryName": "India",
                "longitude": 77.12
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```