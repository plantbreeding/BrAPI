## List Observation Levels [/brapi/v1/observationlevels]

Call to retrieve the list of supported observation levels. 
Observation levels indicate the granularity level at which the measurements are taken.
The values are used to supply the `observationLevel` parameter in the observation unit details call.

### **Deprecated** List observation levels [GET /brapi/v1/observationLevels?&pageSize={pageSize}&page={page}]
+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)
        
        {
            "metadata" : {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data" : ["plant", "plot"]
            }
        }


### GET /brapi/v1/observationlevels [GET /brapi/v1/observationlevels?pageSize={pageSize}&page={page}]
+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)
        
        {
            "metadata" : {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data" : ["plant", "plot"]
            }
        }

