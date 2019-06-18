
# Group Markerprofiles

For the purposes of this API, the definition of markerprofile is *the allele calls for a specified germplasm line, for all markers, for a specified set of genotyping experiments or all experiments.*

Basic concepts in the **Breeding API**:

- *markerprofile*: A set of marker scores for a specific extract from a specific germplasm.
- *extract* : a preparation from a germplasm for an analysis. 
- *sample*: an individual plant or tissue from a plant of a particular germplasm
- *germplasm*: a single genetic entity (cultivar, variety, accession, breeding line) used for analysis
- *marker*: a DNA sequence polymorphism, potentially localized to a single genomic location
- *allele*: one of the two possible states of a marker in each haploid chromosome complement of a specified germplasm, as determined in a specified experiment. A diploid organism has two alleles per marker.
- *missing*: a germplasm/marker/experiment combination for which no allele result is available, whether it was tested for or not




## Allelematrices-search [/brapi/v1/allelematrices-search] 




### Get Allelematrices-search  [GET /brapi/v1/allelematrices-search{?markerProfileDbId}{?markerDbId}{?matrixDbId}{?format}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

See Search Services for additional implementation details.

This uses a more efficient data structure and pagination for large number of markers.

See Search Services for additional implementation details.

Use GET when parameter size is less than 2K bytes.

This method may support asynchronous processing.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Is an array of arrays; each inner array has three entries: ```markerDbId```, ```markerProfileDbId```, ```alleleCall```. Scores have to be represented as described further up. e.g. unknown data as "N", etc. Missing data can be skipped.|


 

+ Parameters
    + markerProfileDbId (Optional, ) ... The marker Profile db ids. Not Required if 'markerDbId' or 'matrixDbId' is present.
    + markerDbId (Optional, ) ... ids of the markers. if none are specified, results are returned for all markers in the database. Not Required if 'markerProfileDbId' or 'matrixDbId' is present.
    + matrixDbId (Optional, ) ... 
    + format (Optional, ) ... format for the datafile to be downloaded. tsv and csv currently supported; flapjack may be supported.
    + expandHomozygotes (Optional, ) ... Should homozygotes NOT be collapsed into a single occurrence?
    + unknownString (Optional, ) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".
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
            "totalCount": 280,
            "totalPages": 140
        },
        "status": []
    },
    "result": {
        "data": [
            [
                "mr01",
                "P1",
                "A"
            ],
            [
                "mr02",
                "P1",
                "C"
            ]
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





### Post Allelematrices-search  [POST /brapi/v1/allelematrices-search]

See Search Services for additional implementation details.

This uses a more efficient data structure and pagination for large number of markers.

Use POST when parameter size is greater than 2K bytes.

- If no format is specified, this call returns the data in JSON form.

- If a format (other than JSON) is specified and the server supports this format, it will return the link to the exported data file in the "datafiles" field of the "metadata".

- If more than one format is requested at a time, the server will throw a "501 Not Implemented" error.

The format of the tsv response can be found on GitHub (https://github.com/plantbreeding/Documentation/wiki/BrAPI-TSV-Expected-Formats)'

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|format|string|The data format of the response data. ie "json", "tsv", etc|
|markerDbId|array[string]|An ID which uniquely identifies a Marker|
|markerProfileDbId|array[string]|An ID which uniquely identifies a Marker Profile|
|matrixDbId|array[string]|An ID which uniquely identifies an Allele Matrix|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|sepPhased|string|The string to use as a separator for phased allele calls.|
|sepUnphased|string|The string to use as a separator for unphased allele calls.|
|unknownString|string|The string to use as a representation for missing data.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Is an array of arrays; each inner array has three entries: ```markerDbId```, ```markerProfileDbId```, ```alleleCall```. Scores have to be represented as described further up. e.g. unknown data as "N", etc. Missing data can be skipped.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "format": "format0",
    "markerDbId": [
        "markerDbId0",
        "markerDbId1"
    ],
    "markerProfileDbId": [
        "markerProfileDbId0",
        "markerProfileDbId1"
    ],
    "matrixDbId": [
        "matrixDbId0",
        "matrixDbId1"
    ],
    "page": 0,
    "pageSize": 0,
    "sepPhased": "sepPhased0",
    "sepUnphased": "sepUnphased0",
    "unknownString": "unknownString0"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "asynchStatus": {
            "asynchId": "",
            "endTime": "2018-12-05",
            "percentComplete": 100,
            "startTime": "2018-12-05",
            "status": "FINISHED"
        },
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 280,
            "totalPages": 140
        },
        "status": []
    },
    "result": {
        "data": [
            [
                "mr01",
                "P1",
                "A"
            ],
            [
                "mr02",
                "P1",
                "C"
            ]
        ]
    }
}
```

+ Response 200 (application/tsv)
```
{
    "metadata": {
        "datafiles": [
            "https://my-fancy-server/files/allelematrix-1234.tsv"
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": []
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



## Allelematrices [/brapi/v1/allelematrices] 




### Get Allelematrices  [GET /brapi/v1/allelematrices{?studyDbId}{?page}{?pageSize}]

This resource is used for reading and writing genomic matrices

GET provides a list of available matrices, optionally filtered by study;



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|description|string|How the matrix was generated|
|lastUpdated|string (date-time)|A date format|
|matrixDbId|string|ID of the matrix|
|matrixName|string|Name of the matrix|
|studyDbId|string|Link to the study where the matrix was produced|


 

+ Parameters
    + studyDbId (Required, ) ... restricts the list of matrices to a specific study.
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
                "description": "example matrix",
                "lastUpdated": "2018-05-03T11:03:56-04:00",
                "matrixDbId": "mat1",
                "matrixName": "Example Matrix",
                "name": "Example Matrix",
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



## Markerprofiles [/brapi/v1/markerprofiles] 




### Get Markerprofiles  [GET /brapi/v1/markerprofiles{?germplasmDbId}{?studyDbId}{?sampleDbId}{?extractDbId}{?page}{?pageSize}]

For the requested Germplasm Id and/or Extract Id, returns the Markerprofile Id and number of non-missing allele calls (marker/allele pairs).



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|analysisMethod|string|The type of analysis performed to determine a set of marker data|
|extractDbId|string| The ID which uniquely identifies this data extract|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|markerProfileDbId|string|Unique in the database. Can be a catenation of unique IDs for germplasm and extract. Required|
|resultCount|integer|Number of markers present in the marker profile|
|sampleDbId|string|The ID which uniquely identifies a sample|
|uniqueDisplayName|string|Human readable display name for this marker profile|


 

+ Parameters
    + germplasmDbId (Optional, ) ... The server's internal ids for the Germplasm IDs, as returned by the Find marker profile by Germplasm service.
    + studyDbId (Optional, ) ... The server's internal id for the StudyDbId
    + sampleDbId (Optional, ) ... The server's internal id for the SampleDbId
    + extractDbId (Optional, ) ... The server's internal id for the ExtractDbId
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
            "totalCount": 14,
            "totalPages": 7
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "analysisMethod": "GBS",
                "extractDbId": "extract1",
                "germplasmDbId": "1",
                "markerProfileDbId": "P1",
                "markerprofileDbId": "P1",
                "resultCount": 20,
                "sampleDbId": "sam00",
                "uniqueDisplayName": "My Fancy Germplasm"
            },
            {
                "analysisMethod": "GBS",
                "extractDbId": "extract2",
                "germplasmDbId": "1",
                "markerProfileDbId": "P2",
                "markerprofileDbId": "P2",
                "resultCount": 20,
                "sampleDbId": "sam01",
                "uniqueDisplayName": "My Fancy Germplasm"
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





### Get Markerprofiles by markerProfileDbId  [GET /brapi/v1/markerprofiles/{markerProfileDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

For the requested marker profile ID, returns the allele call for each marker. 
        
Allele encodings

- Unknown data will by default be encoded by \"N\"

- Homozygotes are returned as a single occurance, e.g. AA -> A, GG -> G

- Phased heterozygotes are by default separated by a pipe (\"|\") and unphased heterozygotes are by default separated by a forward slash (\"/\")

- Dominant markers such as DArTs: 1 for present, 0 for absent
        
- If the user would like to use an empty string (\"\") for any of the parameters, the value should be set to the reserved word \"empty_string\", e.g. sepUnphased=empty_string.

Open issue: The pages of data will need to be sorted sensibly in order for the requested page to be delivered consistently.  By map or genome position? Alphabetically?'"



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|analysisMethod|string|The type of analysis performed to determine a set of marker data|
|data|array[object]|array of marker-name/score pairs|
|extractDbId|string|Required|
|germplasmDbId|string|Required|
|markerProfileDbId|string|Unique in the database. Can be a catenation of unique IDs for germplasm and extract. Required|
|uniqueDisplayName|string|Human readable display name for this marker profile|


 

+ Parameters
    + markerProfileDbId (Required, ) ... The server's internal id for the marker profile
    + expandHomozygotes (Optional, ) ... Should homozygotes NOT be collapsed into a single orrucance?
    + unknownString (Optional, ) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".
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
            "totalCount": 20,
            "totalPages": 10
        },
        "status": []
    },
    "result": {
        "analysisMethod": "GBS",
        "data": [
            {
                "marker1-1": "A"
            },
            {
                "marker1-2": "C"
            }
        ],
        "extractDbId": "extract1",
        "germplasmDbId": "1",
        "markerProfileDbId": "P1",
        "markerprofileDbId": "P1",
        "uniqueDisplayName": "My Fancy Germplasm"
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

