# Group Lists
Calls for manipulating generic lists of item IDs




## Lists [/brapi/v1/lists] 




### Get Lists  [GET /brapi/v1/lists{?listType}{?listName}{?listDbId}{?listSource}{?page}{?pageSize}]

Get filtered set of generic lists

 

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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
                "description": "description0",
                "listDbId": "listDbId0",
                "listName": "listName0",
                "listOwnerName": "listOwnerName0",
                "listOwnerPersonDbId": "listOwnerPersonDbId0",
                "listSize": 0,
                "listSource": "listSource0",
                "listType": "germplasm"
            },
            {
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
                "description": "description1",
                "listDbId": "listDbId1",
                "listName": "listName1",
                "listOwnerName": "listOwnerName1",
                "listOwnerPersonDbId": "listOwnerPersonDbId1",
                "listSize": 0,
                "listSource": "listSource1",
                "listType": "markers"
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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            "data0",
            "data1"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "description": "description0",
        "listDbId": "listDbId0",
        "listName": "listName0",
        "listOwnerName": "listOwnerName0",
        "listOwnerPersonDbId": "listOwnerPersonDbId0",
        "listSize": 0,
        "listSource": "listSource0",
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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            "data0",
            "data1"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "description": "description0",
        "listDbId": "listDbId0",
        "listName": "listName0",
        "listOwnerName": "listOwnerName0",
        "listOwnerPersonDbId": "listOwnerPersonDbId0",
        "listSize": 0,
        "listSource": "listSource0",
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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            "data0",
            "data1"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "description": "description0",
        "listDbId": "listDbId0",
        "listName": "listName0",
        "listOwnerName": "listOwnerName0",
        "listOwnerPersonDbId": "listOwnerPersonDbId0",
        "listSize": 0,
        "listSource": "listSource0",
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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            "data0",
            "data1"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
        "description": "description0",
        "listDbId": "listDbId0",
        "listName": "listName0",
        "listOwnerName": "listOwnerName0",
        "listOwnerPersonDbId": "listOwnerPersonDbId0",
        "listSize": 0,
        "listSource": "listSource0",
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

