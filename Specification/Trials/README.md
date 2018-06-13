
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
                "active": "false",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "programDbId": "27",
                "trialDbId": "1",
                "trialName": "InternationalTrialA",
                "programName": "International Yield Trial",
                "studies": [
                    {
                        "studyName": "Zimbabwe Yield Trial",
                        "locationName": "Zimbabwe",
                        "studyDbId": "1"
                    },
                    {
                        "studyName": "Kenya Yield Trial",
                        "locationName": "Kenya",
                        "studyDbId": "2"
                    }
                ],
                "endDate": "2008-12-31"
            },
            {
                "startDate": "2008-06-01",
                "active": "true",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "programDbId": "35",
                "trialDbId": "2",
                "trialName": "InternationalTrialB",
                "programName": "International Yield Trial 2: Return of the Trial",
                "studies": [
                    {
                        "studyName": "Zimbabwe Yield Trial",
                        "locationName": "Zimbabwe",
                        "studyDbId": "3"
                    },
                    {
                        "studyName": "Kenya Yield Trial",
                        "locationName": "Kenya",
                        "studyDbId": "4"
                    }
                ],
                "endDate": "2009-12-31"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
        "active": "true",
        "contacts": [
            {
                "name": "John Doe",
                "instituteName": "IRRI",
                "contactDbId": "C025",
                "orcid": "0000-0002-0607-8728",
                "email": "j.doe@mail.com",
                "type": "Scientist"
            },
            {
                "name": "Dave Peters",
                "instituteName": "IRRI",
                "contactDbId": "C026",
                "orcid": null,
                "email": null,
                "type": null
            }
        ],
        "additionalInfo": {
            "publications": "pmid:239823988, doi:10.2345/GEZG3T23535",
            "property2Name": "property2Value",
            "property3Name": "property3Value"
        },
        "programDbId": 27,
        "trialDbId": 1,
        "trialName": "InternationalTrialA",
        "programName": "International Yield Trial",
        "datasetAuthorship": {
            "license": "https://creativecommons.org/licenses/by/4.0",
            "datasetPUI": "doi:10.15454/312953986E3"
        },
        "studies": [
            {
                "studyName": "Zimbabwe Yield Trial",
                "locationDbId": "z-2",
                "locationName": "Zimbabwe",
                "studyDbId": 1
            },
            {
                "studyName": "Kenya Yield Trial",
                "locationDbId": "k-1",
                "locationName": "Kenya",
                "studyDbId": 2
            }
        ],
        "endDate": "2008-12-31"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
    }
}
```