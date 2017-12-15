## Observation Unit Details [/brapi/v1/studies/{studyDbId}/observationunits]

The main API call for field data collection, to retrieve all the observation units within a study.

Scope: PHENOTYPING

### Get all observation units [GET /brapi/v1/studies/{studyDbId}/observationunits{?observationLevel}{?pageSize}{?page}]

+ Parameters
    + studyDbId (required, string, `abc123`) ... The study these observation units are related to.
    + observationLevel (required, string, `plot`) ... The granularity level of observation units. Either `plotNumber` or `plantNumber` fields will be relavant depending on whether granularity is plot or plant respectively.
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 1000,
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
                        "observationLevel": "plot",
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
                        "observationUnitXref":[
                            {"source": "biosampleEBI", "id": "SAMEA179865230"},
                            {"source": "gnpis.lot", "id": "INRA:CoeSt6 _SMH03"}, 
                            {"source": "kernelDB", "id": "239865"}
                        ],
                        "observations": [
                            {
                                "observationDbId": "153453453",
                                "observationVariableDbId": "18020",
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": null
                            },
                            { 
                                "observationDbId": "23453454345",
                                "observationVariableDbId": "51496",
                                "observationVariableName": "GW100_g",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": null
                            }
                        ]
                    },
                    {
                        "observatioUnitDbId": "abc-456",
                        "observationUnitName": "Test-2016-location-34-456",
                        "observationLevel": "plot",
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
                                "observationDbId": "3",
                                "observationVariableDbId": "18020",
                                "observationVariableName": "Plant_height",
                                "collector" : "Mr. Technician",
                                "observationTimeStamp" : "2015-06-16T00:53:26Z",
                                "value": null
                            },
                            {   
                                "observationDbId": "4",
                                "observationVariableDbId": "51496",
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
