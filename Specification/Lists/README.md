# Group Lists
Calls for manipulating generic lists of item IDs




## Lists [/brapi/v1/lists] 




### Get Lists  [GET /brapi/v1/lists{?listType}{?listName}{?listDbId}{?listSource}{?page}{?pageSize}]

Get filtered set of generic lists



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of generic list summaries|
|dateCreated|string (date-time)||
|dateModified|string (date-time)||
|description|string||
|listDbId|string||
|listName|string||
|listOwnerName|string||
|listOwnerPersonDbId|string||
|listSize|integer||
|listSource|string||
|listType|string||


 

+ Parameters
    + listType (Optional, ) ... The type of objects contained by this generic list
    + listName (Optional, ) ... The human readable name of this generic list
    + listDbId (Optional, ) ... The unique ID of this generic list
    + listSource (Optional, ) ... The source tag of this generic list
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "dateCreated": "2011-06-14T22:12:51-04:00",
                "dateModified": "2011-06-14T22:12:51-04:00",
                "description": "Example List of germplasm",
                "listDbId": "list1",
                "listName": "Example List 1",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "person1",
                "listSize": 3,
                "listSource": "User Created",
                "listType": "germplasm"
            },
            {
                "dateCreated": "2011-06-14T22:12:51-04:00",
                "dateModified": "2011-06-14T22:12:51-04:00",
                "description": "Example List of germplasm",
                "listDbId": "list2",
                "listName": "Example List 2",
                "listOwnerName": "Rob Robertson",
                "listOwnerPersonDbId": "person2",
                "listSize": 3,
                "listSource": "User Created",
                "listType": "germplasm"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Post Lists  [POST /brapi/v1/lists]

Create a new list

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[string]||
|description|string||
|listName|string||
|listOwnerName|string||
|listOwnerPersonDbId|string||
|listSize|integer||
|listSource|string||
|listType|string||


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|dateCreated|string (date-time)||
|dateModified|string (date-time)||
|description|string||
|listDbId|string||
|listName|string||
|listOwnerName|string||
|listOwnerPersonDbId|string||
|listSize|integer||
|listSource|string||
|listType|string||
|data|array[string]||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "data": [
        "data0",
        "data1"
    ],
    "description": "description0",
    "listName": "listName0",
    "listOwnerName": "listOwnerName0",
    "listOwnerPersonDbId": "listOwnerPersonDbId0",
    "listSize": 0,
    "listSource": "listSource0",
    "listType": "germplasm"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            "string"
        ],
        "dateCreated": "2018-12-05T14:36:04-05:00",
        "dateModified": "2018-12-05T14:36:04-05:00",
        "description": "string",
        "listDbId": "d93d6bb6-dfc3-4d15-8d2e-654c618ce12e",
        "listName": "string",
        "listOwnerName": "string",
        "listOwnerPersonDbId": "string",
        "listSize": 1,
        "listSource": "string",
        "listType": "germplasm"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Lists by listDbId  [GET /brapi/v1/lists/{listDbId}]

Get a specific generic lists



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|dateCreated|string (date-time)||
|dateModified|string (date-time)||
|description|string||
|listDbId|string||
|listName|string||
|listOwnerName|string||
|listOwnerPersonDbId|string||
|listSize|integer||
|listSource|string||
|listType|string||
|data|array[string]||


 

+ Parameters
    + listDbId (Required, ) ... The unique ID of this generic list
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            "1",
            "2",
            "3"
        ],
        "dateCreated": "2011-06-14T22:12:51-04:00",
        "dateModified": "2011-06-14T22:12:51-04:00",
        "description": "Example List of germplasm",
        "listDbId": "list1",
        "listName": "Example List 1",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "person1",
        "listSize": 3,
        "listSource": "User Created",
        "listType": "germplasm"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Lists by listDbId  [PUT /brapi/v1/lists/{listDbId}]

Update an existing generic list

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[string]||
|description|string||
|listName|string||
|listOwnerName|string||
|listOwnerPersonDbId|string||
|listSize|integer||
|listSource|string||
|listType|string||


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|dateCreated|string (date-time)||
|dateModified|string (date-time)||
|description|string||
|listDbId|string||
|listName|string||
|listOwnerName|string||
|listOwnerPersonDbId|string||
|listSize|integer||
|listSource|string||
|listType|string||
|data|array[string]||


 

+ Parameters
    + listDbId (Required, ) ... The unique ID of this generic list
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "data": [
        "data0",
        "data1"
    ],
    "description": "description0",
    "listName": "listName0",
    "listOwnerName": "listOwnerName0",
    "listOwnerPersonDbId": "listOwnerPersonDbId0",
    "listSize": 0,
    "listSource": "listSource0",
    "listType": "germplasm"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            "string"
        ],
        "dateCreated": "2011-06-14T22:12:51-04:00",
        "dateModified": "2018-12-05T14:36:04-05:00",
        "description": "string",
        "listDbId": "list1",
        "listName": "string",
        "listOwnerName": "string",
        "listOwnerPersonDbId": "string",
        "listSize": 1,
        "listSource": "string",
        "listType": "germplasm"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Post Lists Items by listDbId  [POST /brapi/v1/lists/{listDbId}/items]

Add new data to a specific generic lists

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|dateCreated|string (date-time)||
|dateModified|string (date-time)||
|description|string||
|listDbId|string||
|listName|string||
|listOwnerName|string||
|listOwnerPersonDbId|string||
|listSize|integer||
|listSource|string||
|listType|string||
|data|array[string]||


 

+ Parameters
    + listDbId (Required, ) ... The unique ID of this generic list
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            "1",
            "2",
            "3"
        ],
        "dateCreated": "2011-06-14T22:12:51-04:00",
        "dateModified": "2018-12-05T14:36:04-05:00",
        "description": "string",
        "listDbId": "list1",
        "listName": "string",
        "listOwnerName": "string",
        "listOwnerPersonDbId": "string",
        "listSize": 3,
        "listSource": "string",
        "listType": "germplasm"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

