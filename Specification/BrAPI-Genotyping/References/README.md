# Group References

From GA4GH Variants schema documentation

A reference genome is a genome assembly that other genomes are compared to and described with respect to. For example, sequencing reads are mapped to and described with respect to a reference genome in the API, and genetic variations are described as edits to reference scaffolds/contigs. In the API a reference genome is described by a ReferenceSet. In turn a ReferenceSet is composed of a set of Reference objects, each which represents a scaffold or contig in the assembly. Reference sequences are expected to have unique names within a ReferenceSet





### Get - /references [GET /brapi/v2/references{?referenceDbId}{?referenceSetDbId}{?accession}{?md5checksum}{?isDerived}{?minLength}{?maxLength}{?commonCropName}{?programDbId}{?trialDbId}{?studyDbId}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

`GET /references` will return a filtered list of `Reference` JSON objects.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a `Reference`</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a `Reference` within a `ReferenceSet`.</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.</td></tr>
<tr><td><span style="font-weight:bold;">length</span></td><td>integer</td><td>The length of this `Reference` sequence.</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceDivergence</span></td><td>number<br>(float)</td><td>The `sourceDivergence` is the fraction of non-indel bases that do not match the `Reference` this message was derived from.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Germplasm` within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a `Germplasm`</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
</table>


 

+ Parameters
    + referenceDbId (Optional, ) ... The ID of the `Reference` to be retrieved.
    + referenceSetDbId (Optional, ) ... The ID of the `ReferenceSet` to be retrieved.
    + accession (Optional, ) ... If set, return the reference sets for which the `accession` matches this string (case-sensitive, exact match).
    + md5checksum (Optional, ) ... If specified, return the references for which the `md5checksum` matches this string (case-sensitive, exact match).
    + isDerived (Optional, ) ... If the reference is derived from a source sequence
    + minLength (Optional, ) ... The minimum length of the reference sequences to be retrieved.
    + maxLength (Optional, ) ... The maximum length of the reference sequences to be retrieved.
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + trialDbId (Optional, ) ... Use this parameter to only return results associated with the given `Trial` unique identifier. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
    + studyDbId (Optional, ) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + externalReferenceId (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
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
                "commonCropName": "Maize",
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
                "isDerived": false,
                "length": 50000000,
                "md5checksum": "c2365e900c81a89cf74d83dab60df146",
                "referenceDbId": "fc0a81d0",
                "referenceName": "Chromosome 2",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
                "sourceAccessions": [
                    "GCF_000001405.26"
                ],
                "sourceDivergence": 0.01,
                "sourceGermplasm": [
                    {
                        "germplasmDbId": "d4076594",
                        "germplasmName": "A0000003"
                    }
                ],
                "sourceURI": "https://wiki.brapi.org/files/demo.fast",
                "species": {
                    "term": "sonic hedgehog",
                    "termURI": "MGI:MGI:98297"
                }
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




### Get - /references/{referenceDbId} [GET /brapi/v2/references/{referenceDbId}]

`GET /references/{reference_id}` will return a JSON version of
`Reference`.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a `Reference`</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a `Reference` within a `ReferenceSet`.</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.</td></tr>
<tr><td><span style="font-weight:bold;">length</span></td><td>integer</td><td>The length of this `Reference` sequence.</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceDivergence</span></td><td>number<br>(float)</td><td>The `sourceDivergence` is the fraction of non-indel bases that do not match the `Reference` this message was derived from.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Germplasm` within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a `Germplasm`</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
</table>


 

+ Parameters
    + referenceDbId (Required, ) ... The ID of the `Reference` to be retrieved.
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
        "commonCropName": "Maize",
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
        "isDerived": false,
        "length": 50000000,
        "md5checksum": "c2365e900c81a89cf74d83dab60df146",
        "referenceDbId": "fc0a81d0",
        "referenceName": "Chromosome 2",
        "referenceSetDbId": "c1ecfef1",
        "referenceSetName": "The Best Assembly Ever",
        "sourceAccessions": [
            "GCF_000001405.26"
        ],
        "sourceDivergence": 0.01,
        "sourceGermplasm": [
            {
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003"
            }
        ],
        "sourceURI": "https://wiki.brapi.org/files/demo.fast",
        "species": {
            "term": "sonic hedgehog",
            "termURI": "MGI:MGI:98297"
        }
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




### Get - /references/{referenceDbId}/bases [GET /brapi/v2/references/{referenceDbId}/bases{?start}{?end}{?pageToken}]

Lists `Reference` bases by ID and optional range.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">nextPageToken</span></td><td>string</td><td>The continuation token, which is used to page through large result sets. Provide this value in a subsequent request to return the next page of results. This field will be empty if there are not any additional results.</td></tr>
<tr><td><span style="font-weight:bold;">offset</span></td><td>integer</td><td>The offset position (0-based) of the given sequence from the start of this `Reference`. This value will differ for each page in a request.</td></tr>
<tr><td><span style="font-weight:bold;">sequence</span></td><td>string</td><td>A sub-string of the bases that make up this reference. Bases are represented as IUPAC-IUB codes; this string matches the regular expression `[ACGTMRWSYKVHDBN]*`.</td></tr>
</table>


 

+ Parameters
    + referenceDbId (Required, ) ... The ID of the `Reference` to be retrieved.
    + start (Optional, ) ... The start position (0-based) of this query. Defaults to 0.Genomic positions are non-negative integers less than reference length.Requests spanning the join of circular genomes are represented astwo requests one on each side of the join (position 0).
    + end (Optional, ) ... The end position (0-based, exclusive) of this query. Defaults to the length of this `Reference`.
    + pageToken (Optional, ) ... The continuation token, which is used to page through large result sets.To get the next page of results, set this parameter to the value of`next_page_token` from the previous response.
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
        "nextPageToken": "3a3d658a",
        "offset": 20000,
        "sequence": "TAGGATTGAGCTCTATATTAGGATTGAGCTCTATATTAGGATTGAGCTCTATATTAGGATTGAGCTCTATATTAGGATTGAGCTCTATATTAGGATTGAGCTCTATATTAGGATTGAGCTCTATATTAGGATTGAGCTCTATATTAGGATTGAGCTCTATAT"
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




### Post - /search/references [POST /brapi/v2/search/references]

Submit a search request for `References`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/references/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">accessions</span></td><td>array[string]</td><td>If specified, return the references for which the `accession` matches this string (case-sensitive, exact match).</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.</td></tr>
<tr><td><span style="font-weight:bold;">maxLength</span></td><td>integer</td><td>The minimum length of this `References` sequence.</td></tr>
<tr><td><span style="font-weight:bold;">md5checksums</span></td><td>array[string]</td><td>If specified, return the references for which the `md5checksum` matches this string (case-sensitive, exact match).</td></tr>
<tr><td><span style="font-weight:bold;">minLength</span></td><td>integer</td><td>The minimum length of this `References` sequence.</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `References` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbIds</span></td><td>array[string]</td><td>A list of IDs which uniquely identify `ReferenceSets` within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a `Reference`</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a `Reference` within a `ReferenceSet`.</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.</td></tr>
<tr><td><span style="font-weight:bold;">length</span></td><td>integer</td><td>The length of this `Reference` sequence.</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceDivergence</span></td><td>number<br>(float)</td><td>The `sourceDivergence` is the fraction of non-indel bases that do not match the `Reference` this message was derived from.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Germplasm` within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a `Germplasm`</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accessions": [
        "A0009283",
        "A0006657"
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
    "maxLength": 90000,
    "md5checksums": [
        "c2365e900c81a89cf74d83dab60df146"
    ],
    "minLength": 4000,
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
    "referenceDbIds": [
        "04c83ea7",
        "d0998a34"
    ],
    "referenceSetDbIds": [
        "32a19dd7",
        "2c182c18"
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
                "commonCropName": "Maize",
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
                "isDerived": false,
                "length": 50000000,
                "md5checksum": "c2365e900c81a89cf74d83dab60df146",
                "referenceDbId": "fc0a81d0",
                "referenceName": "Chromosome 2",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
                "sourceAccessions": [
                    "GCF_000001405.26"
                ],
                "sourceDivergence": 0.01,
                "sourceGermplasm": [
                    {
                        "germplasmDbId": "d4076594",
                        "germplasmName": "A0000003"
                    }
                ],
                "sourceURI": "https://wiki.brapi.org/files/demo.fast",
                "species": {
                    "term": "sonic hedgehog",
                    "termURI": "MGI:MGI:98297"
                }
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




### Get - /search/references/{searchResultsDbId} [GET /brapi/v2/search/references/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `References` search request <br/>
Clients should submit a search request using the corresponding `POST /search/references` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a `Reference`</td></tr>
<tr><td><span style="font-weight:bold;">referenceName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a `Reference` within a `ReferenceSet`.</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.</td></tr>
<tr><td><span style="font-weight:bold;">length</span></td><td>integer</td><td>The length of this `Reference` sequence.</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The unique identifier for a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string</td><td>The human readable name of a `ReferenceSet`</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceDivergence</span></td><td>number<br>(float)</td><td>The `sourceDivergence` is the fraction of non-indel bases that do not match the `Reference` this message was derived from.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a `Germplasm` within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a `Germplasm`</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
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
                "commonCropName": "Maize",
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
                "isDerived": false,
                "length": 50000000,
                "md5checksum": "c2365e900c81a89cf74d83dab60df146",
                "referenceDbId": "fc0a81d0",
                "referenceName": "Chromosome 2",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
                "sourceAccessions": [
                    "GCF_000001405.26"
                ],
                "sourceDivergence": 0.01,
                "sourceGermplasm": [
                    {
                        "germplasmDbId": "d4076594",
                        "germplasmName": "A0000003"
                    }
                ],
                "sourceURI": "https://wiki.brapi.org/files/demo.fast",
                "species": {
                    "term": "sonic hedgehog",
                    "termURI": "MGI:MGI:98297"
                }
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

