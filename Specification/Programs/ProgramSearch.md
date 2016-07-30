## Program Search [/brapi/v1/programs-search]
Advanced searching for the programs resource.

Status: ACCEPTED.

### Search Programs [/POST]

        + Request (application/json)
            {
                "programDbId": "123",
                "name": "Wheat Resistance Program",
                "abbreviation" : "DRP1",
                "objective" : "Disease resistance",
                "leadPerson" : "Dr. Henry Beachell"
            } 
        
        + Response 200 (application/json)
            {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 10,
                    "totalPages": 1
                },
                "status": {},
                "datafiles": []
            },
            "result" : {
                "data" : [
                    {
                        "programDbId": "123",
                        "name": "Wheat Resistance Program",
                        "abbreviation" : "DRP1",
                        "objective" : "Disease resistance",
                        "leadPerson" : "Dr. Henry Beachell"
                    },
                    {
                        "programDbId": "456",
                        "name": "Wheat Improvement Program",
                        "abbreviation" : "DRP2",
                        "objective" : "Yield improvement",
                        "leadPerson" : "Dr. Norman Borlaug"
                    }
                ]
            }
        }
