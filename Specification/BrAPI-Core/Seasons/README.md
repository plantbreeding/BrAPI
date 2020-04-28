
# Group Season

A season is made of 2 parts; the primary year and a term which defines a segment of the year. This could be a traditional season, like "Spring" or "Summer" or this could be a month, like "May" or "June" or this could be an arbitrary season name which is meaningful to the breeding program like "PlantingTime_3" or "Season E".





### Get - /seasons [GET /brapi/v2/seasons{?seasonDbId}{?season}{?year}{?page}{?pageSize}]

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
|seasonName|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|year|integer|The 4 digit year of the season.|


 

+ Parameters
    + seasonDbId (Optional, ) ... The unique identifier for a season. For backward compatibility it can be a string like '2012', '1957-2004'
    + season (Optional, ) ... The term to describe a given season. Example "Spring" OR "May" OR "Planting_Time_7".
    + year (Optional, ) ... The 4 digit year of a season. Example "2017"
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
                "seasonDbId": "Spring_2018",
                "seasonName": "Spring",
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




### Post - /seasons [POST /brapi/v2/seasons]

Add new season entries to the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|seasonName|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|year|integer|The 4 digit year of the season.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|seasonName|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|year|integer|The 4 digit year of the season.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "seasonDbId": "Spring_2018",
        "seasonName": "Spring",
        "year": 2018
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
                "seasonDbId": "Spring_2018",
                "seasonName": "Spring",
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




### Get - /seasons/{seasonDbId} [GET /brapi/v2/seasons/{seasonDbId}]

Get the a single Season



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|seasonName|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|year|integer|The 4 digit year of the season.|


 

+ Parameters
    + seasonDbId (Required, ) ... The unique identifier for a season. For backward compatibility it can be a string like '2012', '1957-2004'
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
        "seasonDbId": "Spring_2018",
        "seasonName": "Spring",
        "year": 2018
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




### Put - /seasons/{seasonDbId} [PUT /brapi/v2/seasons/{seasonDbId}/]

Update existing Seasons

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|seasonName|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|year|integer|The 4 digit year of the season.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|seasonName|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|year|integer|The 4 digit year of the season.|


 

+ Parameters
    + seasonDbId (Required, ) ... The unique identifier for a season. For backward compatibility it can be a string like '2012', '1957-2004'
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "seasonDbId": "Spring_2018",
    "seasonName": "Spring",
    "year": 2018
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
        "seasonDbId": "Spring_2018",
        "seasonName": "Spring",
        "year": 2018
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

