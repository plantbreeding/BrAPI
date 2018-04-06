
# Group Crops

For multi crop systems this is a useful call to list all the supported crops.

## List supported crops [/brapi/v1/crops]
Scope: CORE.
Status: ACCEPTED.

### List supported crops [GET /brapi/v1/crops{?pageSize}{?page}]
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
