
# Group Observations

API to manage the details of observation variable Traits. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Trait describes what property is being observed. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Trait "Leaf length" or "Flower height". 





## Search [/brapi/v1/search] 




### Post Search Observations  [POST /brapi/v1/search/observations]

Submit a search request for a set of Observations. Returns an Id which reference the results of this search

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|observationDbIds|array[string]|The unique id of an Observation|
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|trialDbIds|array[string]|list of trials to search across|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|programDbIds|array[string]|list of programs to search across|
|observationUnitDbIds|array[string]|The unique id of an Observation Unit|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "fc55fa61",
        "7f5b77be"
    ],
    "locationDbIds": [
        "071d09d3",
        "6e3fc921"
    ],
    "observationDbIds": [
        "6a4a59d8",
        "3ff067e0"
    ],
    "observationLevel": "plot",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationUnitDbIds": [
        "76f559b5",
        "066bc5d3"
    ],
    "observationVariableDbIds": [
        "a646187d",
        "6d23513b"
    ],
    "programDbIds": [
        "d8ca7076",
        "d56b0b68"
    ],
    "seasonDbIds": [
        "Spring 2018",
        "Season A"
    ],
    "studyDbIds": [
        "222e0bc3",
        "8b24d5aa"
    ],
    "trialDbIds": [
        "918c52f8",
        "378f58e6"
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





### Get Search Observations by searchResultsDbId  [GET /brapi/v1/search/observations/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of Observations based on search criteria.

observationTimeStamp - Iso Standard 8601.

observationValue data type inferred from the ontology



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|observationDbId|string|The ID which uniquely identifies an observation|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


 

+ Parameters
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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



## Observations [/brapi/v1/observations] 




### Get Observations  [GET /brapi/v1/observations{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?page}{?pageSize}]

Retrieve all observations where there are measurements for the given observation variables.

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|observationDbId|string|The ID which uniquely identifies an observation|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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





### Post Observations  [POST /brapi/v1/observations]

Add new Observation entities

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|observationDbId|string|The ID which uniquely identifies an observation|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "collector": "917d3ae0",
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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





### Put Observations  [PUT /brapi/v1/observations]

Update multiple Observation entities simultaneously with a single call

Include as many `observationDbIds` in the request as needed.

Note - In strictly typed languages, this structure can be represented as a Map or Dictionary of objects and parsed directly from JSON.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|observationDbId|string|The ID which uniquely identifies an observation|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{}
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
                "additionalInfo": {},
                "collector": "917d3ae0",
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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





### Get Observations by observationDbId  [GET /brapi/v1/observations/{observationDbId}]

Get the details of a specific Observations

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|observationDbId|string|The ID which uniquely identifies an observation|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


 

+ Parameters
    + observationDbId (Required, ) ... The unique ID of an observation
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
        "additionalInfo": {},
        "collector": "917d3ae0",
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationDbId": "ef24b615",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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





### Put Observations by observationDbId  [PUT /brapi/v1/observations/{observationDbId}]

Update an existing Observation

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationVariableName|string|A human readable name for an observation variable|
|value|string|The value of the data collected as an observation|
|collector|string|The name or identifier of the entity which collected the observation|
|observationUnitName|string|A human readable name for an observation unit|
|additionalInfo|object|Additional arbitrary info|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|observationDbId|string|The ID which uniquely identifies an observation|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|


 

+ Parameters
    + observationDbId (Required, ) ... The unique ID of an observation
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "collector": "917d3ae0",
    "germplasmDbId": "2408ab11",
    "germplasmName": "A0000003",
    "observationTimeStamp": "2018-01-01T14:47:23-0600",
    "observationUnitDbId": "598111d4",
    "observationUnitName": "Plot 1",
    "observationVariableDbId": "c403d107",
    "observationVariableName": "Plant Height in meters",
    "season": {
        "season": "Spring",
        "seasonDbId": "Spring_2018",
        "year": 2018
    },
    "studyDbId": "ef2829db",
    "uploadedBy": "a2f7f60b",
    "value": "2.3"
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
        "additionalInfo": {},
        "collector": "917d3ae0",
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationDbId": "ef24b615",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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





### Get Observations Table  [GET /brapi/v1/observations/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?searchResultsDbId}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}]

<p>This service is designed to retrieve a table of time dependant observation values as a matrix of Observation Units and Observation Variables.
This is also sometimes called a Time Series. This service takes the "Sparse Table" approach for representing this time dependant data.</p>
<p>The table may be represented by JSON, CSV, or TSV. The "Accept" HTTP header is used for the client to request different return formats. 
By default, if the "Accept" header is not included in the request, the server should return JSON as described below.</p>
<p>The table is REQUIRED to have the following columns</p>
<ul>
  <li>observationUnitDbId - Each row is related to one Observation Unit</li>
  <li>observationTimeStamp</li>
  <li>At least one column with an observationVariableDbId</li>
</ul>
<p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p>
<ul>
  <li>observationUnitName</li>
  <li>studyDbId</li>
  <li>studyName</li>
  <li>germplasmDbId</li>
  <li>germplasmName</li>
  <li>plotNumber</li>
  <li>plantNumber</li>
  <li>blockNumber</li>
  <li>entryNumber</li>
  <li>replicate</li>
  <li>positionCoordinateX</li>
  <li>positionCoordinateY</li>
</ul>
<p>The JSON representation provides a pair of extra arrays for defining the headers of the table. 
The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names. 
The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table. 
By appending the two arrays, you can construct the complete header row of the table. </p>
<p>For CSV and TSV representations of the table, an extra header row is needed to describe both the Observation Variable DbId and the Observation Variable Name for each data column. 
See the example responses below</p> 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|headerRow|array[string]|The header row describing observation unit fields. Append "observationVariableDbIds" for complete header row of the table.  This array should contain any or all of the following strings; year, studyDbId, studyName, locationDbId, locationName, germplasmDbId, germplasmName, observationUnitDbId, plotNumber, replicate, blockNumber, entryType, X, Y|
|observationVariableDbIds|array[string]|The list of observation variables which have values recorded for them in the data matrix. Append to the "headerRow" for complete header row.|
|data|array[array]|Matrix of observation data recorded for different observation variables across different observation units|
|observationVariableNames|array[string]|The list of observation variable names which have values recorded for them in the data matrix. Order should match "observationVariableDbIds".|


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + searchResultsDbId (Optional, ) ... Permanent unique identifier which references the search results
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/csv)
```
"\"observationTimeStamp\",\"studyDbId\",\"studyName\",\"germplasmDbId\",\"germplasmName\",\"observationUnitDbId\",\"observationUnitName\",\"plotNumber\",\"plantNumber\",\"blockNumber\",\"entryNumber\",\"replicate\",\"positionCoordinateX\",\"positionCoordinateY\",\"2d599b04\",\"a0e84c5c\",\"35c5670a\",\"0144dea8\"\n\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"Plant height\",\"Carotenoid\",\"Root color\",\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"1.1\", \"\",    \"\", \"\"\n\"2019-09-10T18:14:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"1.9\", \"\",    \"\", \"\"\n\"2019-09-10T18:15:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"1.4\", \"\",    \"\", \"\"\n\"2019-09-10T18:16:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"1.5\", \"\",    \"\", \"\"\n\"2019-09-10T18:17:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"\",    \"2.6\", \"\", \"\"\n\"2019-09-10T18:18:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"\",    \"2.3\", \"\", \"\"\n\"2019-09-10T18:19:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"\",    \"3.1\", \"\", \"\"\n\"2019-09-10T18:20:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"\",    \"3.2\", \"\", \"\""
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
            [
                "2019-09-10T18:13:27.223Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1.1",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:14:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "1.9",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:15:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "1.4",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:16:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "1.5",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:17:27.223Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "",
                "2.6",
                "",
                ""
            ],
            [
                "2019-09-10T18:18:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "",
                "2.3",
                "",
                ""
            ],
            [
                "2019-09-10T18:19:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "",
                "3.1",
                "",
                ""
            ],
            [
                "2019-09-10T18:20:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "",
                "3.2",
                "",
                ""
            ]
        ],
        "headerRow": [
            "observationTimeStamp",
            "studyDbId",
            "studyName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "observationUnitName",
            "plotNumber",
            "plantNumber",
            "blockNumber",
            "entryNumber",
            "replicate",
            "positionCoordinateX",
            "positionCoordinateY"
        ],
        "observationVariableDbIds": [
            "367aa1a9",
            "2acb934c",
            "85a21ce1",
            "46f590e5"
        ],
        "observationVariableNames": [
            "Plant height",
            "Carotenoid",
            "Root color",
            "Virus severity"
        ]
    }
}
```

+ Response 200 (application/tsv)
```
"\"observationTimeStamp\"\t\"studyDbId\"\t\"studyName\"\t\"germplasmDbId\"\t\"germplasmName\"\t\"observationUnitDbId\"\t\"observationUnitName\"\t\"plotNumber\"\t\"plantNumber\"\t\"blockNumber\"\t\"entryNumber\"\t\"replicate\"\t\"positionCoordinateX\"\t\"positionCoordinateY\"\t\"2d599b04\"\t\"a0e84c5c\"\t\"35c5670a\"\t\"0144dea8\"\n\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"Plant height\"\t\"Carotenoid\"\t\"Root color\"\t\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"1.1\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:14:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"1.9\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:15:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"1.4\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:16:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"1.5\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:17:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"\"\t\"2.6\"\t\"\"\t\"\"\n\"2019-09-10T18:18:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"\"\t\"2.3\"\t\"\"\t\"\"\n\"2019-09-10T18:19:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"\"\t\"3.1\"\t\"\"\t\"\"\n\"2019-09-10T18:20:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"\"\t\"3.2\"\t\"\"\t\"\""
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

