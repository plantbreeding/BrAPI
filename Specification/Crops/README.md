
# Group Crops

For multi crop systems this is a useful call to list all the supported crops.



## Crops [Get /brapi/v1/crops{?pageSize}{?page}]

For multi crop systems this is a useful call to list all the supported crops.

<a href="https://test-server.brapi.org/brapi/v1/crops"> test-server.brapi.org/brapi/v1/crops</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 3,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            "maize",
            "wheat",
            "rice"
        ]
    }
}
```