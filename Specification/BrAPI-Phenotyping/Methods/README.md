
# Group Methods

API to manage the details of observation variable Methods. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Method describes the way an observation should be collected. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Method "estimation" or "drone image processing". 





## Methods [/brapi/v1/methods] 




### Get Methods  [GET /brapi/v1/methods{?page}{?pageSize}]

Returns a list of Methods available on a server.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.'



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method|
|additionalInfo|object|Additional arbitrary info|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|reference|string|Bibliographical reference describing the method.|
|methodDbId|string|Method unique identifier|
|ontologyReference|object||
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|version|string|Ontology version (no specific format)|
|description|string|Method description.|


 

+ Parameters
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
                "description": "A measuring tape was used",
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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





### Post Methods  [POST /brapi/v1/methods]

Create a new method object in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|description|string|Method description.|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method|
|ontologyReference|object||
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|version|string|Ontology version (no specific format)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|reference|string|Bibliographical reference describing the method.|
|additionalInfo|object|Additional arbitrary info|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method|
|additionalInfo|object|Additional arbitrary info|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|reference|string|Bibliographical reference describing the method.|
|methodDbId|string|Method unique identifier|
|ontologyReference|object||
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|version|string|Ontology version (no specific format)|
|description|string|Method description.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "description": "A measuring tape was used",
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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
                "description": "A measuring tape was used",
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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





### Get Methods by methodDbId  [GET /brapi/v1/methods/{methodDbId}]

Retrieve details about a specific method

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method|
|additionalInfo|object|Additional arbitrary info|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|reference|string|Bibliographical reference describing the method.|
|methodDbId|string|Method unique identifier|
|ontologyReference|object||
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|version|string|Ontology version (no specific format)|
|description|string|Method description.|


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
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
        "description": "A measuring tape was used",
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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





### Put Methods by methodDbId  [PUT /brapi/v1/methods/{methodDbId}]

Update the details of an existing method

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|description|string|Method description.|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method|
|ontologyReference|object||
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|version|string|Ontology version (no specific format)|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|reference|string|Bibliographical reference describing the method.|
|additionalInfo|object|Additional arbitrary info|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method|
|additionalInfo|object|Additional arbitrary info|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|reference|string|Bibliographical reference describing the method.|
|methodDbId|string|Method unique identifier|
|ontologyReference|object||
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|version|string|Ontology version (no specific format)|
|description|string|Method description.|


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "description": "A measuring tape was used",
    "formula": "a^2 + b^2 = c^2",
    "methodClass": "Measurement",
    "methodName": "Measuring Tape",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                "type": [
                    "OBO",
                    "RDF",
                    "WEBPAGE"
                ]
            }
        ],
        "ontologyDbId": "6b071868",
        "ontologyName": "The Crop Ontology",
        "version": "7.2.3"
    },
    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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
        "description": "A measuring tape was used",
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
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

