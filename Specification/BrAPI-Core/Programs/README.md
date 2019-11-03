
# Group Programs

A Program can contain multiple Trials. A Trial can contain multiple Studies. 



## Programs [/brapi/v1/programs] 




### Get Programs  [GET /brapi/v1/programs{?commonCropName}{?programName}{?abbreviation}{?page}{?pageSize}]

Get a filtered list of breeding Programs. This list can be filtered by common crop name to narrow results to a specific crop.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|objective|string|The primary objective of the program|
|leadPersonName|string|The name of the program leader|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|commonCropName|string|Common name for the crop which this program is for|
|programDbId|string|The ID which uniquely identifies the program|
|additionalInfo|object|Additional arbitrary info|
|leadPersonDbId|string|The unique identifier of the program leader|
|abbreviation|string|An abbreviation which represents this program|
|programName|string|Human readable name of the program|


 

+ Parameters
    + commonCropName (Optional, ) ... Filter by the common crop name. Exact match.
    + programName (Optional, ) ... Filter by program name. Exact match.
    + abbreviation (Optional, ) ... Filter by program abbreviation. Exact match.
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
                "abbreviation": "P1",
                "additionalInfo": {},
                "commonCropName": "Tomatillo",
                "documentationURL": "https://wiki.brapi.org",
                "leadPersonDbId": "fe6f5c50",
                "leadPersonName": "Bob Robertson",
                "objective": "Make a better tomatillo",
                "programDbId": "f60f15b2",
                "programName": "Tomatillo_Breeding_Program"
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





### Post Programs  [POST /brapi/v1/programs]

Add new breeding Programs to the database. The `programDbId` is set by the server, all other fields are take from the request body, or a default value is used.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|objective|string|The primary objective of the program|
|leadPersonName|string|The name of the program leader|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|commonCropName|string|Common name for the crop which this program is for|
|additionalInfo|object|Additional arbitrary info|
|leadPersonDbId|string|The unique identifier of the program leader|
|abbreviation|string|An abbreviation which represents this program|
|programName|string|Human readable name of the program|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|objective|string|The primary objective of the program|
|leadPersonName|string|The name of the program leader|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|commonCropName|string|Common name for the crop which this program is for|
|programDbId|string|The ID which uniquely identifies the program|
|additionalInfo|object|Additional arbitrary info|
|leadPersonDbId|string|The unique identifier of the program leader|
|abbreviation|string|An abbreviation which represents this program|
|programName|string|Human readable name of the program|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "abbreviation": "P1",
        "additionalInfo": {},
        "commonCropName": "Tomatillo",
        "documentationURL": "https://wiki.brapi.org",
        "leadPersonDbId": "fe6f5c50",
        "leadPersonName": "Bob Robertson",
        "objective": "Make a better tomatillo",
        "programName": "Tomatillo_Breeding_Program"
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
                "abbreviation": "P1",
                "additionalInfo": {},
                "commonCropName": "Tomatillo",
                "documentationURL": "https://wiki.brapi.org",
                "leadPersonDbId": "fe6f5c50",
                "leadPersonName": "Bob Robertson",
                "objective": "Make a better tomatillo",
                "programDbId": "f60f15b2",
                "programName": "Tomatillo_Breeding_Program"
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





### Get Programs by programDbId  [GET /brapi/v1/programs/{programDbId}]

Get a single breeding Program by Id. This can be used to quickly get the details of a Program when you have the Id from another entity.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|objective|string|The primary objective of the program|
|leadPersonName|string|The name of the program leader|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|commonCropName|string|Common name for the crop which this program is for|
|programDbId|string|The ID which uniquely identifies the program|
|additionalInfo|object|Additional arbitrary info|
|leadPersonDbId|string|The unique identifier of the program leader|
|abbreviation|string|An abbreviation which represents this program|
|programName|string|Human readable name of the program|


 

+ Parameters
    + programDbId (Required, ) ... Filter by the common crop name. Exact match.
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
        "abbreviation": "P1",
        "additionalInfo": {},
        "commonCropName": "Tomatillo",
        "documentationURL": "https://wiki.brapi.org",
        "leadPersonDbId": "fe6f5c50",
        "leadPersonName": "Bob Robertson",
        "objective": "Make a better tomatillo",
        "programDbId": "f60f15b2",
        "programName": "Tomatillo_Breeding_Program"
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





### Put Programs by programDbId  [PUT /brapi/v1/programs/{programDbId}]

Update the details of an existing breeding Program.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|objective|string|The primary objective of the program|
|leadPersonName|string|The name of the program leader|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|commonCropName|string|Common name for the crop which this program is for|
|additionalInfo|object|Additional arbitrary info|
|leadPersonDbId|string|The unique identifier of the program leader|
|abbreviation|string|An abbreviation which represents this program|
|programName|string|Human readable name of the program|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|objective|string|The primary objective of the program|
|leadPersonName|string|The name of the program leader|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|commonCropName|string|Common name for the crop which this program is for|
|programDbId|string|The ID which uniquely identifies the program|
|additionalInfo|object|Additional arbitrary info|
|leadPersonDbId|string|The unique identifier of the program leader|
|abbreviation|string|An abbreviation which represents this program|
|programName|string|Human readable name of the program|


 

+ Parameters
    + programDbId (Required, ) ... Filter by the common crop name. Exact match.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "abbreviation": "P1",
    "additionalInfo": {},
    "commonCropName": "Tomatillo",
    "documentationURL": "https://wiki.brapi.org",
    "leadPersonDbId": "fe6f5c50",
    "leadPersonName": "Bob Robertson",
    "objective": "Make a better tomatillo",
    "programName": "Tomatillo_Breeding_Program"
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
        "abbreviation": "P1",
        "additionalInfo": {},
        "commonCropName": "Tomatillo",
        "documentationURL": "https://wiki.brapi.org",
        "leadPersonDbId": "fe6f5c50",
        "leadPersonName": "Bob Robertson",
        "objective": "Make a better tomatillo",
        "programDbId": "f60f15b2",
        "programName": "Tomatillo_Breeding_Program"
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



## Search [/brapi/v1/search] 




### Post Search Programs  [POST /brapi/v1/search/programs]

Advanced searching for the programs resource.
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|leadPersonDbIds|array[string]|The person DbIds of the program leader to search for|
|programNames|array[string]|A name of a program to search for|
|leadPersonNames|array[string]|The names of the program leader to search for|
|objectives|array[string]|A program objective to search for|
|programDbIds|array[string]|A program identifier to search for|
|commonCropNames|array[string]|Common name for the crop which this program is for|
|abbreviations|array[string]|An abbreviation of a program to search for|


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
        "P1",
        "P2"
    ],
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "leadPersonDbIds": [
        "d8bd96c7",
        "a2b9c8e7"
    ],
    "leadPersonNames": [
        "Bob Robertson",
        "Rob Robertson"
    ],
    "objectives": [
        "Objective Code One",
        "This is a longer objective search query"
    ],
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





### Get Search Programs by searchResultsDbId  [GET /brapi/v1/search/programs/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the programs resource.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|objective|string|The primary objective of the program|
|leadPersonName|string|The name of the program leader|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|commonCropName|string|Common name for the crop which this program is for|
|programDbId|string|The ID which uniquely identifies the program|
|additionalInfo|object|Additional arbitrary info|
|leadPersonDbId|string|The unique identifier of the program leader|
|abbreviation|string|An abbreviation which represents this program|
|programName|string|Human readable name of the program|


 

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
                "abbreviation": "P1",
                "additionalInfo": {},
                "commonCropName": "Tomatillo",
                "documentationURL": "https://wiki.brapi.org",
                "leadPersonDbId": "fe6f5c50",
                "leadPersonName": "Bob Robertson",
                "objective": "Make a better tomatillo",
                "programDbId": "f60f15b2",
                "programName": "Tomatillo_Breeding_Program"
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

