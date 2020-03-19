# Group Variants





### Post - /search/variants [POST /brapi/v2/search/variants]

Gets a list of `Variant` matching the search criteria.

** THIS ENDPOINT USES TOKEN BASED PAGING **

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|Only return variant calls which belong to call sets with these IDs. If unspecified, return all variants and no variant call objects.|
|end|integer|The end of the window (0-based, exclusive) for which overlapping variants should be returned.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|pageToken|string|Used to request a specific page of data to be returned.  Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. |
|referenceDbId|string|Only return variants on this reference.|
|start|integer|The beginning of the window (0-based, inclusive) for which overlapping variants should be returned. Genomic positions are non-negative integers less than reference length. Requests spanning the join of circular genomes are represented as two requests one on each side of the join (position 0).|
|variantSetDbIds|array[string]|The `VariantSet` to search.|


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
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "4639fe3e",
        "b60d900b"
    ],
    "end": 1500,
    "pageSize": 1000,
    "pageToken": "33c27874",
    "referenceDbId": "120a2d5c",
    "start": 100,
    "variantSetDbIds": [
        "ba63d810",
        "434d1760"
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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




### Get - /search/variants/{searchResultsDbId} [GET /brapi/v2/search/variants/{searchResultsDbId}{?pageToken}{?pageSize}]

Gets a list of `Variant` matching the search criteria.

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
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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




### Get - /variants [GET /brapi/v2/variants{?variantDbId}{?variantSetDbId}{?pageToken}{?pageSize}]

Gets a filtered list of `Variants`.

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
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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




### Get - /variants/{variantDbId} [GET /brapi/v2/variants/{variantDbId}]

`GET /variants/{id}` will return a JSON version of `Variant`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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
    + variantDbId (Required, ) ... The ID of the `Variant` to be retrieved.
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
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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




### Get - /variants/{variantDbId}/calls [GET /brapi/v2/variants/{variantDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?pageSize}]

The variant calls for this particular variant. Each one represents the determination of genotype with respect to this variant. `Calls` in this array are implicitly associated with this `Variant`.

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
    + variantDbId (Required, ) ... The ID of the `Variant` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurence (false)
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
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
                "variantName": "Marker A"
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

