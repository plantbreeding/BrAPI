
# Group Ontologies

API to manage the details of stored Ontologies. This could be a reference a local Ontology or a remote public Ontology.  





## Ontologies [/brapi/v1/ontologies] 




### Get Ontologies  [GET /brapi/v1/ontologies{?page}{?pageSize}]

Call to retrieve a list of observation variable ontologies available in the system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|description|string|Human readable description of Ontology|
|authors|string|Ontology's list of authors (no specific format)|
|copyright|string|Ontology copyright|
|additionalInfo|object|Additional arbitrary info|
|version|string|Ontology version (no specific format)|
|licence|string|Ontology licence|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
        "data": [
            {
                "additionalInfo": {},
                "authors": "Bob Robertson, Rob Robertson",
                "copyright": "Copyright 1987, Bob Robertson",
                "description": "This is an example ontology that does not exist",
                "documentationURL": "https://wiki.brapi.org/ontology",
                "licence": "MIT Open source licence",
                "ontologyDbId": "18e186cd",
                "ontologyName": "The Official Ontology",
                "version": "V1.3.2"
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

