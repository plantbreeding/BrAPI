# Group Crossing Projects





## Crossingprojects [/brapi/v1/crossingprojects] 




### Get Crossingprojects by crossingProjectDbId  [GET /brapi/v1/crossingprojects/{crossingProjectDbId}{?page}{?pageSize}]

Get a filtered list of Crossing Projects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|corssingProjectDescription|string|the description for a crossing project|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|programName|string|the human readable name for a program|
|programDbId|string|the unique identifier for a program|


 

+ Parameters
    + crossingProjectDbId (Required, ) ... Search for Crossing Projects with this unique id
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
        "commonCropName": "Cassava",
        "corssingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X2018 and female nursery study Y2018",
        "crossingProjectDbId": "ce0e1c29",
        "crossingProjectName": "IbadanCrosses2018",
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





### Put Crossingprojects by crossingProjectDbId  [PUT /brapi/v1/crossingprojects/{crossingProjectDbId}]

Update an existing Crossing Project entity on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|programName|string|the human readable name for a program|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|corssingProjectDescription|string|the description for a crossing project|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|corssingProjectDescription|string|the description for a crossing project|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|programName|string|the human readable name for a program|
|programDbId|string|the unique identifier for a program|


 

+ Parameters
    + crossingProjectDbId (Required, ) ... Search for Crossing Projects with this unique id
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropName": "Cassava",
    "corssingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X2018 and female nursery study Y2018",
    "crossingProjectName": "IbadanCrosses2018",
    "programDbId": "a088176c",
    "programName": "IITA Cassava"
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
        "commonCropName": "Cassava",
        "corssingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X2018 and female nursery study Y2018",
        "crossingProjectDbId": "ce0e1c29",
        "crossingProjectName": "IbadanCrosses2018",
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





### Get Crossingprojects  [GET /brapi/v1/crossingprojects{?crossingProjectDbId}{?page}{?pageSize}]

Get a filtered list of Crossing Projects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|corssingProjectDescription|string|the description for a crossing project|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|programName|string|the human readable name for a program|
|programDbId|string|the unique identifier for a program|


 

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
                "commonCropName": "Cassava",
                "corssingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X2018 and female nursery study Y2018",
                "crossingProjectDbId": "ce0e1c29",
                "crossingProjectName": "IbadanCrosses2018",
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





### Post Crossingprojects  [POST /brapi/v1/crossingprojects]

Create new Crossing Project entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|programName|string|the human readable name for a program|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|crossingProjectName|string|the human readable name for a crossing project|
|programDbId|string|the unique identifier for a program|
|corssingProjectDescription|string|the description for a crossing project|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|crossingProjectDbId|string|the unique identifier for a crossing project|
|crossingProjectName|string|the human readable name for a crossing project|
|corssingProjectDescription|string|the description for a crossing project|
|commonCropName|string|the common name of a crop (for multi-crop systems)|
|programName|string|the human readable name for a program|
|programDbId|string|the unique identifier for a program|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "commonCropName": "Cassava",
        "corssingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X2018 and female nursery study Y2018",
        "crossingProjectName": "IbadanCrosses2018",
        "programDbId": "a088176c",
        "programName": "IITA Cassava"
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
                "commonCropName": "Cassava",
                "corssingProjectDescription": "Crosses between germplasm X and germplasm Y in male nursery study X2018 and female nursery study Y2018",
                "crossingProjectDbId": "ce0e1c29",
                "crossingProjectName": "IbadanCrosses2018",
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

