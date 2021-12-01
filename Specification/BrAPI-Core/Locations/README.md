
# Group Locations

Location calls.





### Get - /locations [GET /brapi/v2/locations{?locationType}{?locationDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a list of locations.
* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


 

+ Parameters
    + locationType (Optional, ) ... Filter by location type specified.
    + locationDbId (Optional, ) ... Filter by location DbId
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. Use this parameter to only return results associated with the given program. Use `GET /programs` to find the list of available programs on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Reference issue number 460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceId (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "coordinateDescription": "North East corner of greenhouse",
                "coordinateUncertainty": "20",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
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




### Post - /locations [POST /brapi/v2/locations]

Add new locations to database
* The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
* `altitude` is in meters.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "abbreviation": "L1",
        "additionalInfo": {},
        "coordinateDescription": "North East corner of greenhouse",
        "coordinateUncertainty": "20",
        "coordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
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
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
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
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "coordinateDescription": "North East corner of greenhouse",
                "coordinateUncertainty": "20",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
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




### Get - /locations/{locationDbId} [GET /brapi/v2/locations/{locationDbId}]

Get details for a location.
- The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
- `altitude` is in meters.'



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


 

+ Parameters
    + locationDbId (Required, ) ... The internal DB id for a location
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "coordinateDescription": "North East corner of greenhouse",
        "coordinateUncertainty": "20",
        "coordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
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
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
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




### Put - /locations/{locationDbId} [PUT /brapi/v2/locations/{locationDbId}/]

Update the details for an existing location.
- The `countryCode` is as per [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec.
- `altitude` is in meters.'

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


 

+ Parameters
    + locationDbId (Required, ) ... The internal DB id for a location
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "abbreviation": "L1",
    "additionalInfo": {},
    "coordinateDescription": "North East corner of greenhouse",
    "coordinateUncertainty": "20",
    "coordinates": {
        "geometry": {
            "coordinates": [
                -76.506042,
                42.417373,
                123
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
    "externalReferences": [
        {
            "referenceId": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceId": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        }
    ],
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
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "coordinateDescription": "North East corner of greenhouse",
        "coordinateUncertainty": "20",
        "coordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
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
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
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




### Post - /search/locations [POST /brapi/v2/search/locations]

Submit a search request for `Locations`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/locations/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviations|array[string]|An abbreviation which represents this location|
|altitudeMax|number|The maximum altitude to search for|
|altitudeMin|number|The minimum altitude to search for|
|commonCropNames|array[string]|The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.|
|coordinates|object|A GeoJSON Polygon which describes an area to search for other GeoJSON objects. All contained Points and intersecting Polygons should be returned as search results.   All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCodes|array[string]|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryNames|array[string]|The full name of the country to search for|
|externalReferenceIDs|array[string]|**Deprecated in v2.1** Please use `externalReferenceIds`. Reference issue number 460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceIds|array[string]|List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceSources|array[string]|List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)|
|instituteAddresses|array[string]|The street address of the institute to search for|
|instituteNames|array[string]|The name of the institute to search for|
|locationDbIds|array[string]|The location ids to search for|
|locationNames|array[string]|A human readable names to search for|
|locationTypes|array[string]|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.|
|programNames|array[string]|Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


 

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
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "coordinates": {
        "geometry": {
            "coordinates": [
                [
                    [
                        -77.456654,
                        42.241133
                    ],
                    [
                        -75.414133,
                        41.508282
                    ],
                    [
                        -76.506042,
                        42.417373
                    ],
                    [
                        -77.456654,
                        42.241133
                    ]
                ]
            ],
            "type": "Polygon"
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
    "externalReferenceIDs": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceIds": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceSources": [
        "DOI",
        "Field App Name"
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
    ],
    "page": 0,
    "pageSize": 1000,
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "coordinateDescription": "North East corner of greenhouse",
                "coordinateUncertainty": "20",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
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

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/locations/{searchResultsDbId} [GET /brapi/v2/search/locations/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Locations` search request <br/>
Clients should submit a search request using the corresponding `POST /search/location` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|abbreviation|string|An abbreviation which represents this location|
|additionalInfo|object|Additional arbitrary info|
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|countryCode|string| [ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|countryName|string|The full name of the country where this location is  MIAPPE V1.1 (DM-17) Geographic location (country) - The country where the experiment took place, either as a full name or preferably as a 2-letter code.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Reference issue number 460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|instituteAddress|string|The street address of the institute representing this location  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|instituteName|string|Each institute/laboratory can have several experimental field  MIAPPE V1.1 (DM-16) Contact institution - Name and address of the institution responsible for the study.|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "coordinateDescription": "North East corner of greenhouse",
                "coordinateUncertainty": "20",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
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
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
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

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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

