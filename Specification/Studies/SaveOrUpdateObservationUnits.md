### Save Or Update Observation Units [POST]
Call to invoke for saving the measurements (observations) collected from field for all the observation units.
Scope: PHENOYTPING.

+ Parameters
    + observationLevel (required, string, `plot`) ... The granularity level of observation units.
    
+ Request (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [],
                "datafiles": []
            },
            "result" : {
                "transactionDbId": "83748382938",
                "commit" : "true/false",
                "data" : [
                    {
                        "observatioUnitDbId": "abc-123",
                        "observations": [
                            {
                                "observationDbId": 1,
                                "observationVariableId": 18020,
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "11"
                            },
                            {   
                                "observationDbId": 2,
                                "observationVariableId": 51496,
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "111"
                            }
                        ]
                    },
                    {
                        "observatioUnitDbId": "abc-456",
                        "observations": [
                            {
                                "observationDbId": 3,
                                "observationVariableId": 18020,
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "22"
                            },
                            {   
                                "observationDbId": 4,
                                "observationVariableId": 51496,
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "222"
                            }
                        ]
                    }
                ]
            }
        }

+ Response 200 (application/json)

+ Response 500 (application/json)

        {
            "metadata": {
                "status": [ {
                    "message": "Could not update observation values. Invalid data.", "code":"27"
                } ]
            }
        }
