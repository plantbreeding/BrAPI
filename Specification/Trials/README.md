
# Group Trials

Services related to trials. Trials comprise of multiple studies. The trial concept in BrAPI corresponds to the "investigation" concept in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).




## Trials [Get /brapi/v1/trials{?programDbId}{?locationDbId}{?pageSize}{?page}{?active}{?sortBy}{?sortOrder}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016.
<a href="https://test-server.brapi.org/brapi/v1/trials"> test-server.brapi.org/brapi/v1/trials</a> 

+ Parameters
    + programDbId (Optional, string) ... Program filter to only return trials associated with given program id.
    + locationDbId (Optional, string) ... Filter by location
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + active (Optional, boolean) ... Filter active status true/false.
    + sortBy (Optional, string) ... Sort order. Name of the field to sorty by.
    + sortOrder (Optional, string) ... Sort order direction: asc/desc


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "active": "false",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "endDate": "2008-12-31",
                "programDbId": "27",
                "programName": "International Yield Trial",
                "startDate": "2007-06-01",
                "studies": [
                    {
                        "locationName": "Zimbabwe",
                        "studyDbId": "1",
                        "studyName": "Zimbabwe Yield Trial"
                    },
                    {
                        "locationName": "Kenya",
                        "studyDbId": "2",
                        "studyName": "Kenya Yield Trial"
                    }
                ],
                "trialDbId": "1",
                "trialName": "InternationalTrialA"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "endDate": "2009-12-31",
                "programDbId": "35",
                "programName": "International Yield Trial 2: Return of the Trial",
                "startDate": "2008-06-01",
                "studies": [
                    {
                        "locationName": "Zimbabwe",
                        "studyDbId": "3",
                        "studyName": "Zimbabwe Yield Trial"
                    },
                    {
                        "locationName": "Kenya",
                        "studyDbId": "4",
                        "studyName": "Kenya Yield Trial"
                    }
                ],
                "trialDbId": "2",
                "trialName": "InternationalTrialB"
            }
        ]
    }
}
```

## Trials/{trialDbId} [Get /brapi/v1/trials/{trialDbId}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016.
Get trial by id.
<a href="https://test-server.brapi.org/brapi/v1/trials"> test-server.brapi.org/brapi/v1/trials/{trialDbId}</a> 

+ Parameters
    + trialDbId (Required, string) ... The internal trialDbId


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "active": "true",
        "additionalInfo": {
            "property2Name": "property2Value",
            "property3Name": "property3Value",
            "publications": "pmid:239823988, doi:10.2345/GEZG3T23535"
        },
        "contacts": [
            {
                "contactDbId": "C025",
                "email": "j.doe@mail.com",
                "instituteName": "IRRI",
                "name": "John Doe",
                "orcid": "0000-0002-0607-8728",
                "type": "Scientist"
            },
            {
                "contactDbId": "C026",
                "email": null,
                "instituteName": "IRRI",
                "name": "Dave Peters",
                "orcid": null,
                "type": null
            }
        ],
        "datasetAuthorship": {
            "datasetPUI": "doi:10.15454/312953986E3",
            "license": "https://creativecommons.org/licenses/by/4.0"
        },
        "endDate": "2008-12-31",
        "programDbId": 27,
        "programName": "International Yield Trial",
        "startDate": "2007-06-01",
        "studies": [
            {
                "locationDbId": "z-2",
                "locationName": "Zimbabwe",
                "studyDbId": 1,
                "studyName": "Zimbabwe Yield Trial"
            },
            {
                "locationDbId": "k-1",
                "locationName": "Kenya",
                "studyDbId": 2,
                "studyName": "Kenya Yield Trial"
            }
        ],
        "trialDbId": 1,
        "trialName": "InternationalTrialA"
    }
}
```