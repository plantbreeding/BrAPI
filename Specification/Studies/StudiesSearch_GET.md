## Search Studies [/brapi/v1/studies-search]
Scope: PHENOTYPING.
Status: ACCEPTED.
Implementation target date: PAG2016.

Implemented by: Germinate

Used by: Flapjack, Cassavabase

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

Get list of studies

StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD

### Search Studies (GET) [GET /brapi/v1/studies-search{?studyDbId}{?trialDbId}{?programDbId}{?locationDbId}{?seasonDbId}{?studyType}{?germplasmDbIds}{?observationVariableDbIds}{?pageSize}{?page}{?active}{?sortBy}{?sortOrder}]


+ Parameters
    + studyDbId (optional, string, `35`) ... DbId for a study
    + trialDbId  (optional, string, `7`) ... Filter by trial  
    + programDbId (optional, string, `1`) ... Program filter to only return studies associated with given program id.
    + locationDbId (optional, string, `212`) ... Filter by location
    + seasonDbId (optional, string, `2016E`) ... Filter by season or year
    + studyType (optional, string, `Nursery`) ... Filter based on study type e.g. Nursery, Trial or Genotype.
    + germplasmDbIds (optional, array, `CML123,CML`) ... Filter studies where specified germplasm have been used/tested
    + observationVariableDbIds (optional, array, `CO-PH-123,Var-123`) ... Filter studies where specified observation variables have been measured
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + active (optional, boolean, `true`) ... Filter active status true/false. 
    + sortBy (optional, string, `studyDbId`) ... Sort order. Name of the field to sort by.
    + sortOrder (optional, string, `asc`) ... Sort order direction. Ascending/Descending.
    
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "data": [ 
                    {
                        "studyDbId": "35",
                        "name": "Earlygenerationtesting",
                        "trialDbId" : "7",
                        "trialName" : "InternationalTrialA",
                        "studyType": "Trial",
                        "seasons": ["2007 Spring", "2008 Fall"],
                        "locationDbId": "23",
                        "locationName": "Kenya",
                        "programDbId": "27",
                        "programName": "Drought Resistance Program A",
                        "startDate": "2007-06-01",
                        "endDate"  : "2008-12-31",
                        "active" : "true", 
                        "additionalInfo" : {
                            "property1Name" : "property1Value",
                            "property2Name" : "property2Value",
                            "property3Name" : "property3Value"
                        }
                    }
                    ,
                    {
                        "studyDbId": "345",
                        "name": "Earlygenerationtesting",
                        "trialDbId" : "7",
                        "trialName" : "InternationalTrialA",
                        "studyType": "Trial",
                        "seasons": ["2007 Spring", "2008 Fall"],
                        "locationDbId": "33",
                        "locationName": "Zimbabwe",
                        "programDbId": "58",
                        "programName": "Drought Resistance Program B",
                        "startDate": "2005-06-01",
                        "endDate"  : "2008-12-31",
                        "active" : "true",
                        "additionalInfo" : {
                            "property1Name" : "property1Value",
                            "property2Name" : "property2Value",
                            "property3Name" : "property3Value"
                        }
                    }
                ]
            }
        }        
