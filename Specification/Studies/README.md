
# Group Study

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).

Note that dates should be provided in extended ISO 8601 format (for example, "YYYY-MM-DD").




## Observationlevels [/brapi/v1/observationlevels] 




### Get Observationlevels  [GET /brapi/v1/observationlevels{?page}{?pageSize}]

Call to retrieve the list of supported observation levels. 
Observation levels indicate the granularity level at which the measurements are taken. 
The values are used to supply the `observationLevel` parameter in the observation unit details call.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[string]||


 

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
            "plot",
            "plant"
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[string]||


 

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
            "plot",
            "plant"
        ]
    }
}
```



## Search [/brapi/v1/search] 




### Post Search Studies  [POST /brapi/v1/search/studies]

Get list of studies
StartDate and endDate should be ISO8601 format for dates
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|commonCropNames|array[string]|Common names for the crop associated with this study|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm|
|locationDbIds|array[string]|List of location names to filter search results|
|observationVariableDbIds|array[string]|List of observation variable IDs to search for|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|List of program identifiers to filter search results|
|programNames|array[string]|List of program names to filter search results|
|seasonDbIds|array[string]|The ID which uniquely identifies a season|
|sortBy|string|Name of one of the fields within the study object on which results can be sorted|
|sortOrder|string|Order results should be sorted. ex. "ASC" or "DESC"|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|studyTypeDbIds|array[string]|The unique identifier of the type of study being performed.|
|studyTypeNames|array[string]|The name of the type of study being performed. ex. "Yield Trial", etc|
|trialDbIds|array[string]|List of trial identifiers to filter search results|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|string|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date the study ends|
|locationDbId|string|The ID which uniquely identifies a location|
|locationName|string|The human readable name for a location|
|name|string|DEPRECATED in v1.3 - Use "studyName"|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|programName|string|The humane readable name of a program|
|seasons|array[object]|List of seasons over which this study was performed.|
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|startDate|string (date)|The date this study started|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The humane readable name of a study|
|studyType|string|DEPRECATED in v1.3 - See "studyTypeName"|
|studyTypeDbId|string|The unique identifier of the type of study being performed.|
|studyTypeName|string|The name of the type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
            "totalCount": 2,
            "totalPages": 1
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
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
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
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    {
                        "season": "winter",
                        "seasonDbId": "2",
                        "year": "2012"
                    }
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|string|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date the study ends|
|locationDbId|string|The ID which uniquely identifies a location|
|locationName|string|The human readable name for a location|
|name|string|DEPRECATED in v1.3 - Use "studyName"|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|programName|string|The humane readable name of a program|
|seasons|array[object]|List of seasons over which this study was performed.|
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|startDate|string (date)|The date this study started|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The humane readable name of a study|
|studyType|string|DEPRECATED in v1.3 - See "studyTypeName"|
|studyTypeDbId|string|The unique identifier of the type of study being performed.|
|studyTypeName|string|The name of the type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
            "totalCount": 2,
            "totalPages": 1
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
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
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
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    {
                        "season": "winter",
                        "seasonDbId": "2",
                        "year": "2012"
                    }
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            }
        ]
    }
}
```





### **Deprecated** Post Studies-search  [POST /brapi/v1/studies-search]

DEPRECATED in v1.3 - see /search/studies

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm|
|locationDbIds|array[string]|List of location identifiers to filter search results|
|observationVariableDbIds|array[string]|List of observation variable IDs to search for|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|List of program identifiers to filter search results|
|programNames|array[string]|List of program names to filter search results|
|seasonDbId|array[string]|The ID which uniquely identifies a season|
|sortBy|string|Name of one of the fields within the study object on which results can be sorted|
|sortOrder|string|Order results should be sorted. ex. "ASC" or "DESC"|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyLocations|array[string]|List of location names to filter search results|
|studyNames|array[string]|List of study names to filter search results|
|studyType|string|The type of study being performed. ex. "Yeald Trial", etc|
|trialDbIds|array[string]|List of trial identifiers to filter search results|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|string|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date the study ends|
|locationDbId|string|The ID which uniquely identifies a location|
|locationName|string|The human readable name for a location|
|name|string|DEPRECATED in v1.3 - Use "studyName"|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|programName|string|The humane readable name of a program|
|seasons|array[object]|List of seasons over which this study was performed.|
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|startDate|string (date)|The date this study started|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The humane readable name of a study|
|studyType|string|DEPRECATED in v1.3 - See "studyTypeName"|
|studyTypeDbId|string|The unique identifier of the type of study being performed.|
|studyTypeName|string|The name of the type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
            "totalCount": 2,
            "totalPages": 1
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
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
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
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    {
                        "season": "winter",
                        "seasonDbId": "2",
                        "year": "2012"
                    }
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|string|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date the study ends|
|locationDbId|string|The ID which uniquely identifies a location|
|locationName|string|The human readable name for a location|
|name|string|DEPRECATED in v1.3 - Use "studyName"|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|programName|string|The humane readable name of a program|
|seasons|array[object]|List of seasons over which this study was performed.|
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|startDate|string (date)|The date this study started|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The humane readable name of a study|
|studyType|string|DEPRECATED in v1.3 - See "studyTypeName"|
|studyTypeDbId|string|The unique identifier of the type of study being performed.|
|studyTypeName|string|The name of the type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
            "totalCount": 2,
            "totalPages": 1
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
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2014-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 1",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
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
                ],
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
                "trialDbId": "101",
                "trialName": "Peru Yield Trial 1"
            },
            {
                "active": "true",
                "additionalInfo": {
                    "publications": "pmid:23643517318968"
                },
                "commonCropName": "Tomatillo",
                "documentationURL": "https://brapi.org",
                "endDate": "2015-01-01",
                "locationDbId": "1",
                "locationName": "Location 1",
                "name": "Study 2",
                "programDbId": "1",
                "programName": "Program 1",
                "seasons": [
                    {
                        "season": "winter",
                        "seasonDbId": "2",
                        "year": "2012"
                    }
                ],
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "studyType": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study",
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|active|string|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact|
|email|string|The contacts email address |
|instituteName|string|The name of the institution which this contact is part of|
|name|string|The full name of this contact person|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataLinkName|string|The name of the external data link|
|name|string|DEPRECATED in v1.3 - Use "dataLinkName"|
|type|string|The type of external data link|
|url|string|The URL which links to external data|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date the study ends|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|location|object||
|abbreviation|string|An abbreviation which represents this location|
|abreviation|string|Deprecated  Use abbreviation |
|additionalInfo|object|Additional arbitrary info|
|altitude|number|The altitude of this location|
|countryCode|string|[ISO_3166-1_alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) spec|
|countryName|string|The full name of the country where this location is|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|instituteAddress|string|The street address of the institute representing this location|
|instituteAdress|string|Deprecated  Use instituteAddress |
|instituteName|string|each institute/laboratory can have several experimental field|
|latitude|number|The latitude of this location|
|locationDbId|string|string identifier|
|locationName|string|A human readable name for this location|
|locationType|string|The type of location this represents (ex. Breeding Location, Storage Location, etc)|
|longitude|number|the longitude of this location|
|name|string|DEPRECATED in v1.3 - Use "locationName"|
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date)|The date this study started|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyDescription|string|The description of this study|
|studyName|string|The human readable name for a study|
|studyType|string|DEPRECATED in v1.3 - See "studyTypeName"|
|studyTypeDbId|string|The unique identifier of the type of study being performed.|
|studyTypeName|string|The name of the type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
        "commonCropName": "Tomatillo",
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
                "dataLinkName": "image-archive12.zip",
                "name": "image-archive12.zip",
                "type": "Image archive",
                "url": "http://data.inra.fr/archive/multi-spect-flowering.zip"
            },
            {
                "dataLinkName": "image-archive13.zip",
                "name": "image-archive13.zip",
                "type": "Image archive",
                "url": "http://data.inra.fr/archive/biomass-img.zip"
            }
        ],
        "documentationURL": "https://brapi.org",
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
            "documentationURL": "https://brapi.org",
            "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
            "instituteAdress": "71 Pilgrim Avenue Chevy Chase MD 20815",
            "instituteName": "Plant Science Institute",
            "latitude": -11.1274995803833,
            "locationDbId": "1",
            "locationName": "Location 1",
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
        "studyTypeDbId": "2",
        "studyTypeName": "Yield study",
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|List of germplasm associated with a given trial and study|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|acquisitionDate|string (date)|The date this germplasm was aquired by the genebank (MCPD)|
|biologicalStatusOfAccessionCode|integer|The 3 digit code representing the biological status of the accession (MCPD)|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|commonCropName|string|Common name for the crop (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes (MCPD)|
|donorAccessionNumber|string||
|donorInstituteCode|string||
|germplasmPUI|string||
|entryNumber|string|** Deprecated ** use /studies/{studyDbId/layout for positional germplasm relationships|
|genus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|pedigree|string|The cross name and optional selection history.|
|seedSource|string|The source of the seed |
|species|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|studyDbId|string|** Deprecated ** The request contains the studyDbId The ID which uniquely identifies a study within the given database server|
|trialName|string|** Deprecated ** trialName not relevent  The human readable name of a trial|


 

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
                "acquisitionDate": "1984-01-01",
                "biologicalStatusOfAccessionCode": 300,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000001",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000001",
                "documentationURL": "https://brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A001230",
                        "donorInstituteCode": "INRA",
                        "germplasmPUI": "https://doi.org/10.1109/5.771073"
                    },
                    {
                        "donorAccessionNumber": "A004560",
                        "donorInstituteCode": "INRA",
                        "germplasmPUI": "https://doi.org/10.1109/5.231123"
                    }
                ],
                "entryNumber": "2",
                "genus": "Fructus",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "germplasmPUI": "http://pui.per/accession/A000001",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001",
                "seedSource": "open pollination",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "landrace 1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            },
            {
                "accessionNumber": "A000001",
                "acquisitionDate": "1984-01-01",
                "biologicalStatusOfAccessionCode": 300,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000001",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000001",
                "documentationURL": "https://brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A001230",
                        "donorInstituteCode": "INRA",
                        "germplasmPUI": "https://doi.org/10.1109/5.771073"
                    },
                    {
                        "donorAccessionNumber": "A004560",
                        "donorInstituteCode": "INRA",
                        "germplasmPUI": "https://doi.org/10.1109/5.231123"
                    }
                ],
                "entryNumber": "2",
                "genus": "Fructus",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "germplasmPUI": "http://pui.per/accession/A000001",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001",
                "seedSource": "open pollination",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "landrace 1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|additionalInfo|object|Additional arbitrary info|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|


 

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

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|layout|array[object]|List of observation unit position data entities which need to be updated|
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|integer||
|entryType|string||
|observationUnitDbId|string||
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|replicate|integer||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|additionalInfo|object|Additional arbitrary info|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|


 

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
                "X": "1",
                "Y": "1",
                "additionalInfo": {},
                "blockNumber": "0",
                "entryType": "CHECK",
                "germplasmDbId": "2",
                "germplasmName": "Name002",
                "observationLevel": "plot",
                "observationUnitDbId": "11",
                "observationUnitName": "Plot 6",
                "replicate": "0",
                "studyDbId": "1003"
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|observationUnitDbIds|array[string]|List of observation unit references which have been created or updated|


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array||
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|crop|string|Crop name (examples: "Maize", "Wheat")|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO code for the language of submission of the variable.|
|method|object|Method metadata|
|class|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.|
|description|string|Method description.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|name|string|DEPRECATED in v1.3 - Use "methodName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|ontologyDbId|string|DEPRECATED in v1.3 - see "this.ontologyReference.ontologyDbId"|
|ontologyName|string|DEPRECATED in v1.3 - see "this.ontologyReference.ontologyName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object|Scale metadata|
|dataType|string|Class of the scale, entries can be     "Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal             scale that combines the expressions of the different traits composing the complex             trait. For exemple a severity trait might be expressed by a 2 digit and 2 character             code. The first 2 digits are the percentage of the plant covered by a fungus and the 2             characters refer to the delay in development, e.g. "75VD" means "75%" of the plant is              Crop Ontology & Integrated Breeding Platform  Curation Guidelines  5/6/2016 9             infected and the plant is very delayed.      "Date" - The date class is for events expressed in a time format, e.g. yyyymmddThh:mm:ssZ or dd/mm/yy      "Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months      "Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories      "Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectar, branches      "Ordinal" - Ordinal scales are scales composed of ordered categories      "Text" - A free text is used to express the trait.   |
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|name|string|DEPRECATED in v1.3 - Use "scaleName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale|
|validValues|object||
|categories|array[string]|List of possible values and their meaning (examples: ["0=low", "1=medium", "2=high"]|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|class|string|Trait class. (examples: "morphological trait", "phenological trait", "agronomical trait", "physiological trait", "abiotic stress trait", "biotic stress trait", "biochemical trait", "quality traits trait", "fertility trait", etc.)|
|description|string|The description of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|name|string|DEPRECATED in v1.3 - Use "traitName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitName|string|The human readable name of a trait|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|date|string|DEPRECATED in v1.3 - see "submissionTimestamp"|
|name|string|DEPRECATED in v1.3 - Use "observationVariableName"|
|observationVariableDbId|string|Variable unique identifier|
|observationVariableName|string|Variable name (usually a short name)|
|studyDbId|string||
|trialName|string||


 

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
            "totalCount": 5,
            "totalPages": 3
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "string",
                    "description": "string",
                    "formula": "string",
                    "methodDbId": "m1",
                    "methodName": "string",
                    "name": "string",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "string",
                                "type": "OBO",
                                "url": "string"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "string"
                },
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Code",
                    "decimalPlaces": 0,
                    "name": "string",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "string",
                                "type": "OBO",
                                "url": "string"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s1",
                    "scaleName": "string",
                    "validValues": {
                        "categories": [
                            "string"
                        ],
                        "max": 0,
                        "min": 0
                    },
                    "xref": "string"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [
                        "string"
                    ],
                    "attribute": "string",
                    "class": "string",
                    "description": "string",
                    "entity": "string",
                    "mainAbbreviation": "string",
                    "name": "string",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "string",
                                "type": "OBO",
                                "url": "string"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "string",
                    "synonyms": [
                        "string"
                    ],
                    "traitDbId": "t1",
                    "traitName": "string",
                    "xref": "string"
                },
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": "Standard Color Palette",
                    "name": "Standard Color Palette",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/m3",
                                "type": "OBO",
                                "url": "https://ontology.org/m3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "google.com"
                },
                "name": "Carotenoid",
                "observationVariableDbId": "MO_123:100003",
                "observationVariableName": "Carotenoid",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Nominal",
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/s3",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org/s3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s3",
                    "scaleName": "Color",
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/t3",
                                "type": "RDF",
                                "url": "https://ontology.org/t3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t3",
                    "traitName": "Leaf Color",
                    "xref": "xref"
                },
                "xref": "MO_123:100003"
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|operator|string|The name or identifier of the entity which collected the observation|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

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
            "totalCount": 9,
            "totalPages": 5
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationDbId": "1",
                "observationLevel": "plot",
                "observationTimeStamp": "2013-06-14T22:03:51-04:00",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "operator": "Bob",
                "season": {
                    "season": "fall",
                    "seasonDbId": "1",
                    "year": "2011"
                },
                "studyDbId": "1001",
                "uploadedBy": "Bob",
                "value": "1.2"
            },
            {
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationDbId": "2",
                "observationLevel": "plot",
                "observationTimeStamp": "2013-06-14T22:04:51-04:00",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "MO_123:100006",
                "observationVariableName": "Virus severity",
                "operator": "Bob",
                "season": {
                    "season": "fall",
                    "seasonDbId": "1",
                    "year": "2011"
                },
                "studyDbId": "1001",
                "uploadedBy": "Bob",
                "value": "4.5"
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

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|observations|array[object]|List of observation references to be created or updated|
|collector|string||
|observationDbId|string||
|observationTimeStamp|string (date-time)||
|observationUnitDbId|string||
|observationVariableDbId|string||
|value|string||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|observations|array[object]|List of observation references which have been created or updated|
|observationDbId|string||
|observationUnitDbId|string||
|observationVariableDbId|string||


 

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
    "result": {
        "observations": [
            {
                "observationDbId": "19",
                "observationUnitDbId": "11",
                "observationVariableDbId": "MO_123:100002"
            },
            {
                "observationDbId": "20",
                "observationUnitDbId": "11",
                "observationVariableDbId": "MO_123:100003"
            },
            {
                "observationDbId": "21",
                "observationUnitDbId": "11",
                "observationVariableDbId": "MO_123:100005"
            },
            {
                "observationDbId": "22",
                "observationUnitDbId": "11",
                "observationVariableDbId": "MO_123:100004"
            },
            {
                "observationDbId": "1f55443e-c7e1-4b71-bc9c-02ddbca9ab7d",
                "observationUnitDbId": "11",
                "observationVariableDbId": "MO_123:100002"
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





### Get Studies Observationunits by studyDbId  [GET /brapi/v1/studies/{studyDbId}/observationunits{?observationLevel}{?page}{?pageSize}]

The main API call for field data collection, to retrieve all the observation units within a study.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationLevels|string|Concatenation of the levels of this observationUnit. Used to handle non canonical level structures. Format levelType:levelID,levelType:levelID|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|observations|array[object]|List of observations associated with this observation unit|
|collector|string|The name or identifier of the entity which collected the observation|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|value|string|The value of the data collected as an observation|
|pedigree|string|The string representation of the pedigree of this observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyLocation|string|DEPRECATED in v1.3 - see "locationName"|
|studyLocationDbId|string|DEPRECATED in v1.3 - see "locationDbId"|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
                "entryNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239865",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "1",
                        "observationTimeStamp": "2013-06-14T22:03:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "1.2"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "2",
                        "observationTimeStamp": "2013-06-14T22:04:51-04:00",
                        "observationVariableDbId": "MO_123:100006",
                        "observationVariableName": "Virus severity",
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "4.5"
                    },
                    {
                        "collector": "string",
                        "observationDbId": "bb989815-86bf-430b-9d87-054df8919767",
                        "observationTimeStamp": "1970-01-18T14:02:52-05:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "string"
                    }
                ],
                "pedigree": "A000001/A000002",
                "plantNumber": "0",
                "plotNumber": "1",
                "replicate": "0"
            },
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
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "1.1"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "4",
                        "observationTimeStamp": "2013-06-14T22:06:51-04:00",
                        "observationVariableDbId": "MO_123:100006",
                        "observationVariableName": "Virus severity",
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "5.1"
                    }
                ],
                "pedigree": "A000001/A000002",
                "plantNumber": "1",
                "plotNumber": "1",
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

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|observations|array[object]|List of observations associated with this observation unit|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|operator|string|The name or identifier of the entity which collected the observation|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|observationUnitDbIds|array[string]|List of observation unit references which have been created or updated|


 

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
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "observationUnitDbIds": [
            "11"
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation data recorded for different observation variables across different observation units|
|headerRow|array[string]|The header row describing observation unit fields. Append 'observationVariableDbIds' for complete header row of the table. This array should contain any or all of the following strings; year, studyDbId, studyName, locationDbId, locationName, germplasmDbId, germplasmName, observationUnitDbId, plotNumber, replicate, blockNumber, observationTimestamp (DEPRECATED in V1.3), entryType, X, Y|
|observationVariableDbIds|array[string]|The list of observation variables which have values recorded for them in the data matrix. Append to the 'headerRow' for comlete header row.|
|observationVariableNames|array[string]|The list of observation variable names which have values recorded for them in the data matrix. Order should match 'observationVariableDbIds'.|


 

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

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation data recorded for different observation variables across different observation units|
|headerRow|array[string]|The header row describing the data matrix. Append 'observationVariableDbIds' for complete header row.|
|metadata||DEPRECATED|
|observationVariableDbIds|array[string]|The list of observation variables which have values recorded for them in the data matrix. Append to the 'headerRow' for comlete header row.|
|result|object|DEPRECATED|
|data|array[array]||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|observations|array[object]|List of observation references which have been created or updated|
|observationDbId|string||
|observationUnitDbId|string||
|observationVariableDbId|string||


 

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
            "pageSize": 1,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "observations": [
            {
                "observationDbId": "f439cdc6-768f-4d11-b66c-489d980b3d3b",
                "observationUnitDbId": "ee89a58d-b104-437b-9cb4-7b500eaafa11",
                "observationVariableDbId": "MO_123:100002"
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





### **Deprecated** Get Studies Layout by studyDbId  [GET /brapi/v1/studies/{studyDbId}/layout{?page}{?pageSize}]

DEPRECATED in v1.3 - see `GET /studies/{studyDbId}/layouts` (pluralized)



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|additionalInfo|object|Additional arbitrary info|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|


 

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





### **Deprecated** Put Studies Layout by studyDbId  [PUT /brapi/v1/studies/{studyDbId}/layout]

DEPRECATED in v1.3 - see `PUT /studies/{studyDbId}/layouts` (pluralized)

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|layout|array[object]|List of observation unit position data entities which need to be updated|
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|integer||
|entryType|string||
|observationUnitDbId|string||
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|replicate|integer||


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|additionalInfo|object|Additional arbitrary info|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|


 

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
                "X": "1",
                "Y": "1",
                "additionalInfo": {},
                "blockNumber": "0",
                "entryType": "CHECK",
                "germplasmDbId": "2",
                "germplasmName": "Name002",
                "observationLevel": "plot",
                "observationUnitDbId": "11",
                "observationUnitName": "Plot 6",
                "replicate": "0",
                "studyDbId": "1003"
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array||
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|crop|string|Crop name (examples: "Maize", "Wheat")|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO code for the language of submission of the variable.|
|method|object|Method metadata|
|class|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.|
|description|string|Method description.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|name|string|DEPRECATED in v1.3 - Use "methodName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|ontologyDbId|string|DEPRECATED in v1.3 - see "this.ontologyReference.ontologyDbId"|
|ontologyName|string|DEPRECATED in v1.3 - see "this.ontologyReference.ontologyName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object|Scale metadata|
|dataType|string|Class of the scale, entries can be     "Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal             scale that combines the expressions of the different traits composing the complex             trait. For exemple a severity trait might be expressed by a 2 digit and 2 character             code. The first 2 digits are the percentage of the plant covered by a fungus and the 2             characters refer to the delay in development, e.g. "75VD" means "75%" of the plant is              Crop Ontology & Integrated Breeding Platform  Curation Guidelines  5/6/2016 9             infected and the plant is very delayed.      "Date" - The date class is for events expressed in a time format, e.g. yyyymmddThh:mm:ssZ or dd/mm/yy      "Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months      "Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories      "Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectar, branches      "Ordinal" - Ordinal scales are scales composed of ordered categories      "Text" - A free text is used to express the trait.   |
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|name|string|DEPRECATED in v1.3 - Use "scaleName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale|
|validValues|object||
|categories|array[string]|List of possible values and their meaning (examples: ["0=low", "1=medium", "2=high"]|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|class|string|Trait class. (examples: "morphological trait", "phenological trait", "agronomical trait", "physiological trait", "abiotic stress trait", "biotic stress trait", "biochemical trait", "quality traits trait", "fertility trait", etc.)|
|description|string|The description of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|name|string|DEPRECATED in v1.3 - Use "traitName"|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitName|string|The human readable name of a trait|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|date|string|DEPRECATED in v1.3 - see "submissionTimestamp"|
|name|string|DEPRECATED in v1.3 - Use "observationVariableName"|
|observationVariableDbId|string|Variable unique identifier|
|observationVariableName|string|Variable name (usually a short name)|
|studyDbId|string||
|trialName|string||


 

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
            "totalCount": 5,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "string",
                    "description": "string",
                    "formula": "string",
                    "methodDbId": "m1",
                    "methodName": "string",
                    "name": "string",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "string",
                                "type": "OBO",
                                "url": "string"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "string"
                },
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Code",
                    "decimalPlaces": 0,
                    "name": "string",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "string",
                                "type": "OBO",
                                "url": "string"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s1",
                    "scaleName": "string",
                    "validValues": {
                        "categories": [
                            "string"
                        ],
                        "max": 0,
                        "min": 0
                    },
                    "xref": "string"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [
                        "string"
                    ],
                    "attribute": "string",
                    "class": "string",
                    "description": "string",
                    "entity": "string",
                    "mainAbbreviation": "string",
                    "name": "string",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "string",
                                "type": "OBO",
                                "url": "string"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "string",
                    "synonyms": [
                        "string"
                    ],
                    "traitDbId": "t1",
                    "traitName": "string",
                    "xref": "string"
                },
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": "Standard Color Palette",
                    "name": "Standard Color Palette",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/m3",
                                "type": "OBO",
                                "url": "https://ontology.org/m3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "google.com"
                },
                "name": "Carotenoid",
                "observationVariableDbId": "MO_123:100003",
                "observationVariableName": "Carotenoid",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Nominal",
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/s3",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org/s3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s3",
                    "scaleName": "Color",
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/t3",
                                "type": "RDF",
                                "url": "https://ontology.org/t3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t3",
                    "traitName": "Leaf Color",
                    "xref": "xref"
                },
                "xref": "MO_123:100003"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Dried sample on electric scale",
                    "formula": "NA",
                    "methodDbId": "m2",
                    "methodName": "Dry Electric Scale",
                    "name": "Dry Electric Scale",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/m2",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org/m2"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "google.com"
                },
                "name": "Root weight",
                "observationVariableDbId": "MO_123:100004",
                "observationVariableName": "Root weight",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 3,
                    "name": "Kilogram",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/s2",
                                "type": "RDF",
                                "url": "https://ontology.org/s2"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s2",
                    "scaleName": "Kilogram",
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
                    "attribute": "root weight",
                    "class": "Numeric",
                    "description": "root weight",
                    "entity": "entity",
                    "mainAbbreviation": "RW",
                    "name": "Root Weight",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/t2",
                                "type": "OBO",
                                "url": "https://ontology.org/t2"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t2",
                    "traitName": "Root Weight",
                    "xref": "xref"
                },
                "xref": "MO_123:100004"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": "Standard Color Palette",
                    "name": "Standard Color Palette",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/m3",
                                "type": "OBO",
                                "url": "https://ontology.org/m3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "google.com"
                },
                "name": "Root color",
                "observationVariableDbId": "MO_123:100005",
                "observationVariableName": "Root color",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Nominal",
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/s3",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org/s3"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s3",
                    "scaleName": "Color",
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/t4",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org/t4"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t4",
                    "traitName": "Root Color",
                    "xref": "xref"
                },
                "xref": "MO_123:100005"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Percentage",
                    "description": "Image analysis of sample photo",
                    "formula": "Bobs Color Threshold Tool",
                    "methodDbId": "m4",
                    "methodName": "Image analysis",
                    "name": "Image analysis",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/m4",
                                "type": "RDF",
                                "url": "https://ontology.org/m4"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "https://bobsimageanalysis.com"
                },
                "name": "Virus severity",
                "observationVariableDbId": "MO_123:100006",
                "observationVariableName": "Virus severity",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 0,
                    "name": "Percentage",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/s4",
                                "type": "OBO",
                                "url": "https://ontology.org/s4"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s4",
                    "scaleName": "Percentage",
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/t5",
                                "type": "OBO",
                                "url": "https://ontology.org/t5"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t5",
                    "traitName": "Virus severity",
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

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|metadata|object||
|datafiles|array[string]|The datafiles key contains a list of file paths, which can be relative or complete URLs. These files contain additional information related to the returned object and can be retrieved by a subsequent call. The empty list should be returned if no additional data files are present.|
|pagination|object|The pagination object is applicable only when the payload contains a "data" key. It describes the pagination of the data contained in the "data" array, as a way to identify which subset of data is being returned. Pages are zero indexed, so the first page will be page 0 (zero).|
|currentPage|integer||
|pageSize|integer||
|totalCount|integer||
|totalPages|integer||
|status|array[object]|The status field contains a list of informational status messages from the server. If no status is reported, an empty list should be returned. See Error Reporting for more information.|
|code|string|DEPRECATED in v1.3 - see Error Handling best practice documentation|
|message|string|A short message concerning the status of this request/response|
|messageType|string|The logging level for the attached message|
|result|object||
|commit|string|Should these changes be commited|
|data|array[object]|Required array of marker-name/score pairs|
|observationUnitDbId|string||
|observations|array[object]||
|collector|string||
|observationDbId|string||
|observationTimeStamp|string (date-time)||
|observationUnitDbId|string||
|observationVariableDbId|string||
|value|string||
|studyDbId|number||
|transactionDbId|string|The ID representing this transaction|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|observationUnitDbIds|array[string]|List of observation unit references which have been created or updated|


 

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
                "observationUnitDbId": "observationUnitDbId0",
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
            "pageSize": 1,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "observationUnitDbIds": [
            "1"
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|description|string|The description of this study type|
|name|string|DEPRECATED in v1.3 - Use "studyTypeName"|
|studyTypeDbId|string|The unique identifier of a study type|
|studyTypeName|string|The human readable name of a study type|


 

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
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "description": "Description for Nursery study type",
                "name": "Crossing Nursery",
                "studyTypeDbId": "1",
                "studyTypeName": "Crossing Nursery"
            },
            {
                "description": "Description for yield study type",
                "name": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study"
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|description|string|The description of this study type|
|name|string|DEPRECATED in v1.3 - Use "studyTypeName"|
|studyTypeDbId|string|The unique identifier of a study type|
|studyTypeName|string|The human readable name of a study type|


 

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
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "description": "Description for Nursery study type",
                "name": "Crossing Nursery",
                "studyTypeDbId": "1",
                "studyTypeName": "Crossing Nursery"
            },
            {
                "description": "Description for yield study type",
                "name": "Yield study",
                "studyTypeDbId": "2",
                "studyTypeName": "Yield study"
            }
        ]
    }
}
```

