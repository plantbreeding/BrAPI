# Group VariantSets





### Post - /search/variantsets [POST /brapi/v1/search/variantsets]

Gets a list of `VariantSet` matching the search criteria.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|studyDbIds|array[string]|The `Dataset` to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "page": 0,
    "pageSize": 1000,
    "studyDbIds": [
        "studyDbIds1",
        "studyDbIds2"
    ],
    "variantSetDbIds": [
        "variantSetDbIds1",
        "variantSetDbIds2"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "analysis": [
                    {
                        "analysisDbId": "analysisDbId",
                        "analysisName": "analysisName",
                        "created": "created",
                        "description": "description",
                        "software": [
                            "software1",
                            "software2"
                        ],
                        "type": "type",
                        "updated": "updated"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": ""
                    }
                ],
                "callSetCount": 0,
                "referenceSetDbId": "referenceSetDbId",
                "studyDbId": "studyDbId",
                "variantCount": 0,
                "variantSetDbId": "variantSetDbId",
                "variantSetName": "variantSetName"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/variantsets/{searchResultsDbId} [GET /brapi/v1/search/variantsets/{searchResultsDbId}{?page}{?pageSize}]

Gets a list of `VariantSet` matching the search criteria.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 102 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
    }
}
```

+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "analysis": [
                    {
                        "analysisDbId": "analysisDbId",
                        "analysisName": "analysisName",
                        "created": "created",
                        "description": "description",
                        "software": [
                            "software1",
                            "software2"
                        ],
                        "type": "type",
                        "updated": "updated"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": ""
                    }
                ],
                "callSetCount": 0,
                "referenceSetDbId": "referenceSetDbId",
                "studyDbId": "studyDbId",
                "variantCount": 0,
                "variantSetDbId": "variantSetDbId",
                "variantSetName": "variantSetName"
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




### Get - /variantsets [GET /brapi/v1/variantsets{?variantSetDbId}{?page}{?pageSize}]

Will return a filtered list of `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "analysis": [
                    {
                        "analysisDbId": "analysisDbId",
                        "analysisName": "analysisName",
                        "created": "created",
                        "description": "description",
                        "software": [
                            "software1",
                            "software2"
                        ],
                        "type": "type",
                        "updated": "updated"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": ""
                    }
                ],
                "callSetCount": 0,
                "referenceSetDbId": "referenceSetDbId",
                "studyDbId": "studyDbId",
                "variantCount": 0,
                "variantSetDbId": "variantSetDbId",
                "variantSetName": "variantSetName"
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




### Post - /variantsets/extract [POST /brapi/v1/variantsets/extract]

Will perform a search for `Calls` which match the search criteria in `variantSetsExtractRequest`. The results of the search will be used to create a new `VariantSet` on the server. The new `VariantSet` will be returned.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|The CallSet to search.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantDbIds|array[string]|The Variant to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "callSetDbIds1",
        "callSetDbIds2"
    ],
    "sepPhased": "sepPhased",
    "sepUnphased": "sepUnphased",
    "unknownString": "unknownString",
    "variantDbIds": [
        "variantDbIds1",
        "variantDbIds2"
    ],
    "variantSetDbIds": [
        "variantSetDbIds1",
        "variantSetDbIds2"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "analysis": [
            {
                "analysisDbId": "analysisDbId",
                "analysisName": "analysisName",
                "created": "created",
                "description": "description",
                "software": [
                    "software1",
                    "software2"
                ],
                "type": "type",
                "updated": "updated"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": [
                    "DartSeq",
                    "VCF",
                    "Hapmap",
                    "tabular",
                    "JSON"
                ],
                "fileFormat": [
                    "text/csv",
                    "text/tsv",
                    "application/excel",
                    "application/zip",
                    "application/json"
                ],
                "fileURL": ""
            }
        ],
        "callSetCount": 0,
        "referenceSetDbId": "referenceSetDbId",
        "studyDbId": "studyDbId",
        "variantCount": 0,
        "variantSetDbId": "variantSetDbId",
        "variantSetName": "variantSetName"
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




### Get - /variantsets/{variantSetDbId} [GET /brapi/v1/variantsets/{variantSetDbId}]

This call will return a JSON version of a `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The variant set ID.|
|variantSetName|string|The variant set name.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `Variant` to be retrieved.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
        "additionalInfo": {},
        "analysis": [
            {
                "analysisDbId": "analysisDbId",
                "analysisName": "analysisName",
                "created": "created",
                "description": "description",
                "software": [
                    "software1",
                    "software2"
                ],
                "type": "type",
                "updated": "updated"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": [
                    "DartSeq",
                    "VCF",
                    "Hapmap",
                    "tabular",
                    "JSON"
                ],
                "fileFormat": [
                    "text/csv",
                    "text/tsv",
                    "application/excel",
                    "application/zip",
                    "application/json"
                ],
                "fileURL": ""
            }
        ],
        "callSetCount": 0,
        "referenceSetDbId": "referenceSetDbId",
        "studyDbId": "studyDbId",
        "variantCount": 0,
        "variantSetDbId": "variantSetDbId",
        "variantSetName": "variantSetName"
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




### Get - /variantsets/{variantSetDbId}/calls [GET /brapi/v1/variantsets/{variantSetDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

Gets a list of `Calls` associated with a `VariantSet`.

** THIS ENDPOINT USES TOKEN BASED PAGING **



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseSet|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phase set string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
    + page (Optional, ) ... Which result page is requested. Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "currentPageToken": "48bc6ac1",
            "nextPageToken": "cb668f63",
            "pageSize": 1000,
            "prevPageToken": "9659857e",
            "totalCount": 10,
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "genotype": {
                    "values": []
                },
                "genotype_likelihood": [],
                "phaseSet": "phaseSet",
                "variantDbId": "variantDbId",
                "variantName": "variantName"
            }
        ],
        "expandHomozygotes": true,
        "sepPhased": "~",
        "sepUnphased": "|",
        "unknownString": "-"
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




### Get - /variantsets/{variantSetDbId}/callsets [GET /brapi/v1/variantsets/{variantSetDbId}/callsets{?callSetDbId}{?callSetName}{?page}{?pageSize}]

Gets a list of `CallSets` associated with a `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The call set ID.|
|callSetName|string|The call set name.|
|created|integer|The date this call set was created in milliseconds from the epoch.|
|sampleDbId|string|The Biosample entity the call set data was generated from.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|updated|integer|The time at which this call set was last updated in milliseconds from the epoch.|
|variantSetIds|array[string]|The IDs of the variant sets this call set has calls in.|


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + callSetName (Optional, ) ... The human readable name of the `CallSet` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "totalCount": 10,
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "created": 0,
                "sampleDbId": "sampleDbId",
                "studyDbId": "studyDbId",
                "updated": 0,
                "variantSetIds": [
                    "variantSetIds1",
                    "variantSetIds2"
                ]
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




### Get - /variantsets/{variantSetDbId}/variants [GET /brapi/v1/variantsets/{variantSetDbId}/variants{?variantDbId}{?page}{?pageSize}]

This call will return an array of `Variants`.

** THIS ENDPOINT USES TOKEN BASED PAGING **



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]|Similar to "cipos", but for the variant's end position (which is derived from start + svlen).|
|cipos|array[integer]|In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCF v4.2|
|created|integer|The date this variant was created in milliseconds from the epoch.|
|end|integer|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string|The reference on which this variant occurs. (e.g. `chr_20` or `X`)|
|start|integer|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|integer|Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCF v4.2|
|updated|integer|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|array[string]|An array of `VariantSet` IDs this variant belongs to. This also defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string|The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"   DEL  : deletion of sequence following "start"|


 

+ Parameters
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + page (Optional, ) ... Which result page is requested. Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
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
            "currentPageToken": "48bc6ac1",
            "nextPageToken": "cb668f63",
            "pageSize": 1000,
            "prevPageToken": "9659857e",
            "totalCount": 10,
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
                "alternate_bases": [
                    "TAGGATTGAGCTCTATAT"
                ],
                "ciend": [
                    -1000,
                    0
                ],
                "cipos": [
                    -12000,
                    1000
                ],
                "created": "1573671122",
                "end": "518",
                "filtersApplied": true,
                "filtersFailed": [
                    "d629a669",
                    "3f14f578"
                ],
                "filtersPassed": true,
                "referenceBases": "TAGGATTGAGCTCTATAT",
                "referenceName": "chr_20",
                "start": "500",
                "svlen": "1500",
                "updated": "1573672019",
                "variantDbId": "628e89c5",
                "variantNames": [
                    "RefSNP_ID_1",
                    "06ea312e"
                ],
                "variantSetDbId": [
                    "c8ae400b",
                    "ef2c204b"
                ],
                "variantType": "DUP"
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

