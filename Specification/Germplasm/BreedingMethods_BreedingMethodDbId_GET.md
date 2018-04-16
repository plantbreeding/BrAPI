### GET specific breeding method details [GET /brapi/v1/breedingmethods/{breedingMethodDbId}]
+ Parameters
   + breedingMethodDbId (required, string, `BM987`) ... Internal database identifier for a breeding method
+ Response 200 (application/json)
    
        { 
            "metadata" : {
                "pagination": {
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "breedingMethodDbId": "BM987",
                "abbreviation": "MBCR",
                "name": "Male Backcross",
                "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate."
            }
        }

