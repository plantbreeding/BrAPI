
# Group Markers

Search for and get details of specific markers stored in a database



## Markers-search [Get /brapi/v1/markers-search{?markerDbIds}{?name}{?matchMethod}{?includeSynonyms}{?type}{?pageSize}{?page}]

 Scope: CORE.  Status: ACCEPTED.
Implemented by: Germinate
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria.  

+ Parameters
    + markerDbIds (Optional, array) ... The database IDs of the markers to search for
    + name (Optional, string) ... The search pattern for a marker name or synonym. Examples: "11_10002" "11_1%" "11_1*" "11_10?02"
    + matchMethod (Optional, string) ... Possible values are 'case_insensitive', 'exact'
(case sensitive), 'wildcard' (which is case insensitive). Wildcard uses both '*' and '%' for any number of characters
and '?' for one character matching. Default is exact.
    + includeSynonyms (Optional, boolean) ... Whether to include synonyms in the output.
    + type (Optional, string) ... The type of the marker.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "synonyms": [
                    "i_11_10002",
                    "POPA1_0002"
                ],
                "markerDbId": "1185",
                "refAlt": [
                    "A",
                    "T"
                ],
                "type": "SNP",
                "analysisMethods": [
                    "illumina",
                    "kasp"
                ],
                "defaultDisplayName": "11_10002"
            },
            {
                "synonyms": [
                    "i_11_11159",
                    "POPA1_1159"
                ],
                "markerDbId": "1186",
                "refAlt": [
                    "A",
                    "T"
                ],
                "type": "SNP",
                "analysisMethods": [
                    "illumina",
                    "kasp"
                ],
                "defaultDisplayName": "11_11159"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
    }
}
```

## Markers-search [Post /brapi/v1/markers-search]

 Scope: CORE.  Status: ACCEPTED.
Implemented by: Germinate
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria.  

+ Parameters
 
+ Request (application/json)
/definitions/markersSearchRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "synonyms": [
                    "i_11_10002",
                    "POPA1_0002"
                ],
                "markerDbId": "1185",
                "refAlt": [
                    "A",
                    "T"
                ],
                "type": "SNP",
                "analysisMethods": [
                    "illumina",
                    "kasp"
                ],
                "defaultDisplayName": "11_10002"
            },
            {
                "synonyms": [
                    "i_11_11159",
                    "POPA1_1159"
                ],
                "markerDbId": "1186",
                "refAlt": [
                    "A",
                    "T"
                ],
                "type": "SNP",
                "analysisMethods": [
                    "illumina",
                    "kasp"
                ],
                "defaultDisplayName": "11_11159"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
    }
}
```

## Markers [Get /brapi/v1/markers{?name}{?matchMethod}{?include}{?type}{?pageSize}{?page}]

 Scope: CORE.  Status: ACCEPTED.
Implemented by: Germinate
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Other service requests use the servers internal `markerDbId`. This service returns marker records that provide the markerDbId. For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria. - If there is none, an empty array is returned. - If there is one or more than one match, returns an array of all marker records that match the search criteria.  

+ Parameters
    + name (Optional, string) ... The name or synonym.
    + matchMethod (Optional, string) ... Possible values are 'case_insensitive', 'exact'
(case sensitive), 'wildcard' (which is case insensitive). Wildcard uses both '*' and '%' for any number of characters
and '?' for one character matching. Default is exact.
    + include (Optional, string) ... Whether to include synonyms in the output.
    + type (Optional, string) ... The type of the marker.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "data": [
            {
                "synonyms": [
                    "i_11_10002",
                    "POPA1_0002"
                ],
                "markerDbId": "1185",
                "refAlt": [
                    "A",
                    "T"
                ],
                "type": "SNP",
                "analysisMethods": [
                    "illumina",
                    "kasp"
                ],
                "defaultDisplayName": "11_10002"
            },
            {
                "synonyms": [
                    "i_11_11159",
                    "POPA1_1159"
                ],
                "markerDbId": "1186",
                "refAlt": [
                    "A",
                    "T"
                ],
                "type": "SNP",
                "analysisMethods": [
                    "illumina",
                    "kasp"
                ],
                "defaultDisplayName": "11_11159"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
    }
}
```

## Markers/{markerdbid} [Get /brapi/v1/markers/{markerDbId}]

<strong>Status</strong>: ACCEPTED 
<strong>Implemented By</strong>: 

+ Parameters
    + markerDbId (Required, string) ... the internal id of the marker


+ Response 200 (application/json)
```
{
    "result": {
        "synonyms": [
            "i_11_10002",
            "POPA1_0002"
        ],
        "markerDbId": "1185",
        "refAlt": [
            "A",
            "T"
        ],
        "type": "SNP",
        "analysisMethods": [
            "illumina",
            "kasp"
        ],
        "defaultDisplayName": "11_10002"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": []
    }
}
```