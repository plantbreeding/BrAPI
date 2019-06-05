
# Group Locations

Location calls.




## Locations [/brapi/v1/locations] 




### Get Locations  [GET /brapi/v1/locations{?locationType}{?page}{?pageSize}]

Implemented by: Germinate

Get a list of locations.

* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.

* `altitude` is in meters.

**Note**: Consider revising to describe polygon lat/lan points and check if adopting http://geojson.org/ is worth doing for v1.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|altitude|number|The altitude of this location|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|instituteAddress|string|The street address of the institute representing this location|
|instituteName|string|each institute/laboratory can have several experimental field|
|latitude|number|The latitude of this location|
|locationDbId|string|string identifier|
|locationName|string|A human readable name for this location|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|longitude|number|the longitude of this location|


 

+ Parameters
    + locationType (Optional, ) ... Filter by location type specified.
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 17,
            "totalPages": 9
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "abbreviation": "L1",
                "abreviation": "L1",
                "additionalInfo": {
                    "adm1": "Junin",
                    "adm2": "Chanchamayo",
                    "adm3": "San Ramon",
                    "annualMeanTemperature": "23",
                    "annualTotalPrecipitation": "360",
                    "cont": "South America",
                    "creg": "LAC",
                    "local": "San Ramon"
                },
                "altitude": 828,
                "countryCode": "PER",
                "countryName": "Peru",
                "documentationURL": "https://brapi.org",
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteAdress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute",
                "latitude": -11.1274995803833,
                "locationDbId": "1",
                "locationName": "Location 1",
                "locationType": "Storage location",
                "longitude": -75.35639190673828,
                "name": "Location 1"
            },
            {
                "abbreviation": "L2",
                "abreviation": "L2",
                "additionalInfo": {},
                "altitude": 964,
                "countryCode": "PER",
                "countryName": "Peru",
                "documentationURL": "https://brapi.org",
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteAdress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute",
                "latitude": -11.161160469055176,
                "locationDbId": "2",
                "locationName": "Location 2",
                "locationType": "Breeding location",
                "longitude": -75.34171295166016,
                "name": "Location 2"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Locations by locationDbId  [GET /brapi/v1/locations/{locationDbId}]

Get details for a location.

- The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.

- `altitude` is in meters.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|altitude|number|The altitude of this location|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|instituteAddress|string|The street address of the institute representing this location|
|instituteName|string|each institute/laboratory can have several experimental field|
|latitude|number|The latitude of this location|
|locationDbId|string|string identifier|
|locationName|string|A human readable name for this location|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|longitude|number|the longitude of this location|


 

+ Parameters
    + locationDbId (Required, ) ... The internal DB id for a location
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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
        "abbreviation": "L1",
        "abreviation": "L1",
        "additionalInfo": {
            "adm1": "Junin",
            "adm2": "Chanchamayo",
            "adm3": "San Ramon",
            "annualMeanTemperature": "23",
            "annualTotalPrecipitation": "360",
            "cont": "South America",
            "creg": "LAC",
            "local": "San Ramon"
        },
        "altitude": 828,
        "countryCode": "PER",
        "countryName": "Peru",
        "documentationURL": "https://brapi.org",
        "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
        "instituteAdress": "71 Pilgrim Avenue Chevy Chase MD 20815",
        "instituteName": "Plant Science Institute",
        "latitude": -11.1274995803833,
        "locationDbId": "1",
        "locationName": "Location 1",
        "locationType": "Storage location",
        "longitude": -75.35639190673828,
        "name": "Location 1"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

