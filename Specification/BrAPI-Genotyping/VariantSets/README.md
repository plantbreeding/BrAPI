# Group VariantSets




## Variantsets [/brapi/v1/variantsets] 




### Post Variantsets Extract  [POST /brapi/v1/variantsets/extract]

`POST /variantsets/extract` will perform a search for `Calls` which match the search criteria in `variantSetsExtractRequest`
The results of the search will be used to create a new `VariantSet` on the server. The new `VariantSet` will be returned.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|sepPhased|string|The string used as a separator for phased allele calls.|
|variantSetDbIds|array[string]|The VariantSet to search.|
|variantDbIds|array[string]|The Variant to search.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|callSetDbIds|array[string]|The CallSet to search.|
|unknownString|string|The string used as a representation for missing data.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|software|array[string]|The software run to generate this analysis.|
|additionalInfo|object|Additional arbitrary info|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|variantSetName|string|The variant set name.|
|variantCount|integer|The number of Variants included in this VariantSet|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantSetDbId|string|The variant set ID.|


 

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





### Get Variantsets  [GET /brapi/v1/variantsets{?variantSetDbId}{?page}{?pageSize}]

`GET /variantsets` will return a filtered list of `VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|software|array[string]|The software run to generate this analysis.|
|additionalInfo|object|Additional arbitrary info|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|variantSetName|string|The variant set name.|
|variantCount|integer|The number of Variants included in this VariantSet|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantSetDbId|string|The variant set ID.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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





### Get Variantsets Callsets by variantSetDbId  [GET /brapi/v1/variantsets/{variantSetDbId}/callsets{?callSetDbId}{?callSetName}{?page}{?pageSize}]

 Gets a list of `CallSets` associated with a `VariantSet`.
Also See:
`GET /callsets?variantSetDbId={variantSetDbId}` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The call set ID.|
|sampleDbId|string|The Biosample entity the call set data was generated from.|
|callSetName|string|The call set name.|
|updated|string (int64)|The time at which this call set was last updated in milliseconds from the epoch.|
|variantSetIds|array[string]|The IDs of the variant sets this call set has calls in.|
|created|string (int64)|The date this call set was created in milliseconds from the epoch.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + callSetName (Optional, ) ... The human readbale name of the `CallSet` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "created": "",
                "sampleDbId": "sampleDbId",
                "studyDbId": "studyDbId",
                "updated": "",
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





### Get Variantsets Calls by variantSetDbId  [GET /brapi/v1/variantsets/{variantSetDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

 Gets a list of `Calls` associated with a `VariantSet`.
Also See:
`GET /calls?variantSetDbId={variantSetDbId}` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|sepPhased|string|The string used as a separator for phased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|phaseset|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phaseset string.|
|genotype_likelihood|array[number]|The genotype likelihoods for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepUnphased|string|The string used as a separator for unphased allele calls.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
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
                "callSetDbId": "callSetDbId",
                "callSetName": "callSetName",
                "genotype": {
                    "values": []
                },
                "genotype_likelihood": [],
                "phaseset": "phaseset",
                "variantDbId": "variantDbId",
                "variantName": "variantName"
            }
        ],
        "sepPhased": "sepPhased",
        "sepUnphased": "sepUnphased",
        "unknownString": "unknownString"
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





### Get Variantsets by variantSetDbId  [GET /brapi/v1/variantsets/{variantSetDbId}]

`GET /variantsets/{variantSetDbId}` will return a JSON version of
`VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|software|array[string]|The software run to generate this analysis.|
|additionalInfo|object|Additional arbitrary info|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|variantSetName|string|The variant set name.|
|variantCount|integer|The number of Variants included in this VariantSet|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantSetDbId|string|The variant set ID.|


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `Variant` to be retrieved.
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





### Get Variantsets Variants by variantSetDbId  [GET /brapi/v1/variantsets/{variantSetDbId}/variants{?variantDbId}{?page}{?pageSize}]

`GET /variantsets/{variant_set_id}` will return a JSON version of
`VariantSet`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|ciend|array[integer]||
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|cipos|array[integer]||
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)||
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|variantType|string||
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|variantDbId|string|The variant ID.|
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|referenceName|string||
|variantSetDbId|string|The ID of the `VariantSet` this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|


 

+ Parameters
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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
                "alternate_bases": [
                    "alternate_bases1",
                    "alternate_bases2"
                ],
                "ciend": [],
                "cipos": [],
                "created": "",
                "end": "",
                "filtersFailed": [
                    "filtersFailed1",
                    "filtersFailed2"
                ],
                "referenceBases": "referenceBases",
                "referenceName": "referenceName",
                "start": "",
                "svlen": "",
                "updated": "",
                "variantDbId": "variantDbId",
                "variantNames": [
                    "variantNames1",
                    "variantNames2"
                ],
                "variantSetDbId": "variantSetDbId",
                "variantType": "variantType"
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



## Search [/brapi/v1/search] 




### Post Search Variantsets  [POST /brapi/v1/search/variantsets]

`POST /variantsets/search` must accept a JSON version of
`SearchVariantSetsRequest` as the post body and will return a JSON version
of `SearchVariantSetsResponse`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|variantSetDbIds|array[string]|The VariantSet to search.|
|studyDbIds|array[string]|The `Dataset` to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
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





### Get Search Variantsets by searchResultsDbId  [GET /brapi/v1/search/variantsets/{searchResultsDbId}{?page}{?pageSize}]

`POST /variantsets/search` must accept a JSON version of
`SearchVariantSetsRequest` as the post body and will return a JSON version
of `SearchVariantSetsResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|analysis|array[object]|Set of Analysis descriptors for this VariantSet|
|analysisName|string||
|created|string|The time at which this record was created, in ISO 8601 format.|
|description|string||
|analysisDbId|string|Formats of id  name  description  accessions are described in the documentation on general attributes and formats.|
|type|string|The type of analysis.|
|updated|string|The time at which this record was last updated, in ISO 8601 format.|
|software|array[string]|The software run to generate this analysis.|
|additionalInfo|object|Additional arbitrary info|
|referenceSetDbId|string|The ID of the reference set that describes the sequences used by the variants in this set.|
|callSetCount|integer|The number of CallSets included in this VariantSet|
|availableFormats|array[object]|When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.   dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)  fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|fileURL|string (uri)|A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.|
|fileFormat|string|fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevent request and response.|
|dataFormat|string|dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)|
|variantSetName|string|The variant set name.|
|variantCount|integer|The number of Variants included in this VariantSet|
|studyDbId|string|The ID of the dataset this variant set belongs to.|
|variantSetDbId|string|The variant set ID.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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

