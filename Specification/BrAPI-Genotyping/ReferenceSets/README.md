# Group Reference Sets





### Get - /referencesets [GET /brapi/v2/referencesets{?referenceSetDbId}{?accession}{?assemblyPUI}{?md5checksum}{?trialDbId}{?studyDbId}{?commonCropName}{?programDbId}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Gets a filtered list of `ReferenceSets`.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|assemblyPUI|string|The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.|
|commonCropName|string|Common name for the crop|
|description|string|Optional free text description of this reference set.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).|
|md5checksum|string|Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|Specifies a FASTA format file/string.|
|species|object|An ontology term describing an attribute.|
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + referenceSetDbId (Optional, ) ... The ID of the `ReferenceSet` to be retrieved.
    + accession (Optional, ) ... If set, return the reference sets for which the `accession` matches this string (case-sensitive, exact match).
    + assemblyPUI (Optional, ) ... If set, return the reference sets for which the `assemblyId` matches this string (case-sensitive, exact match).
    + md5checksum (Optional, ) ... If set, return the reference sets for which the `md5checksum` matches this string (case-sensitive, exact match).
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
                "assemblyPUI": "doi://10.12345/fake/9876",
                "commonCropName": "Maize",
                "description": "This is an example description for an assembly",
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
                "md5checksum": "c2365e900c81a89cf74d83dab60df146",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
                "sourceAccessions": [
                    "A0000002",
                    "A0009393"
                ],
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




### Get - /referencesets/{referenceSetDbId} [GET /brapi/v2/referencesets/{referenceSetDbId}]

Gets a `ReferenceSet` by ID.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|assemblyPUI|string|The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.|
|commonCropName|string|Common name for the crop|
|description|string|Optional free text description of this reference set.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).|
|md5checksum|string|Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|Specifies a FASTA format file/string.|
|species|object|An ontology term describing an attribute.|
|term|string|Ontology term - the label of the ontology term the termId is pointing to.|
|termURI|string|Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.|


 

+ Parameters
    + referenceSetDbId (Required, ) ... The ID of the `ReferenceSet` to be retrieved.
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
        "assemblyPUI": "doi://10.12345/fake/9876",
        "commonCropName": "Maize",
        "description": "This is an example description for an assembly",
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
        "md5checksum": "c2365e900c81a89cf74d83dab60df146",
        "referenceSetDbId": "c1ecfef1",
        "referenceSetName": "The Best Assembly Ever",
        "sourceAccessions": [
            "A0000002",
            "A0009393"
        ],
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




### Post - /search/referencesets [POST /brapi/v2/search/referencesets]

Submit a search request for `ReferenceSets`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/referencesets/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|accessions||If set, return the reference sets for which the `accession` matches this string (case-sensitive, exact match).|
|assemblyPUIs||If set, return the reference sets for which the `assemblyId` matches this string (case-sensitive, exact match).|
|commonCropNames|array[string]|The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.|
|externalReferenceIDs|array[string]|**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceIds|array[string]|List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceSources|array[string]|List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm to search for|
|germplasmNames|array[string]|List of human readable names to identify germplasm to search for|
|md5checksums||If set, return the reference sets for which the `md5checksum` matches this string (case-sensitive, exact match).|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.|
|programNames|array[string]|Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.|
|referenceSetDbIds||The `ReferenceSets` to search.|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|trialDbIds|array[string]|The ID which uniquely identifies a trial to search for|
|trialNames|array[string]|The human readable name of a trial to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|assemblyPUI|string|The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.|
|commonCropName|string|Common name for the crop|
|description|string|Optional free text description of this reference set.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).|
|md5checksum|string|Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|Specifies a FASTA format file/string.|
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
    "assemblyPUIs": [
        "doi:10.15454/312953986E3",
        "doi:10.15454/312953986E3"
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
    "md5checksums": [
        "c2365e900c81a89cf74d83dab60df146"
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
                "assemblyPUI": "doi://10.12345/fake/9876",
                "commonCropName": "Maize",
                "description": "This is an example description for an assembly",
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
                "md5checksum": "c2365e900c81a89cf74d83dab60df146",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
                "sourceAccessions": [
                    "A0000002",
                    "A0009393"
                ],
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




### Get - /search/referencesets/{searchResultsDbId} [GET /brapi/v2/search/referencesets/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `ReferenceSets` search request <br/>
Clients should submit a search request using the corresponding `POST /search/referencesets` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|assemblyPUI|string|The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.|
|commonCropName|string|Common name for the crop|
|description|string|Optional free text description of this reference set.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|isDerived|boolean (boolean)|A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).|
|md5checksum|string|Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.|
|referenceSetDbId|string|The unique identifier for a ReferenceSet|
|referenceSetName|string|The human readable name of a ReferenceSet|
|sourceAccessions|array[string]|All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.|
|sourceGermplasm|array[object]|All known corresponding Germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|The human readable name of a germplasm|
|sourceURI|string|Specifies a FASTA format file/string.|
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
                "assemblyPUI": "doi://10.12345/fake/9876",
                "commonCropName": "Maize",
                "description": "This is an example description for an assembly",
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
                "md5checksum": "c2365e900c81a89cf74d83dab60df146",
                "referenceSetDbId": "c1ecfef1",
                "referenceSetName": "The Best Assembly Ever",
                "sourceAccessions": [
                    "A0000002",
                    "A0009393"
                ],
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

