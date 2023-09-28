# Group Allele Matrix

The Allele Matrix object is used to describe a matrix of genotyping results. This 2d array of data reduces the overall size of the response for larger datasets, when compared to the Calls endpoints. This makes genotype data retrieval faster and easier. 




### Get - /allelematrix [GET /brapi/v2/allelematrix{?dimensionVariantPage}{?dimensionVariantPageSize}{?dimensionCallSetPage}{?dimensionCallSetPageSize}{?preview}{?dataMatrixNames}{?dataMatrixAbbreviations}{?positionRange}{?germplasmDbId}{?germplasmName}{?germplasmPUI}{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}]

Use this endpoint to retrieve a two dimensional matrix of genotype data. The response structure is based on the VCF file format, 
but the search and filter parameters give the ability to slice and merge data sets. This allows the user to return the subset of data they are interested in, 
without having to download the entire genotype file.
<br/>Each row of data (outer array) corresponds to a variant definition, and each column (inner array) corresponds to a callSet.    



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.</td></tr>
<tr><td><span style="font-weight:bold;">dataMatrices</span></td><td>array[object]</td><td>The 'dataMatrices' are an array of matrix objects that hold the allele data and associated metadata. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrix</span></td><td>array[array]</td><td>The two dimensional array of data, providing the allele matrix or an additional layer of metadata associated with each genotype value. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrixAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this data matrix. These codes should match the VCF standard when possible and the key word "GT" is reserved for the allele matrix. Examples of other metadata matrices include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrixName</span></td><td>string</td><td>The name of the field represented in this data matrix. The key word "Genotype" is reserved for the allele matrix. Examples of other metadata matrices include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this data matrix. This is intended to help parse the data out of JSON.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
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
</table>


 

+ Parameters
    + dimensionVariantPage (Optional, integer) ... The requested page number for the Variant dimension of the matrix
    + dimensionVariantPageSize (Optional, integer) ... The requested page size for the Variant dimension of the matrix
    + dimensionCallSetPage (Optional, integer) ... The requested page number for the CallSet dimension of the matrix
    + dimensionCallSetPageSize (Optional, integer) ... The requested page size for the CallSet dimension of the matrix
    + preview (Optional, boolean) ... Default Value = false<br/>If 'preview' is set to true, then the server should return with the "dataMatrices" field as null or empty. All other data fields should be returned normally. This is intended to be a preview and give the client a sense of how large the matrix returned will be<br/>If 'preview' is set to false or not set (default), then the server should return all the matrix data as requested.
    + dataMatrixNames (Optional, string) ... "dataMatrixNames" is a comma seperated list of names (ie 'Genotype, Read Depth' etc). This list controls which data matrices are returned in the response.<br> This maps to a FORMAT field in the VCF file standard.
    + dataMatrixAbbreviations (Optional, string) ... "dataMatrixAbbreviations" is a comma seperated list of abbreviations (ie 'GT, RD' etc). This list controls which data matrices are returned in the response.<br> This maps to a FORMAT field in the VCF file standard.
    + positionRange (Optional, string) ... The postion range to search<br/> Uses the format "contig:start-end" where "contig" is the chromosome or contig name, "start" is  the starting position of the range, and "end" is the ending position of the range<br> Example: CRHOM_1:12000-14000
    + germplasmDbId (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + germplasmName (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` by its human readable name. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + germplasmPUI (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` by its global permanent unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + callSetDbId (Optional, string) ... The ID which uniquely identifies a `CallSet` within the given database server
    + variantDbId (Optional, string) ... The ID which uniquely identifies a `Variant` within the given database server
    + variantSetDbId (Optional, string) ... The ID which uniquely identifies a `VariantSet` within the given database server
    + expandHomozygotes (Optional, boolean) ... Should homozygotes be expanded (true) or collapsed into a single occurrence (false)
    + unknownString (Optional, string) ... The string to use as a representation for missing data
    + sepPhased (Optional, string) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, string) ... The string to use as a separator for unphased allele calls
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
        "dataMatrices": [
            {
                "dataMatrix": [
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
                "dataMatrixAbbreviation": "GT",
                "dataMatrixName": "Genotype",
                "dataType": "string"
            },
            {
                "dataMatrix": [
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
                "dataMatrixAbbreviation": "GQ",
                "dataMatrixName": "Genotype Quality",
                "dataType": "integer"
            }
        ],
        "expandHomozygotes": true,
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




### Post - /search/allelematrix [POST /brapi/v2/search/allelematrix]

Use this endpoint to retrieve a two dimensional matrix of genotype data. The response structure is based on the VCF format, but the search and filter parameters give the ability to slice and merge data sets. This allows the user to return the subset of data they are interested in, without having to download the entire genotype file.
<br/>Each row of data (outer array) corresponds to a variant definition, and each column (inner array) corresponds to a callSet. 
<br/>Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. If a server needs more time to process the request, it might respond with a `searchResultsDbId`. Use the corresponding `GET /search/allelematrix/{searchResultsDbId}` to retrieve the results of the search. 
<br/>Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `CallSets` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">dataMatrixAbbreviations</span></td><td>array[string]</td><td>`dataMatrixAbbreviations` is a comma seperated list of abbreviations (ie 'GT', 'RD' etc). This list controls which data matrices are returned in the response.</td></tr>
<tr><td><span style="font-weight:bold;">dataMatrixNames</span></td><td>array[string]</td><td>`dataMatrixNames` is a list of names (ie 'Genotype', 'Read Depth' etc). This list controls which data matrices are returned in the response.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `Germplasm` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>A list of human readable `Germplasm` names</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUIs</span></td><td>array[string]</td><td>A list of permanent unique identifiers associated with `Germplasm`</td></tr>
<tr><td><span style="font-weight:bold;">pagination</span></td><td>array[object]</td><td>Pagination for the matrix</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.dimension</span></td><td>string</td><td>the dimension of the matrix being paginated</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.page</span></td><td>integer</td><td>the requested page number (zero indexed)</td></tr>
<tr><td>pagination<br><span style="font-weight:bold;margin-left:5px">.pageSize</span></td><td>integer</td><td>the maximum number of elements per page in this dimension of the matrix</td></tr>
<tr><td><span style="font-weight:bold;">positionRanges</span></td><td>array[string]</td><td>The postion range to search <br/> Uses the format "<chrom>:<start>-<end>" where <chrom> is the chromosome name, <start> is  the starting position of the range, and <end> is the ending position of the range</td></tr>
<tr><td><span style="font-weight:bold;">preview</span></td><td>boolean</td><td>Default Value = false <br/> If 'preview' is set to true, then the server should only return the lists of 'callSetDbIds',  'variantDbIds', and 'variantSetDbIds'. The server should not return any matrix data. This is intended to be a preview and give the client a sense of how large the matrix returned will be <br/> If 'preview' is set to false or not set (default), then the server should return all the matrix data as requested.</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `Samples` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `Variants` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `VariantSets` within the given database server</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.</td></tr>
<tr><td><span style="font-weight:bold;">dataMatrices</span></td><td>array[object]</td><td>The 'dataMatrices' are an array of matrix objects that hold the allele data and associated metadata. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrix</span></td><td>array[array]</td><td>The two dimensional array of data, providing the allele matrix or an additional layer of metadata associated with each genotype value. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrixAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this data matrix. These codes should match the VCF standard when possible and the key word "GT" is reserved for the allele matrix. Examples of other metadata matrices include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrixName</span></td><td>string</td><td>The name of the field represented in this data matrix. The key word "Genotype" is reserved for the allele matrix. Examples of other metadata matrices include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this data matrix. This is intended to help parse the data out of JSON.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
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
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "a03202ec",
        "274e4f63"
    ],
    "dataMatrixAbbreviations": [
        "GT",
        "RD"
    ],
    "dataMatrixNames": [
        "Genotype",
        "Read Depth"
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
        "dataMatrices": [
            {
                "dataMatrix": [
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
                "dataMatrixAbbreviation": "GT",
                "dataMatrixName": "Genotype",
                "dataType": "string"
            },
            {
                "dataMatrix": [
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
                "dataMatrixAbbreviation": "GQ",
                "dataMatrixName": "Genotype Quality",
                "dataType": "integer"
            }
        ],
        "expandHomozygotes": true,
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




### Get - /search/allelematrix/{searchResultsDbId} [GET /brapi/v2/search/allelematrix/{searchResultsDbId}]

Use this endpoint to retrieve a two dimensional matrix of genotype data. The response structure is based on the VCF format, but the search and filter parameters give the ability to slice and merge data sets. This allows the user to return the subset of data they are interested in, without having to download the entire genotype file.
<br/>Each row of data (outer array) corresponds to a variant definition, and each column (inner array) corresponds to a callSet. 
<br/>Clients should submit a search request using the corresponding `POST /search/allelematrix` endpoint. Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. If a server needs more time to process the request, it might respond with a `searchResultsDbId`. Use this endpoint to retrieve the results of the search. 
<br/>Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A list of unique identifiers for the CallSets contained in the matrix response. This array should match the ordering for columns in the matrix. A CallSet is a unique combination of a Sample and a sequencing event. CallSets often have a 1-to-1 relationship with Samples, but this is not always the case.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A list of unique identifiers for the VariantSets contained in the matrix response. A VariantSet is a data set originating from a sequencing event. Often, users will only be interested in data from a single VariantSet, but in some cases a user might be interested in a matrix with data from multiple VariantSets.</td></tr>
<tr><td><span style="font-weight:bold;">dataMatrices</span></td><td>array[object]</td><td>The 'dataMatrices' are an array of matrix objects that hold the allele data and associated metadata. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrix</span></td><td>array[array]</td><td>The two dimensional array of data, providing the allele matrix or an additional layer of metadata associated with each genotype value. Each matrix should be the same size and orientation, aligned with the "callSetDbIds" as columns and the "variantDbIds" as rows.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrixAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this data matrix. These codes should match the VCF standard when possible and the key word "GT" is reserved for the allele matrix. Examples of other metadata matrices include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataMatrixName</span></td><td>string</td><td>The name of the field represented in this data matrix. The key word "Genotype" is reserved for the allele matrix. Examples of other metadata matrices include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>dataMatrices<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this data matrix. This is intended to help parse the data out of JSON.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
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
</table>


 

+ Parameters
    + searchResultsDbId (Required, string) ... Unique identifier which references the search results
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
        "dataMatrices": [
            {
                "dataMatrix": [
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
                "dataMatrixAbbreviation": "GT",
                "dataMatrixName": "Genotype",
                "dataType": "string"
            },
            {
                "dataMatrix": [
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
                "dataMatrixAbbreviation": "GQ",
                "dataMatrixName": "Genotype Quality",
                "dataType": "integer"
            }
        ],
        "expandHomozygotes": true,
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

