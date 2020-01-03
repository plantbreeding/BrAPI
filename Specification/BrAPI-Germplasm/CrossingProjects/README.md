# Group Crossing Projects






### Get - /crossingprojects [GET /brapi/v1/crossingprojects{?crossingProjectDbId}{?page}{?pageSize}]

Get a filtered list of Crossing Projects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + crossingProjectDbId (Optional, ) ... Search for Crossing Projects with this unique id
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
                "commonCropName": "Cassava",
                "crossingProjectDbId": "ce0e1c29",
                "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
                "crossingProjectName": "Ibadan_Crosses_2018",
                "programDbId": "a088176c",
                "programName": "IITA Cassava"
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




### Post - /crossingprojects [POST /brapi/v1/crossingprojects]

Create new Crossing Project entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "commonCropName": "Cassava",
        "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
        "crossingProjectName": "Ibadan_Crosses_2018",
        "programDbId": "a088176c",
        "programName": "IITA Cassava"
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
                "commonCropName": "Cassava",
                "crossingProjectDbId": "ce0e1c29",
                "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
                "crossingProjectName": "Ibadan_Crosses_2018",
                "programDbId": "a088176c",
                "programName": "IITA Cassava"
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




### Get - /crossingprojects/{crossingProjectDbId} [GET /brapi/v1/crossingprojects/{crossingProjectDbId}{?page}{?pageSize}]

Get a filtered list of Crossing Projects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + crossingProjectDbId (Required, ) ... Search for Crossing Projects with this unique id
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
        "commonCropName": "Cassava",
        "crossingProjectDbId": "ce0e1c29",
        "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
        "crossingProjectName": "Ibadan_Crosses_2018",
        "programDbId": "a088176c",
        "programName": "IITA Cassava"
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




### Put - /crossingprojects/{crossingProjectDbId} [PUT /brapi/v1/crossingprojects/{crossingProjectDbId}]

Update an existing Crossing Project entity on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectDescription|string|the description for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|programName|string|the human readable name for a program|


 

+ Parameters
    + crossingProjectDbId (Required, ) ... Search for Crossing Projects with this unique id
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropName": "Cassava",
    "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
    "crossingProjectName": "Ibadan_Crosses_2018",
    "programDbId": "a088176c",
    "programName": "IITA Cassava"
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
        "commonCropName": "Cassava",
        "crossingProjectDbId": "ce0e1c29",
        "crossingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X_2018 and female nursery study Y_2018",
        "crossingProjectName": "Ibadan_Crosses_2018",
        "programDbId": "a088176c",
        "programName": "IITA Cassava"
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

