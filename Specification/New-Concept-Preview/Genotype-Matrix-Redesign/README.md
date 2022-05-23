
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">callSetDbId</span></td><td>string</td><td>The ID of the call set this variant call belongs to. <br/>If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet`  is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td><span style="font-weight:bold;">callSetName</span></td><td>string</td><td>The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td><span style="font-weight:bold;">genotype</span></td><td>string</td><td>The value of this genotype</td></tr>
<tr><td><span style="font-weight:bold;">genotypeFields</span></td><td>array[object]</td><td>Genotype fields are additional layers of metadata associated with each genotype.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldValue</span></td><td>string</td><td>The additional metadata value associated with this genotype call</td></tr>
<tr><td><span style="font-weight:bold;">phaseSet</span></td><td>string</td><td>If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string</td><td>The ID of the Variant this call belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantName</span></td><td>string</td><td>The name of the Variant this call belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>string</td><td>The ID of the Variant Set this call belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetName</span></td><td>string</td><td>The name of the Variant Set this call belongs to.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]</td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetDbId</span></td><td>string</td><td>The ID of the call set this variant call belongs to. <br/>If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet`  is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetName</span></td><td>string</td><td>The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype</span></td><td>string</td><td>The value of this genotype</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeFields</span></td><td>array[object]</td><td>Genotype fields are additional layers of metadata associated with each genotype.</td></tr>
<tr><td>data<br>.genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>data<br>.genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td>data<br>.genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>data<br>.genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldValue</span></td><td>string</td><td>The additional metadata value associated with this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.phaseSet</span></td><td>string</td><td>If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The ID of the Variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantName</span></td><td>string</td><td>The name of the Variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetDbId</span></td><td>string</td><td>The ID of the Variant Set this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetName</span></td><td>string</td><td>The name of the Variant Set this call belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "callSetDbId": "16466f55",
        "callSetName": "Sample_123_DNA_Run_456",
        "genotype": "1/1",
        "genotypeFields": [
            {
                "fieldAbbreviation": "GQ",
                "fieldName": "Genotype Quality",
                "fieldType": "integer",
                "fieldValue": "45.2"
            }
        ],
        "phaseSet": "6410afc5",
        "variantDbId": "538c8ecf",
        "variantName": "Marker A",
        "variantSetDbId": "8c8ecf53",
        "variantSetName": "Marker A"
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
                "genotype": "1/1",
                "genotypeFields": [
                    {
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality",
                        "fieldType": "integer",
                        "fieldValue": "45.2"
                    }
                ],
                "phaseSet": "6410afc5",
                "variantDbId": "538c8ecf",
                "variantName": "Marker A",
                "variantSetDbId": "8c8ecf53",
                "variantSetName": "Marker A"
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

Use this endpoint to retrieve a two dimensional matrix of genotype data. The response structure is based on the VCF format, with the enhanced ability to slice and merge data sets. This allows the user to return the subset of data they are interested in, without having to download the entire genotype file.
<br/>Each row of data (outer array) corresponds to a variant definition, and each column (inner array) corresponds to a callSet. 
<br/>Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. If a server needs more time to process the request, it might respond with a `searchResultsDbId`. Use the corresponding `GET /search/calls/{searchResultsDbId}` to retrieve the results of the search. 
<br/>Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>The CallSet to search.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">genotypeFields</span></td><td>array[string]</td><td>If `includeGenotypeFields` is true and `preview` is false, this array controls which Genotype Field matrices are returned. Each Genotype Field matrix can be identified by its name or abbreviation.</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>The germplasm to search</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>The germplasm to search</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUIs</span></td><td>array[string]</td><td>The germplasm to search</td></tr>
<tr><td><span style="font-weight:bold;">includeGenotypeFields</span></td><td>boolean</td><td>Default Value = true <br/> If 'includeGenotypeFields' is set to false, then the `genotypeFields` array should be omitted or returned null in the response <br/> If 'includeGenotypeFields' is set to true or not set (default), then the server should return all `genotypeFields` metadata it has available</td></tr>
<tr><td><span style="font-weight:bold;">pagination</span></td><td>array[object]</td><td>Pagination for the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.dimension</span></td><td>string</td><td>the dimension of the matrix being paginated</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.page</span></td><td>integer</td><td>the requested page number (zero indexed)</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.pageSize</span></td><td>integer</td><td>the maximum number of elements per page in this dimension of the matrix</td></tr>
<tr><td><span style="font-weight:bold;">positionRanges</span></td><td>array[string]</td><td>The postion range to search <br/> Uses the format "<chrom>:<start>-<end>" where <chrom> is the chromosome name, <start> is  the starting position of the range, and <end> is the ending position of the range</td></tr>
<tr><td><span style="font-weight:bold;">preview</span></td><td>boolean</td><td>Default Value = false <br/> If 'preview' is set to true, then the server should only return the lists of 'callSetDbIds',  'variantDbIds', and 'variantSetDbIds'. The server should not return any matrix data. This is intended to be a preview and give the client a sense of how large the matrix returned will be <br/> If 'preview' is set to false or not set (default), then the server should return all the matrix data as requested.</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbIds</span></td><td>array[string]</td><td>The samples to search</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>The Variant to search.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>The VariantSet to search.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">genotypeFields</span></td><td>array[object]</td><td>Genotype fields are additional layers of metadata associated with each genotype. They are organized here as a collection of additional matrices the same size and orientation as the genotype matrix.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field matrix. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldMatrix</span></td><td>array[array]</td><td>The Genotype Field matrix data, providing an additional layer of metadata associated with each genotype value. This matrix should be the same size and orientation as the genotype matrix.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field matrix. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldType</span></td><td>string</td><td>The type of field represented in this Genotype Field matrix. This is intended to help parse the data out of JSON.</td></tr>
<tr><td><span style="font-weight:bold;">genotypeMatrix</span></td><td>array[array]</td><td>The whole genotype matrix, as a two dimensional array.</td></tr>
<tr><td><span style="font-weight:bold;">pagination</span></td><td>array[object]</td><td>Pagination for the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.dimension</span></td><td>string</td><td>The dimension of the matrix being paginated</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.page</span></td><td>integer</td><td>the requested page number (zero indexed)</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.pageSize</span></td><td>integer</td><td>the maximum number of elements per page in this dimension of the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.totalCount</span></td><td>integer</td><td>The total number of elements that are available on the server and match the requested query parameters.</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.totalPages</span></td><td>integer</td><td>The total number of pages of elements available on the server. This should be calculated with the following formula.  <br/>totalPages = CEILING( totalCount / requested_page_size)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the Variants contained in the matrix response. This array should match the ordering for rows in the matrix.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.</td></tr>
<tr><td><span style="font-weight:bold;">variants</span></td><td>array[object]</td><td>A list of unique identifiers and other metadata for the Variants contained in the matrix response. This is a subset of fields from the `GET /variant` data model. These metadata fields were chosen to mimic the metadata in a VCF file.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.alternateBases</span></td><td>array[string]</td><td>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.contig</span></td><td>string</td><td>The chromosome or linkage group name where this variant exists</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.end</span></td><td>integer</td><td>The end position of this variant</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.referenceBases</span></td><td>string</td><td>The reference bases for this variant. They start at the given start position.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.start</span></td><td>integer</td><td>The start position of this variant</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The unique identifier of a Variant</td></tr>
</table>


 

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
    "genotypeFields": [
        "Read Depth",
        "GQ"
    ],
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
    "includeGenotypeFields": false,
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
        "expandHomozygotes": true,
        "genotypeFields": [
            {
                "fieldAbbreviation": "GQ",
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
        "genotypeMatrix": [
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
        "variantDbIds": [
            "feb54257",
            "feb40355",
            "feb40323"
        ],
        "variantSetDbIds": [
            "cfde3944",
            "cfde2077",
            "cfde4424"
        ],
        "variants": [
            {
                "alternateBases": [
                    "A"
                ],
                "contig": "CHROM_20",
                "end": 24370,
                "referenceBases": "G",
                "start": 14370,
                "variantDbId": "feb54257"
            },
            {
                "alternateBases": [
                    "G",
                    "T"
                ],
                "contig": "CHROM_20",
                "end": 1113696,
                "referenceBases": "A",
                "start": 1110696,
                "variantDbId": "feb40355"
            },
            {
                "alternateBases": [
                    "G",
                    "GTCA"
                ],
                "contig": "CHROM_20",
                "end": 1237567,
                "referenceBases": "GTC",
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

Use this endpoint to retrieve a two dimensional matrix of genotype data. The response structure is based on the VCF format, with the enhanced ability to slice and merge data sets. This allows the user to return the subset of data they are interested in, without having to download the entire genotype file.
<br/>Each row of data (outer array) corresponds to a variant definition, and each column (inner array) corresponds to a callSet. 
<br/>Clients should submit a search request using the corresponding `POST /search/variantmatrix` endpoint. Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. If a server needs more time to process the request, it might respond with a `searchResultsDbId`. Use this endpoint to retrieve the results of the search. 
<br/>Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">genotypeFields</span></td><td>array[object]</td><td>Genotype fields are additional layers of metadata associated with each genotype. They are organized here as a collection of additional matrices the same size and orientation as the genotype matrix.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field matrix. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldMatrix</span></td><td>array[array]</td><td>The Genotype Field matrix data, providing an additional layer of metadata associated with each genotype value. This matrix should be the same size and orientation as the genotype matrix.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field matrix. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldType</span></td><td>string</td><td>The type of field represented in this Genotype Field matrix. This is intended to help parse the data out of JSON.</td></tr>
<tr><td><span style="font-weight:bold;">genotypeMatrix</span></td><td>array[array]</td><td>The whole genotype matrix, as a two dimensional array.</td></tr>
<tr><td><span style="font-weight:bold;">pagination</span></td><td>array[object]</td><td>Pagination for the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.dimension</span></td><td>string</td><td>The dimension of the matrix being paginated</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.page</span></td><td>integer</td><td>the requested page number (zero indexed)</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.pageSize</span></td><td>integer</td><td>the maximum number of elements per page in this dimension of the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.totalCount</span></td><td>integer</td><td>The total number of elements that are available on the server and match the requested query parameters.</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.totalPages</span></td><td>integer</td><td>The total number of pages of elements available on the server. This should be calculated with the following formula.  <br/>totalPages = CEILING( totalCount / requested_page_size)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the Variants contained in the matrix response. This array should match the ordering for rows in the matrix.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.</td></tr>
<tr><td><span style="font-weight:bold;">variants</span></td><td>array[object]</td><td>A list of unique identifiers and other metadata for the Variants contained in the matrix response. This is a subset of fields from the `GET /variant` data model. These metadata fields were chosen to mimic the metadata in a VCF file.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.alternateBases</span></td><td>array[string]</td><td>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.contig</span></td><td>string</td><td>The chromosome or linkage group name where this variant exists</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.end</span></td><td>integer</td><td>The end position of this variant</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.referenceBases</span></td><td>string</td><td>The reference bases for this variant. They start at the given start position.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.start</span></td><td>integer</td><td>The start position of this variant</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The unique identifier of a Variant</td></tr>
</table>


 

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
        "expandHomozygotes": true,
        "genotypeFields": [
            {
                "fieldAbbreviation": "GQ",
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
        "genotypeMatrix": [
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
        "variantDbIds": [
            "feb54257",
            "feb40355",
            "feb40323"
        ],
        "variantSetDbIds": [
            "cfde3944",
            "cfde2077",
            "cfde4424"
        ],
        "variants": [
            {
                "alternateBases": [
                    "A"
                ],
                "contig": "CHROM_20",
                "end": 24370,
                "referenceBases": "G",
                "start": 14370,
                "variantDbId": "feb54257"
            },
            {
                "alternateBases": [
                    "G",
                    "T"
                ],
                "contig": "CHROM_20",
                "end": 1113696,
                "referenceBases": "A",
                "start": 1110696,
                "variantDbId": "feb40355"
            },
            {
                "alternateBases": [
                    "G",
                    "GTCA"
                ],
                "contig": "CHROM_20",
                "end": 1237567,
                "referenceBases": "GTC",
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




### Get - /variantmatrix [GET /brapi/v2/variantmatrix{?dimensionVariantPage}{?dimensionVariantPageSize}{?dimensionCallSetPage}{?dimensionCallSetPageSize}{?positionRange}{?germplasmDbId}{?germplasmName}{?germplasmPUI}{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}]

Use this endpoint to retrieve a two dimensional matrix of genotype data. The response structure is based on the VCF format, with the enhanced ability to slice and merge data sets. This allows the user to return the subset of data they are interested in, without having to download the entire genotype file.
<br/>Each row of data (outer array) corresponds to a variant definition, and each column (inner array) corresponds to a callSet.    



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">genotypeFields</span></td><td>array[object]</td><td>Genotype fields are additional layers of metadata associated with each genotype. They are organized here as a collection of additional matrices the same size and orientation as the genotype matrix.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field matrix. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldMatrix</span></td><td>array[array]</td><td>The Genotype Field matrix data, providing an additional layer of metadata associated with each genotype value. This matrix should be the same size and orientation as the genotype matrix.</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field matrix. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td>genotypeFields<br><span style="font-weight:bold;margin-left:5px">.fieldType</span></td><td>string</td><td>The type of field represented in this Genotype Field matrix. This is intended to help parse the data out of JSON.</td></tr>
<tr><td><span style="font-weight:bold;">genotypeMatrix</span></td><td>array[array]</td><td>The whole genotype matrix, as a two dimensional array.</td></tr>
<tr><td><span style="font-weight:bold;">pagination</span></td><td>array[object]</td><td>Pagination for the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.dimension</span></td><td>string</td><td>The dimension of the matrix being paginated</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.page</span></td><td>integer</td><td>the requested page number (zero indexed)</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.pageSize</span></td><td>integer</td><td>the maximum number of elements per page in this dimension of the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.totalCount</span></td><td>integer</td><td>The total number of elements that are available on the server and match the requested query parameters.</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.totalPages</span></td><td>integer</td><td>The total number of pages of elements available on the server. This should be calculated with the following formula.  <br/>totalPages = CEILING( totalCount / requested_page_size)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the Variants contained in the matrix response. This array should match the ordering for rows in the matrix.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.</td></tr>
<tr><td><span style="font-weight:bold;">variants</span></td><td>array[object]</td><td>A list of unique identifiers and other metadata for the Variants contained in the matrix response. This is a subset of fields from the `GET /variant` data model. These metadata fields were chosen to mimic the metadata in a VCF file.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.alternateBases</span></td><td>array[string]</td><td>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.contig</span></td><td>string</td><td>The chromosome or linkage group name where this variant exists</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.end</span></td><td>integer</td><td>The end position of this variant</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.referenceBases</span></td><td>string</td><td>The reference bases for this variant. They start at the given start position.</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.start</span></td><td>integer</td><td>The start position of this variant</td></tr>
<tr><td>variants<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The unique identifier of a Variant</td></tr>
</table>


 

+ Parameters
    + dimensionVariantPage (Optional, ) ... The requested page number for the Variant dimension of the matrix
    + dimensionVariantPageSize (Optional, ) ... The requested page size for the Variant dimension of the matrix
    + dimensionCallSetPage (Optional, ) ... The requested page number for the CallSet dimension of the matrix
    + dimensionCallSetPageSize (Optional, ) ... The requested page size for the CallSet dimension of the matrix
    + positionRange (Optional, ) ... The postion range to search<br/>Uses the format "contig:start-end" where "contig" is the chromosome or contig name, "start" is the starting position of the range, and "end" is the ending position of the range
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
        "expandHomozygotes": true,
        "genotypeFields": [
            {
                "fieldAbbreviation": "GQ",
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
        "genotypeMatrix": [
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
        "variantDbIds": [
            "feb54257",
            "feb40355",
            "feb40323"
        ],
        "variantSetDbIds": [
            "cfde3944",
            "cfde2077",
            "cfde4424"
        ],
        "variants": [
            {
                "alternateBases": [
                    "A"
                ],
                "contig": "CHROM_20",
                "end": 24370,
                "referenceBases": "G",
                "start": 14370,
                "variantDbId": "feb54257"
            },
            {
                "alternateBases": [
                    "G",
                    "T"
                ],
                "contig": "CHROM_20",
                "end": 1113696,
                "referenceBases": "A",
                "start": 1110696,
                "variantDbId": "feb40355"
            },
            {
                "alternateBases": [
                    "G",
                    "GTCA"
                ],
                "contig": "CHROM_20",
                "end": 1237567,
                "referenceBases": "GTC",
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

