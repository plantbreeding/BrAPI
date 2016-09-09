## Get Observation Units by observation variable ids [/brapi/v1/studies/{studyDbId}/observations?observationVariableDbIds={observationVariableDbIds}]
Scope: CORE.
Status: ACCEPTED.
Implementation target date: PAG2016

Retrieve all plots where there are measurements for the given observation variables.

### Get Observation Units by observation variable ids [GET]

+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    + observationVariableDbId (required, number, `2` ... Numeric `id` of that variable (combination of trait, unit and method)

+ Response 200 (application/json)
    
        {
            "metadata" : 
                "status": null,
                "datafiles": [],
                "pagination": {
                    "pageSize": 1,
                    "currentPage": 1,
                    "totalCount": 1,
                    "totalPages": 1
                },
            "result" : {
                "data" : [ 
                    {
                        "studyDbId": 1,
                        "obserationDbId": 3383838,
                        "observationUnitDbId": 11,
                        "observationUnitName": "ZIPA_68_Ibadan_2014",
                        "observationLevel" : "plot",
                        "observationVariableDbId" : 393939,
                        "observationVariableName" : "Yield", 
                        "observationTimestamp" : "2015-11-05 15:12",
                        "uploadedBy" : "dbUserId",
                        "operator" : "Jane Doe",
                        "germplasmDbId" : 8383,
                        "germplasmName": 143,
                        "value" : 5,
                    }
                ]
            }
        }
