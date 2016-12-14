## List Observation Levels [/brapi/v1/observationLevels]

Call to retrieve the list of supported observation levels. 
Observation levels indicate the granularity level at which the measurements are taken.
The values are used to supply the `observationLevel` parameter in the observation unit details call.

### List observation levels [GET]

+ Response 200 (application/json)
        
        {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
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

