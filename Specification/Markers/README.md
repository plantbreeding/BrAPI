
# Group Markers

Search for and get details of specific markers stored in a database



## Markers-search [/brapi/v1/markers-search] 




### **Deprecated** Get Markers-search  [GET /brapi/v1/markers-search{?markerDbIds}{?name}{?matchMethod}{?includeSynonyms}{?type}{?page}{?pageSize}]

 Scope: CORE.  Status: ACCEPTED.
Implemented by: Germinate
See Search Services for additional implementation details.
Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria. 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|analysisMethods|array[string]|List of the genotyping platforms used to interrogate the marker|
|defaultDisplayName|string|DEPRECATED in v 1.3 - see "markerName"|
|markerDbId|string|Internal db identifier|
|markerName|string|A string representing the marker that will be meaningful to the user|
|refAlt|array[string]|List of the reference (as the first item) and alternatives (the remaining items)|
|synonyms|array[string]|List of other names for this marker|
|type|string|The type of marker, e.g. SNP|


 

+ Parameters
    + markerDbIds (Optional, ) ... The database IDs of the markers to search for
    + name (Optional, ) ... The search pattern for a marker name or synonym. Examples: "11_10002" "11_1%" "11_1*" "11_10?02"
    + matchMethod (Optional, ) ... Possible values are 'case_insensitive', 'exact'
(case sensitive), 'wildcard' (which is case insensitive). Wildcard uses both '*' and '%' for any number of characters
and '?' for one character matching. Default is exact.
    + includeSynonyms (Optional, ) ... Whether to include synonyms in the output.
    + type (Optional, ) ... The type of the marker.
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
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "analysisMethods": [
                    "illumina"
                ],
                "defaultDisplayName": "marker1-1",
                "markerDbId": "mr01",
                "markerName": "marker1-1",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10010"
                ],
                "type": "marker"
            },
            {
                "analysisMethods": [
                    "kasp"
                ],
                "defaultDisplayName": "marker1-2",
                "markerDbId": "mr02",
                "markerName": "marker1-2",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10020"
                ],
                "type": "marker"
            }
        ]
    }
}
```





### **Deprecated** Post Markers-search  [POST /brapi/v1/markers-search]

 Scope: CORE.  Status: ACCEPTED.
Implemented by: Germinate
See Search Services for additional implementation details.
Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria. 

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|includeSynonyms|boolean|Should an array of synonyms be included in the response|
|markerDbIds|array[string]|List of IDs which uniquely identify markers |
|markerNames|array[string]|The search pattern for the marker name or synonym.|
|matchMethod|string|How to perform string matching during search. 'exact' will search for exact, case sensitive matches only. 'case_insensitive' will search for exact matches, but case insensitive. 'wildcard' will allow the special characters '*' (star) and '%' (percent) to represent variable length arbitrary strings, and the special character '?' (question) to represent one arbitrary character.|
|name|string|DEPRECATED in v 1.3 - see "markerNames"|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|type|string|DEPRECATED in v 1.3 - see "types"|
|types|array[string]|The type of marker, e.g. SNP|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|analysisMethods|array[string]|List of the genotyping platforms used to interrogate the marker|
|defaultDisplayName|string|DEPRECATED in v 1.3 - see "markerName"|
|markerDbId|string|Internal db identifier|
|markerName|string|A string representing the marker that will be meaningful to the user|
|refAlt|array[string]|List of the reference (as the first item) and alternatives (the remaining items)|
|synonyms|array[string]|List of other names for this marker|
|type|string|The type of marker, e.g. SNP|


 

+ Parameters


 
+ Request (application/json)
```
{
    "markerDbIds": [
        "markerDbIds0",
        "markerDbIds1"
    ],
    "markerNames": [
        "markerNames0",
        "markerNames1"
    ],
    "matchMethod": "exact",
    "name": "name0",
    "page": 0,
    "pageSize": 0,
    "type": "type0",
    "types": [
        "types0",
        "types1"
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
                "analysisMethods": [
                    "illumina"
                ],
                "defaultDisplayName": "marker1-1",
                "markerDbId": "mr01",
                "markerName": "marker1-1",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10010"
                ],
                "type": "marker"
            },
            {
                "analysisMethods": [
                    "kasp"
                ],
                "defaultDisplayName": "marker1-2",
                "markerDbId": "mr02",
                "markerName": "marker1-2",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10020"
                ],
                "type": "marker"
            }
        ]
    }
}
```



## Markers [/brapi/v1/markers] 




### Get Markers  [GET /brapi/v1/markers{?markerDbId}{?markerName}{?name}{?matchMethod}{?includeSynonyms}{?include}{?type}{?page}{?pageSize}]

Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria.
If there is none, an empty array is returned. If there is one or more than one match, returns an array of all marker records that match the search criteria.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|analysisMethods|array[string]|List of the genotyping platforms used to interrogate the marker|
|defaultDisplayName|string|DEPRECATED in v 1.3 - see "markerName"|
|markerDbId|string|Internal db identifier|
|markerName|string|A string representing the marker that will be meaningful to the user|
|refAlt|array[string]|List of the reference (as the first item) and alternatives (the remaining items)|
|synonyms|array[string]|List of other names for this marker|
|type|string|The type of marker, e.g. SNP|


 

+ Parameters
    + markerDbId (Optional, ) ... The database ID of the markers to search for
    + markerName (Optional, ) ... The search paramater for a marker name or synonym.
    + name (Optional, ) ... DEPRECAED in v1.3 - see "markerName"
    + matchMethod (Optional, ) ... DEPRECAED in v1.3 - see /search/markers
    + includeSynonyms (Optional, ) ... Whether to include synonyms in the output.
    + include (Optional, ) ... DEPRECATED in v1.1 - see "includeSynonyms"
    + type (Optional, ) ... The type of the marker.
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
                "analysisMethods": [
                    "illumina"
                ],
                "defaultDisplayName": "marker1-1",
                "markerDbId": "mr01",
                "markerName": "marker1-1",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10010"
                ],
                "type": "marker"
            },
            {
                "analysisMethods": [
                    "kasp"
                ],
                "defaultDisplayName": "marker1-2",
                "markerDbId": "mr02",
                "markerName": "marker1-2",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10020"
                ],
                "type": "marker"
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





### Get Markers by markerDbId  [GET /brapi/v1/markers/{markerDbId}]

Status: ACCEPTED 
Implemented By:



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|analysisMethods|array[string]|List of the genotyping platforms used to interrogate the marker|
|defaultDisplayName|string|DEPRECATED in v 1.3 - see "markerName"|
|markerDbId|string|Internal db identifier|
|markerName|string|A string representing the marker that will be meaningful to the user|
|refAlt|array[string]|List of the reference (as the first item) and alternatives (the remaining items)|
|synonyms|array[string]|List of other names for this marker|
|type|string|The type of marker, e.g. SNP|


 

+ Parameters
    + markerDbId (Required, ) ... the internal id of the marker
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
        "analysisMethods": [
            "kasp"
        ],
        "defaultDisplayName": "marker1-2",
        "markerDbId": "mr02",
        "markerName": "marker1-2",
        "refAlt": [
            "A",
            "T"
        ],
        "synonyms": [
            "i_11_10020"
        ],
        "type": "marker"
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



## Search [/brapi/v1/search] 




### Post Search Markers  [POST /brapi/v1/search/markers]

See Search Services for additional implementation details.
Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. 
If there is none, an empty array is returned. If there is one or more than one match, returns an array of all marker records that match the search criteria. '

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|includeSynonyms|boolean|Should an array of synonyms be included in the response|
|markerDbIds|array[string]|List of IDs which uniquely identify markers |
|markerNames|array[string]|The search pattern for the marker name or synonym.|
|matchMethod|string|How to perform string matching during search. 'exact' will search for exact, case sensitive matches only. 'case_insensitive' will search for exact matches, but case insensitive. 'wildcard' will allow the special characters '*' (star) and '%' (percent) to represent variable length arbitrary strings, and the special character '?' (question) to represent one arbitrary character.|
|name|string|DEPRECATED in v 1.3 - see "markerNames"|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|type|string|DEPRECATED in v 1.3 - see "types"|
|types|array[string]|The type of marker, e.g. SNP|


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
    "markerDbIds": [
        "markerDbIds0",
        "markerDbIds1"
    ],
    "markerNames": [
        "markerNames0",
        "markerNames1"
    ],
    "matchMethod": "exact",
    "name": "name0",
    "page": 0,
    "pageSize": 0,
    "type": "type0",
    "types": [
        "types0",
        "types1"
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





### Get Search Markers by searchResultsDbId  [GET /brapi/v1/search/markers/{searchResultsDbId}{?page}{?pageSize}]

See Search Services for additional implementation details. Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria. '



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|analysisMethods|array[string]|List of the genotyping platforms used to interrogate the marker|
|defaultDisplayName|string|DEPRECATED in v 1.3 - see "markerName"|
|markerDbId|string|Internal db identifier|
|markerName|string|A string representing the marker that will be meaningful to the user|
|refAlt|array[string]|List of the reference (as the first item) and alternatives (the remaining items)|
|synonyms|array[string]|List of other names for this marker|
|type|string|The type of marker, e.g. SNP|


 

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
                "analysisMethods": [
                    "illumina"
                ],
                "defaultDisplayName": "marker1-1",
                "markerDbId": "mr01",
                "markerName": "marker1-1",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10010"
                ],
                "type": "marker"
            },
            {
                "analysisMethods": [
                    "kasp"
                ],
                "defaultDisplayName": "marker1-2",
                "markerDbId": "mr02",
                "markerName": "marker1-2",
                "refAlt": [
                    "A",
                    "T"
                ],
                "synonyms": [
                    "i_11_10020"
                ],
                "type": "marker"
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

