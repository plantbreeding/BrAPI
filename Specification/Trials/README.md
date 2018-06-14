
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
                "startDate": "2007-06-01",
                "trialName": "InternationalTrialA",
                "endDate": "2008-12-31",
                "additionalInfo": {
                    "property2Name": "property2Value",
                    "property1Name": "property1Value",
                    "property3Name": "property3Value"
                },
                "studies": [
                    {
                        "studyDbId": "1",
                        "studyName": "Zimbabwe Yield Trial",
                        "locationName": "Zimbabwe"
                    },
                    {
                        "studyDbId": "2",
                        "studyName": "Kenya Yield Trial",
                        "locationName": "Kenya"
                    }
                ],
                "active": "false",
                "programName": "International Yield Trial",
                "trialDbId": "1",
                "programDbId": "27"
            },
            {
                "startDate": "2008-06-01",
                "trialName": "InternationalTrialB",
                "endDate": "2009-12-31",
                "additionalInfo": {
                    "property2Name": "property2Value",
                    "property1Name": "property1Value",
                    "property3Name": "property3Value"
                },
                "studies": [
                    {
                        "studyDbId": "3",
                        "studyName": "Zimbabwe Yield Trial",
                        "locationName": "Zimbabwe"
                    },
                    {
                        "studyDbId": "4",
                        "studyName": "Kenya Yield Trial",
                        "locationName": "Kenya"
                    }
                ],
                "active": "true",
                "programName": "International Yield Trial 2: Return of the Trial",
                "trialDbId": "2",
                "programDbId": "35"
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
        "status": [],
        "datafiles": []
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
        "startDate": "2007-06-01",
        "datasetAuthorship": {
            "license": "https://creativecommons.org/licenses/by/4.0",
            "datasetPUI": "doi:10.15454/312953986E3"
        },
        "contacts": [
            {
                "instituteName": "IRRI",
                "name": "John Doe",
                "contactDbId": "C025",
                "email": "j.doe@mail.com",
                "orcid": "0000-0002-0607-8728",
                "type": "Scientist"
            },
            {
                "instituteName": "IRRI",
                "name": "Dave Peters",
                "contactDbId": "C026",
                "email": null,
                "orcid": null,
                "type": null
            }
        ],
        "endDate": "2008-12-31",
        "additionalInfo": {
            "property2Name": "property2Value",
            "publications": "pmid:239823988, doi:10.2345/GEZG3T23535",
            "property3Name": "property3Value"
        },
        "studies": [
            {
                "studyDbId": 1,
                "locationDbId": "z-2",
                "locationName": "Zimbabwe",
                "studyName": "Zimbabwe Yield Trial"
            },
            {
                "studyDbId": 2,
                "locationDbId": "k-1",
                "locationName": "Kenya",
                "studyName": "Kenya Yield Trial"
            }
        ],
        "active": "true",
        "programName": "International Yield Trial",
        "trialDbId": 1,
        "programDbId": 27,
        "trialName": "InternationalTrialA"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [],
        "datafiles": []
    }
}
```