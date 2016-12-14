## Get Trial By Id [/brapi/v1/trials/{trialDbId}]

Scope: CORE.
Status: ACCEPTED.
Implementation target date: PAG2016.

Get trial by id.

### Get trial by Id [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "trialDbId" : 1,
                "trialName" : "InternationalTrialA",
                "programDbId": 27,
                "programName": "International Yield Trial",
                "startDate": "2007-06-01",
                "endDate"  : "2008-12-31",
                "active" : "true", 
                "studies" : [
                    {
                        "studyDbId" : 1,
                        "studyName" : "Zimbabwe Yield Trial",
                        "locationName" : "Zimbabwe"
                    },
                    {
                        "studyDbId" : 2,
                        "studyName" : "Kenya Yield Trial",
                        "locationName" : "Kenya"
                    }
                ],
                "additionalInfo" : {
                    "property1Name" : "property1Value",
                    "property2Name" : "property2Value",
                    "property3Name" : "property3Value"
                }
            }
        }        
