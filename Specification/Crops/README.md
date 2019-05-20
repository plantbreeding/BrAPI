
# Group Crops

For multi crop systems this is a useful call to list all the supported crops.



## Commoncropnames [/brapi/v1/commoncropnames] 




### Get Commoncropnames  [GET /brapi/v1/commoncropnames{?page}{?pageSize}]

List the common crop names for the crops available in a database server. 

This call is **required** for multi-crop systems where data from multiple crops may be stored in the same database server. A distinct database server is defined by everything in the URL before "/brapi/v1", including host name and base path.  

This call is recommended for single crop systems to be compatible with multi-crop clients. For a single crop system the response should contain an array with exactly 1 element. 

The common crop name can be used as a search parameter for Programs, Studies, and Germplasm.


test-server.brapi.org/brapi/v1/commonCropNames



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[string]|array of crop names availible on the server|


 

+ Parameters
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
            "Tomatillo",
            "Paw Paw"
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



## Crops [/brapi/v1/crops] 




### **Deprecated** Get Crops  [GET /brapi/v1/crops{?page}{?pageSize}]

For multi crop systems this is a useful call to list all the supported crops.


test-server.brapi.org/brapi/v1/crops



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[string]|array of crop names availible on the server|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 2,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": []
    }
}
```

