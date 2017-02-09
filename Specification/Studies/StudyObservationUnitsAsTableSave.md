### Save study Observation Units as table [POST]

Scope: PHENOTYPING

+ Request
    
        {
            "metadata": {
                "pagination" : { 
                    "pageSize":20, 
                    "currentPage":0, 
                    "totalCount":2, 
                    "totalPages":1 
                },
                "status" : [],
                "datafiles": []
            },
            "result" : {
                "headerRow": [ "observationUnitDbId", "collector", "observationTimestamp", "variable1Id", "variable2Id", "variable3Id" ],
                "observationVariableDbIds": [ "variable1Id", "variable2Id", "variable2Id"],
                "data" :
                [
                    [1, "Mr. Technician1", "2015-06-16T10:00:00Z", "variable1Value", "variable2Value", "variable3Value"],
                    [2, "Mr. Technician2", "2015-06-16T11:00:01Z", "variable1Value", "variable2Value", "variable3Value"]
                ]
            }
        }
        
+ Response 200

