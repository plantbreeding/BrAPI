
# Group Genotype Matrix Redesign


Genotype Matrix Redesign description 




### Post - /search/calls [POST /brapi/v2/search/calls]

Submit a search request for `Calls`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/calls/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details. 
<br/>
<br/>
<strong>NOTE:</strong> This endpoint uses Token based pagination. Please Review the 
<a target="_blank" href="https://wiki.brapi.org/index.php/Pagination">Pagination documentation</a> for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]|The CallSet to search.|
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|pageToken|string|Used to request a specific page of data to be returned.  Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. |
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantDbIds|array[string]|The Variant to search.|
|variantSetDbIds|array[string]|The VariantSet to search.|


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
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

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
    "pageSize": 1000,
    "pageToken": "33c27874",
    "sepPhased": "~",
    "sepUnphased": "|",
    "unknownString": "-",
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




### Get - /search/calls/{searchResultsDbId} [GET /brapi/v2/search/calls/{searchResultsDbId}{?pageToken}{?pageSize}]

Get the results of a `Calls` search request <br/>
Clients should submit a search request using the corresponding `POST /search/calls` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>
<br/>
<strong>NOTE:</strong> This endpoint uses Token based pagination. Please Review the 
<a target="_blank" href="https://wiki.brapi.org/index.php/Pagination">Pagination documentation</a> for additional implementation details.



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
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
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




### Get - /variantmatrix1 [GET /brapi/v2/variantmatrix1{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?pageSize}]

Two dimensional matrix representing the raw contents of a VCF



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]||
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|vcfHeaders|array[string]||


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
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
            [
                "#CHROM",
                "POS",
                "ID",
                "REF",
                "ALT",
                "QUAL",
                "FILTER",
                "INFO",
                "FORMAT",
                "aca00001",
                "aca00002",
                "aca00003"
            ],
            [
                "20",
                "14370",
                "feb54257",
                "G",
                "A",
                "29",
                "PASS",
                "NS=3;DP=14;AF=0.5;DB;H2",
                "GT:GQ:DP:HQ",
                "0|0:48:1:51,51",
                "1|0:48:8:51,51",
                "1/1:43:5:.,."
            ],
            [
                "20",
                "17330",
                "feb40323",
                "T",
                "A",
                "3",
                "q10",
                "NS=3;DP=11;AF=0.017",
                "GT:GQ:DP:HQ",
                "0|0:49:3:58,50",
                "0|1:3:5:65,3",
                "0/0:41:3"
            ],
            [
                "20",
                "1110696",
                "feb40355",
                "A",
                "G,T",
                "67",
                "PASS",
                "NS=2;DP=10;AF=0.333,0.667;AA=T;DB",
                "GT:GQ:DP:HQ",
                "1|2:21:6:23,27",
                "2|1:2:0:18,2",
                "2/2:35:4"
            ]
        ],
        "expandHomozygotes": true,
        "sepPhased": "~",
        "sepUnphased": "|",
        "unknownString": "-",
        "vcfHeaders": [
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null,
            null
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




### Get - /variantmatrix2 [GET /brapi/v2/variantmatrix2{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?pageSize}]

Two dimensional matrix representing the raw contents of a VCF



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]||
|data|array[object]||
|row|array[string]||
|variantDbId|string||
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|format|string||
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
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
            {
                "row": [
                    "0|0:48:1:51,51",
                    "1|0:48:8:51,51",
                    "1/1:43:5:.,."
                ],
                "variantDbId": "feb54257"
            },
            {
                "row": [
                    "0|0:48:1:51,51",
                    "1|0:48:8:51,51",
                    "1/1:43:5:.,."
                ],
                "variantDbId": "feb40355"
            },
            {
                "row": [
                    "0|0:48:1:51,51",
                    "1|0:48:8:51,51",
                    "1/1:43:5:.,."
                ],
                "variantDbId": "feb40323"
            }
        ],
        "expandHomozygotes": true,
        "format": "GT:GQ:DP:HQ",
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




### Get - /variantmatrix3 [GET /brapi/v2/variantmatrix3{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?pageSize}]

Two dimensional matrix representing the raw contents of a VCF



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]||
|data|array[array]||
|dataMasks|array[object]||
|mask|array[array]||
|maskType|string||
|expandHomozygotes|boolean|Should homozygotes be expanded (true) or collapsed into a single occurrence (false)|
|sepPhased|string|The string used as a separator for phased allele calls.|
|sepUnphased|string|The string used as a separator for unphased allele calls.|
|unknownString|string|The string used as a representation for missing data.|
|variantDbIds|array[string]||


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
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
        "dataMasks": [
            {
                "mask": [
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
                "maskType": "Genotype Quality"
            }
        ],
        "expandHomozygotes": true,
        "sepPhased": "~",
        "sepUnphased": "|",
        "unknownString": "-",
        "variantDbIds": [
            "feb54257",
            "feb40355",
            "feb40323"
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




### Get - /variantmatrix4 [GET /brapi/v2/variantmatrix4{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?pageSize}]

Two dimensional matrix representing the raw contents of a VCF



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|callSetDbIds|array[string]||
|data|array[array]||
|dataMasks|array[object]||
|mask|array[array]||
|maskType|string||
|variantDbIds|array[string]||


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
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
                515,
                1027,
                1028
            ],
            [
                515,
                1027,
                1028
            ],
            [
                515,
                1027,
                1028
            ]
        ],
        "dataMasks": [
            {
                "mask": [
                    [
                        48,
                        48,
                        43
                    ],
                    [
                        49,
                        3,
                        41
                    ],
                    [
                        21,
                        2,
                        35
                    ]
                ],
                "maskType": "Genotype Quality"
            }
        ],
        "variantDbIds": [
            "feb54257",
            "feb40355",
            "feb40323"
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

