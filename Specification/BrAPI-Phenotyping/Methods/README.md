
# Group Methods

API to manage the details of observation variable Methods. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Method describes the way an observation should be collected. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Method "estimation" or "drone image processing". 






### Get - /methods [GET /brapi/v2/methods{?methodDbId}{?observationVariableDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Returns a list of Methods available on a server.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.'



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|bibliographicalReference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


 

+ Parameters
    + methodDbId (Optional, ) ... The unique identifier for a method
    + observationVariableDbId (Optional, ) ... The unique identifier for an observation variable
    + externalReferenceID (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceID` parameter)
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
                "additionalInfo": {},
                "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
                "description": "A measuring tape was used",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": "OBO"
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                }
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




### Post - /methods [POST /brapi/v2/methods]

Create new method objects in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|bibliographicalReference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|bibliographicalReference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
        "description": "A measuring tape was used",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        }
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
                "additionalInfo": {},
                "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
                "description": "A measuring tape was used",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": "OBO"
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                }
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




### Get - /methods/{methodDbId} [GET /brapi/v2/methods/{methodDbId}]

Retrieve details about a specific method

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|bibliographicalReference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
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
        "additionalInfo": {},
        "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
        "description": "A measuring tape was used",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        }
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




### Put - /methods/{methodDbId} [PUT /brapi/v2/methods/{methodDbId}/]

Update the details of an existing method

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|bibliographicalReference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|bibliographicalReference|string|Bibliographical reference describing the method.  MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.|
|description|string|Method description  MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method  MIAPPE V1.1 (DM-88) Method  Name of the method of observation|
|ontologyReference|object|MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).|
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
    "description": "A measuring tape was used",
    "externalReferences": [
        {
            "referenceID": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
            "referenceSource": "OBO Library"
        },
        {
            "referenceID": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        }
    ],
    "formula": "a^2 + b^2 = c^2",
    "methodClass": "Measurement",
    "methodName": "Measuring Tape",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                "type": "OBO"
            }
        ],
        "ontologyDbId": "6b071868",
        "ontologyName": "The Crop Ontology",
        "version": "7.2.3"
    }
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
        "additionalInfo": {},
        "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
        "description": "A measuring tape was used",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        }
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

