# Group Variants

A `Variant` describes a site of interest in a genetic sequence. It is usually described in terms of being compared to a `Reference`. 

A `Variant` may also describe a more traditional marker, which can be positioned on a `GenomeMap`





### Post - /search/variants [POST /brapi/v2/search/variants]

Submit a search request for `Variants`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/variants/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>
<br/>
<strong>NOTE:</strong> This endpoint uses Token based pagination. Please Review the 
<a target="_blank" href="https://wiki.brapi.org/index.php/Pagination">Pagination documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>**Deprecated in v2.1** Parameter unnecessary. Github issue number #474  <br/>Only return variant calls which belong to call sets with these IDs. If unspecified, return all variants and no variant call objects.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">end</span></td><td>integer</td><td>The end of the window (0-based, exclusive) for which overlapping variants should be returned.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">pageToken</span></td><td>string</td><td>**Deprecated in v2.1** Please use `page`. Github issue number #451  <br>Used to request a specific page of data to be returned. <br>Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. </td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceDbIds`. Github issue number #472 <br/>Only return variants on this reference.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbIds</span></td><td>array[string]</td><td>The unique identifier representing a genotype `Reference`</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbIds</span></td><td>array[string]</td><td>The unique identifier representing a genotype `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">start</span></td><td>integer</td><td>The beginning of the window (0-based, inclusive) for which overlapping variants should be returned. Genomic positions are non-negative integers less than reference length. Requests spanning the join of circular genomes are represented as two requests one on each side of the join (position 0).</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `Variants`</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `VariantSets`</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternateBases</span></td><td>array[string]</td><td>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">alternate_bases</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `alternateBases`. Github issue number #549 <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">ciend</span></td><td>array[integer]</td><td>Similar to "cipos", but for the variant's end position (which is derived from start + svlen).</td></tr>
<tr><td><span style="font-weight:bold;">cipos</span></td><td>array[integer]</td><td>In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The timestamp when this variant was created.</td></tr>
<tr><td><span style="font-weight:bold;">end</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br>The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated  by `start + referenceBases.length`.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">filtersApplied</span></td><td>boolean<br>(boolean)</td><td>True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.</td></tr>
<tr><td><span style="font-weight:bold;">filtersFailed</span></td><td>array[string]</td><td>Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.</td></tr>
<tr><td><span style="font-weight:bold;">filtersPassed</span></td><td>boolean<br>(boolean)</td><td>True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.</td></tr>
<tr><td><span style="font-weight:bold;">referenceBases</span></td><td>string</td><td>The reference bases for this variant. They start at the given start position.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string</td><td>The unique identifier for a Reference</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string</td><td>The reference on which this variant occurs. (e.g. `chr_20` or `X`)</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of the ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">start</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br> The start position at which this variant occurs (0-based). This corresponds to the first base of the string  of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning  the join of circular genomes are represented as two variants one on each side of the join (position 0).</td></tr>
<tr><td><span style="font-weight:bold;">svlen</span></td><td>integer</td><td>Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this variant was last updated.</td></tr>
<tr><td><span style="font-weight:bold;">variantNames</span></td><td>array[string]</td><td>A human readable name associated with a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>array[string]</td><td>An array of `VariantSet` IDs this variant belongs to. This also defines the `ReferenceSet` against which the `Variant` is to be interpreted.</td></tr>
<tr><td><span style="font-weight:bold;">variantType</span></td><td>string</td><td>The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"   DEL  : deletion of sequence following "start"</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "4639fe3e",
        "b60d900b"
    ],
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "end": 1500,
    "externalReferenceIDs": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceIds": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceSources": [
        "DOI",
        "Field App Name"
    ],
    "page": 0,
    "pageSize": 1000,
    "pageToken": "33c27874",
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "referenceDbId": "120a2d5c",
    "referenceDbIds": [
        "89ab4d17",
        "74d3b63d"
    ],
    "referenceSetDbIds": [
        "d3b63d4d",
        "3b63d74b"
    ],
    "start": 100,
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "trialDbIds": [
        "d2593dc2",
        "9431a731"
    ],
    "trialNames": [
        "All Yield Trials 2016",
        "Disease Resistance Study Comparison Group"
    ],
    "variantDbIds": [
        "3b63d889",
        "ab4d174d"
    ],
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
                "alternateBases": [
                    "T",
                    "TAC"
                ],
                "alternate_bases": [
                    "T",
                    "TAC"
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
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "filtersApplied": true,
                "filtersFailed": [
                    "d629a669",
                    "3f14f578"
                ],
                "filtersPassed": true,
                "referenceBases": "A",
                "referenceDbId": "fc0a81d0",
                "referenceName": "chr_20",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
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




### Get - /search/variants/{searchResultsDbId} [GET /brapi/v2/search/variants/{searchResultsDbId}{?pageToken}{?page}{?pageSize}]

Get the results of a `Variants` search request <br/>
Clients should submit a search request using the corresponding `POST /search/variants` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternateBases</span></td><td>array[string]</td><td>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">alternate_bases</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `alternateBases`. Github issue number #549 <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">ciend</span></td><td>array[integer]</td><td>Similar to "cipos", but for the variant's end position (which is derived from start + svlen).</td></tr>
<tr><td><span style="font-weight:bold;">cipos</span></td><td>array[integer]</td><td>In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The timestamp when this variant was created.</td></tr>
<tr><td><span style="font-weight:bold;">end</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br>The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated  by `start + referenceBases.length`.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">filtersApplied</span></td><td>boolean<br>(boolean)</td><td>True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.</td></tr>
<tr><td><span style="font-weight:bold;">filtersFailed</span></td><td>array[string]</td><td>Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.</td></tr>
<tr><td><span style="font-weight:bold;">filtersPassed</span></td><td>boolean<br>(boolean)</td><td>True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.</td></tr>
<tr><td><span style="font-weight:bold;">referenceBases</span></td><td>string</td><td>The reference bases for this variant. They start at the given start position.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string</td><td>The unique identifier for a Reference</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string</td><td>The reference on which this variant occurs. (e.g. `chr_20` or `X`)</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of the ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">start</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br> The start position at which this variant occurs (0-based). This corresponds to the first base of the string  of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning  the join of circular genomes are represented as two variants one on each side of the join (position 0).</td></tr>
<tr><td><span style="font-weight:bold;">svlen</span></td><td>integer</td><td>Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this variant was last updated.</td></tr>
<tr><td><span style="font-weight:bold;">variantNames</span></td><td>array[string]</td><td>A human readable name associated with a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>array[string]</td><td>An array of `VariantSet` IDs this variant belongs to. This also defines the `ReferenceSet` against which the `Variant` is to be interpreted.</td></tr>
<tr><td><span style="font-weight:bold;">variantType</span></td><td>string</td><td>The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"   DEL  : deletion of sequence following "start"</td></tr>
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
                "alternateBases": [
                    "T",
                    "TAC"
                ],
                "alternate_bases": [
                    "T",
                    "TAC"
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
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "filtersApplied": true,
                "filtersFailed": [
                    "d629a669",
                    "3f14f578"
                ],
                "filtersPassed": true,
                "referenceBases": "A",
                "referenceDbId": "fc0a81d0",
                "referenceName": "chr_20",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
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




### Get - /variants [GET /brapi/v2/variants{?variantDbId}{?variantSetDbId}{?referenceDbId}{?referenceSetDbId}{?pageToken}{?page}{?pageSize}{?externalReferenceId}{?externalReferenceSource}]

Gets a filtered list of `Variants`.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternateBases</span></td><td>array[string]</td><td>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">alternate_bases</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `alternateBases`. Github issue number #549 <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">ciend</span></td><td>array[integer]</td><td>Similar to "cipos", but for the variant's end position (which is derived from start + svlen).</td></tr>
<tr><td><span style="font-weight:bold;">cipos</span></td><td>array[integer]</td><td>In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The timestamp when this variant was created.</td></tr>
<tr><td><span style="font-weight:bold;">end</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br>The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated  by `start + referenceBases.length`.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">filtersApplied</span></td><td>boolean<br>(boolean)</td><td>True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.</td></tr>
<tr><td><span style="font-weight:bold;">filtersFailed</span></td><td>array[string]</td><td>Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.</td></tr>
<tr><td><span style="font-weight:bold;">filtersPassed</span></td><td>boolean<br>(boolean)</td><td>True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.</td></tr>
<tr><td><span style="font-weight:bold;">referenceBases</span></td><td>string</td><td>The reference bases for this variant. They start at the given start position.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string</td><td>The unique identifier for a Reference</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string</td><td>The reference on which this variant occurs. (e.g. `chr_20` or `X`)</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of the ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">start</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br> The start position at which this variant occurs (0-based). This corresponds to the first base of the string  of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning  the join of circular genomes are represented as two variants one on each side of the join (position 0).</td></tr>
<tr><td><span style="font-weight:bold;">svlen</span></td><td>integer</td><td>Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this variant was last updated.</td></tr>
<tr><td><span style="font-weight:bold;">variantNames</span></td><td>array[string]</td><td>A human readable name associated with a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>array[string]</td><td>An array of `VariantSet` IDs this variant belongs to. This also defines the `ReferenceSet` against which the `Variant` is to be interpreted.</td></tr>
<tr><td><span style="font-weight:bold;">variantType</span></td><td>string</td><td>The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"   DEL  : deletion of sequence following "start"</td></tr>
</table>


 

+ Parameters
    + variantDbId (Optional, ) ... The ID which uniquely identifies a `Variant`
    + variantSetDbId (Optional, ) ... The ID which uniquely identifies a `VariantSet`
    + referenceDbId (Optional, ) ... The ID which uniquely identifies a `Reference`
    + referenceSetDbId (Optional, ) ... The ID which uniquely identifies a `ReferenceSet`
    + pageToken (Optional, ) ... **Deprecated in v2.1** Please use `page`. Github issue number #451 <br> Used to request a specific page of data to be returned.<br> Tokenized pages are for large data sets which can not be efficiently broken into indexed pages. Use the nextPageToken and prevPageToken from a prior response to construct a query and move to the next or previous page respectively. 
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + externalReferenceId (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
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
                "alternateBases": [
                    "T",
                    "TAC"
                ],
                "alternate_bases": [
                    "T",
                    "TAC"
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
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "filtersApplied": true,
                "filtersFailed": [
                    "d629a669",
                    "3f14f578"
                ],
                "filtersPassed": true,
                "referenceBases": "A",
                "referenceDbId": "fc0a81d0",
                "referenceName": "chr_20",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
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

The endpoint `GET /variants/{id}` will return a JSON version of `Variant`.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternateBases</span></td><td>array[string]</td><td>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">alternate_bases</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `alternateBases`. Github issue number #549 <br>The bases that appear instead of the reference bases. Multiple alternate alleles are possible.</td></tr>
<tr><td><span style="font-weight:bold;">ciend</span></td><td>array[integer]</td><td>Similar to "cipos", but for the variant's end position (which is derived from start + svlen).</td></tr>
<tr><td><span style="font-weight:bold;">cipos</span></td><td>array[integer]</td><td>In the case of structural variants, start and end of the variant may not be known with an exact base position. "cipos" provides an interval with high confidence for the start position. The interval is provided by 0 or 2 signed integers which are added to the start position. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The timestamp when this variant was created.</td></tr>
<tr><td><span style="font-weight:bold;">end</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br>The end position (exclusive), resulting in [start, end) closed-open interval. This is typically calculated  by `start + referenceBases.length`.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">filtersApplied</span></td><td>boolean<br>(boolean)</td><td>True if filters were applied for this variant. VCF column 7 "FILTER" any value other than the missing value.</td></tr>
<tr><td><span style="font-weight:bold;">filtersFailed</span></td><td>array[string]</td><td>Zero or more filters that failed for this variant. VCF column 7 "FILTER" shared across all alleles in the same VCF record.</td></tr>
<tr><td><span style="font-weight:bold;">filtersPassed</span></td><td>boolean<br>(boolean)</td><td>True if all filters for this variant passed. VCF column 7 "FILTER" value PASS.</td></tr>
<tr><td><span style="font-weight:bold;">referenceBases</span></td><td>string</td><td>The reference bases for this variant. They start at the given start position.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string</td><td>The unique identifier for a Reference</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string</td><td>The reference on which this variant occurs. (e.g. `chr_20` or `X`)</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of the ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">start</span></td><td>integer</td><td>This field is optional and may be ignored if there is no relevant map or reference to be associated with. <br> The start position at which this variant occurs (0-based). This corresponds to the first base of the string  of reference bases. Genomic positions are non-negative integers less than reference length. Variants spanning  the join of circular genomes are represented as two variants one on each side of the join (position 0).</td></tr>
<tr><td><span style="font-weight:bold;">svlen</span></td><td>integer</td><td>Length of the - if labeled as such in variant_type - structural variation. Based on the use in VCF v4.2</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this variant was last updated.</td></tr>
<tr><td><span style="font-weight:bold;">variantNames</span></td><td>array[string]</td><td>A human readable name associated with a `Variant`</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>array[string]</td><td>An array of `VariantSet` IDs this variant belongs to. This also defines the `ReferenceSet` against which the `Variant` is to be interpreted.</td></tr>
<tr><td><span style="font-weight:bold;">variantType</span></td><td>string</td><td>The "variant_type" is used to denote e.g. structural variants. Examples:   DUP  : duplication of sequence following "start"   DEL  : deletion of sequence following "start"</td></tr>
</table>


 

+ Parameters
    + variantDbId (Required, ) ... The ID which uniquely identifies a `Variant`
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
        "alternateBases": [
            "T",
            "TAC"
        ],
        "alternate_bases": [
            "T",
            "TAC"
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
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "filtersApplied": true,
        "filtersFailed": [
            "d629a669",
            "3f14f578"
        ],
        "filtersPassed": true,
        "referenceBases": "A",
        "referenceDbId": "fc0a81d0",
        "referenceName": "chr_20",
        "referenceSetDbId": "c1ecfef1",
        "referenceSetName": "The Best Assembly Ever",
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




### Get - /variants/{variantDbId}/calls [GET /brapi/v2/variants/{variantDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?page}{?pageSize}]

The variant calls for this particular variant. Each one represents the determination of genotype with respect to this variant. `Calls` in this array are implicitly associated with this `Variant`.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[object]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The `data` array is part of the BrAPI standard List Response JSON container. `data` will always contain the primary list of objects being returned by a BrAPI endpoint. `data` is also the only array impacted by the `metadata.pagination` details. When the pagination parameters change, the `data` array will reflect those changes in the JSON response.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.callSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID of the call set this variant call belongs to.  If this field is not present, the ordering of the call sets from a `SearchCallSetsRequest` over this `VariantSet` is guaranteed to match the ordering of the calls on this `Variant`. The number of results will also be the same.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a VariantSet</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
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
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantName</span></td><td>string</td><td>The name of the variant this call belongs to.</td></tr>
<tr><td>data<br><span style="font-weight:bold;margin-left:5px">.variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
</table>


 

+ Parameters
    + variantDbId (Required, ) ... The ID which uniquely identifies a `Variant`
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

