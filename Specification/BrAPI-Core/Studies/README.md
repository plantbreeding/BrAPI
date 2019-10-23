
# Group Study

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).

Note that dates should be provided in extended ISO 8601 format (for example, "YYYY-MM-DD").




## Search [/brapi/v1/search] 




### Post Search Studies  [POST /brapi/v1/search/studies]

Get list of studies
StartDate and endDate should be ISO-8601 format for dates
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|locationDbIds|array[string]|List of location names to filter search results|
|programDbIds|array[string]|List of program identifiers to filter search results|
|studyNames|array[string]|List of study names to filter search results|
|sortOrder|string|Order results should be sorted. ex. "ASC" or "DESC"|
|commonCropNames|array[string]|Common names for the crop associated with this study|
|seasonDbIds|array[string]|The ID which uniquely identifies a season|
|sortBy|string|Name of one of the fields within the study object on which results can be sorted|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm|
|trialDbIds|array[string]|List of trial identifiers to filter search results|
|studyTypes|array[string]|The type of study being performed. ex. "Yield Trial", etc|
|studyDbIds|array[string]|List of study identifiers to search for|
|active|boolean|Is this study currently active|
|observationVariableDbIds|array[string]|List of observation variable IDs to search for|
|programNames|array[string]|List of program names to filter search results|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "active": true,
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "germplasmDbIds": [
        "fa4ad588",
        "5731ebe2"
    ],
    "locationDbIds": [
        "d6e7c6a9",
        "8f9f6916"
    ],
    "observationVariableDbIds": [
        "819e508f",
        "f540b703"
    ],
    "programDbIds": [
        "9a855886",
        "51697c22"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "seasonDbIds": [
        "Harvest Two 2017",
        "Summer 2018"
    ],
    "sortBy": [
        "studyDbId",
        "trialDbId",
        "programDbId",
        "locationDbId",
        "seasonDbId",
        "studyType",
        "studyName",
        "studyLocation",
        "programName",
        "germplasmDbId",
        "observationVariableDbId"
    ],
    "sortOrder": [
        "ASC",
        "DESC"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "studyTypes": [
        "Yield Trial",
        "Disease Resistance Trial"
    ],
    "trialDbIds": [
        "29f375a1",
        "753d882b"
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





### Get Search Studies by searchResultsDbId  [GET /brapi/v1/search/studies/{searchResultsDbId}{?page}{?pageSize}]

Get list of studies

StartDate and endDate should be ISO-8601 format for dates

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|location|object||
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteName|string|each institute/laboratory can have several experimental field|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|countryName|string|The full name of the country where this location is|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|altitude|number|The altitude/elevation of this location (in meters)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|additionalInfo|object|Additional arbitrary info|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|parameterName|string|Name of the environment parameter constant within the experiment|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|unit|string|Unit of the value for this parameter|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|studyName|string|The human readable name for a study|
|license|string|The usage license associated with the study data|
|culturalPractices|string|General description of the cultural practices of the study.|
|active|boolean|Is this study currently active|
|endDate|string (date)|The date the study ends|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|trialDbId|string|The ID which uniquely identifies a trial|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|startDate|string (date)|The date this study started|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|commonCropName|string|Common name for the crop associated with this study|
|studyDescription|string|The description of this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|email|string|The contacts email address |
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|additionalInfo|object|Additional arbitrary info|
|trialName|string|The human readable name of a trial|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||


 

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
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Grape",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
                "dataLinks": [
                    {
                        "dataLinkName": "image-archive.zip",
                        "type": "Image Archive",
                        "url": "https://brapi.org/image-archive.zip",
                        "version": "1.0.0"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "environmentParameters": [
                    {
                        "description": "the soil type was clay",
                        "parameterName": "soil type",
                        "parameterPUI": "PECO:0007155",
                        "unit": "pH",
                        "unitPUI": "PECO:0007059",
                        "value": "clay soil",
                        "valuePUI": "ENVO:00002262"
                    }
                ],
                "experimentalDesign": {
                    "PUI": "CO_715:0000145",
                    "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
                },
                "growthFacility": {
                    "PUI": "CO_715:0000162",
                    "description": "field environment condition, greenhouse"
                },
                "lastUpdate": {
                    "timestamp": "2018-01-01T14:47:23-0600",
                    "version": "1.2.3"
                },
                "license": "MIT License",
                "location": {
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
                },
                "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
                "seasons": [
                    "Spring_2018"
                ],
                "startDate": "2018-01-01",
                "studyDbId": "175ac75a",
                "studyDescription": "This is a yield study for Spring 2018",
                "studyName": "Grape_Yield_Spring_2018",
                "studyType": "Phenotyping",
                "trialDbId": "48b327ea",
                "trialName": "Grape_Yield_Trial"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```



## Studytypes [/brapi/v1/studytypes] 




### Get Studytypes  [GET /brapi/v1/studytypes{?page}{?pageSize}]

Call to retrieve the list of study types.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[string]||


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 3,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": null
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



## Studies [/brapi/v1/studies] 




### Get Studies  [GET /brapi/v1/studies{?commonCropName}{?studyType}{?programDbId}{?locationDbId}{?seasonDbId}{?trialDbId}{?studyDbId}{?germplasmDbId}{?observationVariableDbId}{?active}{?sortBy}{?sortOrder}{?page}{?pageSize}]

Get list of studies

StartDate and endDate should be ISO-8601 format for dates



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|location|object||
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteName|string|each institute/laboratory can have several experimental field|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|countryName|string|The full name of the country where this location is|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|altitude|number|The altitude/elevation of this location (in meters)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|additionalInfo|object|Additional arbitrary info|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|parameterName|string|Name of the environment parameter constant within the experiment|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|unit|string|Unit of the value for this parameter|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|studyName|string|The human readable name for a study|
|license|string|The usage license associated with the study data|
|culturalPractices|string|General description of the cultural practices of the study.|
|active|boolean|Is this study currently active|
|endDate|string (date)|The date the study ends|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|trialDbId|string|The ID which uniquely identifies a trial|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|startDate|string (date)|The date this study started|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|commonCropName|string|Common name for the crop associated with this study|
|studyDescription|string|The description of this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|email|string|The contacts email address |
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|additionalInfo|object|Additional arbitrary info|
|trialName|string|The human readable name of a trial|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||


 

+ Parameters
    + commonCropName (Optional, ) ... Common name for the crop associated with this study
    + studyType (Optional, ) ... Filter based on study type unique identifier
    + programDbId (Optional, ) ... Program filter to only return studies associated with given program id.
    + locationDbId (Optional, ) ... Filter by location
    + seasonDbId (Optional, ) ... Filter by season or year
    + trialDbId (Optional, ) ... Filter by trial
    + studyDbId (Optional, ) ... Filter by study DbId
    + germplasmDbId (Optional, ) ... Filter by germplasm DbId
    + observationVariableDbId (Optional, ) ... Filter by observation variable DbId
    + active (Optional, ) ... Filter active status true/false.
    + sortBy (Optional, ) ... Name of the field to sort by.
    + sortOrder (Optional, ) ... Sort order direction. Ascending/Descending.
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
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Grape",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
                "dataLinks": [
                    {
                        "dataLinkName": "image-archive.zip",
                        "type": "Image Archive",
                        "url": "https://brapi.org/image-archive.zip",
                        "version": "1.0.0"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "environmentParameters": [
                    {
                        "description": "the soil type was clay",
                        "parameterName": "soil type",
                        "parameterPUI": "PECO:0007155",
                        "unit": "pH",
                        "unitPUI": "PECO:0007059",
                        "value": "clay soil",
                        "valuePUI": "ENVO:00002262"
                    }
                ],
                "experimentalDesign": {
                    "PUI": "CO_715:0000145",
                    "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
                },
                "growthFacility": {
                    "PUI": "CO_715:0000162",
                    "description": "field environment condition, greenhouse"
                },
                "lastUpdate": {
                    "timestamp": "2018-01-01T14:47:23-0600",
                    "version": "1.2.3"
                },
                "license": "MIT License",
                "location": {
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
                },
                "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
                "seasons": [
                    "Spring_2018"
                ],
                "startDate": "2018-01-01",
                "studyDbId": "175ac75a",
                "studyDescription": "This is a yield study for Spring 2018",
                "studyName": "Grape_Yield_Spring_2018",
                "studyType": "Phenotyping",
                "trialDbId": "48b327ea",
                "trialName": "Grape_Yield_Trial"
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





### Post Studies  [POST /brapi/v1/studies]

Create new studies

Implementation Notes

StartDate and endDate should be ISO-8601 format for dates

`studDbId` is generated by the server.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|location|object||
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteName|string|each institute/laboratory can have several experimental field|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|countryName|string|The full name of the country where this location is|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|altitude|number|The altitude/elevation of this location (in meters)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|additionalInfo|object|Additional arbitrary info|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|parameterName|string|Name of the environment parameter constant within the experiment|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|unit|string|Unit of the value for this parameter|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|studyName|string|The human readable name for a study|
|license|string|The usage license associated with the study data|
|culturalPractices|string|General description of the cultural practices of the study.|
|active|boolean|Is this study currently active|
|endDate|string (date)|The date the study ends|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|trialDbId|string|The ID which uniquely identifies a trial|
|startDate|string (date)|The date this study started|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|commonCropName|string|Common name for the crop associated with this study|
|studyDescription|string|The description of this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|email|string|The contacts email address |
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|additionalInfo|object|Additional arbitrary info|
|trialName|string|The human readable name of a trial|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|location|object||
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteName|string|each institute/laboratory can have several experimental field|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|countryName|string|The full name of the country where this location is|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|altitude|number|The altitude/elevation of this location (in meters)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|additionalInfo|object|Additional arbitrary info|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|parameterName|string|Name of the environment parameter constant within the experiment|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|unit|string|Unit of the value for this parameter|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|studyName|string|The human readable name for a study|
|license|string|The usage license associated with the study data|
|culturalPractices|string|General description of the cultural practices of the study.|
|active|boolean|Is this study currently active|
|endDate|string (date)|The date the study ends|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|trialDbId|string|The ID which uniquely identifies a trial|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|startDate|string (date)|The date this study started|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|commonCropName|string|Common name for the crop associated with this study|
|studyDescription|string|The description of this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|email|string|The contacts email address |
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|additionalInfo|object|Additional arbitrary info|
|trialName|string|The human readable name of a trial|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataLinkName": "image-archive.zip",
                "type": "Image Archive",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.0"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "location": {
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
        },
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "Grape_Yield_Spring_2018",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
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
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Grape",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
                "dataLinks": [
                    {
                        "dataLinkName": "image-archive.zip",
                        "type": "Image Archive",
                        "url": "https://brapi.org/image-archive.zip",
                        "version": "1.0.0"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "environmentParameters": [
                    {
                        "description": "the soil type was clay",
                        "parameterName": "soil type",
                        "parameterPUI": "PECO:0007155",
                        "unit": "pH",
                        "unitPUI": "PECO:0007059",
                        "value": "clay soil",
                        "valuePUI": "ENVO:00002262"
                    }
                ],
                "experimentalDesign": {
                    "PUI": "CO_715:0000145",
                    "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
                },
                "growthFacility": {
                    "PUI": "CO_715:0000162",
                    "description": "field environment condition, greenhouse"
                },
                "lastUpdate": {
                    "timestamp": "2018-01-01T14:47:23-0600",
                    "version": "1.2.3"
                },
                "license": "MIT License",
                "location": {
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
                },
                "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
                "seasons": [
                    "Spring_2018"
                ],
                "startDate": "2018-01-01",
                "studyDbId": "175ac75a",
                "studyDescription": "This is a yield study for Spring 2018",
                "studyName": "Grape_Yield_Spring_2018",
                "studyType": "Phenotyping",
                "trialDbId": "48b327ea",
                "trialName": "Grape_Yield_Trial"
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





### Get Studies by studyDbId  [GET /brapi/v1/studies/{studyDbId}]

Retrieve the information of the study required for field data collection

An additionalInfo field was added to provide a controlled vocabulary for less common data fields.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|location|object||
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteName|string|each institute/laboratory can have several experimental field|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|countryName|string|The full name of the country where this location is|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|altitude|number|The altitude/elevation of this location (in meters)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|additionalInfo|object|Additional arbitrary info|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|parameterName|string|Name of the environment parameter constant within the experiment|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|unit|string|Unit of the value for this parameter|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|studyName|string|The human readable name for a study|
|license|string|The usage license associated with the study data|
|culturalPractices|string|General description of the cultural practices of the study.|
|active|boolean|Is this study currently active|
|endDate|string (date)|The date the study ends|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|trialDbId|string|The ID which uniquely identifies a trial|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|startDate|string (date)|The date this study started|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|commonCropName|string|Common name for the crop associated with this study|
|studyDescription|string|The description of this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|email|string|The contacts email address |
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|additionalInfo|object|Additional arbitrary info|
|trialName|string|The human readable name of a trial|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||


 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
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
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataLinkName": "image-archive.zip",
                "type": "Image Archive",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.0"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "location": {
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
        },
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01",
        "studyDbId": "175ac75a",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "Grape_Yield_Spring_2018",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
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





### Put Studies by studyDbId  [PUT /brapi/v1/studies/{studyDbId}]

Update an existing Study with new data

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|location|object||
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteName|string|each institute/laboratory can have several experimental field|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|countryName|string|The full name of the country where this location is|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|altitude|number|The altitude/elevation of this location (in meters)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|additionalInfo|object|Additional arbitrary info|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|parameterName|string|Name of the environment parameter constant within the experiment|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|unit|string|Unit of the value for this parameter|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|studyName|string|The human readable name for a study|
|license|string|The usage license associated with the study data|
|culturalPractices|string|General description of the cultural practices of the study.|
|active|boolean|Is this study currently active|
|endDate|string (date)|The date the study ends|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|trialDbId|string|The ID which uniquely identifies a trial|
|startDate|string (date)|The date this study started|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|commonCropName|string|Common name for the crop associated with this study|
|studyDescription|string|The description of this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|email|string|The contacts email address |
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|additionalInfo|object|Additional arbitrary info|
|trialName|string|The human readable name of a trial|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|location|object||
|coordinateDescription|string|Describes the precision and landmarks of the coordinate values used for this location. (ex. the site, the nearest town, a 10 kilometers radius circle, +/- 20 meters, etc)|
|instituteName|string|each institute/laboratory can have several experimental field|
|topography|string|Describes the topography of the land at the location. (ex. Plateau, Cirque, Hill, Valley, etc)|
|countryName|string|The full name of the country where this location is|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|altitude|number|The altitude/elevation of this location (in meters)|
|slope|string|Describes the approximate slope (height/distance) of the location.|
|exposure|string|Describes the level of protection/exposure for things like sun light and wind.|
|instituteAddress|string|The street address of the institute representing this location|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|type|string|Feature|
|geometry|object||
|abbreviation|string|An abbreviation which represents this location|
|siteStatus|string|Description of the accessibility of the location (ex. Public, Private)|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|environmentType|string|Describes the general type of environment of the location. (ex. forest, field, nursery, etc)|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location|
|additionalInfo|object|Additional arbitrary info|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string||
|description|string||
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.|
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|parameterName|string|Name of the environment parameter constant within the experiment|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value|
|unit|string|Unit of the value for this parameter|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|studyName|string|The human readable name for a study|
|license|string|The usage license associated with the study data|
|culturalPractices|string|General description of the cultural practices of the study.|
|active|boolean|Is this study currently active|
|endDate|string (date)|The date the study ends|
|observationUnitsDescription|string|The human readable description of the observation units design|
|seasons|array[string]|List of seasons over which this study was performed.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|trialDbId|string|The ID which uniquely identifies a trial|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|startDate|string (date)|The date this study started|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|type|string|The type of external data link|
|url|string (uri)|The URL which links to external data|
|version|string|The version number of the data set.|
|commonCropName|string|Common name for the crop associated with this study|
|studyDescription|string|The description of this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|email|string|The contacts email address |
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|additionalInfo|object|Additional arbitrary info|
|trialName|string|The human readable name of a trial|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string||
|description|string||


 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "active": true,
    "additionalInfo": {},
    "commonCropName": "Grape",
    "contacts": [
        {
            "contactDbId": "5f4e5509",
            "email": "bob@bob.com",
            "instituteName": "The BrAPI Institute",
            "name": "Bob Robertson",
            "orcid": "http://orcid.org/0000-0001-8640-1750",
            "type": "PI"
        }
    ],
    "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
    "dataLinks": [
        {
            "dataLinkName": "image-archive.zip",
            "type": "Image Archive",
            "url": "https://brapi.org/image-archive.zip",
            "version": "1.0.0"
        }
    ],
    "documentationURL": "https://wiki.brapi.org",
    "endDate": "2018-01-01",
    "environmentParameters": [
        {
            "description": "the soil type was clay",
            "parameterName": "soil type",
            "parameterPUI": "PECO:0007155",
            "unit": "pH",
            "unitPUI": "PECO:0007059",
            "value": "clay soil",
            "valuePUI": "ENVO:00002262"
        }
    ],
    "experimentalDesign": {
        "PUI": "CO_715:0000145",
        "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
    },
    "growthFacility": {
        "PUI": "CO_715:0000162",
        "description": "field environment condition, greenhouse"
    },
    "lastUpdate": {
        "timestamp": "2018-01-01T14:47:23-0600",
        "version": "1.2.3"
    },
    "license": "MIT License",
    "location": {
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
    },
    "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
    "seasons": [
        "Spring_2018"
    ],
    "startDate": "2018-01-01",
    "studyDescription": "This is a yield study for Spring 2018",
    "studyName": "Grape_Yield_Spring_2018",
    "studyType": "Phenotyping",
    "trialDbId": "48b327ea",
    "trialName": "Grape_Yield_Trial"
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
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataLinkName": "image-archive.zip",
                "type": "Image Archive",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.0"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "location": {
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
        },
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01",
        "studyDbId": "175ac75a",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "Grape_Yield_Spring_2018",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
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



## Seasons [/brapi/v1/seasons] 




### Get Seasons  [GET /brapi/v1/seasons{?seasonDbId}{?season}{?year}{?page}{?pageSize}]

Call to retrieve all seasons in the database.

A season is made of 2 parts; the primary year and a term which defines a segment of the year. 
This could be a traditional season, like "Spring" or "Summer" or this could be a month, like 
"May" or "June" or this could be an arbitrary season name which is meaningful to the breeding 
program like "PlantingTime_3" or "Season E"



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|


 

+ Parameters
    + seasonDbId (Optional, ) ... The unique identifier for a season. For backward compatibility it can be a string like '2012', '1957-2004'
    + season (Optional, ) ... The term to describe a given season. Example "Spring" OR "May" OR "Planting_Time_7".
    + year (Optional, ) ... The 4 digit year of a season. Example "2017"
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
                "season": "Spring",
                "seasonDbId": "Spring_2018",
                "year": 2018
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

