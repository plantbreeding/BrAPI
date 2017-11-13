## Save Phenotypes for Many Studies [/brapi/v1/phenotypes] 
Scope: PHENOTYPING.

Notes: 
Along with the study specific phenotype saving calls (in the observationUnit and table formats), this call allows phenotypes to be saved and images to optionally be transferred as well.

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|transactionDbId|Long|internal DB id ||
|metadata|object|pagination, status, datafiles|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list of objects||Y|
|datafiles|list||Y|
|result|object|data|Y|
|transactionDbId|Long|transactionDbId||
|data| object| List of objects grouping the observationUnits and their observations||

### Save Observation Unit Phenotypes [POST]
Call to invoke for saving the measurements (observations) collected from field for all the observation units.

Observation timestamp should be ISO 8601 https://www.w3.org/TR/NOTE-datetime

In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call. In this case a format parameter should be passed as well.

Images can be optionally be uploaded using this call by providing a zipfile of all images in the datafiles, along with the actual zipfile in multi-part form data.

Scope: PHENOYTPING.

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
                                "observationTimeStamp" : "2015-06-16T00:53:26-0800",
                                "value": "11"
                            },
                            {   
                                "observationVariableDbId": "51496",
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26-0800",
                                "value": "111"
                            },
                            {   
                                "observationVariableDbId": "51497",
                                "observationVariableName": "image",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26-0800",
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
                                "observationTimeStamp" : "2015-06-16T00:53:26-0800",
                                "value": "22"
                            },
                            {   
                                "observationVariableDbId": "51496",
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26-0800",
                                "value": "222"
                            },
                            {   
                                "observationVariableDbId": "51497",
                                "observationVariableName": "image",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26-0800",
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
