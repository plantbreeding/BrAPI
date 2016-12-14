## Observation Unit Details [/brapi/v1/studies/{studyId}/observationunits?observationLevel={observationLevel}]

The main API call for field data collection, to retrieve all the observation units within a study.

### Get all observation units [GET]

+ Parameters
    + observationLevel (required, string, `plot`) ... The granularity level of observation units. 
      Either `plotNumber` or `plantNumber` fields will be relavant depending on whether granularity is plot or plant respectively.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status" : [],
                "datafiles": []
            },
            "result" : { 
                "data" : [
                    {
                        "observationUnitDbId": "abc-123",
                        "observationUnitName": "Test-2016-location-34-575",
                        "germplasmDbId": "1",
                        "germplasmName": "IR-8",
                        "pedigree": "IR-8-FP/IR-8-MP",
                        "entryNumber": "1",
                        "entryType": "Test entry",
                        "plotNumber": "1",
                        "plantNumber" : "0",
                        "blockNumber" : "1",
                        "X" : "1",
                        "Y" : "1",
                        "replicate": "1",
                        "observations": [
                            {
                                "observationDbId": 153453453,
                                "observationVariableId": 18020,
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": null
                            },
                            { 
                                "observationDbId": 23453454345,
                                "observationVariableId": 51496,
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": null
                            }
                        ]
                    },
                    {
                        "observatioUnitDbId": "abc-456",
                        "germplasmDbId": "2",
                        "germplasmName": "IR-9",
                        "pedigree": "IR-9-FP/IR-9-MP",
                        "enrtyNumber": "2",
                        "entryType": "Check entry",
                        "plotNumber": "2",
                        "plantNumber" : "0",
                        "blockNumber" : "2",
                        "X" : "1",
                        "Y" : "2",
                        "replicate": "1",
                        "observations": [
                            {
                                "observationDbId": 3,
                                "observationVariableId": 18020,
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": null
                            },
                            {   
                                "observationDbId": 4,
                                "observationVariableId": 51496,
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": null
                            }
                        ]
                    }
                ]
            }
        }
