
# Group Crops

For multi crop systems this is a useful call to list all the supported crops.



## Commoncropnames [Get /brapi/v1/commonCropNames{?pageSize}{?page}]

List the common crop names for the crops available in a database server. 

This call is **required** for multi-crop systems where data from multiple crops may be stored in the same database server. A distinct database server is defined by everything in the URL before "/brapi/v1", including host name and base path.  

This call is recommended for single crop systems to be compatible with multi-crop clients. For a single crop system the response should contain an array with exactly 1 element. 

The common crop name can be used as a search parameter for Programs, Studies, and Germplasm.

<a href="https://test-server.brapi.org/brapi/v1/commonCropNames"> test-server.brapi.org/brapi/v1/commonCropNames</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            "maize",
            "wheat",
            "rice",
            "potato"
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 3,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
    }
}
```

## Crops [Get /brapi/v1/crops{?pageSize}{?page}]

For multi crop systems this is a useful call to list all the supported crops.

<a href="https://test-server.brapi.org/brapi/v1/crops"> test-server.brapi.org/brapi/v1/crops</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            "maize",
            "wheat",
            "rice"
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 3,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
    }
}
```