## Observation Unit Details [/brapi/v1/studies/{studyDbId}/observationunits/{observationUnitDbId}]

The main API call for field data collection, to retrieve all the observation units within a study.

Scope: PHENOTYPING, Sample Tracking

### Get all observation units [GET /brapi/v1/studies/{studyDbId}/observationunits/{observationUnitDbId}]

+ Parameters
    + studyDbId (required, string, `abc123`) ... The study these observation units are related to.
    + observationUnitDbId (required, string, `def456`) ... The internal ID of an Observation Unit

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status" : [],
                "datafiles": []
            },
            "result" : {
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
            }
        }
