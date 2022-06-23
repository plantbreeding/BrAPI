# Group Calls

From the GA4GH Variants specification:

A Call encodes the genotype of an individual with respect to a variant, as determined by some analysis of experimental data.




### Get - /calls [GET /brapi/v2/calls{?callSetDbId}{?variantDbId}{?variantSetDbId}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?page}{?pageSize}]

Gets a filtered list of `Call` JSON objects.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]</td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetDbId</span></td><td>string</td><td>The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetName</span></td><td>string</td><td>The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype</span></td><td>object</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>`ListValue` is a wrapper around a repeated field of values. <br>The JSON representation for `ListValue` is JSON array.</td></tr>
<tr><td>data<br>.genotype<br><span style="font-weight:bold;margin-left:5px">.values</span></td><td>array</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>Repeated field of dynamically typed values.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeMetadata</span></td><td>array[object]</td><td>Genotype Metadata are additional layers of metadata associated with each genotype.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldValue</span></td><td>string</td><td>The additional metadata value associated with this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeValue</span></td><td>string</td><td>The value of this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype_likelihood</span></td><td>array[number]</td><td>**Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491              <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.phaseSet</span></td><td>string</td><td>If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The ID of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantName</span></td><td>string</td><td>The name of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetDbId</span></td><td>string</td><td>The unique identifier for a VariantSet</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
</table>


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID which uniquely identifies a `CallSet` within the given database server
    + variantDbId (Optional, ) ... The ID which uniquely identifies a `Variant` within the given database server
    + variantSetDbId (Optional, ) ... The ID which uniquely identifies a `VariantSet` within the given database server
    + expandHomozygotes (Optional, ) ... Should homozygotes be expanded (true) or collapsed into a single occurrence (false)
    + unknownString (Optional, ) ... The string to use as a representation for missing data
    + sepPhased (Optional, ) ... The string to use as a separator for phased allele calls
    + sepUnphased (Optional, ) ... The string to use as a separator for unphased allele calls
    + pageToken (Optional, ) ... **Deprecated in v2.1** Please use `page`. Github issue number #451 <br> Used to request a specific page of data to be returned.<br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. 
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
                "callSetDbId": "16466f55",
                "callSetName": "Sample_123_DNA_Run_456",
                "genotype": {
                    "values": [
                        "AA"
                    ]
                },
                "genotypeMetadata": [
                    {
                        "dataType": "integer",
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality",
                        "fieldValue": "45.2"
                    }
                ],
                "genotypeValue": "1/1",
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
<tr><td><span style="font-weight:bold;">callSetDbId</span></td><td>string</td><td>The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td><span style="font-weight:bold;">callSetName</span></td><td>string</td><td>The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td><span style="font-weight:bold;">genotype</span></td><td>object</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>`ListValue` is a wrapper around a repeated field of values. <br>The JSON representation for `ListValue` is JSON array.</td></tr>
<tr><td>genotype<br><span style="font-weight:bold;margin-left:5px">.values</span></td><td>array</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>Repeated field of dynamically typed values.</td></tr>
<tr><td><span style="font-weight:bold;">genotypeMetadata</span></td><td>array[object]</td><td>Genotype Metadata are additional layers of metadata associated with each genotype.</td></tr>
<tr><td>genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldValue</span></td><td>string</td><td>The additional metadata value associated with this genotype call</td></tr>
<tr><td><span style="font-weight:bold;">genotypeValue</span></td><td>string</td><td>The value of this genotype call</td></tr>
<tr><td><span style="font-weight:bold;">genotype_likelihood</span></td><td>array[number]</td><td>**Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491              <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.</td></tr>
<tr><td><span style="font-weight:bold;">phaseSet</span></td><td>string</td><td>If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string</td><td>The ID of the variant this call belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantName</span></td><td>string</td><td>The name of the variant this call belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>string</td><td>The unique identifier for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]</td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetDbId</span></td><td>string</td><td>The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetName</span></td><td>string</td><td>The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype</span></td><td>object</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>`ListValue` is a wrapper around a repeated field of values. <br>The JSON representation for `ListValue` is JSON array.</td></tr>
<tr><td>data<br>.genotype<br><span style="font-weight:bold;margin-left:5px">.values</span></td><td>array</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>Repeated field of dynamically typed values.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeMetadata</span></td><td>array[object]</td><td>Genotype Metadata are additional layers of metadata associated with each genotype.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldValue</span></td><td>string</td><td>The additional metadata value associated with this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeValue</span></td><td>string</td><td>The value of this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype_likelihood</span></td><td>array[number]</td><td>**Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491              <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.phaseSet</span></td><td>string</td><td>If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The ID of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantName</span></td><td>string</td><td>The name of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetDbId</span></td><td>string</td><td>The unique identifier for a VariantSet</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
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
        "genotype": {
            "values": [
                "AA"
            ]
        },
        "genotypeMetadata": [
            {
                "dataType": "integer",
                "fieldAbbreviation": "GQ",
                "fieldName": "Genotype Quality",
                "fieldValue": "45.2"
            }
        ],
        "genotypeValue": "1/1",
        "genotype_likelihood": [
            1.0
        ],
        "phaseSet": "6410afc5",
        "variantDbId": "538c8ecf",
        "variantName": "Marker A",
        "variantSetDbId": "87a6ac1e",
        "variantSetName": "Maize QC DataSet 002334"
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
                "callSetDbId": "16466f55",
                "callSetName": "Sample_123_DNA_Run_456",
                "genotype": {
                    "values": [
                        "AA"
                    ]
                },
                "genotypeMetadata": [
                    {
                        "dataType": "integer",
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality",
                        "fieldValue": "45.2"
                    }
                ],
                "genotypeValue": "1/1",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `CallSets` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">pageToken</span></td><td>string</td><td>**Deprecated in v2.1** Please use `page`. Github issue number #451  <br>Used to request a specific page of data to be returned. <br>Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. </td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `Variant` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `VariantSets` within the given database server</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]</td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetDbId</span></td><td>string</td><td>The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetName</span></td><td>string</td><td>The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype</span></td><td>object</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>`ListValue` is a wrapper around a repeated field of values. <br>The JSON representation for `ListValue` is JSON array.</td></tr>
<tr><td>data<br>.genotype<br><span style="font-weight:bold;margin-left:5px">.values</span></td><td>array</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>Repeated field of dynamically typed values.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeMetadata</span></td><td>array[object]</td><td>Genotype Metadata are additional layers of metadata associated with each genotype.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldValue</span></td><td>string</td><td>The additional metadata value associated with this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeValue</span></td><td>string</td><td>The value of this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype_likelihood</span></td><td>array[number]</td><td>**Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491              <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.phaseSet</span></td><td>string</td><td>If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The ID of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantName</span></td><td>string</td><td>The name of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetDbId</span></td><td>string</td><td>The unique identifier for a VariantSet</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
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
    "page": 0,
    "pageSize": 1000,
    "pageToken": "33c27874",
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
                "genotypeMetadata": [
                    {
                        "dataType": "integer",
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality",
                        "fieldValue": "45.2"
                    }
                ],
                "genotypeValue": "1/1",
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
        "sepPhased": "|",
        "sepUnphased": "/",
        "unknownString": "."
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




### Get - /search/calls/{searchResultsDbId} [GET /brapi/v2/search/calls/{searchResultsDbId}{?pageToken}{?page}{?pageSize}]

Get the results of a `Calls` search request <br/>
Clients should submit a search request using the corresponding `POST /search/calls` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]</td><td></td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetDbId</span></td><td>string</td><td>The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetName</span></td><td>string</td><td>The name of the call set this variant call belongs to. If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype</span></td><td>object</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>`ListValue` is a wrapper around a repeated field of values. <br>The JSON representation for `ListValue` is JSON array.</td></tr>
<tr><td>data<br>.genotype<br><span style="font-weight:bold;margin-left:5px">.values</span></td><td>array</td><td>**Deprecated in v2.1** Please use `genotypeValue` or `genotypeMetadata`. Github issue number #491              <br>Repeated field of dynamically typed values.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeMetadata</span></td><td>array[object]</td><td>Genotype Metadata are additional layers of metadata associated with each genotype.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality" <br> This maps to a FORMAT field in the VCF file standard.</td></tr>
<tr><td>data<br>.genotypeMetadata<br><span style="font-weight:bold;margin-left:5px">.fieldValue</span></td><td>string</td><td>The additional metadata value associated with this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotypeValue</span></td><td>string</td><td>The value of this genotype call</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.genotype_likelihood</span></td><td>array[number]</td><td>**Deprecated in v2.1** Please use `genotypeMetadata`. Github issue number #491              <br>The genotype likelihood for this variant call. Each array entry represents how likely a specific genotype is for this call as log10(P(data  genotype)), analogous to the GL tag in the VCF spec. The value ordering is defined by the GL tag in the VCF spec.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.phaseSet</span></td><td>string</td><td>If this field is populated, this variant call's genotype ordering implies the phase of the bases and  is consistent with any other variant calls on the same contig which have the same phase set string.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string</td><td>The ID of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantName</span></td><td>string</td><td>The name of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetDbId</span></td><td>string</td><td>The unique identifier for a VariantSet</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
</table>


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
    + pageToken (Optional, ) ... **Deprecated in v2.1** Please use `page`. Github issue number #451 <br> Used to request a specific page of data to be returned.<br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. 
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
                "callSetDbId": "16466f55",
                "callSetName": "Sample_123_DNA_Run_456",
                "genotype": {
                    "values": [
                        "AA"
                    ]
                },
                "genotypeMetadata": [
                    {
                        "dataType": "integer",
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality",
                        "fieldValue": "45.2"
                    }
                ],
                "genotypeValue": "1/1",
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
        "sepPhased": "|",
        "sepUnphased": "/",
        "unknownString": "."
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

