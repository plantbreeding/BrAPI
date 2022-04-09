# Group References





### Get - /references [GET /brapi/v2/references{?referenceDbId}{?referenceSetDbId}{?accession}{?md5checksum}{?isDerived}{?minLength}{?maxLength}{?trialDbId}{?studyDbId}{?commonCropName}{?programDbId}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

`GET /references` will return a filtered list of `Reference` JSON objects.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|length|integer|The length of this reference's sequence.|
|md5checksum|string|The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).|
|referenceDbId|string|The unique identifier for a Reference|
|referenceName|string|The human readable name of a Reference within a Reference Set.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.|
|sourceDivergence|number (float)|The `sourceDivergence` is the fraction of non-indel bases that do not match the reference this message was derived from.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.|
|species|object|An ontology term describing an attribute.|
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + referenceDbId (Optional, ) ... The ID of the `Reference` to be retrieved.
    + referenceSetDbId (Optional, ) ... The ID of the `ReferenceSet` to be retrieved.
    + accession (Optional, ) ... If set, return the reference sets for which the `accession` matches this string (case-sensitive, exact match).
    + md5checksum (Optional, ) ... If specified, return the references for which the `md5checksum` matches this string (case-sensitive, exact match).
    + isDerived (Optional, ) ... If the reference is derived from a source sequence
    + minLength (Optional, ) ... The minimum length of the reference sequences to be retrieved.
    + maxLength (Optional, ) ... The maximum length of the reference sequences to be retrieved.
    + trialDbId (Optional, ) ... The unique identifier for a Trial
    + studyDbId (Optional, ) ... The unique identifier for a Study
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
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

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|length|integer|The length of this reference's sequence.|
|md5checksum|string|The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).|
|referenceDbId|string|The unique identifier for a Reference|
|referenceName|string|The human readable name of a Reference within a Reference Set.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.|
|sourceDivergence|number (float)|The `sourceDivergence` is the fraction of non-indel bases that do not match the reference this message was derived from.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.|
|species|object|An ontology term describing an attribute.|
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

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

|Field|Type|Description|
|---|---|---| 
|nextPageToken|string|The continuation token, which is used to page through large result sets. Provide this value in a subsequent request to return the next page of results. This field will be empty if there are not any additional results.|
|offset|integer|The offset position (0-based) of the given sequence from the start of this `Reference`. This value will differ for each page in a request.|
|sequence|string|A sub-string of the bases that make up this reference. Bases are represented as IUPAC-IUB codes; this string matches the regular expression `[ACGTMRWSYKVHDBN]*`.|


 

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

|Field|Type|Description|
|---|---|---| 
|accessions|array[string]|If specified, return the references for which the `accession` matches this string (case-sensitive, exact match).|
|commonCropNames|array[string]|The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.|
|externalReferenceIDs|array[string]|**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceIds|array[string]|List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceSources|array[string]|List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm to search for|
|germplasmNames|array[string]|List of human readable names to identify germplasm to search for|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|maxLength|integer|The minimum length of this reference's sequence.|
|md5checksums|array[string]|If specified, return the references for which the `md5checksum` matches this string (case-sensitive, exact match).|
|minLength|integer|The minimum length of this reference's sequence.|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.|
|programNames|array[string]|Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.|
|referenceDbIds|array[string]|The `References` to search.|
|referenceSetDbIds|array[string]|The `ReferenceSets` to search.|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|trialDbIds|array[string]|The ID which uniquely identifies a trial to search for|
|trialNames|array[string]|The human readable name of a trial to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|length|integer|The length of this reference's sequence.|
|md5checksum|string|The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).|
|referenceDbId|string|The unique identifier for a Reference|
|referenceName|string|The human readable name of a Reference within a Reference Set.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.|
|sourceDivergence|number (float)|The `sourceDivergence` is the fraction of non-indel bases that do not match the reference this message was derived from.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.|
|species|object|An ontology term describing an attribute.|
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

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

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A sequence X is said to be derived from source sequence Y, if X and Y are of the same length and the per-base sequence divergence at A/C/G/T bases is sufficiently small. Two sequences derived from the same official sequence share the same coordinates and annotations, and can be replaced with the official sequence for certain use cases.|
|length|integer|The length of this reference's sequence.|
|md5checksum|string|The MD5 checksum uniquely representing this `Reference` as a lower-case hexadecimal string, calculated as the MD5 of the upper-case sequence excluding all whitespace characters (this is equivalent to SQ:M5 in SAM).|
|referenceDbId|string|The unique identifier for a Reference|
|referenceName|string|The human readable name of a Reference within a Reference Set.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) which must include a version number, e.g. `GCF_000001405.26`.|
|sourceDivergence|number (float)|The `sourceDivergence` is the fraction of non-indel bases that do not match the reference this message was derived from.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|The URI from which the sequence was obtained. Specifies a FASTA format file/string with one name, sequence pair. In most cases, clients should call the `getReferenceBases()` method to obtain sequence bases for a `Reference` instead of attempting to retrieve this URI.|
|species|object|An ontology term describing an attribute.|
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

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

