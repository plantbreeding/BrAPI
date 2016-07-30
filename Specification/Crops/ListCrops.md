For multi crop systems this is a useful call to list all the supported crops.

## List supported crops [/brapi/v1/crops]
Scope: CORE.
Status: ACCEPTED.

### List supported crops [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 2,
                    "currentPage": 1,
                    "totalCount": 100,
                    "totalPages": 50
                },
                "status" : {},
                "datafiles": []
            },
            "result": {
                "data": [
                    "maize", "wheat", "rice"
                ]
            }
        }
