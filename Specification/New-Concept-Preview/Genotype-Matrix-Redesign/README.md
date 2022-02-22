
# Group Genotype Matrix Redesign


Genotype Matrix Redesign description 




### Put - /calls [PUT /brapi/v2/calls]

Update existing `Calls` with new genotype value or metadata
<br/>Implementation Note - 
<br/>A `Call` object does not have a DbId of its own. It is defined by the unique combination of 
`callSetDbId`, `variantDbId`, and `variantSetDbId`. These three fields MUST be present for every 
`call` update request. This endpoint should not allow these fields to be modified for a given 
`call`. Modifying these fields in the database is effectively moving a cell to a different location
in the genotype matrix. This action is dangerous and can cause data collisions.     

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to. <br/>If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet`  is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values. <br/>The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseSet|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|callSetDbId|string|The ID of the call set this variant call belongs to. <br/>If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet`  is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|callSetName|string|The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.|
|genotype|object|`ListValue` is a wrapper around a repeated field of values. <br/>The JSON representation for `ListValue` is JSON array.|
|values|array|Repeated field of dynamically typed values.|
|genotype_likelihood|array[number]|The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.|
|phaseSet|string|If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.|
|variantDbId|string|The ID of the variant this call belongs to.|
|variantName|string|The name of the variant this call belongs to.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "callSetDbId": "16466f55",
        "callSetName": "Sample_123_DNA_Run_456",
        "genotype": {
            "values": [
                "1/1"
            ]
        },
        "genotype_likelihood": [
            1.0
        ],
        "phaseSet": "6410afc5",
        "variantDbId": "538c8ecf",
        "variantName": "Marker A"
    }
]
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
                        "1/1"
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
        "sepPhased": "|",
        "sepUnphased": "/",
        "unknownString": "."
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




### Post - /search/variantmatrix [POST /brapi/v2/search/variantmatrix]

Submit a search request for `Calls`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/calls/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details. 
<br/>

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|The CallSet to search.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|germplasmDbIds|array[string]|The germplasm to search|
|germplasmNames|array[string]|The germplasm to search|
|germplasmPUIs|array[string]|The germplasm to search|
|pagination|array[object]|Pagination for the matrix|
|dimension|string|the dimension of the matrix being paginated|
|page|integer|the requested page number (zero indexed)|
|pageSize|integer|the maximum number of elements per page in this dimension of the matrix|
|positionRanges|array[string]|The postion range to search <br/> Uses the format "<chrom>:<start>-<end>" where <chrom> is the chromosome name, <start> is  the starting position of the range, and <end> is the ending position of the range|
|preview|boolean|Default Value = false <br/> If 'preview' is set to true, then the server should only return the lists of 'callSetDbIds',  'variantDbIds', and 'variantSetDbIds'. The server should not return any matrix data. This is intended to be a preview and give the client a sense of how large the matrix returned will be <br/> If 'preview' is set to false or not set (default), then the server should return all the matrix data as requested.|
|sampleDbIds|array[string]|The samples to search|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantDbIds|array[string]|The Variant to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]||
|data|array[array]||
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|genotypeFields|array[object]||
|fieldMatrix|array[array]||
|fieldName|string||
|fieldType|string||
|pagination|array[object]|Pagination for the matrix|
|dimension|string|the dimension of the matrix being paginated|
|page|integer|the requested page number (zero indexed)|
|pageSize|integer|the maximum number of elements per page in this dimension of the matrix|
|totalCount|integer|The total number of elements that are available on the server and match the requested query parameters.|
|totalPages|integer|The total number of pages of elements available on the server. This should be calculated with the following formula.  <br/>totalPages = CEILING( totalCount / requested_page_size)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantSetDbIds|array[string]||
|variants|array[object]||
|chromosome|string||
|end|integer||
|ploidy|integer||
|start|integer||
|variantDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "a03202ec",
        "274e4f63"
    ],
    "expandHomozygotes": true,
    "germplasmDbIds": [
        "a03202ec",
        "274e4f63"
    ],
    "germplasmNames": [
        "a03202ec",
        "274e4f63"
    ],
    "germplasmPUIs": [
        "a03202ec",
        "274e4f63"
    ],
    "pagination": [
        {
            "dimension": "variants",
            "page": 0,
            "pageSize": 500
        },
        {
            "dimension": "callsets",
            "page": 4,
            "pageSize": 1000
        }
    ],
    "positionRanges": [
        "20:1000-35000",
        "20:87000-125000"
    ],
    "preview": true,
    "sampleDbIds": [
        "a03202ec",
        "274e4f63"
    ],
    "sepPhased": "|",
    "sepUnphased": "/",
    "unknownString": ".",
    "variantDbIds": [
        "bba0b258",
        "ff97d4f0"
    ],
    "variantSetDbIds": [
        "407c0508",
        "49e24dfc"
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
        "callSetDbIds": [
            "aca00001",
            "aca00002",
            "aca00003"
        ],
        "data": [
            [
                "0|0",
                "1|0",
                "1/1"
            ],
            [
                "0|0",
                "1|0",
                "1/1"
            ],
            [
                "0|0",
                "1|0",
                "1/1"
            ]
        ],
        "expandHomozygotes": true,
        "genotypeFields": [
            {
                "fieldMatrix": [
                    [
                        "48",
                        "48",
                        "43"
                    ],
                    [
                        "49",
                        "3",
                        "41"
                    ],
                    [
                        "21",
                        "2",
                        "35"
                    ]
                ],
                "fieldName": "Genotype Quality",
                "fieldType": "integer"
            }
        ],
        "pagination": [
            {
                "dimension": "VARIANTS",
                "page": 0,
                "pageSize": 500,
                "totalCount": 10000,
                "totalPages": 20
            },
            {
                "dimension": "CALLSETS",
                "page": 4,
                "pageSize": 1000,
                "totalCount": 10000,
                "totalPages": 10
            }
        ],
        "sepPhased": "|",
        "sepUnphased": "/",
        "unknownString": ".",
        "variantSetDbIds": [
            "cfde3944",
            "cfde2077",
            "cfde4424"
        ],
        "variants": [
            {
                "chromosome": "20",
                "end": 24370,
                "ploidy": 2,
                "start": 14370,
                "variantDbId": "feb54257"
            },
            {
                "chromosome": "20",
                "end": 1113696,
                "ploidy": 2,
                "start": 1110696,
                "variantDbId": "feb40355"
            },
            {
                "chromosome": "20",
                "end": 1237567,
                "ploidy": 2,
                "start": 1234567,
                "variantDbId": "feb40323"
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




### Get - /search/variantmatrix/{searchResultsDbId} [GET /brapi/v2/search/variantmatrix/{searchResultsDbId}]

Get the results of a `Calls` search request <br/>
Clients should submit a search request using the corresponding `POST /search/calls` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]||
|data|array[array]||
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|genotypeFields|array[object]||
|fieldMatrix|array[array]||
|fieldName|string||
|fieldType|string||
|pagination|array[object]|Pagination for the matrix|
|dimension|string|the dimension of the matrix being paginated|
|page|integer|the requested page number (zero indexed)|
|pageSize|integer|the maximum number of elements per page in this dimension of the matrix|
|totalCount|integer|The total number of elements that are available on the server and match the requested query parameters.|
|totalPages|integer|The total number of pages of elements available on the server. This should be calculated with the following formula.  <br/>totalPages = CEILING( totalCount / requested_page_size)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantSetDbIds|array[string]||
|variants|array[object]||
|chromosome|string||
|end|integer||
|ploidy|integer||
|start|integer||
|variantDbId|string||


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
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
        "callSetDbIds": [
            "aca00001",
            "aca00002",
            "aca00003"
        ],
        "data": [
            [
                "0|0",
                "1|0",
                "1/1"
            ],
            [
                "0|0",
                "1|0",
                "1/1"
            ],
            [
                "0|0",
                "1|0",
                "1/1"
            ]
        ],
        "expandHomozygotes": true,
        "genotypeFields": [
            {
                "fieldMatrix": [
                    [
                        "48",
                        "48",
                        "43"
                    ],
                    [
                        "49",
                        "3",
                        "41"
                    ],
                    [
                        "21",
                        "2",
                        "35"
                    ]
                ],
                "fieldName": "Genotype Quality",
                "fieldType": "integer"
            }
        ],
        "pagination": [
            {
                "dimension": "VARIANTS",
                "page": 0,
                "pageSize": 500,
                "totalCount": 10000,
                "totalPages": 20
            },
            {
                "dimension": "CALLSETS",
                "page": 4,
                "pageSize": 1000,
                "totalCount": 10000,
                "totalPages": 10
            }
        ],
        "sepPhased": "|",
        "sepUnphased": "/",
        "unknownString": ".",
        "variantSetDbIds": [
            "cfde3944",
            "cfde2077",
            "cfde4424"
        ],
        "variants": [
            {
                "chromosome": "20",
                "end": 24370,
                "ploidy": 2,
                "start": 14370,
                "variantDbId": "feb54257"
            },
            {
                "chromosome": "20",
                "end": 1113696,
                "ploidy": 2,
                "start": 1110696,
                "variantDbId": "feb40355"
            },
            {
                "chromosome": "20",
                "end": 1237567,
                "ploidy": 2,
                "start": 1234567,
                "variantDbId": "feb40323"
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




### Get - /variantmatrix [GET /brapi/v2/variantmatrix{?dimensionVariantPage}{?dimensionVariantPage}{?dimensionVariantPage}{?dimensionVariantPage}{?positionRange}{?germplasmDbId}{?germplasmName}{?germplasmPUI}{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}]

Two dimensional matrix representing the raw contents of a VCF



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]||
|data|array[array]||
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|genotypeFields|array[object]||
|fieldMatrix|array[array]||
|fieldName|string||
|fieldType|string||
|pagination|array[object]|Pagination for the matrix|
|dimension|string|the dimension of the matrix being paginated|
|page|integer|the requested page number (zero indexed)|
|pageSize|integer|the maximum number of elements per page in this dimension of the matrix|
|totalCount|integer|The total number of elements that are available on the server and match the requested query parameters.|
|totalPages|integer|The total number of pages of elements available on the server. This should be calculated with the following formula.  <br/>totalPages = CEILING( totalCount / requested_page_size)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantSetDbIds|array[string]||
|variants|array[object]||
|chromosome|string||
|end|integer||
|ploidy|integer||
|start|integer||
|variantDbId|string||


 

+ Parameters
    + dimensionVariantPage (Optional, ) ... The requested page number for the Variant dimension of the matrix
    + dimensionVariantPage (Optional, ) ... The requested page size for the Variant dimension of the matrix
    + dimensionVariantPage (Optional, ) ... The requested page number for the CallSet dimension of the matrix
    + dimensionVariantPage (Optional, ) ... The requested page size for the CallSet dimension of the matrix
    + positionRange (Optional, ) ... The postion range to search<br/>Uses the format "<chrom>:<start>-<end>" where <chrom> is the chromosome name, <start> is the starting position of the range, and <end> is the ending position of the range
    + germplasmDbId (Optional, ) ... Internal database identifier
    + germplasmName (Optional, ) ... Name of the germplasm
    + germplasmPUI (Optional, ) ... Permanent unique identifier (DOI, URI, etc.)
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurrence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
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
        "callSetDbIds": [
            "aca00001",
            "aca00002",
            "aca00003"
        ],
        "data": [
            [
                "0|0",
                "1|0",
                "1/1"
            ],
            [
                "0|0",
                "1|0",
                "1/1"
            ],
            [
                "0|0",
                "1|0",
                "1/1"
            ]
        ],
        "expandHomozygotes": true,
        "genotypeFields": [
            {
                "fieldMatrix": [
                    [
                        "48",
                        "48",
                        "43"
                    ],
                    [
                        "49",
                        "3",
                        "41"
                    ],
                    [
                        "21",
                        "2",
                        "35"
                    ]
                ],
                "fieldName": "Genotype Quality",
                "fieldType": "integer"
            }
        ],
        "pagination": [
            {
                "dimension": "VARIANTS",
                "page": 0,
                "pageSize": 500,
                "totalCount": 10000,
                "totalPages": 20
            },
            {
                "dimension": "CALLSETS",
                "page": 4,
                "pageSize": 1000,
                "totalCount": 10000,
                "totalPages": 10
            }
        ],
        "sepPhased": "|",
        "sepUnphased": "/",
        "unknownString": ".",
        "variantSetDbIds": [
            "cfde3944",
            "cfde2077",
            "cfde4424"
        ],
        "variants": [
            {
                "chromosome": "20",
                "end": 24370,
                "ploidy": 2,
                "start": 14370,
                "variantDbId": "feb54257"
            },
            {
                "chromosome": "20",
                "end": 1113696,
                "ploidy": 2,
                "start": 1110696,
                "variantDbId": "feb40355"
            },
            {
                "chromosome": "20",
                "end": 1237567,
                "ploidy": 2,
                "start": 1234567,
                "variantDbId": "feb40323"
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

