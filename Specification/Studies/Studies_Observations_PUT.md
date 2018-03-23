
### Create or Update Observations for a Study [PUT /brapi/v1/studies/{studyDbId}/observations]

Implementation Guidelines:
+ If an `observationDbId` is "null" or an empty string in the request, a NEW observation should be created for the given study and observationUnit
+ If an `observationDbId` is populated but not found in the database, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client.
+ If an `observationDbId` is populated and found in the database, but the existing entry is not associated with the given study or observationUnit, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client.
+ If an `observationDbId` is populated and found in the database and is associated with the given study and observationUnit, then it should be updated with the new data given.

+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    
+ Request
        
        {
            "observations": [
                {
                    "observationDbId": "153453453",
                    "observationUnitDbId": "333888",
                    "observationVariableDbId": "18020",
                    "collector": "Mr. Technician",
                    "observationTimeStamp": "2015-06-16T00:53:26Z",
                    "value": "55.2"
                },
                {
                    "observationDbId": "",
                    "observationUnitDbId": "333888",
                    "observationVariableDbId": "18021",
                    "collector": "Mr. Technician",
                    "observationTimeStamp": "2015-06-16T00:53:26Z",
                    "value": "2.9998"
                },
                {
                    "observationDbId": null,
                    "observationUnitDbId": "333888",
                    "observationVariableDbId": "18022",
                    "collector": "Mr. Technician",
                    "observationTimeStamp": "2015-06-16T00:53:26Z",
                    "value": "0.003"
                }
            ]
        }


+ Response 200 (application/json)
    
        {
            "metadata": {
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "observations": [
                    {
                        "observationDbId": "153453453",
                        "observationVariableDbId": "18020",
                        "observationUnitDbId": "333888"
                    },
                    {
                        "observationDbId": "23456",
                        "observationVariableDbId": "18021",
                        "observationUnitDbId": "333888"
                    },
                    {
                        "observationDbId": "34567",
                        "observationVariableDbId": "18022",
                        "observationUnitDbId": "333888"
                    }
                ]
            }
        }
