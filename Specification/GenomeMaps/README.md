
# Group Genome Maps

Retrieving genetic or physical maps
- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome




## Maps [/brapi/v1/maps] 




### Get Maps  [GET /brapi/v1/maps{?species}{?commonCropName}{?scientificName}{?type}{?page}{?pageSize}]

Get list of maps

 

+ Parameters
    + species (Optional, ) ... DEPRECATED in v1.3 - See "scientificName"
    + commonCropName (Optional, ) ... The common name of the crop, found from "GET /commoncropnames"
    + scientificName (Optional, ) ... Full scientific binomial format name. This includes Genus, Species, and Sub-species
    + type (Optional, ) ... Type of map
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
            "totalCount": 1,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "comments": "comments",
                "commonCropName": null,
                "documentationURL": null,
                "linkageGroupCount": 3,
                "mapDbId": "gm1",
                "mapName": null,
                "markerCount": 22,
                "name": "Genome Map 1",
                "publishedDate": "2018-01-01",
                "scientificName": null,
                "species": "novus",
                "type": "Genetic",
                "unit": "cM"
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





### Get Maps by mapDbId  [GET /brapi/v1/maps/{mapDbId}{?page}{?pageSize}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup

 

+ Parameters
    + mapDbId (Required, ) ... The internal db id of a selected map
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
                "linkageGroupName": "1",
                "markerCount": 11,
                "maxPosition": 1110
            },
            {
                "linkageGroupName": "2",
                "markerCount": 5,
                "maxPosition": 5050
            }
        ],
        "documentationURL": null,
        "linkageGroups": [
            {
                "linkageGroupName": "1",
                "markerCount": 11,
                "maxPosition": 1110
            },
            {
                "linkageGroupName": "2",
                "markerCount": 5,
                "maxPosition": 5050
            }
        ],
        "mapDbId": "gm1",
        "mapName": null,
        "name": "Genome Map 1",
        "type": "Genetic",
        "unit": "cM"
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





### Get Maps Positions by mapDbId  [GET /brapi/v1/maps/{mapDbId}/positions{?linkageGroupId}{?linkageGroupName}{?page}{?pageSize}]

All the markers in a given Map, ordered by linkageGroup and position.

 

+ Parameters
    + mapDbId (Required, ) ... unique id of the map
    + linkageGroupId (Optional, ) ... Deprecated Use linkageGroupName instead
    + linkageGroupName (Optional, ) ... The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
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
            "totalCount": 22,
            "totalPages": 11
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "linkageGroupName": "1",
                "location": "1000",
                "markerDbId": "mr01",
                "markerName": "marker1-1"
            },
            {
                "linkageGroupName": "1",
                "location": "1020",
                "markerDbId": "mr02",
                "markerName": "marker1-2"
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





### Get Maps Positions by mapDbId and linkageGroupName  [GET /brapi/v1/maps/{mapDbId}/positions/{linkageGroupName}{?min}{?max}{?page}{?pageSize}]

All the markers in a specific Linkage Group (aka Chromasome) inside a particular Map, ordered by position.

 

+ Parameters
    + mapDbId (Required, ) ... unique id of the map
    + linkageGroupName (Required, ) ... The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    + min (Optional, ) ... minimum position on linkage group
    + max (Optional, ) ... maximum position on linkage group
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
            "totalCount": 22,
            "totalPages": 11
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "location": "1000",
                "markerDbId": "mr01",
                "markerName": "marker1-1"
            },
            {
                "location": "1020",
                "markerDbId": "mr02",
                "markerName": "marker1-2"
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

