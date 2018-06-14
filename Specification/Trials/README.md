
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
    "result": {
        "data": [
            {
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
                "endDate": "2008-12-31",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "startDate": "2007-06-01",
                "trialDbId": "1",
                "programDbId": "27",
                "active": "false",
                "programName": "International Yield Trial",
                "trialName": "InternationalTrialA"
            },
            {
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
                "endDate": "2009-12-31",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "startDate": "2008-06-01",
                "trialDbId": "2",
                "programDbId": "35",
                "active": "true",
                "programName": "International Yield Trial 2: Return of the Trial",
                "trialName": "InternationalTrialB"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Trials/{trialdbid} [Get /brapi/v1/trials/{trialDbId}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016.
Get trial by id.
<a href="https://test-server.brapi.org/brapi/v1/trials"> test-server.brapi.org/brapi/v1/trials/{trialDbId}</a> 

+ Parameters
    + trialDbId (Required, string) ... The internal trialDbId


+ Response 200 (application/json)
```
{
    "result": {
        "studies": [
            {
                "locationName": "Zimbabwe",
                "locationDbId": "z-2",
                "studyDbId": 1,
                "studyName": "Zimbabwe Yield Trial"
            },
            {
                "locationName": "Kenya",
                "locationDbId": "k-1",
                "studyDbId": 2,
                "studyName": "Kenya Yield Trial"
            }
        ],
        "endDate": "2008-12-31",
        "additionalInfo": {
            "property3Name": "property3Value",
            "publications": "pmid:239823988, doi:10.2345/GEZG3T23535",
            "property2Name": "property2Value"
        },
        "startDate": "2007-06-01",
        "trialDbId": 1,
        "programDbId": 27,
        "datasetAuthorship": {
            "license": "https://creativecommons.org/licenses/by/4.0",
            "datasetPUI": "doi:10.15454/312953986E3"
        },
        "active": "true",
        "contacts": [
            {
                "type": "Scientist",
                "email": "j.doe@mail.com",
                "contactDbId": "C025",
                "instituteName": "IRRI",
                "name": "John Doe",
                "orcid": "0000-0002-0607-8728"
            },
            {
                "type": null,
                "email": null,
                "contactDbId": "C026",
                "instituteName": "IRRI",
                "name": "Dave Peters",
                "orcid": null
            }
        ],
        "programName": "International Yield Trial",
        "trialName": "InternationalTrialA"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```