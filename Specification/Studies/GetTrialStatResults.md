## Get statistical results by trial [/brapi/v2/trials/{id}/statisticalobservations]
Scope: PHENOTYPING, ANALYSIS.
This call is meant to get statistical results based on raw observations, eg. Meta-R. The proposal is included at trial level for multilocaltion analysis results. CIMMYT's IWIS currently supports this information.

Notes: A similar call at study level may be considered for single-site analysis

### Retrieve statistical results by trial's entrys [GET]

+ Parameters
    + trialDbId (required, integer, `T2233`) ... Identifier of the trial. Usually a number, could be alphanumeric.

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 100,
                    "currentPage": 0,
                    "totalCount": 480,
                    "totalPages": 5
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": [
                    {
                        "germplasmDbId": "1",
                        "entryNumber": "1",
                        "studyDbId",
                        "observations": [
                            {
                                "observationDbId": 153453453,
                                "observationVariableId": 18020,
                                "value": 10.0101
                            },
                            {
                                "observationDbId": 23453454345,
                                "observationVariableId": 51496,
                                "value": 11.2021
                            }
                        ]
                    }
                ]
            }
        }
