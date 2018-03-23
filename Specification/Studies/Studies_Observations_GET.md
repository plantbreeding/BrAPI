## Observations for a Study [/brapi/v1/studies/{studyDbId}/observations]

Retrieve all observations where there are measurements for the given observation variables.

observationTimestamp should be ISO8601 format with timezone: YYYY-MM-DDThh:mm:ss+hhmm

### Get Observations for a Study [GET /brapi/v1/studies/{studyDbId}/observations{?observationVariableDbIds}{?pageSize}{?page}]

+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    + observationVariableDbIds (optional, array, `393939,393938`) ... Comma separated set of observation variable DbIds (combination of trait, unit and method)
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
    
        {
            "metadata" : {
                "pagination" : { 
                    "pageSize": 1000, 
                    "currentPage": 0, 
                    "totalCount": 2, 
                    "totalPages": 1 
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data" : [ 
                    {
                        "studyDbId": "1",
                        "obserationDbId": "12345",
                        "observationUnitDbId": "11",
                        "observationUnitName": "ZIPA_68_Ibadan_2014",
                        "observationLevel" : "plot",
                        "observationVariableDbId" : "393938",
                        "observationVariableName" : "Yield", 
                        "observationTimestamp" : "2015-11-05T15:12:56+0100",
                        "uploadedBy" : "dbUserId",
                        "operator" : "Jane Doe",
                        "germplasmDbId" : "8383",
                        "germplasmName": "Pahang",
                        "value" : "5"
                    },
                    {
                        "studyDbId": "1",
                        "obserationDbId": "23456",
                        "observationUnitDbId": "11",
                        "observationUnitName": "ZIPA_68_Ibadan_2014",
                        "observationLevel" : "plot",
                        "observationVariableDbId" : "393939",
                        "observationVariableName" : "Dry Weight", 
                        "observationTimestamp" : "2015-11-05T15:13:56+0100",
                        "uploadedBy" : "dbUserId",
                        "operator" : "Jane Doe",
                        "germplasmDbId" : "8383",
                        "germplasmName": "Pahang",
                        "value" : "22.3"
                    }
                ]
            }
        }
