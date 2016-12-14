## List supported crops [/brapi/v1/crops]
Scope: CORE.
Status: ACCEPTED.

### List supported crops [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 2,
                    "currentPage": 0,
                    "totalCount": 100,
                    "totalPages": 50
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
