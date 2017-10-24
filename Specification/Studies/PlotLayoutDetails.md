## Plot Layout Details [/brapi/v1/studies/{studyDbId}/layout?pageSize={pageSize}&page={page}]
Scope: PHENOTYPING.
Status: ACCEPTED.
Implementation target date: PAG2016
Notes: the plot information.

Retrieve the plot layout of the study with id {id}.

### Retrieve plot layout details [GET]

+ Parameters
   + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)
    
        {
            "metadata" : {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 1,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data" : [ 
                    {
                        "studyDbId": 1,
                        "observationUnitDbId": 11,
                        "observationUnitName": "ZIPA_68_Ibadan_2014",
                        "observationLevel": "plot",
                        "replicate": 1,
                        "germplasmDbId": 143,
                        "germplasmName": "ZIPA_68",
                        "blockNumber": 1,
                        "X": 20,
                        "Y": 22,
                        "entryType": "check/test/filler",
                        "additionalInfo" : { 
                        }
                    }
                ]
            }
        }

