
# Group Genome Maps

Retrieving genetic or physical maps
- type: [Genetic | Physical]
- unit: [cM | Mb]
- linkageGroup: may be scaffold (i.e. linkageGroupCount may consist of chromosomes or scaffolds or a combination of the two)
- For genetic maps, map naming convention should tell whether it is a consensus or mapping population (name of population) map for genetic maps
- For physical maps, map naming convention should tell whether it is a reference genome (name of line) or pan-genome



## Post - /search/markerpositions/{ID} [/brapi/v1//search/markerpositions/{searchResultsDbId}] 



### /search/markerpositions/{searchResultsDbId} [POST /brapi/v1/search/markerpositions/{searchResultsDbId}{?page}{?pageSize}]

Get marker position information, based on Map, Linkage Group, and Marker ID



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|mapDbId|string|The unique ID of the map|
|mapName|string|The human readbale name of the map|
|markerDbId|string|Internal db identifier|
|markerName|string|The human readable name for a marker|
|position|integer|The position of a marker within a linkage group|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "data": []
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```


## Get - /markerpositions [/brapi/v1//markerpositions] 



### /markerpositions [GET /brapi/v1/markerpositions{?mapDbId}{?linkageGroupName}{?markerDbId}{?minPosition}{?maxPosition}{?page}{?pageSize}]

Get marker position information, based on Map, Linkage Group, and Marker ID



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|mapDbId|string|The unique ID of the map|
|mapName|string|The human readbale name of the map|
|markerDbId|string|Internal db identifier|
|markerName|string|The human readable name for a marker|
|position|integer|The position of a marker within a linkage group|


 

+ Parameters
    + mapDbId (Optional, ) ... unique id of a map
    + linkageGroupName (Optional, ) ... The chromosome identifier or the generic linkage group identifier if the chromosome is not applicable.
    + markerDbId (Optional, ) ... The unique id for a marker
    + minPosition (Optional, ) ... The minimum position
    + maxPosition (Optional, ) ... The maximum position
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "data": []
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```


## Post - /search/markerpositions [/brapi/v1//search/markerpositions] 



### /search/markerpositions [POST /brapi/v1/search/markerpositions]

Get marker position information, based on Map, Linkage Group, and Marker ID

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|linkageGroupNames|array[string]|The Uniquely Identifiable name of this linkage group|
|mapDbIds|array[string]|The unique ID of the map|
|markerDbIds|array[string]|Internal db identifier|
|maxPosition|integer|The maximum position|
|minPosition|integer|The minimum position|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "linkageGroupNames": [
        "linkageGroupNames1",
        "linkageGroupNames2"
    ],
    "mapDbIds": [
        "mapDbIds1",
        "mapDbIds2"
    ],
    "markerDbIds": [
        "markerDbIds1",
        "markerDbIds2"
    ],
    "maxPosition": 0,
    "minPosition": 0
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "searchResultDbId": "551ae08c"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```


## Get - /maps [/brapi/v1//maps] 



### /maps [GET /brapi/v1/maps{?commonCropName}{?scientificName}{?type}{?programDbId}{?trialDbId}{?studyDbId}{?page}{?pageSize}]

Get list of maps



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|comments|string|Additional comments|
|commonCropName|string|The common name of the crop, found from "GET /commoncropnames"|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroupCount|integer (int32)|The number of linkage groups present in this genome map|
|mapDbId|string|The ID which uniquely identifies this genome map|
|mapName|string|A human readable name for this genome map|
|markerCount|integer (int32)|The number of markers present in this genome map|
|publishedDate|string (date)|The date this genome was published|
|scientificName|string|Full scientific binomial format name. This includes Genus, Species, and Sub-species|
|type|string|The type of map this represents, ussually "Genetic"|
|unit|string|The units used to describe the data in this map|


 

+ Parameters
    + commonCropName (Optional, ) ... The common name of the crop, found from "GET /commoncropnames"
    + scientificName (Optional, ) ... Full scientific binomial format name. This includes Genus, Species, and Sub-species
    + type (Optional, ) ... Type of map
    + programDbId (Optional, ) ... Unique Id to filter by Program
    + trialDbId (Optional, ) ... Unique Id to filter by Trial
    + studyDbId (Optional, ) ... Unique Id to filter by Study
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```


## Get - /maps/{ID} [/brapi/v1//maps/{mapDbId}] 



### /maps/{mapDbId} [GET /brapi/v1/maps/{mapDbId}{?page}{?pageSize}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|comments|string|Additional comments|
|commonCropName|string|The common name of the crop, found from "GET /commoncropnames"|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|linkageGroupCount|integer (int32)|The number of linkage groups present in this genome map|
|mapDbId|string|The ID which uniquely identifies this genome map|
|mapName|string|A human readable name for this genome map|
|markerCount|integer (int32)|The number of markers present in this genome map|
|publishedDate|string (date)|The date this genome was published|
|scientificName|string|Full scientific binomial format name. This includes Genus, Species, and Sub-species|
|type|string|The type of map this represents, ussually "Genetic"|
|unit|string|The units used to describe the data in this map|


 

+ Parameters
    + mapDbId (Required, ) ... The internal db id of a selected map
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "documentationURL": "https://brapi.org",
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
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```


## Get - /maps/{ID}/linkagegroups [/brapi/v1//maps/{mapDbId}/linkagegroups] 



### /maps/{mapDbId}/linkagegroups [GET /brapi/v1/maps/{mapDbId}/linkagegroups{?page}{?pageSize}]

Get the Linkage Groups of a specific Genomic Map. A Linkage Group is the BrAPI generic term for a named section of a map. A Linkage Group can represent a Chromosome, Scaffold, or Linkage Group.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|linkageGroupName|string|The Uniquely Identifiable name of this linkage group|
|markerCount|integer|The number of markers associated with this linkage group|
|maxPosition|integer|The maximum position of a marker within this linkage group|


 

+ Parameters
    + mapDbId (Required, ) ... The internal db id of a selected map
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "data": []
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

