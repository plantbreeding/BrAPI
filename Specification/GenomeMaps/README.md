
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



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|comments|string|Additional comments|
|commonCropName|string|The common name of the crop, found from "GET /commoncropnames"|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroupCount|integer (int32)|The number of linkage groups present in this genome map|
|mapDbId|string|The ID which uniquely identifies this genome map|
|mapName|string|A human readable name for this genome map|
|markerCount|integer (int32)|The number of markers present in this genome map|
|name|string|DEPRECATED in v1.3 - Use "mapName"|
|publishedDate|string (date)|The date this genome was published|
|scientificName|string|Full scientific binomial format name. This includes Genus, Species, and Sub-species|
|species|string|DEPRECATED in v1.3 - See "scientificName"|
|type|string|The type of map this represents, ussually "Genetic"|
|unit|string|The units used to describe the data in this map|


 

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
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "comments": "comments",
                "commonCropName": "Paw Paw",
                "documentationURL": "https://brapi.org",
                "linkageGroupCount": 1,
                "mapDbId": "gm1",
                "mapName": "Genome Map 1",
                "markerCount": 11,
                "name": "Genome Map 1",
                "publishedDate": "2018-01-01",
                "scientificName": "Asimina triloba",
                "species": "triloba",
                "type": "Genetic",
                "unit": "cM"
            },
            {
                "comments": "comments",
                "commonCropName": "Paw Paw",
                "documentationURL": "https://brapi.org",
                "linkageGroupCount": 2,
                "mapDbId": "gm2",
                "mapName": "Genome Map 2",
                "markerCount": 11,
                "name": "Genome Map 2",
                "publishedDate": "2018-01-01",
                "scientificName": "Asimina triloba",
                "species": "triloba",
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



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]|List of linkage group details associated with a given map|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|markerCount|integer|The number of markers associated with this linkage group|
|maxPosition|integer|The maximum position of a marker within this linkage group|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroups|array[object]|**Deprecated** Use "data"|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|markerCount|integer|The number of markers associated with this linkage group|
|maxPosition|integer|The maximum position of a marker within this linkage group|
|mapDbId|string|The ID which uniquely identifies this genome map|
|mapName|string|A human readable name for this map|
|name|string|DEPRECATED in v1.3 - Use "mapName"|
|type|string|The type of map this represents, ussually "Genetic" or "Physical"|
|unit|string|The units used to describe the data in this map|


 

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
            "totalCount": 1,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "linkageGroupName": "1",
                "markerCount": 11,
                "maxPosition": 1110
            }
        ],
        "documentationURL": "https://brapi.org",
        "linkageGroups": [
            {
                "linkageGroupName": "1",
                "markerCount": 11,
                "maxPosition": 1110
            }
        ],
        "mapDbId": "gm1",
        "mapName": "Genome Map 1",
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



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|location|string|The position of a marker within a linkage group|
|markerDbId|string|Internal db identifier|
|markerName|string|The human readable name for a marker|


 

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
            "totalCount": 11,
            "totalPages": 6
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



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|location|string|The position of a marker within a linkage group|
|markerDbId|string|Internal db identifier|
|markerName|string|The human readable name for a marker|


 

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
            "totalCount": 11,
            "totalPages": 6
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

