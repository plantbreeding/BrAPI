
# Group Locations

Location calls.




## Locations [/brapi/v1/locations] 




### Get Locations  [GET /brapi/v1/locations{?locationType}{?page}{?pageSize}]

Get a list of locations.
* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|instituteName|string|each institute/laboratory can have several experimental field|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|altitude|number|The altitude/elevation of this location (in meters)|
|locationName|string|A human readable name for this location|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|locationDbId|string|The unique identifier for a Location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteAddress|string|The street address of the institute representing this location|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|additionalInfo|object|Additional arbitrary info|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|


 

+ Parameters
    + locationType (Optional, ) ... Filter by location type specified.
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "abbreviation": "L1",
                "additionalInfo": {},
                "altitude": 35.6,
                "coordinateDescription": "North East corner of greenhouse",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
                "countryCode": "PER",
                "countryName": "Peru",
                "documentationURL": "https://brapi.org",
                "environmentType": "Nursery",
                "exposure": "Structure, no exposure",
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "locationType": "Storage Location",
                "siteStatus": "Private",
                "slope": "0",
                "topography": "Valley"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Post Locations  [POST /brapi/v1/locations]

Add new locations to database
* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|instituteName|string|each institute/laboratory can have several experimental field|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|altitude|number|The altitude/elevation of this location (in meters)|
|locationName|string|A human readable name for this location|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteAddress|string|The street address of the institute representing this location|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|additionalInfo|object|Additional arbitrary info|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|instituteName|string|each institute/laboratory can have several experimental field|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|altitude|number|The altitude/elevation of this location (in meters)|
|locationName|string|A human readable name for this location|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|locationDbId|string|The unique identifier for a Location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteAddress|string|The street address of the institute representing this location|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|additionalInfo|object|Additional arbitrary info|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "abbreviation": "L1",
        "additionalInfo": {},
        "altitude": 35.6,
        "coordinateDescription": "North East corner of greenhouse",
        "coordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "countryCode": "PER",
        "countryName": "Peru",
        "documentationURL": "https://brapi.org",
        "environmentType": "Nursery",
        "exposure": "Structure, no exposure",
        "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
        "instituteName": "Plant Science Institute",
        "locationName": "Location 1",
        "locationType": "Storage Location",
        "siteStatus": "Private",
        "slope": "0",
        "topography": "Valley"
    }
]
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "abbreviation": "L1",
                "additionalInfo": {},
                "altitude": 35.6,
                "coordinateDescription": "North East corner of greenhouse",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
                "countryCode": "PER",
                "countryName": "Peru",
                "documentationURL": "https://brapi.org",
                "environmentType": "Nursery",
                "exposure": "Structure, no exposure",
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "locationType": "Storage Location",
                "siteStatus": "Private",
                "slope": "0",
                "topography": "Valley"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Locations by locationDbId  [GET /brapi/v1/locations/{locationDbId}]

Get details for a location.
- The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
- `altitude` is in meters.'



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|instituteName|string|each institute/laboratory can have several experimental field|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|altitude|number|The altitude/elevation of this location (in meters)|
|locationName|string|A human readable name for this location|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|locationDbId|string|The unique identifier for a Location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteAddress|string|The street address of the institute representing this location|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|additionalInfo|object|Additional arbitrary info|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|


 

+ Parameters
    + locationDbId (Required, ) ... The internal DB id for a location
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "abbreviation": "L1",
        "additionalInfo": {},
        "altitude": 35.6,
        "coordinateDescription": "North East corner of greenhouse",
        "coordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "countryCode": "PER",
        "countryName": "Peru",
        "documentationURL": "https://brapi.org",
        "environmentType": "Nursery",
        "exposure": "Structure, no exposure",
        "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
        "instituteName": "Plant Science Institute",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "locationType": "Storage Location",
        "siteStatus": "Private",
        "slope": "0",
        "topography": "Valley"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Put Locations by locationDbId  [PUT /brapi/v1/locations/{locationDbId}]

Update the details for an existing location.
- The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
- `altitude` is in meters.'

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|instituteName|string|each institute/laboratory can have several experimental field|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|altitude|number|The altitude/elevation of this location (in meters)|
|locationName|string|A human readable name for this location|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteAddress|string|The street address of the institute representing this location|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|additionalInfo|object|Additional arbitrary info|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|instituteName|string|each institute/laboratory can have several experimental field|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|altitude|number|The altitude/elevation of this location (in meters)|
|locationName|string|A human readable name for this location|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|locationDbId|string|The unique identifier for a Location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteAddress|string|The street address of the institute representing this location|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|additionalInfo|object|Additional arbitrary info|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|


 

+ Parameters
    + locationDbId (Required, ) ... The internal DB id for a location
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "abbreviation": "L1",
    "additionalInfo": {},
    "altitude": 35.6,
    "coordinateDescription": "North East corner of greenhouse",
    "coordinates": {
        "geometry": {
            "coordinates": [
                -76.506042,
                42.417373
            ],
            "type": "Point"
        },
        "type": "Feature"
    },
    "countryCode": "PER",
    "countryName": "Peru",
    "documentationURL": "https://brapi.org",
    "environmentType": "Nursery",
    "exposure": "Structure, no exposure",
    "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
    "instituteName": "Plant Science Institute",
    "locationName": "Location 1",
    "locationType": "Storage Location",
    "siteStatus": "Private",
    "slope": "0",
    "topography": "Valley"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "abbreviation": "L1",
        "additionalInfo": {},
        "altitude": 35.6,
        "coordinateDescription": "North East corner of greenhouse",
        "coordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "countryCode": "PER",
        "countryName": "Peru",
        "documentationURL": "https://brapi.org",
        "environmentType": "Nursery",
        "exposure": "Structure, no exposure",
        "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
        "instituteName": "Plant Science Institute",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "locationType": "Storage Location",
        "siteStatus": "Private",
        "slope": "0",
        "topography": "Valley"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```



## Search [/brapi/v1/search] 




### Post Search Locations  [POST /brapi/v1/search/locations]

Advanced searching for the locations resource.
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|altitudeMax|number|The maximum altitude to search for|
|instituteNames|array[string]|The name of the institute to search for|
|coordinatesArea|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|countryNames|array[string]|The full name of the country to search for|
|locationTypes|array[string]|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|locationDbIds|array[string]|The location ids to search for|
|abbreviations|array[string]|An abbreviation which represents this location|
|instituteAddresses|array[string]|The street address of the institute to search for|
|locationNames|array[string]|A human readable names to search for|
|altitudeMin|number|The minimum altitude to search for|
|countryCodes|array[string]|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "abbreviations": [
        "L1",
        "LHC"
    ],
    "altitudeMax": 200,
    "altitudeMin": 20,
    "coordinatesArea": {
        "geometry": {
            "coordinates": [
                -76.506042,
                42.417373
            ],
            "type": "Point"
        },
        "type": "Feature"
    },
    "countryCodes": [
        "USA",
        "PER"
    ],
    "countryNames": [
        "United States of America",
        "Peru"
    ],
    "instituteAddresses": [
        "123 Main Street",
        "456 Side Street"
    ],
    "instituteNames": [
        "The Institute",
        "The Other Institute"
    ],
    "locationDbIds": [
        "b28911cf",
        "5071d1e4"
    ],
    "locationNames": [
        "Location Alpha",
        "The Large Hadron Collider"
    ],
    "locationTypes": [
        "Nursery",
        "Storage Location"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "searchResultDbId": "551ae08c"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Search Locations by searchResultsDbId  [GET /brapi/v1/search/locations/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the locations resource.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|instituteName|string|each institute/laboratory can have several experimental field|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|altitude|number|The altitude/elevation of this location (in meters)|
|locationName|string|A human readable name for this location|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|locationDbId|string|The unique identifier for a Location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteAddress|string|The street address of the institute representing this location|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|additionalInfo|object|Additional arbitrary info|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "abbreviation": "L1",
                "additionalInfo": {},
                "altitude": 35.6,
                "coordinateDescription": "North East corner of greenhouse",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
                "countryCode": "PER",
                "countryName": "Peru",
                "documentationURL": "https://brapi.org",
                "environmentType": "Nursery",
                "exposure": "Structure, no exposure",
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "locationType": "Storage Location",
                "siteStatus": "Private",
                "slope": "0",
                "topography": "Valley"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

