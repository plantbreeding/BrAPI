## List supported crops [/brapi/v1/crops]
Scope: CORE.
Status: ACCEPTED.

### List supported crops [GET]
+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `10`) ... Which result page is requested
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
