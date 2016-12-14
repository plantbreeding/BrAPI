## List Trial Summaries 

Scope: CORE.
Status: ACCEPTED.
Implementation target date: PAG2016.

Get list of trials.

### List of trial summaries [GET]

+ Parameters
    + programDbId (optional, string, `1`) ... Program filter to only return trials associated with given program id.
    + locationDbId (optional, string, `212`) ... Filter by location
    + pageSize (optional, integer, `1000`) 
    + page (optional, integer, `100`)
    + active (optional, boolean, `true/false`) ... Filter active status true/false. 
    + sortBy (optional, boolean, `studyDbId`) ... Sort order. Name of the field to sorty by.
    + sortOrder (optional, boolean, `asc/desc`) ... Sort order direction. Ascending/Descending.
    
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 2,
                    "currentPage": 0,
                    "totalCount": 100,
                    "totalPages": 50
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "data": [ 
                    {
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
                ]
            }
        }        

