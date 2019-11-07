# Group Crosses




## Put - /crosses [/brapi/v1//crosses] 



### /crosses [PUT /brapi/v1/crosses]

Update existing Cross entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|crossAttributes|array[object]|Set of custom attributes associated with a cross|
|crossAttributeName|string|the human readable name of a cross attribute|
|crossAttributeValue|string|the value of a cross attribute|
|crossDbId|string|the unique identifier for a cross|
|crossName|string|the human readable name for a cross|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|pollinationTimeStamp|string (date-time)|the timestamp when the polination took place|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "d105fd6f": {
        "additionalInfo": {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
        },
        "crossAttributes": [
            {
                "crossAttributeName": "string",
                "crossAttributeValue": "string"
            }
        ],
        "crossName": "myIbadanCrosses2018_01",
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "myIbadanCrosses2018",
        "parent1": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "myIbadanPlot9001",
            "parentType": "MALE"
        },
        "parent2": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "myIbadanPlot9001",
            "parentType": "MALE"
        },
        "pollinationTimeStamp": "2019-08-15T15:49:00.327Z"
    }
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
        "data": [
            {
                "additionalInfo": {},
                "crossAttributes": [
                    {
                        "crossAttributeName": "crossAttributeName",
                        "crossAttributeValue": "crossAttributeValue"
                    }
                ],
                "crossDbId": "d105fd6f",
                "crossName": "myIbadanCrosses2018_01",
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "myIbadanCrosses2018",
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "myIbadanPlot9001",
                    "parentType": [
                        "MALE",
                        "FEMALE",
                        "SELF",
                        "POPULATION"
                    ]
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "myIbadanPlot9001",
                    "parentType": [
                        "MALE",
                        "FEMALE",
                        "SELF",
                        "POPULATION"
                    ]
                },
                "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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


## Post - /crosses [/brapi/v1//crosses] 



### /crosses [POST /brapi/v1/crosses]

Create new Cross entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|crossAttributes|array[object]|Set of custom attributes associated with a cross|
|crossAttributeName|string|the human readable name of a cross attribute|
|crossAttributeValue|string|the value of a cross attribute|
|crossName|string|the human readable name for a cross|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|pollinationTimeStamp|string (date-time)|the timestamp when the polination took place|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|crossAttributes|array[object]|Set of custom attributes associated with a cross|
|crossAttributeName|string|the human readable name of a cross attribute|
|crossAttributeValue|string|the value of a cross attribute|
|crossDbId|string|the unique identifier for a cross|
|crossName|string|the human readable name for a cross|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|pollinationTimeStamp|string (date-time)|the timestamp when the polination took place|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "crossAttributes": [
            {
                "crossAttributeName": "crossAttributeName",
                "crossAttributeValue": "crossAttributeValue"
            }
        ],
        "crossName": "myIbadanCrosses2018_01",
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "myIbadanCrosses2018",
        "parent1": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "myIbadanPlot9001",
            "parentType": [
                "MALE",
                "FEMALE",
                "SELF",
                "POPULATION"
            ]
        },
        "parent2": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "myIbadanPlot9001",
            "parentType": [
                "MALE",
                "FEMALE",
                "SELF",
                "POPULATION"
            ]
        },
        "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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
                "crossAttributes": [
                    {
                        "crossAttributeName": "crossAttributeName",
                        "crossAttributeValue": "crossAttributeValue"
                    }
                ],
                "crossDbId": "d105fd6f",
                "crossName": "myIbadanCrosses2018_01",
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "myIbadanCrosses2018",
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "myIbadanPlot9001",
                    "parentType": [
                        "MALE",
                        "FEMALE",
                        "SELF",
                        "POPULATION"
                    ]
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "myIbadanPlot9001",
                    "parentType": [
                        "MALE",
                        "FEMALE",
                        "SELF",
                        "POPULATION"
                    ]
                },
                "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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


## Get - /crosses [/brapi/v1//crosses] 



### /crosses [GET /brapi/v1/crosses{?crossingProjectDbId}{?page}{?pageSize}]

Get a filtered list of Cross entities.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|crossAttributes|array[object]|Set of custom attributes associated with a cross|
|crossAttributeName|string|the human readable name of a cross attribute|
|crossAttributeValue|string|the value of a cross attribute|
|crossDbId|string|the unique identifier for a cross|
|crossName|string|the human readable name for a cross|
|crossType|string|the type of cross|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|parent1|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2|object||
|germplasmDbId|string|the unique identifier for a germplasm|
|germplasmName|string|the human readable name for a germplasm|
|observationUnitDbId|string|the unique identifier for an observation unit|
|observationUnitName|string|the human readable name for an observation unit|
|parentType|string|The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|pollinationTimeStamp|string (date-time)|the timestamp when the polination took place|


 

+ Parameters
    + crossingProjectDbId (Optional, ) ... Search for Crossing Projects with this unique id
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
                "crossAttributes": [
                    {
                        "crossAttributeName": "crossAttributeName",
                        "crossAttributeValue": "crossAttributeValue"
                    }
                ],
                "crossDbId": "d105fd6f",
                "crossName": "myIbadanCrosses2018_01",
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "myIbadanCrosses2018",
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "myIbadanPlot9001",
                    "parentType": [
                        "MALE",
                        "FEMALE",
                        "SELF",
                        "POPULATION"
                    ]
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "myIbadanPlot9001",
                    "parentType": [
                        "MALE",
                        "FEMALE",
                        "SELF",
                        "POPULATION"
                    ]
                },
                "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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

