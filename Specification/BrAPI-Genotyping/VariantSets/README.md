# Group VariantSets





### Post - /search/variantsets [POST /brapi/v2/search/variantsets]

Submit a search request for `VariantSets`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/variantsets/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|The CallSet to search.|
|commonCropNames|array[string]|The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.|
|programNames|array[string]|Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|variantDbIds|array[string]|The Variant to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Unique identifier for this analysis description|
|analysisName|string|A human readable name for this analysis|
|created|string (date-time)|The time at which this record was created, in ISO 8601 format.|
|description|string|A human readable description of the analysis|
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string (date-time)|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The unique identifier for a VariantSet|
|variantSetName|string|The human readable name for a VariantSet|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "9569cfc4",
        "da1e888c"
    ],
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "page": 0,
    "pageSize": 1000,
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "variantDbIds": [
        "c80f068b",
        "eb7c5f50"
    ],
    "variantSetDbIds": [
        "b2903842",
        "dcbb8558"
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
        "datafiles": [],
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
                        "analysisDbId": "6191a6bd",
                        "analysisName": "Standard QC",
                        "created": "2018-01-01T14:47:23-0600",
                        "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                        "software": [
                            "https://github.com/genotyping/QC"
                        ],
                        "type": "QC",
                        "updated": "2018-01-01T14:47:23-0600"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": "VCF",
                        "fileFormat": "application/excel",
                        "fileURL": "https://brapi.org/example/VCF_1.xlsx"
                    },
                    {
                        "dataFormat": "VCF",
                        "fileFormat": "text/csv",
                        "fileURL": "https://brapi.org/example/VCF_2.csv"
                    }
                ],
                "callSetCount": 341,
                "referenceSetDbId": "57eae639",
                "studyDbId": "2fc3b034",
                "variantCount": 250,
                "variantSetDbId": "87a6ac1e",
                "variantSetName": "Maize QC DataSet 002334"
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
        "datafiles": [],
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




### Get - /search/variantsets/{searchResultsDbId} [GET /brapi/v2/search/variantsets/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `VariantSets` search request <br/>
Clients should submit a search request using the corresponding `POST /search/variantsets` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Unique identifier for this analysis description|
|analysisName|string|A human readable name for this analysis|
|created|string (date-time)|The time at which this record was created, in ISO 8601 format.|
|description|string|A human readable description of the analysis|
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string (date-time)|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The unique identifier for a VariantSet|
|variantSetName|string|The human readable name for a VariantSet|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
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
                        "analysisDbId": "6191a6bd",
                        "analysisName": "Standard QC",
                        "created": "2018-01-01T14:47:23-0600",
                        "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                        "software": [
                            "https://github.com/genotyping/QC"
                        ],
                        "type": "QC",
                        "updated": "2018-01-01T14:47:23-0600"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": "VCF",
                        "fileFormat": "application/excel",
                        "fileURL": "https://brapi.org/example/VCF_1.xlsx"
                    },
                    {
                        "dataFormat": "VCF",
                        "fileFormat": "text/csv",
                        "fileURL": "https://brapi.org/example/VCF_2.csv"
                    }
                ],
                "callSetCount": 341,
                "referenceSetDbId": "57eae639",
                "studyDbId": "2fc3b034",
                "variantCount": 250,
                "variantSetDbId": "87a6ac1e",
                "variantSetName": "Maize QC DataSet 002334"
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
        "datafiles": [],
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




### Get - /variantsets [GET /brapi/v2/variantsets{?variantSetDbId}{?variantDbId}{?callSetDbId}{?studyDbId}{?studyName}{?commonCropName}{?programDbId}{?page}{?pageSize}]

Will return a filtered list of `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Unique identifier for this analysis description|
|analysisName|string|A human readable name for this analysis|
|created|string (date-time)|The time at which this record was created, in ISO 8601 format.|
|description|string|A human readable description of the analysis|
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string (date-time)|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The unique identifier for a VariantSet|
|variantSetName|string|The human readable name for a VariantSet|


 

+ Parameters
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + studyDbId (Optional, ) ... Filter by study DbId
    + studyName (Optional, ) ... Filter by study name
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. Use this parameter to only return results associated with the given program. Use `GET /programs` to find the list of available programs on a server.
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
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
                        "analysisDbId": "6191a6bd",
                        "analysisName": "Standard QC",
                        "created": "2018-01-01T14:47:23-0600",
                        "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                        "software": [
                            "https://github.com/genotyping/QC"
                        ],
                        "type": "QC",
                        "updated": "2018-01-01T14:47:23-0600"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": "VCF",
                        "fileFormat": "application/excel",
                        "fileURL": "https://brapi.org/example/VCF_1.xlsx"
                    },
                    {
                        "dataFormat": "VCF",
                        "fileFormat": "text/csv",
                        "fileURL": "https://brapi.org/example/VCF_2.csv"
                    }
                ],
                "callSetCount": 341,
                "referenceSetDbId": "57eae639",
                "studyDbId": "2fc3b034",
                "variantCount": 250,
                "variantSetDbId": "87a6ac1e",
                "variantSetName": "Maize QC DataSet 002334"
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




### Post - /variantsets/extract [POST /brapi/v2/variantsets/extract]

Will perform a search for `Calls` which match the search criteria in `variantSetsExtractRequest`. The results of the search will be used to create a new `VariantSet` on the server. The new `VariantSet` will be returned.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|The CallSet to search.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|unknownString|string|The string used as a representation for missing data.|
|variantDbIds|array[string]|The Variant to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Unique identifier for this analysis description|
|analysisName|string|A human readable name for this analysis|
|created|string (date-time)|The time at which this record was created, in ISO 8601 format.|
|description|string|A human readable description of the analysis|
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string (date-time)|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The unique identifier for a VariantSet|
|variantSetName|string|The human readable name for a VariantSet|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "9569cfc4",
        "da1e888c"
    ],
    "expandHomozygotes": true,
    "sepPhased": "~",
    "sepUnphased": "|",
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "unknownString": "-",
    "variantDbIds": [
        "c80f068b",
        "eb7c5f50"
    ],
    "variantSetDbIds": [
        "b2903842",
        "dcbb8558"
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
        "datafiles": [],
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
                "analysisDbId": "6191a6bd",
                "analysisName": "Standard QC",
                "created": "2018-01-01T14:47:23-0600",
                "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                "software": [
                    "https://github.com/genotyping/QC"
                ],
                "type": "QC",
                "updated": "2018-01-01T14:47:23-0600"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": "VCF",
                "fileFormat": "application/excel",
                "fileURL": "https://brapi.org/example/VCF_1.xlsx"
            },
            {
                "dataFormat": "VCF",
                "fileFormat": "text/csv",
                "fileURL": "https://brapi.org/example/VCF_2.csv"
            }
        ],
        "callSetCount": 341,
        "referenceSetDbId": "57eae639",
        "studyDbId": "2fc3b034",
        "variantCount": 250,
        "variantSetDbId": "87a6ac1e",
        "variantSetName": "Maize QC DataSet 002334"
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




### Get - /variantsets/{variantSetDbId} [GET /brapi/v2/variantsets/{variantSetDbId}]

This call will return a JSON version of a `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisDbId|string|Unique identifier for this analysis description|
|analysisName|string|A human readable name for this analysis|
|created|string (date-time)|The time at which this record was created, in ISO 8601 format.|
|description|string|A human readable description of the analysis|
|software|array[string]|The software run to generate this analysis.|
|type|string|The type of analysis.|
|updated|string (date-time)|The time at which this record was last updated, in ISO 8601 format.|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantCount|integer|The number of Variants included in this VariantSet|
|variantSetDbId|string|The unique identifier for a VariantSet|
|variantSetName|string|The human readable name for a VariantSet|


 

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
        "datafiles": [],
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
                "analysisDbId": "6191a6bd",
                "analysisName": "Standard QC",
                "created": "2018-01-01T14:47:23-0600",
                "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                "software": [
                    "https://github.com/genotyping/QC"
                ],
                "type": "QC",
                "updated": "2018-01-01T14:47:23-0600"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": "VCF",
                "fileFormat": "application/excel",
                "fileURL": "https://brapi.org/example/VCF_1.xlsx"
            },
            {
                "dataFormat": "VCF",
                "fileFormat": "text/csv",
                "fileURL": "https://brapi.org/example/VCF_2.csv"
            }
        ],
        "callSetCount": 341,
        "referenceSetDbId": "57eae639",
        "studyDbId": "2fc3b034",
        "variantCount": 250,
        "variantSetDbId": "87a6ac1e",
        "variantSetName": "Maize QC DataSet 002334"
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




### Get - /variantsets/{variantSetDbId}/calls [GET /brapi/v2/variantsets/{variantSetDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?pageSize}]

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
|variantSetDbId|string|The unique identifier for a VariantSet|
|variantSetName|string|The human readable name for a VariantSet|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurrence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
    + pageToken (Optional, ) ... Used to request a specific page of data to be returned.Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. 
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
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
                "callSetDbId": "16466f55",
                "callSetName": "Sample_123_DNA_Run_456",
                "genotype": {
                    "values": [
                        "AA"
                    ]
                },
                "genotype_likelihood": [
                    1.0
                ],
                "phaseSet": "6410afc5",
                "variantDbId": "538c8ecf",
                "variantName": "Marker A",
                "variantSetDbId": "87a6ac1e",
                "variantSetName": "Maize QC DataSet 002334"
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




### Get - /variantsets/{variantSetDbId}/callsets [GET /brapi/v2/variantsets/{variantSetDbId}/callsets{?callSetDbId}{?callSetName}{?page}{?pageSize}]

Gets a list of `CallSets` associated with a `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The call set ID.|
|callSetName|string|The call set name.|
|created|string (date-time)|The date this call set was created|
|sampleDbId|string|The Biosample entity the call set data was generated from.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|updated|string (date-time)|The time at which this call set was last updated|
|variantSetDbIds|array[string]|The IDs of the variant sets this call set has calls in.|


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + callSetName (Optional, ) ... The human readable name of the `CallSet` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
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
                "callSetDbId": "eb2bfd3d",
                "callSetName": "Sample_123_DNA_Run_456",
                "created": "2018-01-01T14:47:23-0600",
                "sampleDbId": "5e50e11d",
                "studyDbId": "708149c1",
                "updated": "2018-01-01T14:47:23-0600",
                "variantSetDbIds": [
                    "cfd3d60f",
                    "a4e8bfe9"
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




### Get - /variantsets/{variantSetDbId}/variants [GET /brapi/v2/variantsets/{variantSetDbId}/variants{?variantDbId}{?pageToken}{?pageSize}]

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
|created|string (date-time)|The timestamp when this variant was created.|
|end|integer|This field is optional and may be ignored if there is no relevant map or reference to be associated with.  The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated  by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string|The reference on which this variant occurs. (e.g. `chr_20` or `X`)|
|start|integer|This field is optional and may be ignored if there is no relevant map or reference to be associated with.  The start position at which this variant occurs (0-based). This corresponds to the first base of the string  of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning  the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|integer|Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCF v4.2|
|updated|string (date-time)|The time at which this variant was last updated.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|array[string]|An array of `VariantSet` IDs this variant belongs to. This also defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string|The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"   DEL  : deletion of sequence following "start"|


 

+ Parameters
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + pageToken (Optional, ) ... Used to request a specific page of data to be returned.Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. 
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
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
                "created": "2018-01-01T14:47:23-0600",
                "end": 518,
                "filtersApplied": true,
                "filtersFailed": [
                    "d629a669",
                    "3f14f578"
                ],
                "filtersPassed": true,
                "referenceBases": "TAGGATTGAGCTCTATAT",
                "referenceName": "chr_20",
                "start": 500,
                "svlen": 1500,
                "updated": "2018-01-01T14:47:23-0600",
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

