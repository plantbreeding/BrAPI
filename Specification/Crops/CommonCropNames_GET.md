## List supported crops [/brapi/v1/commonCropNames]

List the common crop names for the crops available in a database server. 

This call is **required** for multi-crop systems where data from multiple crops may be stored in the same database server. A distinct database server is defined by everything in the URL before "/brapi/v1", including host name and base path.  

This call is recommended for single crop systems to be compatible with multi-crop clients. For a single crop system the response should contain an array with exactly 1 element. 

The common crop name can be used as a search parameter for Programs, Studies, and Germplasm.

### List supported crops [GET /brapi/v1/commonCropNames{?pageSize}{?page}]
+ Parameters
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 3,
                    "totalPages": 1
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "data": [
                    "maize", "wheat", "rice"
                ]
            }
        }
