# Group Variants




## Variants [/brapi/v1/variants] 




### Get Variants  [GET /brapi/v1/variants{?variantDbId}{?variantSetDbId}{?page}{?pageSize}]

`GET /variants` will return a filtered list of `Variants`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]||
|cipos|array[integer]||
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string||
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)||
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|string|The ID of the `VariantSet` this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string||


 

+ Parameters
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
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





### Get Variants Calls by variantDbId  [GET /brapi/v1/variants/{variantDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?page}{?pageSize}]

 The variant calls for this particular variant. Each one represents the determination of genotype with respect to this variant. `Call`s in this array are implicitly associated with this `Variant`.
Also See:
`GET /calls?variantDbId={variantDbId}` 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values.  The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihoods for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseset|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and is consistent with any other variant calls on the same contig which have the same phaseset string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + variantDbId (Required, ) ... The ID of the `Variant` to be retrieved.
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





### Get Variants by variantDbId  [GET /brapi/v1/variants/{variantDbId}]

`GET /variants/{id}` will return a JSON version of `Variant`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]||
|cipos|array[integer]||
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string||
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)||
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|string|The ID of the `VariantSet` this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string||


 

+ Parameters
    + variantDbId (Required, ) ... The ID of the `Variant` to be retrieved.
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



## Search [/brapi/v1/search] 




### Post Search Variants  [POST /brapi/v1/search/variants]

`POST /variants/search` must accept a JSON version of
`SearchVariantsRequest` as the post body and will return a JSON version of
`SearchVariantsResponse`.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|Only return variant calls which belong to call sets with these IDs. If unspecified, return all variants and no variant call objects.|
|end|string (int64)|Required. The end of the window (0-based, exclusive) for which overlapping variants should be returned.|
|reference_name|string|Required. Only return variants on this reference.|
|start|string (int64)|Required. The beginning of the window (0-based, inclusive) for which overlapping variants should be returned. Genomic positions are non-negative integers less than reference length. Requests spanning the join of circular genomes are represented as two requests one on each side of the join (position 0).|
|variantSetDbIds|array[string]|The `VariantSet` to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "callSetDbIds1",
        "callSetDbIds2"
    ],
    "end": "",
    "reference_name": "reference_name",
    "start": "",
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





### Get Search Variants by searchResultsDbId  [GET /brapi/v1/search/variants/{searchResultsDbId}{?page}{?pageSize}]

`POST /variants/search` must accept a JSON version of
`SearchVariantsRequest` as the post body and will return a JSON version of
`SearchVariantsResponse`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|alternate_bases|array[string]|The bases that appear instead of the reference bases. Multiple alternate alleles are possible.|
|ciend|array[integer]||
|cipos|array[integer]||
|created|string (int64)|The date this variant was created in milliseconds from the epoch.|
|end|string (int64)|The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated by `start + referenceBases.length`.|
|filtersApplied|boolean (boolean)|True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.|
|filtersFailed|array[string]|Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.|
|filtersPassed|boolean (boolean)|True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.|
|referenceBases|string|The reference bases for this variant. They start at the given start position.|
|referenceName|string||
|start|string (int64)|The start position at which this variant occurs (0-based). This corresponds to the first base of the string of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning the join of circular genomes are represented as two variants one on each side of the join (position 0).|
|svlen|string (int64)||
|updated|string (int64)|The time at which this variant was last updated in milliseconds from the epoch.|
|variantDbId|string|The variant ID.|
|variantNames|array[string]|Names for the variant, for example a RefSNP ID.|
|variantSetDbId|string|The ID of the `VariantSet` this variant belongs to. This transitively defines the `ReferenceSet` against which the `Variant` is to be interpreted.|
|variantType|string||


 

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

