## Study Details [/brapi/v1/studies/{studyDbId}?expand={expand}]
Scope: CORE.
Status: ACCEPTED.
Implementation target date: PAG2016  Implemented by: Germinate

Notes: an additionalInfo field was added to provide a controlled vocabulary for less common data fields.

Retrieve the information of the study required for field data collection

###### Response data types

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|studyDbId|Long|internal DB id ||
|studyName|string|Human readable name||
|years|list|list of years the trials is running||
|locationDbId|string| Location ID||
|additionalInfo|object|Generic name value pair properties/attributes ||

### Retrieve study details [GET]

+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    + expand (optional, string, `location,observationVariables,germplasm,observationunits,layout`) ... Comma separated list of study details sections to expand. If none is specified, each details section will only produce a link to get details using relevant BrAPI call, by default.
    
+ Response 200 (application/json)
    
        {             
            "metadata": {
                "pagination" : null,
                "status" : null,
                "datafiles": []
            },
            "result" : {
                "studyDbId": 35,
                "studyName": "Earlygenerationtesting",
                "studyType": "Yield study",
                "locationDbId": 34,
                "locationName" : "Zimbabwe",
                "seasons": ["2005 Winter", "2008 Summer"],
                "trialDbId": 57,
                "trialName": "International Yield Trial",
                "startDate": "2005-06-01",
                "endDate"  : "2008-12-31",
                "active" : "true",
                "additionalInfo" : {
                    "studyObjective" : "Increase yield",
                    "principalInvestigator" : "Dr. Breeder",
                    "property1Name" : "property1Value",
                    "property2Name" : "property2Value",
                    "property3Name" : "property3Value"
                },
                "observationVariables" : "/brapi/v1/studies/{studyDbId}/observationVariables", 
                "location" : "/brapi/v1/locations/{locationDbId}",
                "germplasm" : "/brapi/v1/studies/{studyDbId}/germplasm",
                "observationunits": "/brapi/v1/studies/{studyId}/observationunits", 
                "layout" : "/brapi/v1/studies/{studyDbId}/layout"
            }
        }
