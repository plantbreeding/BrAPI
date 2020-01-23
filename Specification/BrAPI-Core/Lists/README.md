# Group Lists
Calls for manipulating generic lists of item IDs





### Get - /lists [GET /brapi/v1/lists{?listType}{?listName}{?listDbId}{?listSource}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get filtered set of generic lists



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDbId|string|The unique identifier for a List|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


 

+ Parameters
    + listType (Optional, ) ... The type of objects contained by this generic list
    + listName (Optional, ) ... The human readable name of this generic list
    + listDbId (Optional, ) ... The unique ID of this generic list
    + listSource (Optional, ) ... The source tag of this generic list
    + externalReferenceID (Optional, ) ... Search for Germplasm by an external reference
    + externalReferenceSource (Optional, ) ... Search for Germplasm by an external reference
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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
                    }
                ],
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": [
                    "germplasm",
                    "markers",
                    "programs",
                    "trials",
                    "studies",
                    "observationUnits",
                    "observations",
                    "observationVariables",
                    "samples"
                ]
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




### Post - /lists [POST /brapi/v1/lists]

Create a new list

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|data|array[string]|The list of DbIds contained in this list|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDbId|string|The unique identifier for a List|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            },
            {
                "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                "referenceSource": "BrAPI Example Server"
            }
        ],
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": [
            "germplasm",
            "markers",
            "programs",
            "trials",
            "studies",
            "observationUnits",
            "observations",
            "observationVariables",
            "samples"
        ]
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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
                    }
                ],
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": [
                    "germplasm",
                    "markers",
                    "programs",
                    "trials",
                    "studies",
                    "observationUnits",
                    "observations",
                    "observationVariables",
                    "samples"
                ]
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




### Get - /lists/{listDbId} [GET /brapi/v1/lists/{listDbId}]

Get a specific generic lists



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|data|array[string]|The list of DbIds contained in this list|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDbId|string|The unique identifier for a List|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


 

+ Parameters
    + listDbId (Required, ) ... The unique ID of this generic list
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
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            },
            {
                "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                "referenceSource": "BrAPI Example Server"
            }
        ],
        "listDbId": "6f621cfa",
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": [
            "germplasm",
            "markers",
            "programs",
            "trials",
            "studies",
            "observationUnits",
            "observations",
            "observationVariables",
            "samples"
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




### Put - /lists/{listDbId} [PUT /brapi/v1/lists/{listDbId}]

Update an existing generic list

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|data|array[string]|The list of DbIds contained in this list|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|data|array[string]|The list of DbIds contained in this list|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDbId|string|The unique identifier for a List|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


 

+ Parameters
    + listDbId (Required, ) ... The unique ID of this generic list
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "data": [
        "758a78c0",
        "2c78f9ee"
    ],
    "dateCreated": "2018-01-01T14:47:23-0600",
    "dateModified": "2018-01-01T14:47:23-0600",
    "externalReferences": [
        {
            "referenceID": "doi:10.155454/12349537E12",
            "referenceSource": "DOI"
        },
        {
            "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
            "referenceSource": "OBO Library"
        },
        {
            "referenceID": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        },
        {
            "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
            "referenceSource": "BrAPI Example Server"
        }
    ],
    "listDescription": "This is a list of germplasm I would like to investigate next season",
    "listName": "MyGermplasm_Sept_2020",
    "listOwnerName": "Bob Robertson",
    "listOwnerPersonDbId": "58db0628",
    "listSize": 53,
    "listSource": "GeneBank Repository 1.3",
    "listType": [
        "germplasm",
        "markers",
        "programs",
        "trials",
        "studies",
        "observationUnits",
        "observations",
        "observationVariables",
        "samples"
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
        "additionalInfo": {},
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            },
            {
                "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                "referenceSource": "BrAPI Example Server"
            }
        ],
        "listDbId": "6f621cfa",
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": [
            "germplasm",
            "markers",
            "programs",
            "trials",
            "studies",
            "observationUnits",
            "observations",
            "observationVariables",
            "samples"
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




### Post - /lists/{listDbId}/items [POST /brapi/v1/lists/{listDbId}/items]

Add new data to a specific generic lists

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|data|array[string]|The list of DbIds contained in this list|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDbId|string|The unique identifier for a List|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


 

+ Parameters
    + listDbId (Required, ) ... The unique ID of this generic list
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    "758a78c0",
    "2c78f9ee"
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
        "additionalInfo": {},
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            },
            {
                "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                "referenceSource": "BrAPI Example Server"
            }
        ],
        "listDbId": "6f621cfa",
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": [
            "germplasm",
            "markers",
            "programs",
            "trials",
            "studies",
            "observationUnits",
            "observations",
            "observationVariables",
            "samples"
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




### Post - /search/lists [POST /brapi/v1/search/lists]

Advanced searching for the list resource.
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|dateCreatedRangeEnd|string (date-time)||
|dateCreatedRangeStart|string (date-time)||
|dateModifiedRangeEnd|string (date-time)||
|dateModifiedRangeStart|string (date-time)||
|externalReferenceIDs|array[string]|List of external references for the trait to search for|
|externalReferenceSources|array[string]|List of external references sources for the trait to search for|
|listDbIds|array[string]||
|listNames|array[string]||
|listOwnerNames|array[string]||
|listOwnerPersonDbIds|array[string]||
|listSources|array[string]||
|listType|string||
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDbId|string|The unique identifier for a List|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dateCreatedRangeEnd": "2018-01-01T14:47:23-0600",
    "dateCreatedRangeStart": "2018-01-01T14:47:23-0600",
    "dateModifiedRangeEnd": "2018-01-01T14:47:23-0600",
    "dateModifiedRangeStart": "2018-01-01T14:47:23-0600",
    "externalReferenceIDs": [
        "http://purl.obolibrary.org/obo/ro.owl",
        "14a19841"
    ],
    "externalReferenceSources": [
        "OBO Library",
        "Field App Name"
    ],
    "listDbIds": [
        "55f20cf6",
        "3193ca3d"
    ],
    "listNames": [
        "Planing List 1",
        "Bobs List"
    ],
    "listOwnerNames": [
        "Bob Robertson",
        "Rob Robertson"
    ],
    "listOwnerPersonDbIds": [
        "bob@bob.com",
        "rob@bob.com"
    ],
    "listSources": [
        "USER",
        "SYSTEM",
        "EXTERNAL"
    ],
    "listType": [
        "germplasm",
        "markers",
        "programs",
        "trials",
        "studies",
        "observationUnits",
        "observations",
        "observationVariables",
        "samples"
    ],
    "page": 0,
    "pageSize": 1000
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
                "additionalInfo": {},
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
                    }
                ],
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": [
                    "germplasm",
                    "markers",
                    "programs",
                    "trials",
                    "studies",
                    "observationUnits",
                    "observations",
                    "observationVariables",
                    "samples"
                ]
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




### Get - /search/lists/{searchResultsDbId} [GET /brapi/v1/search/lists/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the list resource.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|listDbId|string|The unique identifier for a List|
|listDescription|string|Description of a List|
|listName|string|Human readable name of a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|listSize|integer|The number of elements in a List|
|listSource|string|The description of where a List originated from|
|listType|string||


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 102 (application/json)
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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
                    }
                ],
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": [
                    "germplasm",
                    "markers",
                    "programs",
                    "trials",
                    "studies",
                    "observationUnits",
                    "observations",
                    "observationVariables",
                    "samples"
                ]
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

