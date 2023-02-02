# Group CallSets

A `CallSet` represents a `Sample` that was used during some sequencing event. In most cases, the `CallSet` will have a 1-to-1 relationship with a given `Sample`. However, in some cases, a single `Sample` may be used in multiple different sequencing events or experiments. The `CallSet` gives an identifier to the relationship between a `Sample` and a genotype sequencing event. 

In a VCF file, `CallSets` are the columns are the data matrix. 





### Get - /callsets [GET /brapi/v2/callsets{?callSetDbId}{?callSetName}{?variantSetDbId}{?sampleDbId}{?germplasmDbId}{?page}{?pageSize}{?externalReferenceId}{?externalReferenceSource}]

Gets a filtered list of `CallSet` JSON objects.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a CallSet within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">callSetName</span></td><td>string</td><td>The human readable name which identifies a germplasm within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The date this call set was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbId</span></td><td>string</td><td>The Biosample entity the call set data was generated from.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this call set was last updated</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>The IDs of the variantSets this callSet has calls in.</td></tr>
</table>


 

+ Parameters
    + callSetDbId (Optional, ) ... The ID which uniquely identifies a `CallSet` within the given database server
    + callSetName (Optional, ) ... The human readable name of a `CallSet`.
    + variantSetDbId (Optional, ) ... The ID which uniquely identifies a `VariantSet` within the given database server
    + sampleDbId (Optional, ) ... The ID which uniquely identifies a `Sample` within the given database server<br>Filter results to only include `CallSets` generated from this `Sample`
    + germplasmDbId (Optional, ) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
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
                "callSetDbId": "eb2bfd3d",
                "callSetName": "Sample_123_DNA_Run_456",
                "created": "2018-01-01T14:47:23-0600",
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




### Get - /callsets/{callSetDbId} [GET /brapi/v2/callsets/{callSetDbId}]

Gets a `CallSet` by ID.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a CallSet within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">callSetName</span></td><td>string</td><td>The human readable name which identifies a germplasm within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The date this call set was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbId</span></td><td>string</td><td>The Biosample entity the call set data was generated from.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this call set was last updated</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>The IDs of the variantSets this callSet has calls in.</td></tr>
</table>


 

+ Parameters
    + callSetDbId (Required, ) ... The ID which uniquely identifies a `CallSet` within the given database server
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
        "callSetDbId": "eb2bfd3d",
        "callSetName": "Sample_123_DNA_Run_456",
        "created": "2018-01-01T14:47:23-0600",
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
        "sampleDbId": "5e50e11d",
        "studyDbId": "708149c1",
        "updated": "2018-01-01T14:47:23-0600",
        "variantSetDbIds": [
            "cfd3d60f",
            "a4e8bfe9"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Get - /callsets/{callSetDbId}/calls [GET /brapi/v2/callsets/{callSetDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?page}{?pageSize}]

Gets a list of `Calls` associated with a `CallSet`.



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
    + callSetDbId (Required, ) ... The ID which uniquely identifies a `CallSet` within the given database server
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




### Post - /search/callsets [POST /brapi/v2/search/callsets]

Submit a search request for `CallSets` 
<br> Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/callsets/{searchResultsDbId}` to retrieve the results of the search. 
<br> Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `CallSets` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">callSetNames</span></td><td>array[string]</td><td>A list of human readable names associated with `CallSets`</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `Samples` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">sampleNames</span></td><td>array[string]</td><td>A list of human readable names associated with `Samples`</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `VariantSets` within the given database server</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a CallSet within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">callSetName</span></td><td>string</td><td>The human readable name which identifies a germplasm within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The date this call set was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbId</span></td><td>string</td><td>The Biosample entity the call set data was generated from.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this call set was last updated</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>The IDs of the variantSets this callSet has calls in.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "6c7486b2",
        "49c36a73"
    ],
    "callSetNames": [
        "Sample_123_DNA_Run_456",
        "Sample_789_DNA_Run_101"
    ],
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
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
    "germplasmDbIds": [
        "e9c6edd7",
        "1b1df4a6"
    ],
    "germplasmNames": [
        "A0000003",
        "A0000477"
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
    "sampleDbIds": [
        "758d3f6d",
        "39c0a3f7"
    ],
    "sampleNames": [
        "Sample_123",
        "Sample_789"
    ],
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
    "variantSetDbIds": [
        "8a9a8972",
        "32a2649a"
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
                "callSetDbId": "eb2bfd3d",
                "callSetName": "Sample_123_DNA_Run_456",
                "created": "2018-01-01T14:47:23-0600",
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




### Get - /search/callsets/{searchResultsDbId} [GET /brapi/v2/search/callsets/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `CallSets` search request 
<br> Clients should submit a search request using the corresponding `POST /search/callsets` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. 
<br>Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a CallSet within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">callSetName</span></td><td>string</td><td>The human readable name which identifies a germplasm within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">created</span></td><td>string<br>(date-time)</td><td>The date this call set was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">sampleDbId</span></td><td>string</td><td>The Biosample entity the call set data was generated from.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">updated</span></td><td>string<br>(date-time)</td><td>The time at which this call set was last updated</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>The IDs of the variantSets this callSet has calls in.</td></tr>
</table>


 

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
                "callSetDbId": "eb2bfd3d",
                "callSetName": "Sample_123_DNA_Run_456",
                "created": "2018-01-01T14:47:23-0600",
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

