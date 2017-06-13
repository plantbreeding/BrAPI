### Save Observation Unit Phenotypes [POST]
Call to invoke for saving the measurements (observations) collected from field for all the observation units.

Observation timestamp should be ISO 8601 https://www.w3.org/TR/NOTE-datetime

In case where JSON data is zipped for faster transfer speed, the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.

Images can be uploaded using this call by providing a zipfile of all images in the datafiles, along with the actual zipfile in multi-part form data.

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
                "datafiles": [
                    {
                        "file_name": "all_images.zip",
                        "md5checksum": "A2B4C6"
                    }
                ]
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
                                "observationVariableId": 18020,
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "11"
                            },
                            {   
                                "observationVariableId": 51496,
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "111"
                            },
                            {   
                                "observationVariableId": 51497,
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
                                "observationVariableId": 18020,
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "22"
                            },
                            {   
                                "observationVariableId": 51496,
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": "222"
                            },
                            {   
                                "observationVariableId": 51497,
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
