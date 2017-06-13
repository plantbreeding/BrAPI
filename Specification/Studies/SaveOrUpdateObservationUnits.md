### Save Or Update Observation Units [POST]
Call to invoke for saving the measurements (observations) collected from field for all the observation units.

Observation timestamp should be ISO 8601 https://www.w3.org/TR/NOTE-datetime

In case where JSON data is zipped for faster transfer speed, the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.

This call can be used in conjunction with the new /media resource to upload images.

Scope: PHENOYTPING.

+ Parameters
    + observationLevel (required, string, `plot`) ... The granularity level of observation units.
    + format (default is JSON, but can be zip) ... In case where JSON data is zipped for faster transfer speed, the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
    
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
