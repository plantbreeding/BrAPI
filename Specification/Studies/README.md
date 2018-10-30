
# Group Study

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).

Note that dates should be provided in extended ISO 8601 format (for example, "YYYY-MM-DD").




## Observationlevels [/brapi/v1/observationlevels] 




### Get Observationlevels  [GET /brapi/v1/observationlevels{?page}{?pageSize}]

Call to retrieve the list of supported observation levels. 
Observation levels indicate the granularity level at which the measurements are taken. 
The values are used to supply the `observationLevel` parameter in the observation unit details call.

 

+ Parameters
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
            "totalCount": 11,
            "totalPages": 6
        },
        "status": []
    },
    "result": {
        "data": [
            "plant",
            "plot"
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





### **Deprecated** Get ObservationLevels  [GET /brapi/v1/observationLevels{?page}{?pageSize}]

 ** DEPRECTED ** Use /observationlevels
Call to retrieve the list of supported observation levels. Observation levels indicate the granularity level at which the measurements are taken. The values are used to supply the `observationLevel` parameter in the observation unit details call. 

 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 11,
            "totalPages": 6
        },
        "status": []
    },
    "result": {
        "data": [
            "plant",
            "plot"
        ]
    }
}
```



## Search [/brapi/v1/search] 




### Post Search Studies  [POST /brapi/v1/search/studies]

Get list of studies
StartDate and endDate should be ISO8601 format for dates
See Search Services for additional implementation details.

 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropNames": [
        "commonCropNames0",
        "commonCropNames1"
    ],
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "programNames": [
        "programNames0",
        "programNames1"
    ],
    "seasonDbIds": [
        "seasonDbIds0",
        "seasonDbIds1"
    ],
    "sortBy": "studyDbId",
    "sortOrder": "ASC",
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "studyNames": [
        "studyNames0",
        "studyNames1"
    ],
    "studyTypeDbIds": [
        "studyTypeDbIds0",
        "studyTypeDbIds1"
    ],
    "studyTypeNames": [
        "studyTypeNames0",
        "studyTypeNames1"
    ],
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



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
        "searchResultDbId": "551ae08c-4548-4bde-ad70-f23beb25e2ea"
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





### Get Search Studies by searchResultsDbId  [GET /brapi/v1/search/studies/{searchResultsDbId}{?page}{?pageSize}]

Get list of studies

StartDate and endDate should be ISO8601 format for dates

See Search Services for additional implementation details.

 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
            "totalCount": 3,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "active": "true",
                "additionalInfo": {
                    "studyObjective": "Increase yield"
                },
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "fall 2011",
                    "winter 2012"
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyType": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "winter 2012"
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyType": "Yield study",
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Seasons [/brapi/v1/seasons] 




### Get Seasons  [GET /brapi/v1/seasons{?seasonDbId}{?season}{?year}{?page}{?pageSize}]

Call to retrive all seasons in the database.

A season is made of 2 parts

- The primary year 

- A term which defines a segment of the year. 
This could be a traditional season, like "Spring" or "Summer"; 
this could be a month, like "May" or "June"; 
or this could be an arbitrary season name which is meaningful to the breeding program like "PlantingTime_3" or "Season E"

 

+ Parameters
    + seasonDbId (Optional, ) ... The unique identifier for a season
    + season (Optional, ) ... The term to describe a given season. Example "Spring" OR "May" OR "PlantingTime7"
    + year (Optional, ) ... The 4 digit year of a season. Example "2017"
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
                "season": "fall",
                "seasonDbId": "1",
                "year": "2011"
            },
            {
                "season": "winter",
                "seasonDbId": "2",
                "year": "2012"
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



## Studies-search [/brapi/v1/studies-search] 




### **Deprecated** Get Studies-search  [GET /brapi/v1/studies-search{?studyType}{?programDbId}{?locationDbId}{?seasonDbId}{?trialDbId}{?studyDbId}{?germplasmDbIds}{?observationVariableDbIds}{?page}{?pageSize}{?active}{?sortBy}{?sortOrder}]

DEPRECATED in v1.3 - see GET /studies

 

+ Parameters
    + studyType (Optional, ) ... Filter based on study type e.g. Nursery, Trial or Genotype.
    + programDbId (Optional, ) ... Program filter to only return studies associated with given program id.
    + locationDbId (Optional, ) ... Filter by location
    + seasonDbId (Optional, ) ... Filter by season or year
    + trialDbId (Optional, ) ... Filter by trial
    + studyDbId (Optional, ) ... Filter by study DbId
    + germplasmDbIds (Optional, ) ... Filter studies where specified germplasm have been used/tested
    + observationVariableDbIds (Optional, ) ... Filter studies where specified observation variables have been measured
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + active (Optional, ) ... Filter active status true/false.
    + sortBy (Optional, ) ... Sort order. Name of the field to sort by.
    + sortOrder (Optional, ) ... Sort order direction. Ascending/Descending.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 3,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "active": "true",
                "additionalInfo": {
                    "studyObjective": "Increase yield"
                },
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "fall 2011",
                    "winter 2012"
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyType": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "winter 2012"
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyType": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            }
        ]
    }
}
```





### **Deprecated** Post Studies-search  [POST /brapi/v1/studies-search]

DEPRECATED in v1.3 - see /search/studies

 

+ Parameters


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "programNames": [
        "programNames0",
        "programNames1"
    ],
    "seasonDbId": [
        "seasonDbId0",
        "seasonDbId1"
    ],
    "sortBy": "studyDbId",
    "sortOrder": "asc",
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "studyLocations": [
        "studyLocations0",
        "studyLocations1"
    ],
    "studyNames": [
        "studyNames0",
        "studyNames1"
    ],
    "studyType": "studyType0",
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 3,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "active": "true",
                "additionalInfo": {
                    "studyObjective": "Increase yield"
                },
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "fall 2011",
                    "winter 2012"
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyType": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "winter 2012"
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyType": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            }
        ]
    }
}
```



## Studies [/brapi/v1/studies] 




### Get Studies  [GET /brapi/v1/studies{?commonCropName}{?studyType}{?studyTypeDbId}{?programDbId}{?locationDbId}{?seasonDbId}{?trialDbId}{?studyDbId}{?germplasmDbIds}{?observationVariableDbIds}{?active}{?sortBy}{?sortOrder}{?page}{?pageSize}]

Get list of studies

Implementation Notes

StartDate and endDate should be ISO8601 format for dates

See Search Services for additional implementation details.

 

+ Parameters
    + commonCropName (Optional, ) ... Common name for the crop associated with this study
    + studyType (Optional, ) ... DEPRECATED in v1.3 - see "studyTypeDbId"
    + studyTypeDbId (Optional, ) ... Filter based on study type unique identifier
    + programDbId (Optional, ) ... Program filter to only return studies associated with given program id.
    + locationDbId (Optional, ) ... Filter by location
    + seasonDbId (Optional, ) ... Filter by season or year
    + trialDbId (Optional, ) ... Filter by trial
    + studyDbId (Optional, ) ... Filter by study DbId
    + germplasmDbIds (Optional, ) ... DEPRECATED in v1.3 - see /search/studies
    + observationVariableDbIds (Optional, ) ... DEPRECATED in v1.3 - see /search/studies
    + active (Optional, ) ... Filter active status true/false.
    + sortBy (Optional, ) ... Name of the field to sort by.
    + sortOrder (Optional, ) ... Sort order direction. Ascending/Descending.
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
            "totalCount": 3,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "active": "true",
                "additionalInfo": {
                    "studyObjective": "Increase yield"
                },
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "fall 2011",
                    "winter 2012"
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyType": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    "winter 2012"
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyType": "Yield study",
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





### Get Studies by studyDbId  [GET /brapi/v1/studies/{studyDbId}]

Retrieve the information of the study required for field data collection

An additionalInfo field was added to provide a controlled vocabulary for less common data fields.

Linked data

- Observation Variables: ```/brapi/v1/studies/{studyDbId}/observationvariables``` 

- Germplasm: ```/brapi/v1/studies/{studyDbId}/germplasm``` 

- Observation Units: ```/brapi/v1/studies/{studyDbId}/observationunits``` 

- Layout: ```brapi/v1/studies/{studyDbId}/layout```

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
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
        "active": "true",
        "additionalInfo": {
            "studyObjective": "Increase yield"
        },
        "commonCropName": null,
        "contacts": [
            {
                "contactDbId": "1",
                "email": "a.breeder@brapi.org",
                "instituteName": "Plant Science Institute",
                "name": "A. Breeder",
                "orcid": "0000-0002-0607-8728",
                "type": "Breeder"
            },
            {
                "contactDbId": "2",
                "email": "b.breeder@brapi.org",
                "instituteName": "Plant Science Institute",
                "name": "B. Breeder",
                "orcid": "0000-0002-0607-8729",
                "type": "Breeder"
            }
        ],
        "dataLinks": [
            {
                "dataLinkName": null,
                "name": "image-archive12.zip",
                "type": "Image archive",
                "url": "http://data.inra.fr/archive/multi-spect-flowering.zip"
            },
            {
                "dataLinkName": null,
                "name": "image-archive13.zip",
                "type": "Image archive",
                "url": "http://data.inra.fr/archive/biomass-img.zip"
            }
        ],
        "documentationURL": null,
        "endDate": "2014-01-01",
        "lastUpdate": {
            "timestamp": "2015-01-01T00:00:00-05:00",
            "version": "1.1"
        },
        "license": "https://creativecommons.org/licenses/by/4.0",
        "location": {
            "abbreviation": "L1",
            "abreviation": "L1",
            "additionalInfo": {
                "adm1": "Junin",
                "adm2": "Chanchamayo",
                "adm3": "San Ramon",
                "annualMeanTemperature": "23",
                "annualTotalPrecipitation": "360",
                "cont": "South America",
                "creg": "LAC",
                "local": "San Ramon"
            },
            "altitude": 828,
            "countryCode": "PER",
            "countryName": "Peru",
            "documentationURL": null,
            "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
            "instituteAdress": "71 Pilgrim Avenue Chevy Chase MD 20815",
            "instituteName": "Plant Science Institute",
            "latitude": -11.1274995803833,
            "locationDbId": "1",
            "locationName": null,
            "locationType": "Storage location",
            "longitude": -75.35639190673828,
            "name": "Location 1"
        },
        "seasons": [
            "fall 2011",
            "winter 2012"
        ],
        "startDate": "2013-01-01",
        "studyDbId": "1001",
        "studyDescription": "Field yield phenotyping study",
        "studyName": "Study 1",
        "studyType": "Yield study",
        "studyTypeDbId": null,
        "studyTypeName": null,
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





### Get Studies Germplasm by studyDbId  [GET /brapi/v1/studies/{studyDbId}/germplasm{?page}{?pageSize}]

Get the available Germplasm which are associated with this study

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
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
            "totalCount": 4,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A000001",
                "acquisitionDate": null,
                "biologicalStatusOfAccessionCode": null,
                "breedingMethodDbId": null,
                "commonCropName": null,
                "countryOfOriginCode": null,
                "defaultDisplayName": null,
                "documentationURL": null,
                "donors": null,
                "entryNumber": "1",
                "genus": null,
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "germplasmPUI": "http://pui.per/accession/A000001",
                "instituteCode": null,
                "instituteName": null,
                "pedigree": "A000001",
                "seedSource": "open pollination",
                "species": null,
                "speciesAuthority": null,
                "subtaxa": null,
                "subtaxaAuthority": null,
                "synonyms": [
                    "landrace 1"
                ],
                "taxonIds": null,
                "typeOfGermplasmStorageCode": null
            },
            {
                "accessionNumber": "A000002",
                "acquisitionDate": null,
                "biologicalStatusOfAccessionCode": null,
                "breedingMethodDbId": null,
                "commonCropName": null,
                "countryOfOriginCode": null,
                "defaultDisplayName": null,
                "documentationURL": null,
                "donors": null,
                "entryNumber": "4",
                "genus": null,
                "germplasmDbId": "2",
                "germplasmName": "Name002",
                "germplasmPUI": "http://pui.per/accession/A000002",
                "instituteCode": null,
                "instituteName": null,
                "pedigree": "A000002",
                "seedSource": "open pollination",
                "species": null,
                "speciesAuthority": null,
                "subtaxa": null,
                "subtaxaAuthority": null,
                "synonyms": [
                    "landrace 2"
                ],
                "taxonIds": null,
                "typeOfGermplasmStorageCode": null
            }
        ],
        "studyDbId": "1001",
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





### Get Studies Layouts by studyDbId  [GET /brapi/v1/studies/{studyDbId}/layouts{?page}{?pageSize}]

Retrive the layout details for a study. Returns an array of observation unit position data which describes where each unit and germplasm is located within the study layout

Retrieve the plot layout of the study with id {id}.

For each observationUnit within a study, return the `block`, `replicate`, and `entryType` values as well as the `X` and `Y` coordinates. `entryType` can be "check", "test", or "filler".

Also return some human readable meta data about the observationUnit and germplasm.

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
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
            "totalCount": 4,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "1",
                "additionalInfo": {},
                "blockNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plot",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "replicate": "0",
                "studyDbId": "1001"
            },
            {
                "X": "1",
                "Y": "1",
                "additionalInfo": {},
                "blockNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plant",
                "observationUnitDbId": "2",
                "observationUnitName": "Plant 1",
                "replicate": "0",
                "studyDbId": "1001"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Studies Layouts by studyDbId  [PUT /brapi/v1/studies/{studyDbId}/layouts]

Modify a study layout

Update the layout data for a set of observation units within a study. Each layout object is a subset of fields within an observationUnit, so it doesnt make sense to create a new layout object by itself.

Implementation Notes:

+ If any of the fields in the request object is missing, that piece of data will not be updated. 

+ If an observationUnitDbId can not be found within the given study, an error will be returned. 

+ `entryType` can have the values "check", "test", or "filler". 

+ The response should match the structure of the response from `GET studies/{studyDbId}/layout`, but it should only contain the layout objects which have been updated by the PUT request. Also, pagination is not available in the response.

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "layout": [
        {
            "X": "X0",
            "Y": "Y0",
            "blockNumber": 0,
            "entryType": "CHECK",
            "observationUnitDbId": "observationUnitDbId0",
            "positionCoordinateX": "positionCoordinateX0",
            "positionCoordinateXType": "LONGITUDE",
            "positionCoordinateY": "positionCoordinateY0",
            "positionCoordinateYType": "LONGITUDE",
            "replicate": 0
        },
        {
            "X": "X1",
            "Y": "Y1",
            "blockNumber": 0,
            "entryType": "TEST",
            "observationUnitDbId": "observationUnitDbId1",
            "positionCoordinateX": "positionCoordinateX1",
            "positionCoordinateXType": "LATITUDE",
            "positionCoordinateY": "positionCoordinateY1",
            "positionCoordinateYType": "LATITUDE",
            "replicate": 0
        }
    ]
}
```



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
        "data": [
            {
                "X": "10",
                "Y": "12",
                "additionalInfo": {},
                "blockNumber": "0",
                "entryType": "CHECK",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plot",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "replicate": "0",
                "studyDbId": "1001"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Post Studies Observationunits Zip by studyDbId  [POST /brapi/v1/studies/{studyDbId}/observationunits/zip]

If ''observationUnitDbId'' or ''observationDbId'' is populated, they should be considered updates to existing records. 

If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. 

If ''observationUnitDbId'' or ''observationDbId'' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds.

 

+ Parameters
    + studyDbId (Required, ) ... The study these observation units are related to.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "observationUnitDbIds": [
            "observationUnitDbIds0",
            "observationUnitDbIds1"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Studies Observationvariables by studyDbId  [GET /brapi/v1/studies/{studyDbId}/observationvariables{?page}{?pageSize}]

List all the observation variables measured in the study.

Refer to the data type definition of variables in `/Specification/ObservationVariables/README.md`.

 

+ Parameters
    + studyDbId (Required, ) ... string database unique identifier
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
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Standard rolled measuring tape",
                    "formula": "a^2 + b^2 = c^2",
                    "methodDbId": "m1",
                    "methodName": null,
                    "name": "Tape Measure",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 1,
                    "name": "Centimeter",
                    "ontologyRefernce": null,
                    "scaleDbId": "s1",
                    "scaleName": null,
                    "validValues": {
                        "categories": [],
                        "max": 99999,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "plant height",
                    "class": "Numeric",
                    "description": "plant height",
                    "entity": "entity",
                    "mainAbbreviation": "H",
                    "name": "Plant Height",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t1",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": null,
                    "name": "Standard Color Palette",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Carotenoid",
                "observationVariableDbId": "MO_123:100003",
                "observationVariableName": "Carotenoid",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": null,
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyRefernce": null,
                    "scaleDbId": "s3",
                    "scaleName": null,
                    "validValues": {
                        "categories": [
                            "dark red",
                            "red",
                            "dark blue",
                            "blue",
                            "black"
                        ],
                        "max": 0,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "leaf color",
                    "class": "Categorical",
                    "description": "color of leaf sample",
                    "entity": "entity",
                    "mainAbbreviation": "LC",
                    "name": "Leaf Color",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t3",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100003"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": null,
                    "name": "Standard Color Palette",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Root color",
                "observationVariableDbId": "MO_123:100005",
                "observationVariableName": "Root color",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": null,
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyRefernce": null,
                    "scaleDbId": "s3",
                    "scaleName": null,
                    "validValues": {
                        "categories": [
                            "dark red",
                            "red",
                            "dark blue",
                            "blue",
                            "black"
                        ],
                        "max": 0,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "root color",
                    "class": "Categorical",
                    "description": "color of root sample",
                    "entity": "entity",
                    "mainAbbreviation": "RC",
                    "name": "Root Color",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t4",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100005"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Percentage",
                    "description": "Image analysis of sample photo",
                    "formula": "Bobs Color Threshold Tool",
                    "methodDbId": "m4",
                    "methodName": null,
                    "name": "Image analysis",
                    "ontologyRefernce": null,
                    "reference": "https://bobsimageanalysis.com"
                },
                "name": "Virus severity",
                "observationVariableDbId": "MO_123:100006",
                "observationVariableName": "Virus severity",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": null,
                    "decimalPlaces": 0,
                    "name": "Percentage",
                    "ontologyRefernce": null,
                    "scaleDbId": "s4",
                    "scaleName": null,
                    "validValues": {
                        "categories": [],
                        "max": 100,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "Virus severity",
                    "class": "Percentage",
                    "description": "Percentage of contaminated sample",
                    "entity": "entity",
                    "mainAbbreviation": "LC",
                    "name": "Virus severity",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t5",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100006"
            }
        ],
        "studyDbId": "1001",
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





### Get Studies Observations by studyDbId  [GET /brapi/v1/studies/{studyDbId}/observations{?observationVariableDbIds}{?page}{?pageSize}]

Retrieve all observations where there are measurements for the given observation variables.

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + observationVariableDbIds (Optional, ) ... Numeric `id` of that variable (combination of trait, unit and method)
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
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationDbId": "3",
                "observationLevel": "plant",
                "observationTimestamp": "2013-06-14T22:05:51-04:00",
                "observationUnitDbId": "2",
                "observationUnitName": "Plant 1",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "operator": "Bob",
                "studyDbId": "1001",
                "uploadedBy": "Bob",
                "value": "1.1"
            },
            {
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationDbId": "4",
                "observationLevel": "plant",
                "observationTimestamp": "2013-06-14T22:06:51-04:00",
                "observationUnitDbId": "2",
                "observationUnitName": "Plant 1",
                "observationVariableDbId": "MO_123:100006",
                "observationVariableName": "Virus susceptibility",
                "operator": "Bob",
                "studyDbId": "1001",
                "uploadedBy": "Bob",
                "value": "5.1"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Studies Observations by studyDbId  [PUT /brapi/v1/studies/{studyDbId}/observations]

Implementation Guidelines: 

+ If an `observationDbId` is "null" or an empty string in the request, a NEW observation should be created for the given study and observationUnit 

+ If an `observationDbId` is populated but not found in the database, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client. 

+ If an `observationDbId` is populated and found in the database, but the existing entry is not associated with the given study or observationUnit, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client. 

+ If an `observationDbId` is populated and found in the database and is associated with the given study and observationUnit, then it should be updated with the new data given.

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "observations": [
        {
            "collector": "collector0",
            "observationDbId": "observationDbId0",
            "observationTimeStamp": "2018-01-01T14:47:23-0600",
            "observationUnitDbId": "observationUnitDbId0",
            "observationVariableDbId": "observationVariableDbId0",
            "value": "value0"
        },
        {
            "collector": "collector1",
            "observationDbId": "observationDbId1",
            "observationTimeStamp": "2018-01-01T14:47:23-0600",
            "observationUnitDbId": "observationUnitDbId1",
            "observationVariableDbId": "observationVariableDbId1",
            "value": "value1"
        }
    ]
}
```



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
    "result": null
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





### Get Studies Observationunits by studyDbId  [GET /brapi/v1/studies/{studyDbId}/observationunits{?observationLevel}{?page}{?pageSize}]

The main API call for field data collection, to retrieve all the observation units within a study.

 

+ Parameters
    + studyDbId (Required, ) ... The study these observation units are related to.
    + observationLevel (Optional, ) ... The granularity level of observation units. Either `plotNumber` or `plantNumber` fields will be relavant depending on whether granularity is plot or plant respectively.
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
            "totalCount": 4,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "1",
                "entryNumber": "2",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationUnitDbId": "2",
                "observationUnitName": "Plant 1",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865815",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH13",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239167",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "3",
                        "observationTimeStamp": "2013-06-14T22:05:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": null,
                        "value": "1.1"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "4",
                        "observationTimeStamp": "2013-06-14T22:06:51-04:00",
                        "observationVariableDbId": "MO_123:100006",
                        "observationVariableName": "Virus severity",
                        "season": null,
                        "value": "5.1"
                    }
                ],
                "pedigree": "A000001/A000002",
                "plantNumber": "1",
                "plotNumber": "1",
                "replicate": "0"
            },
            {
                "X": "1",
                "Y": "2",
                "blockNumber": "1",
                "entryNumber": "3",
                "entryType": "TEST",
                "germplasmDbId": "2",
                "germplasmName": "Name002",
                "observationUnitDbId": "3",
                "observationUnitName": "Plot 2",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865682",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH51",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239146",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "5",
                        "observationTimeStamp": "2013-06-14T22:07:51-04:00",
                        "observationVariableDbId": "MO_123:100003",
                        "observationVariableName": "Carotenoid",
                        "season": null,
                        "value": "2.1"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "6",
                        "observationTimeStamp": "2013-06-14T22:08:51-04:00",
                        "observationVariableDbId": "MO_123:100005",
                        "observationVariableName": "Root color",
                        "season": null,
                        "value": "dark blue"
                    }
                ],
                "pedigree": "A000001/A000002",
                "plantNumber": "0",
                "plotNumber": "2",
                "replicate": "0"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Studies Observationunits by studyDbId  [PUT /brapi/v1/studies/{studyDbId}/observationunits]

Use this call for uploading new Observations as JSON to a system.

Note: If ''observationUnitDbId'' or ''observationDbId'' is populated, they should be considered updates to existing records. 
If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. 
If ''observationUnitDbId'' or ''observationDbId'' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds.

 

+ Parameters
    + studyDbId (Required, ) ... The study these observation units are related to.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{}
```



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
        "status": [
            {
                "code": "200",
                "message": "Upload Successful",
                "messageType": null
            }
        ]
    },
    "result": {
        "observationUnitDbIds": [
            "080f6dd1-82a8-4308-a858-3c36d9e55948"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Studies Table by studyDbId  [GET /brapi/v1/studies/{studyDbId}/table{?format}]

Retrieve the details of the study required for field data collection. Includes actual trait data.

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + format (Optional, ) ... The format parameter will cause the data to be dumped to a file in the specified format. Currently, tsv and csv are supported.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/csv)
```
"year,studyDbId,studyName,locationDbId,locationName,germplasmDbId,germplasmName,observationUnitDbId,plotNumber,replicate,blockNumber,observationTimestamp,entryType,X,Y,variable1DbId,variable2DbId,variable3DbId\n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc123,1,1,1,2017-06-16T00:53:26Z,Test Entry,1,2,25.3,103.4,50.75 \n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc124,1,1,1,2017-06-16T00:54:57Z,Test Entry,2,2,27.9,98.65,45.345\n"
```

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
        "data": [
            [
                "2011",
                "1001",
                "Study 1",
                "1",
                "Peru",
                "1",
                "Name001",
                "2",
                "1",
                "0",
                "1",
                "2013-06-14T22:05:51-04:00",
                "TEST",
                "1",
                "1",
                "1.1",
                "",
                "",
                "5.1"
            ],
            [
                "2012",
                "1001",
                "Study 1",
                "1",
                "Peru",
                "2",
                "Name002",
                "3",
                "2",
                "0",
                "1",
                "2013-06-14T22:07:51-04:00",
                "TEST",
                "1",
                "2",
                "",
                "2.1",
                "dark blue",
                ""
            ],
            [
                "2012",
                "1001",
                "Study 1",
                "1",
                "Peru",
                "2",
                "Name002",
                "4",
                "2",
                "0",
                "1",
                "2013-06-14T22:09:51-04:00",
                "TEST",
                "1",
                "2",
                "",
                "1.8",
                "blue",
                ""
            ],
            [
                "2011",
                "1001",
                "Study 1",
                "1",
                "Peru",
                "1",
                "Name001",
                "1",
                "1",
                "0",
                "0",
                "2013-06-14T22:03:51-04:00",
                "CHECK",
                "10",
                "12",
                "1.2",
                "",
                "",
                "4.5"
            ]
        ],
        "headerRow": [
            "year",
            "studyDbId",
            "studyName",
            "locationDbId",
            "locationName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "plotNumber",
            "replicate",
            "blockNumber",
            "observationTimestamp",
            "entryType",
            "X",
            "Y"
        ],
        "observationVariableDbIds": [
            "MO_123:100002",
            "MO_123:100003",
            "MO_123:100005",
            "MO_123:100006"
        ],
        "observationVariableNames": [
            "Plant height",
            "Carotenoid",
            "Root color",
            "Virus severity"
        ]
    }
}
```

+ Response 200 (application/tsv)
```
"year\tstudyDbId\tstudyName\tlocationDbId\tlocationName\tgermplasmDbId\tgermplasmName\tobservationUnitDbId\tplotNumber\treplicate\tblockNumber\tobservationTimestamp\tentryType\tX\tY\tvariable1DbId\tvariable2DbId\tvariable3DbId\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc123\t1\t1\t1\t2017-06-16T00:53:26Z\tTest Entry\t1\t2\t25.3\t103.4\t50.75\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc124\t1\t1\t1\t2017-06-16T00:54:57Z\tTest Entry\t2\t2\t27.9\t98.65\t45.345\n"
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





### Post Studies Table by studyDbId  [POST /brapi/v1/studies/{studyDbId}/table]

This call can be used to create new observations in bulk.

Note: If you need to update any existing observation, please use `PUT /studies/{studyDbId}/observations`. This call should only be used to create NEW observations.

Implementation Guidelines:

+ All observations submitted through this call should create NEW observation records in the database under the given observation unit. 

+ Each "observationUnitDbId" listed should already exist in the database. If the server can not find a given "observationUnitDbId", it should report an error. (see Error Handling) 

+ The response of this call should be the set of "observationDbIds" created from this call, along with the associated "observationUnitDbId" and "observationVariableDbId" that each observation is associated with.

+ Images can optionally be saved using this call by providing a zipped file of all images in the datafiles. The physical zipped file should be transferred as well in the mulit-part form data.

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "data": [
        [
            "data0",
            "data1"
        ],
        [
            "data0",
            "data1"
        ]
    ],
    "headerRow": [
        "headerRow0",
        "headerRow1"
    ],
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
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "result": {
        "data": [
            [
                "data0",
                "data1"
            ],
            [
                "data0",
                "data1"
            ]
        ]
    }
}
```



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
    "result": null
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





### **Deprecated** Get Studies Layout by studyDbId  [GET /brapi/v1/studies/{studyDbId}/layout{?page}{?pageSize}]

DEPRECATED in v1.3 - see `GET /studies/{studyDbId}/layouts` (pluralized)

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
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
            "totalCount": 4,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "1",
                "additionalInfo": {},
                "blockNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plant",
                "observationUnitDbId": "2",
                "observationUnitName": "Plant 1",
                "replicate": "0",
                "studyDbId": "1001"
            },
            {
                "X": "1",
                "Y": "2",
                "additionalInfo": {},
                "blockNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "2",
                "germplasmName": "Name002",
                "observationLevel": "plot",
                "observationUnitDbId": "3",
                "observationUnitName": "Plot 2",
                "replicate": "0",
                "studyDbId": "1001"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### **Deprecated** Put Studies Layout by studyDbId  [PUT /brapi/v1/studies/{studyDbId}/layout]

DEPRECATED in v1.3 - see `PUT /studies/{studyDbId}/layouts` (pluralized)

 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "layout": [
        {
            "X": "X0",
            "Y": "Y0",
            "blockNumber": 0,
            "entryType": "CHECK",
            "observationUnitDbId": "observationUnitDbId0",
            "positionCoordinateX": "positionCoordinateX0",
            "positionCoordinateXType": "LONGITUDE",
            "positionCoordinateY": "positionCoordinateY0",
            "positionCoordinateYType": "LONGITUDE",
            "replicate": 0
        },
        {
            "X": "X1",
            "Y": "Y1",
            "blockNumber": 0,
            "entryType": "TEST",
            "observationUnitDbId": "observationUnitDbId1",
            "positionCoordinateX": "positionCoordinateX1",
            "positionCoordinateXType": "LATITUDE",
            "positionCoordinateY": "positionCoordinateY1",
            "positionCoordinateYType": "LATITUDE",
            "replicate": 0
        }
    ]
}
```



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
        "data": [
            {
                "X": "10",
                "Y": "12",
                "additionalInfo": {},
                "blockNumber": "0",
                "entryType": "CHECK",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plot",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "replicate": "0",
                "studyDbId": "1001"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### **Deprecated** Get Studies ObservationVariables by studyDbId  [GET /brapi/v1/studies/{studyDbId}/observationVariables]




test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationVariables

 

+ Parameters
    + studyDbId (Required, ) ... string database unique identifier




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
        "data": [
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Standard rolled measuring tape",
                    "formula": "a^2 + b^2 = c^2",
                    "methodDbId": "m1",
                    "methodName": null,
                    "name": "Tape Measure",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 1,
                    "name": "Centimeter",
                    "ontologyRefernce": null,
                    "scaleDbId": "s1",
                    "scaleName": null,
                    "validValues": {
                        "categories": [],
                        "max": 99999,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "plant height",
                    "class": "Numeric",
                    "description": "plant height",
                    "entity": "entity",
                    "mainAbbreviation": "H",
                    "name": "Plant Height",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t1",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": null,
                    "name": "Standard Color Palette",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Carotenoid",
                "observationVariableDbId": "MO_123:100003",
                "observationVariableName": "Carotenoid",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": null,
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyRefernce": null,
                    "scaleDbId": "s3",
                    "scaleName": null,
                    "validValues": {
                        "categories": [
                            "dark red",
                            "red",
                            "dark blue",
                            "blue",
                            "black"
                        ],
                        "max": 0,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "leaf color",
                    "class": "Categorical",
                    "description": "color of leaf sample",
                    "entity": "entity",
                    "mainAbbreviation": "LC",
                    "name": "Leaf Color",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t3",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100003"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": null,
                    "name": "Standard Color Palette",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Root color",
                "observationVariableDbId": "MO_123:100005",
                "observationVariableName": "Root color",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": null,
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyRefernce": null,
                    "scaleDbId": "s3",
                    "scaleName": null,
                    "validValues": {
                        "categories": [
                            "dark red",
                            "red",
                            "dark blue",
                            "blue",
                            "black"
                        ],
                        "max": 0,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "root color",
                    "class": "Categorical",
                    "description": "color of root sample",
                    "entity": "entity",
                    "mainAbbreviation": "RC",
                    "name": "Root Color",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t4",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100005"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Percentage",
                    "description": "Image analysis of sample photo",
                    "formula": "Bobs Color Threshold Tool",
                    "methodDbId": "m4",
                    "methodName": null,
                    "name": "Image analysis",
                    "ontologyRefernce": null,
                    "reference": "https://bobsimageanalysis.com"
                },
                "name": "Virus severity",
                "observationVariableDbId": "MO_123:100006",
                "observationVariableName": "Virus severity",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": null,
                    "decimalPlaces": 0,
                    "name": "Percentage",
                    "ontologyRefernce": null,
                    "scaleDbId": "s4",
                    "scaleName": null,
                    "validValues": {
                        "categories": [],
                        "max": 100,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "Virus severity",
                    "class": "Percentage",
                    "description": "Percentage of contaminated sample",
                    "entity": "entity",
                    "mainAbbreviation": "LC",
                    "name": "Virus severity",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t5",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100006"
            }
        ],
        "studyDbId": "1001",
        "trialName": "Peru Yield Trial 1"
    }
}
```





### **Deprecated** Post Studies Observationunits by studyDbId  [POST /brapi/v1/studies/{studyDbId}/observationunits{?format}]

This call has been deprecated in V1.1. Use instead: "PUT /studies/{studyDbId}/observationunits" and "PUT /studies/{studyDbId}/observationunits/zip"

 

+ Parameters
    + studyDbId (Required, ) ... The study these observation units are related to.
    + format (Required, ) ... (default is JSON, but can be zip) In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
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
        "commit": "commit0",
        "data": [
            {
                "observatioUnitDbId": "observatioUnitDbId0",
                "observations": [
                    {
                        "collector": "collector0",
                        "observationDbId": "observationDbId0",
                        "observationTimeStamp": "2018-01-01T14:47:23-0600",
                        "observationUnitDbId": "observationUnitDbId0",
                        "observationVariableDbId": "observationVariableDbId0",
                        "value": "value0"
                    },
                    {
                        "collector": "collector1",
                        "observationDbId": "observationDbId1",
                        "observationTimeStamp": "2018-01-01T14:47:23-0600",
                        "observationUnitDbId": "observationUnitDbId1",
                        "observationVariableDbId": "observationVariableDbId1",
                        "value": "value1"
                    }
                ]
            },
            {
                "observatioUnitDbId": "observatioUnitDbId1",
                "observations": [
                    {
                        "collector": "collector0",
                        "observationDbId": "observationDbId0",
                        "observationTimeStamp": "2018-01-01T14:47:23-0600",
                        "observationUnitDbId": "observationUnitDbId0",
                        "observationVariableDbId": "observationVariableDbId0",
                        "value": "value0"
                    },
                    {
                        "collector": "collector1",
                        "observationDbId": "observationDbId1",
                        "observationTimeStamp": "2018-01-01T14:47:23-0600",
                        "observationUnitDbId": "observationUnitDbId1",
                        "observationVariableDbId": "observationVariableDbId1",
                        "value": "value1"
                    }
                ]
            }
        ],
        "transactionDbId": "transactionDbId0"
    }
}
```



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
        "status": [
            {
                "code": "200",
                "message": "Upload Successful"
            }
        ]
    },
    "result": {
        "observationUnitDbIds": [
            "5873048a-f30d-435c-931a-c88b522304cc"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Studytypes [/brapi/v1/studytypes] 




### Get Studytypes  [GET /brapi/v1/studytypes{?studyTypeDbId}{?page}{?pageSize}]

Call to retrieve the list of study types.

 

+ Parameters
    + studyTypeDbId (Optional, ) ... Filter based on study type unique identifier
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
            "totalCount": 3,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "description": "Description for Nursery study type",
                "name": "Crossing Nursery",
                "studyTypeDbId": null,
                "studyTypeName": null
            },
            {
                "description": "Description for yield study type",
                "name": "Yield study",
                "studyTypeDbId": null,
                "studyTypeName": null
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





### **Deprecated** Get StudyTypes  [GET /brapi/v1/studyTypes{?page}{?pageSize}]

 ** DEPRECTED ** Use /studytypes
Call to retrieve the list of study types.
Scope: PHENOTYPING. Implementation target date: PAG2016 

 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 3,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "description": "Description for Nursery study type",
                "name": "Crossing Nursery",
                "studyTypeDbId": null,
                "studyTypeName": null
            },
            {
                "description": "Description for yield study type",
                "name": "Yield study",
                "studyTypeDbId": null,
                "studyTypeName": null
            }
        ]
    }
}
```

