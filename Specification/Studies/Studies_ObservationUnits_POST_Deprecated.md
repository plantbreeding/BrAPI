### **Deprecated** Save Observation Unit Phenotypes [POST /brapi/v1/studies/{studyDbId}/observationunits?observationLevel={observationLevel}&pageSize={pageSize}&page={page}]

This call has been deprecated in V1.1. Use instead: "PUT /studies/{studyDbId}/observationunits" and "PUT /studies/{studyDbId}/observationunits/zip"

+ Parameters
    + format (default is JSON, but can be zip) ... In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
    
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
                "datafiles": [ "all_images.zip" ]
            },
            "result" : {
                "transactionDbId": "83748382938",
                "commit" : "true/false",
                "data" : [
                    {
                        "observatioUnitDbId": "abc-123",
                        "studyDbId": 2,
                        "observations": [
                            {
                                "observationVariableDbId": "18020",
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "11"
                            },
                            {   
                                "observationVariableDbId": "51496",
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "111"
                            },
                            {   
                                "observationVariableDbId": "51497",
                                "observationVariableName": "image",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "myimage1.jpg"
                            }
                        ]
                    },
                    {
                        "observatioUnitDbId": "abc-456",
                        "studyDbId": 3,
                        "observations": [
                            {
                                "observationVariableDbId": "18020",
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "22"
                            },
                            {   
                                "observationVariableDbId": "51496",
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "222"
                            },
                            {   
                                "observationVariableDbId": "51497",
                                "observationVariableName": "image",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "myimage2.jpg"
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
                    "code":"27",
                    "message": "Could not update observation values. Invalid data."
                } ]
            }
        }