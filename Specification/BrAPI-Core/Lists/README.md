# Group Lists
Calls for manipulating generic lists of item IDs




## Lists [/brapi/v1/lists] 




### Get Lists  [GET /brapi/v1/lists{?listType}{?listName}{?listDbId}{?listSource}{?page}{?pageSize}]

Get filtered set of generic lists



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|listDescription|string|Description of a List|
|listSource|string|The description of where a List originated from|
|listDbId|string|The unique identifier for a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


 

+ Parameters
    + listType (Optional, ) ... The type of objects contained by this generic list
    + listName (Optional, ) ... The human readable name of this generic list
    + listDbId (Optional, ) ... The unique ID of this generic list
    + listSource (Optional, ) ... The source tag of this generic list
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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
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





### Post Lists  [POST /brapi/v1/lists]

Create a new list

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|listDescription|string|Description of a List|
|data|array[string]|The list of DbIds contained in this list|
|listSource|string|The description of where a List originated from|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|listDescription|string|Description of a List|
|listSource|string|The description of where a List originated from|
|listDbId|string|The unique identifier for a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


 

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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
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





### Get Lists by listDbId  [GET /brapi/v1/lists/{listDbId}]

Get a specific generic lists



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|listDescription|string|Description of a List|
|data|array[string]|The list of DbIds contained in this list|
|listSource|string|The description of where a List originated from|
|listDbId|string|The unique identifier for a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


 

+ Parameters
    + listDbId (Required, ) ... The unique ID of this generic list
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
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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





### Put Lists by listDbId  [PUT /brapi/v1/lists/{listDbId}]

Update an existing generic list

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|listDescription|string|Description of a List|
|data|array[string]|The list of DbIds contained in this list|
|listSource|string|The description of where a List originated from|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|listDescription|string|Description of a List|
|data|array[string]|The list of DbIds contained in this list|
|listSource|string|The description of where a List originated from|
|listDbId|string|The unique identifier for a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


 

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
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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





### Post Lists Items by listDbId  [POST /brapi/v1/lists/{listDbId}/items]

Add new data to a specific generic lists

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|listDescription|string|Description of a List|
|data|array[string]|The list of DbIds contained in this list|
|listSource|string|The description of where a List originated from|
|listDbId|string|The unique identifier for a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


 

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
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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



## Search [/brapi/v1/search] 




### Post Search Lists  [POST /brapi/v1/search/lists]

Advanced searching for the list resource.
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|listOwnerPersonDbIds|array[string]||
|listDbIds|array[string]||
|dateModifiedRangeStart|string (date-time)||
|listType|string||
|listOwnerNames|array[string]||
|listSources|array[string]||
|listNames|array[string]||
|dateCreatedRangeStart|string (date-time)||
|dateModifiedRangeEnd|string (date-time)||
|dateCreatedRangeEnd|string (date-time)||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dateCreatedRangeEnd": "2018-01-01T14:47:23-0600",
    "dateCreatedRangeStart": "2018-01-01T14:47:23-0600",
    "dateModifiedRangeEnd": "2018-01-01T14:47:23-0600",
    "dateModifiedRangeStart": "2018-01-01T14:47:23-0600",
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
        "Rob Bobertson"
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





### Get Search Lists by searchResultsDbId  [GET /brapi/v1/search/lists/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the list resource.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|listDescription|string|Description of a List|
|listSource|string|The description of where a List originated from|
|listDbId|string|The unique identifier for a List|
|listOwnerName|string|Human readable name of a List Owner. (usually a user or person)|
|listType|string||
|listName|string|Human readable name of a List|
|listOwnerPersonDbId|string|The unique identifier for a List Owner. (usually a user or person)|
|dateCreated|string (date-time)|Timestamp when the entity was first created|
|dateModified|string (date-time)|Timestamp when the entity was last updated|
|additionalInfo|object|Additional arbitrary info|
|listSize|integer|The number of elements in a List|


 

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
                "additionalInfo": {},
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
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

