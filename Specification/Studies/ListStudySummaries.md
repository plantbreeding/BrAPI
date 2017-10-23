## List Study Summaries [/brapi/v1/studies-search?studyType={studyType}&seasonDbId={seasonDbId}&locationDbId={locationDbId}&programDbId={programDbId}&germplasmDbIds={germplasmDbIds}&observationVariableDbIds={observationVariableDbIds}&pageSize={pageSize}&page={page}&active={active}&sortBy={sortBy}&sortOrder={sortOrder}]
Scope: PHENOTYPING.
Status: ACCEPTED.
Implementation target date: PAG2016.

Implemented by: Germinate

Used by: Flapjack, Cassavabase

Get list of studies

StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD

### List of study summaries [GET]

+ Parameters
    + studyType (optional, string, `Nursery`) ... Filter based on study type e.g. Nursery, Trial or Genotype.
    + programDbId (optional, string, `1`) ... Program filter to only return studies associated with given program id.
    + locationDbId (optional, string, `212`) ... Filter by location
    + seasonDbId (optional, string, `2016E`) ... Filter by season or year
    + pageSize (optional, integer, `1000`) 
    + page (optional, integer, `100`)
    + germplasmDbIds (optional, array, `["CML123", "CML"]`) ... Filter studies where specified germplasm have been used/tested
    + observationVariableDbIds (optional, array, `["CO-PH-123" , "Var-123"]`) ... Filter studies where specified observation variables have been measured
    + active (optional, boolean, `true/false`) ... Filter active status true/false. 
    + sortBy (optional, boolean, `studyDbId`) ... Sort order. Name of the field to sorty by.
    + sortOrder (optional, boolean, `asc/desc`) ... Sort order direction. Ascending/Descending.
    
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
                        "studyDbId": 35,
                        "name": "Earlygenerationtesting",
                        "trialDbId" : 1,
                        "trialName" : "InternationalTrialA",
                        "studyType": "Trial",
                        "seasons": ["2007 Spring", "2008 Fall"],
                        "locationDbId": 23,
                        "locationName": "Kenya",
                        "programDbId": 27,
                        "programName": "Drought Resistance Program A",
                        "startDate": "2007-06-01",
                        "endDate"  : "2008-12-31",
                        "studyType": "Trial",
                        "active" : "true", 
                        "additionalInfo" : {
                            "property1Name" : "property1Value",
                            "property2Name" : "property2Value",
                            "property3Name" : "property3Value"
                        }
                    }
                    ,
                    {
                        "studyDbId": 345,
                        "name": "Earlygenerationtesting",
                        "trialDbId" : 1,
                        "trialName" : "InternationalTrialA",
                        "seasons": ["2007 Spring", "2008 Fall"],
                        "locationDbId": 33,
                        "locationName": "Zimbabwe",
                        "programDbId": 58,
                        "programName": "Drought Resistance Program B",
                        "startDate": "2005-06-01",
                        "endDate"  : "2008-12-31",
                        "studyType": "Trial",
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
