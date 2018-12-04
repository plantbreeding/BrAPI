
# Group Trials

Services related to trials. Trials comprise of multiple studies. The trial concept in BrAPI corresponds to the "investigation" concept in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).




## Trials [/brapi/v1/trials] 




### Get Trials  [GET /brapi/v1/trials{?commonCropName}{?programDbId}{?locationDbId}{?active}{?sortBy}{?sortOrder}{?page}{?pageSize}]

Retrieve a filtered list of Trials. A Trial is a collection of studies

 

+ Parameters
    + commonCropName (Optional, ) ... Common name for the crop associated with this trial
    + programDbId (Optional, ) ... Program filter to only return trials associated with given program id.
    + locationDbId (Optional, ) ... Filter by location
    + active (Optional, ) ... Filter active status true/false.
    + sortBy (Optional, ) ... Sort order. Name of the field to sorty by.
    + sortOrder (Optional, ) ... Sort order direction: asc/desc
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 10,
            "totalPages": 5
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "active": false,
                "additionalInfo": {
                    "donorName": "Donor1",
                    "publications": "doi:10.2345/GEZG3T23535",
                    "specialProject": "Project1"
                },
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2013-07-05",
                "programDbId": "1",
                "programName": "Program 1",
                "startDate": "2013-01-01",
                "studies": [
                    {
                        "locationDbId": "1",
                        "locationName": "Location 1",
                        "studyDbId": "1001",
                        "studyName": "Study 1"
                    },
                    {
                        "locationDbId": "1",
                        "locationName": "Location 1",
                        "studyDbId": "1002",
                        "studyName": "Study 2"
                    }
                ],
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": false,
                "additionalInfo": {
                    "donorName": "Donor1",
                    "publications": "doi:10.2345/GEZG3T23535",
                    "specialProject": "Project1"
                },
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2013-07-05",
                "programDbId": "1",
                "programName": "Program 1",
                "startDate": "2013-01-01",
                "studies": [
                    {
                        "locationDbId": "1",
                        "locationName": "Location 1",
                        "studyDbId": "1001",
                        "studyName": "Study 1"
                    },
                    {
                        "locationDbId": "1",
                        "locationName": "Location 1",
                        "studyDbId": "1002",
                        "studyName": "Study 2"
                    }
                ],
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Trials by trialDbId  [GET /brapi/v1/trials/{trialDbId}]

Get trial by id.

 

+ Parameters
    + trialDbId (Required, ) ... The internal trialDbId
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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
        "active": false,
        "additionalInfo": {
            "donorName": "Donor1",
            "publications": "doi:10.2345/GEZG3T23535",
            "specialProject": "Project1"
        },
        "commonCropName": "Tomatillo",
        "contacts": [
            {
                "contactDbId": "4",
                "email": "b.technician@brapi.org",
                "instituteName": "Plant Science Institute",
                "name": "B. Technician",
                "orcid": "0000-0002-0607-8732",
                "type": "Technician"
            },
            {
                "contactDbId": "3",
                "email": "a.technician@brapi.org",
                "instituteName": "Plant Science Institute",
                "name": "A. Technician",
                "orcid": "0000-0002-0607-8731",
                "type": "Technician"
            }
        ],
        "datasetAuthorship": {
            "datasetPUI": "doi:10.15454/312953986E3",
            "license": "https://creativecommons.org/licenses/by/4.0"
        },
        "datasetAuthorships": [
            {
                "datasetPUI": "doi:10.15454/312953986E3",
                "license": "https://creativecommons.org/licenses/by/4.0"
            }
        ],
        "documentationURL": "https://brapi.org",
        "endDate": "2013-07-05",
        "programDbId": "1",
        "programName": "Program 1",
        "publications": [
            {
                "publicationPUI": "doi:10.15454/312953986E3",
                "publicationReference": "https://brapi.org"
            }
        ],
        "startDate": "2013-01-01",
        "studies": [
            {
                "locationDbId": "1",
                "locationName": "Location 1",
                "studyDbId": "1001",
                "studyName": "Study 1"
            },
            {
                "locationDbId": "1",
                "locationName": "Location 1",
                "studyDbId": "1002",
                "studyName": "Study 2"
            }
        ],
        "trialDbId": "101",
        "trialName": "Peru Yield Trial 1"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

