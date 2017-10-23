## Get Observation Units by observation variable ids [/brapi/v1/studies/{studyDbId}/observations?observationVariableDbIds={observationVariableDbIds}&pageSize={pageSize}&page={page}]
Scope: CORE.
Status: ACCEPTED.
Implementation target date: PAG2016

Retrieve all plots where there are measurements for the given observation variables.

observationTimestamp should be ISO8601 format with timezone: YYYY-MM-DDThh:mm:ss+hhmm

### Get Observation Units by observation variable ids [GET]

+ Parameters
   + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
   + observationVariableDbId (required, number, `2` ... Numeric `id` of that variable (combination of trait, unit and method)
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `10`) ... Which result page is requested

+ Response 200 (application/json)
    
        {
            "metadata" : {
                "pagination" : { 
                    "pageSize": 1000, 
                    "currentPage": 0, 
                    "totalCount": 1, 
                    "totalPages": 1 
                },
                "status": [],
                "datafiles": [],
            }
            "result" : {
                "data" : [ 
                    {
                        "studyDbId": "1",
                        "obserationDbId": "3383838",
                        "observationUnitDbId": 11,
                        "observationUnitName": "ZIPA_68_Ibadan_2014",
                        "observationLevel" : "plot",
                        "observationVariableDbId" : 393939,
                        "observationVariableName" : "Yield", 
                        "observationTimestamp" : "2015-11-05T15:12:56+0100",
                        "uploadedBy" : "dbUserId",
                        "operator" : "Jane Doe",
                        "germplasmDbId" : 8383,
                        "germplasmName": 143,
                        "value" : 5
                    }
                ]
            }
        }
