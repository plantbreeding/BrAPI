# Group Reference Sets

From GA4GH Variants schema documentation

A reference genome is a genome assembly that other genomes are compared to and described with respect to. For example, sequencing reads are mapped to and described with respect to a reference genome in the API, and genetic variations are described as edits to reference scaffolds/contigs. In the API a reference genome is described by a ReferenceSet. In turn a ReferenceSet is composed of a set of Reference objects, each which represents a scaffold or contig in the assembly. Reference sequences are expected to have unique names within a ReferenceSet




### Get - /referencesets [GET /brapi/v2/referencesets{?referenceSetDbId}{?accession}{?assemblyPUI}{?md5checksum}{?commonCropName}{?programDbId}{?trialDbId}{?studyDbId}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Gets a filtered list of `ReferenceSets`.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">assemblyPUI</span></td><td>string</td><td>The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Optional free text description of this reference set.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>Specifies a FASTA format file/string.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
</table>


 

+ Parameters
    + referenceSetDbId (Optional, string) ... The ID of the `ReferenceSet` to be retrieved.
    + accession (Optional, string) ... If set, return the reference sets for which the `accession` matches this string (case-sensitive, exact match).
    + assemblyPUI (Optional, string) ... If set, return the reference sets for which the `assemblyId` matches this string (case-sensitive, exact match).
    + md5checksum (Optional, string) ... If set, return the reference sets for which the `md5checksum` matches this string (case-sensitive, exact match).
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + trialDbId (Optional, string) ... Use this parameter to only return results associated with the given `Trial` unique identifier. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
    + studyDbId (Optional, string) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + externalReferenceId (Optional, string) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, string) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">assemblyPUI</span></td><td>string</td><td>The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Optional free text description of this reference set.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>Specifies a FASTA format file/string.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
</table>


 

+ Parameters
    + referenceSetDbId (Required, string) ... The ID of the `ReferenceSet` to be retrieved.
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">accessions</span></td><td>array[string]</td><td>If set, return the reference sets for which the `accession` matches this string (case-sensitive, exact match).</td></tr>
<tr><td><span style="font-weight:bold;">assemblyPUIs</span></td><td>array[string]</td><td>If set, return the reference sets for which the `assemblyId` matches this string (case-sensitive, exact match).</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">md5checksums</span></td><td>array[string]</td><td>If set, return the reference sets for which the `md5checksum` matches this string (case-sensitive, exact match).</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbIds</span></td><td>array[string]</td><td>The `ReferenceSets` to search.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">assemblyPUI</span></td><td>string</td><td>The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Optional free text description of this reference set.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>Specifies a FASTA format file/string.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">assemblyPUI</span></td><td>string</td><td>The remaining information is about the source of the sequences Public id of this reference set, such as `GRCH_37`.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Optional free text description of this reference set.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">isDerived</span></td><td>boolean<br>(boolean)</td><td>A reference set may be derived from a source if it contains additional sequences, or some of the sequences within it are derived (see the definition of `isDerived` in `Reference`).</td></tr>
<tr><td><span style="font-weight:bold;">md5checksum</span></td><td>string</td><td>Order-independent MD5 checksum which identifies this `ReferenceSet`.  To compute this checksum, make a list of `Reference.md5checksum` for all `Reference` s in this set. Then sort that list, and take the MD5 hash of all the strings concatenated together. Express the hash as a lower-case hexadecimal string.</td></tr>
<tr><td><span style="font-weight:bold;">sourceAccessions</span></td><td>array[string]</td><td>All known corresponding accession IDs in INSDC (GenBank/ENA/DDBJ) ideally with a version number, e.g. `NC_000001.11`.</td></tr>
<tr><td><span style="font-weight:bold;">sourceGermplasm</span></td><td>array[object]</td><td>All known corresponding Germplasm</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm within the given database server</td></tr>
<tr><td>sourceGermplasm<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">sourceURI</span></td><td>string</td><td>Specifies a FASTA format file/string.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>object</td><td>An ontology term describing an attribute.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.term</span></td><td>string</td><td>Ontology term - the label of the ontology term the termId is pointing to.</td></tr>
<tr><td>species<br><span style="font-weight:bold;margin-left:5px">.termURI</span></td><td>string</td><td>Ontology term identifier - the CURIE for an ontology term. It differs from the standard GA4GH schema's :ref:`id ` in that it is a CURIE pointing to an information resource outside of the scope of the schema or its resource implementation.</td></tr>
</table>


 

+ Parameters
    + searchResultsDbId (Required, string) ... Unique identifier which references the search results
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
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

