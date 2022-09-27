# Group Pedigree
These end points can be used to interact with Pedigree Trees. Each response will be a set of Pedigree Node objects. Each of these Node objects represent a particular Germplasm and all the links to its parents, siblings, and children. From a list of Node objects, a client application should have all the information it needs to draw a Pedigree tree visualization, or calculate genetic distances. 






### Get - /pedigree [GET /brapi/v2/pedigree{?accessionNumber}{?collection}{?familyCode}{?binomialName}{?genus}{?species}{?synonym}{?includeParents}{?includeSiblings}{?includeProgeny}{?includeFullTree}{?pedigreeDepth}{?progenyDepth}{?commonCropName}{?programDbId}{?trialDbId}{?studyDbId}{?germplasmDbId}{?germplasmName}{?germplasmPUI}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of pedigree nodes which represent a subset of a pedigree tree



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodDbId</span></td><td>string</td><td>The unique identifier for the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodName</span></td><td>string</td><td>The human readable name of the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>The crossing project used to generate this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingYear</span></td><td>integer</td><td>The year the parents were originally crossed</td></tr>
<tr><td><span style="font-weight:bold;">defaultDisplayName</span></td><td>string</td><td>Human readable name used for display purposes</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">familyCode</span></td><td>string</td><td>The code representing the family of this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUI</span></td><td>string</td><td>The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.</td></tr>
<tr><td><span style="font-weight:bold;">parents</span></td><td>array[object]</td><td>A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known.  <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">pedigreeString</span></td><td>string</td><td>The string representation of the pedigree for this germplasm in PURDY notation</td></tr>
<tr><td><span style="font-weight:bold;">progeny</span></td><td>array[object]</td><td>A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes. <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows        the type of parent this germplasm is to each of the child germplasm references. <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">siblings</span></td><td>array[object]</td><td>A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Siblings share at least one parent with the given germplasm.  <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
</table>


 

+ Parameters
    + accessionNumber (Optional, ) ... The unique identifier for a material or germplasm within a genebankMCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").
    + collection (Optional, ) ... A specific panel/collection/population name this germplasm belongs to.
    + familyCode (Optional, ) ... A familyCode representing the family this germplasm belongs to.
    + binomialName (Optional, ) ... The full binomial name (scientific name) of a germplasm
    + genus (Optional, ) ... The scientific genus of a germplasm
    + species (Optional, ) ... The scientific species of a germplasm
    + synonym (Optional, ) ... An alternative name or ID used to reference this germplasm
    + includeParents (Optional, ) ... If this parameter is true, include the array of parents in the response
    + includeSiblings (Optional, ) ... If this parameter is true, include the array of siblings in the response
    + includeProgeny (Optional, ) ... If this parameter is true, include the array of progeny in the response
    + includeFullTree (Optional, ) ... Recursively include ALL of the nodes present in this pedigree tree.
    + pedigreeDepth (Optional, ) ... Recursively include this number of levels up the tree in the response
    + progenyDepth (Optional, ) ... Recursively include this number of levels down the tree in the response
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + trialDbId (Optional, ) ... Use this parameter to only return results associated with the given `Trial` unique identifier. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
    + studyDbId (Optional, ) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + germplasmDbId (Optional, ) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + germplasmName (Optional, ) ... Use this parameter to only return results associated with the given `Germplasm` by its human readable name. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + germplasmPUI (Optional, ) ... Use this parameter to only return results associated with the given `Germplasm` by its global permanent unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
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
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "crossingProjectDbId": "625e745a",
                "crossingYear": 2005,
                "defaultDisplayName": "A0000003",
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
                "familyCode": "F0000203",
                "germplasmDbId": "1098ebaf",
                "germplasmName": "A0021004",
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "parents": [
                    {
                        "germplasmDbId": "b66958de",
                        "germplasmName": "A0000592",
                        "parentType": "MALE"
                    },
                    {
                        "germplasmDbId": "a55847ed",
                        "germplasmName": "A0000592",
                        "parentType": "FEMALE"
                    }
                ],
                "pedigreeString": "A0000001/A0000002",
                "progeny": [
                    {
                        "germplasmDbId": "e8d5dad7",
                        "germplasmName": "A0021011",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "ac07fbd8",
                        "germplasmName": "A0021012",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "07f45f67",
                        "germplasmName": "A0021013",
                        "parentType": "FEMALE"
                    }
                ],
                "siblings": [
                    {
                        "germplasmDbId": "334f53a3",
                        "germplasmName": "A0021005"
                    },
                    {
                        "germplasmDbId": "7bbbda8c",
                        "germplasmName": "A0021006"
                    },
                    {
                        "germplasmDbId": "ab1d9b26",
                        "germplasmName": "A0021007"
                    }
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Post - /pedigree [POST /brapi/v2/pedigree]

Send a list of new pedigree nodes to a server

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodDbId</span></td><td>string</td><td>The unique identifier for the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodName</span></td><td>string</td><td>The human readable name of the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>The crossing project used to generate this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingYear</span></td><td>integer</td><td>The year the parents were originally crossed</td></tr>
<tr><td><span style="font-weight:bold;">defaultDisplayName</span></td><td>string</td><td>Human readable name used for display purposes</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">familyCode</span></td><td>string</td><td>The code representing the family of this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUI</span></td><td>string</td><td>The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.</td></tr>
<tr><td><span style="font-weight:bold;">parents</span></td><td>array[object]</td><td>A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known.  <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">pedigreeString</span></td><td>string</td><td>The string representation of the pedigree for this germplasm in PURDY notation</td></tr>
<tr><td><span style="font-weight:bold;">progeny</span></td><td>array[object]</td><td>A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes. <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows        the type of parent this germplasm is to each of the child germplasm references. <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">siblings</span></td><td>array[object]</td><td>A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Siblings share at least one parent with the given germplasm.  <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodDbId</span></td><td>string</td><td>The unique identifier for the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodName</span></td><td>string</td><td>The human readable name of the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>The crossing project used to generate this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingYear</span></td><td>integer</td><td>The year the parents were originally crossed</td></tr>
<tr><td><span style="font-weight:bold;">defaultDisplayName</span></td><td>string</td><td>Human readable name used for display purposes</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">familyCode</span></td><td>string</td><td>The code representing the family of this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUI</span></td><td>string</td><td>The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.</td></tr>
<tr><td><span style="font-weight:bold;">parents</span></td><td>array[object]</td><td>A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known.  <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">pedigreeString</span></td><td>string</td><td>The string representation of the pedigree for this germplasm in PURDY notation</td></tr>
<tr><td><span style="font-weight:bold;">progeny</span></td><td>array[object]</td><td>A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes. <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows        the type of parent this germplasm is to each of the child germplasm references. <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">siblings</span></td><td>array[object]</td><td>A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Siblings share at least one parent with the given germplasm.  <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "breedingMethodDbId": "ffcce7ef",
        "breedingMethodName": "Male Backcross",
        "crossingProjectDbId": "625e745a",
        "crossingYear": 2005,
        "defaultDisplayName": "A0000003",
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
        "familyCode": "F0000203",
        "germplasmDbId": "1098ebaf",
        "germplasmName": "A0021004",
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "parents": [
            {
                "germplasmDbId": "b66958de",
                "germplasmName": "A0000592",
                "parentType": "MALE"
            },
            {
                "germplasmDbId": "a55847ed",
                "germplasmName": "A0000592",
                "parentType": "FEMALE"
            }
        ],
        "pedigreeString": "A0000001/A0000002",
        "progeny": [
            {
                "germplasmDbId": "e8d5dad7",
                "germplasmName": "A0021011",
                "parentType": "FEMALE"
            },
            {
                "germplasmDbId": "ac07fbd8",
                "germplasmName": "A0021012",
                "parentType": "FEMALE"
            },
            {
                "germplasmDbId": "07f45f67",
                "germplasmName": "A0021013",
                "parentType": "FEMALE"
            }
        ],
        "siblings": [
            {
                "germplasmDbId": "334f53a3",
                "germplasmName": "A0021005"
            },
            {
                "germplasmDbId": "7bbbda8c",
                "germplasmName": "A0021006"
            },
            {
                "germplasmDbId": "ab1d9b26",
                "germplasmName": "A0021007"
            }
        ]
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
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "crossingProjectDbId": "625e745a",
                "crossingYear": 2005,
                "defaultDisplayName": "A0000003",
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
                "familyCode": "F0000203",
                "germplasmDbId": "1098ebaf",
                "germplasmName": "A0021004",
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "parents": [
                    {
                        "germplasmDbId": "b66958de",
                        "germplasmName": "A0000592",
                        "parentType": "MALE"
                    },
                    {
                        "germplasmDbId": "a55847ed",
                        "germplasmName": "A0000592",
                        "parentType": "FEMALE"
                    }
                ],
                "pedigreeString": "A0000001/A0000002",
                "progeny": [
                    {
                        "germplasmDbId": "e8d5dad7",
                        "germplasmName": "A0021011",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "ac07fbd8",
                        "germplasmName": "A0021012",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "07f45f67",
                        "germplasmName": "A0021013",
                        "parentType": "FEMALE"
                    }
                ],
                "siblings": [
                    {
                        "germplasmDbId": "334f53a3",
                        "germplasmName": "A0021005"
                    },
                    {
                        "germplasmDbId": "7bbbda8c",
                        "germplasmName": "A0021006"
                    },
                    {
                        "germplasmDbId": "ab1d9b26",
                        "germplasmName": "A0021007"
                    }
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Put - /pedigree [PUT /brapi/v2/pedigree/]

Send a list of pedigree nodes to update existing information on a server

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodDbId</span></td><td>string</td><td>The unique identifier for the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodName</span></td><td>string</td><td>The human readable name of the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>The crossing project used to generate this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingYear</span></td><td>integer</td><td>The year the parents were originally crossed</td></tr>
<tr><td><span style="font-weight:bold;">defaultDisplayName</span></td><td>string</td><td>Human readable name used for display purposes</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">familyCode</span></td><td>string</td><td>The code representing the family of this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUI</span></td><td>string</td><td>The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.</td></tr>
<tr><td><span style="font-weight:bold;">parents</span></td><td>array[object]</td><td>A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known.  <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">pedigreeString</span></td><td>string</td><td>The string representation of the pedigree for this germplasm in PURDY notation</td></tr>
<tr><td><span style="font-weight:bold;">progeny</span></td><td>array[object]</td><td>A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes. <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows        the type of parent this germplasm is to each of the child germplasm references. <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">siblings</span></td><td>array[object]</td><td>A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Siblings share at least one parent with the given germplasm.  <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "<germplasmDbId_1>": {
        "breedingMethodDbId": "ffcce7ef",
        "breedingMethodName": "Male Backcross",
        "crossingProjectDbId": "625e745a",
        "crossingYear": 2005,
        "defaultDisplayName": "A0021004",
        "familyCode": "F0000203",
        "germplasmDbId": "<germplasmDbId_1>",
        "germplasmName": "A0021004",
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "parents": [
            {
                "germplasmDbId": "b66958de",
                "germplasmName": "A0000592",
                "parentType": "MALE"
            },
            {
                "germplasmDbId": "a55847ed",
                "germplasmName": "A0036658",
                "parentType": "FEMALE"
            }
        ],
        "pedigreeString": "A0000592/A0036658",
        "progeny": [
            {
                "germplasmDbId": "c66ddf14",
                "germplasmName": "A0006842",
                "parentType": "FEMALE"
            },
            {
                "germplasmDbId": "3a548793",
                "germplasmName": "A0037593",
                "parentType": "FEMALE"
            },
            {
                "germplasmDbId": "<germplasmDbId_2>",
                "germplasmName": "A0031485",
                "parentType": "MALE"
            }
        ],
        "siblings": [
            {
                "germplasmDbId": "46c9785f",
                "germplasmName": "A0001126"
            },
            {
                "germplasmDbId": "d7534a70",
                "germplasmName": "A0009514"
            }
        ]
    },
    "<germplasmDbId_2>": {
        "breedingMethodDbId": "ffcce7ef",
        "breedingMethodName": "Male Backcross",
        "crossingProjectDbId": "745ad753",
        "crossingYear": 2005,
        "defaultDisplayName": "A0031485",
        "familyCode": "F0000203",
        "germplasmDbId": "<germplasmDbId_2>",
        "germplasmName": "A0031485",
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "parents": [
            {
                "germplasmDbId": "<germplasmDbId_1>",
                "germplasmName": "A0021004",
                "parentType": "MALE"
            },
            {
                "germplasmDbId": "7eda5584",
                "germplasmName": "A0001126",
                "parentType": "FEMALE"
            }
        ],
        "pedigreeString": "A0021004/A0001126",
        "progeny": [
            {
                "germplasmDbId": "ddf14c66",
                "germplasmName": "A0001466",
                "parentType": "MALE"
            }
        ],
        "siblings": [
            {
                "germplasmDbId": "5f46c978",
                "germplasmName": "A0005469"
            }
        ]
    }
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
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "crossingProjectDbId": "625e745a",
                "crossingYear": 2005,
                "defaultDisplayName": "A0000003",
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
                "familyCode": "F0000203",
                "germplasmDbId": "1098ebaf",
                "germplasmName": "A0021004",
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "parents": [
                    {
                        "germplasmDbId": "b66958de",
                        "germplasmName": "A0000592",
                        "parentType": "MALE"
                    },
                    {
                        "germplasmDbId": "a55847ed",
                        "germplasmName": "A0000592",
                        "parentType": "FEMALE"
                    }
                ],
                "pedigreeString": "A0000001/A0000002",
                "progeny": [
                    {
                        "germplasmDbId": "e8d5dad7",
                        "germplasmName": "A0021011",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "ac07fbd8",
                        "germplasmName": "A0021012",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "07f45f67",
                        "germplasmName": "A0021013",
                        "parentType": "FEMALE"
                    }
                ],
                "siblings": [
                    {
                        "germplasmDbId": "334f53a3",
                        "germplasmName": "A0021005"
                    },
                    {
                        "germplasmDbId": "7bbbda8c",
                        "germplasmName": "A0021006"
                    },
                    {
                        "germplasmDbId": "ab1d9b26",
                        "germplasmName": "A0021007"
                    }
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Post - /search/pedigree [POST /brapi/v2/search/pedigree]

Submit a search request for `Pedigree`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/germplasm/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">accessionNumbers</span></td><td>array[string]</td><td>A collection of unique identifiers for materials or germplasm within a genebank  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").</td></tr>
<tr><td><span style="font-weight:bold;">binomialNames</span></td><td>array[string]</td><td>List of the full binomial name (scientific name) to identify a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">collections</span></td><td>array[string]</td><td>A specific panel/collection/population name this germplasm belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">familyCodes</span></td><td>array[string]</td><td>A familyCode representing the family this germplasm belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">genus</span></td><td>array[string]</td><td>List of Genus names to identify germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUIs</span></td><td>array[string]</td><td>List of Permanent Unique Identifiers to identify germplasm</td></tr>
<tr><td><span style="font-weight:bold;">includeFullTree</span></td><td>boolean</td><td>If this parameter is true, recursively include ALL of the nodes available in this pedigree tree</td></tr>
<tr><td><span style="font-weight:bold;">includeParents</span></td><td>boolean</td><td>If this parameter is true, include the array of parents in the response</td></tr>
<tr><td><span style="font-weight:bold;">includeProgeny</span></td><td>boolean</td><td>If this parameter is true, include the array of progeny in the response</td></tr>
<tr><td><span style="font-weight:bold;">includeSiblings</span></td><td>boolean</td><td>If this parameter is true, include the array of siblings in the response</td></tr>
<tr><td><span style="font-weight:bold;">instituteCodes</span></td><td>array[string]</td><td>The code for the institute that maintains the material.  <br/> MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">pedigreeDepth</span></td><td>integer</td><td>Recursively include this number of levels up the tree in the response (parents, grand-parents, great-grand-parents, etc)</td></tr>
<tr><td><span style="font-weight:bold;">progenyDepth</span></td><td>integer</td><td>Recursively include this number of levels down the tree in the response (children, grand-children, great-grand-children, etc)</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">species</span></td><td>array[string]</td><td>List of Species names to identify germplasm</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>List of alternative names or IDs used to reference this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodDbId</span></td><td>string</td><td>The unique identifier for the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodName</span></td><td>string</td><td>The human readable name of the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>The crossing project used to generate this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingYear</span></td><td>integer</td><td>The year the parents were originally crossed</td></tr>
<tr><td><span style="font-weight:bold;">defaultDisplayName</span></td><td>string</td><td>Human readable name used for display purposes</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">familyCode</span></td><td>string</td><td>The code representing the family of this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUI</span></td><td>string</td><td>The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.</td></tr>
<tr><td><span style="font-weight:bold;">parents</span></td><td>array[object]</td><td>A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known.  <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">pedigreeString</span></td><td>string</td><td>The string representation of the pedigree for this germplasm in PURDY notation</td></tr>
<tr><td><span style="font-weight:bold;">progeny</span></td><td>array[object]</td><td>A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes. <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows        the type of parent this germplasm is to each of the child germplasm references. <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">siblings</span></td><td>array[object]</td><td>A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Siblings share at least one parent with the given germplasm.  <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accessionNumbers": [
        "A0000003",
        "A0000477"
    ],
    "binomialNames": [
        "Aspergillus fructus",
        "Zea mays"
    ],
    "collections": [
        "RDP1",
        "MDP1"
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
    "familyCodes": [
        "f0000203",
        "fa009965"
    ],
    "genus": [
        "Aspergillus",
        "Zea"
    ],
    "germplasmDbIds": [
        "e9c6edd7",
        "1b1df4a6"
    ],
    "germplasmNames": [
        "A0000003",
        "A0000477"
    ],
    "germplasmPUIs": [
        "http://pui.per/accession/A0000003",
        "http://pui.per/accession/A0000477"
    ],
    "includeFullTree": true,
    "includeParents": true,
    "includeProgeny": true,
    "includeSiblings": true,
    "instituteCodes": [
        "PER001",
        "NOR001"
    ],
    "page": 0,
    "pageSize": 1000,
    "pedigreeDepth": 3,
    "progenyDepth": 3,
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "species": [
        "fructus",
        "mays"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "synonyms": [
        "variety_1",
        "2c38f9b6"
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
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "crossingProjectDbId": "625e745a",
                "crossingYear": 2005,
                "defaultDisplayName": "A0000003",
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
                "familyCode": "F0000203",
                "germplasmDbId": "1098ebaf",
                "germplasmName": "A0021004",
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "parents": [
                    {
                        "germplasmDbId": "b66958de",
                        "germplasmName": "A0000592",
                        "parentType": "MALE"
                    },
                    {
                        "germplasmDbId": "a55847ed",
                        "germplasmName": "A0000592",
                        "parentType": "FEMALE"
                    }
                ],
                "pedigreeString": "A0000001/A0000002",
                "progeny": [
                    {
                        "germplasmDbId": "e8d5dad7",
                        "germplasmName": "A0021011",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "ac07fbd8",
                        "germplasmName": "A0021012",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "07f45f67",
                        "germplasmName": "A0021013",
                        "parentType": "FEMALE"
                    }
                ],
                "siblings": [
                    {
                        "germplasmDbId": "334f53a3",
                        "germplasmName": "A0021005"
                    },
                    {
                        "germplasmDbId": "7bbbda8c",
                        "germplasmName": "A0021006"
                    },
                    {
                        "germplasmDbId": "ab1d9b26",
                        "germplasmName": "A0021007"
                    }
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




### Get - /search/pedigree/{searchResultsDbId} [GET /brapi/v2/search/pedigree/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Pedigree` search request <br/>
Clients should submit a search request using the corresponding `POST /search/germplasm` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodDbId</span></td><td>string</td><td>The unique identifier for the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">breedingMethodName</span></td><td>string</td><td>The human readable name of the breeding method used to create this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>The crossing project used to generate this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">crossingYear</span></td><td>integer</td><td>The year the parents were originally crossed</td></tr>
<tr><td><span style="font-weight:bold;">defaultDisplayName</span></td><td>string</td><td>Human readable name used for display purposes</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">familyCode</span></td><td>string</td><td>The code representing the family of this germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmPUI</span></td><td>string</td><td>The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.</td></tr>
<tr><td><span style="font-weight:bold;">parents</span></td><td>array[object]</td><td>A list of parent germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Typically, this array should only have one parent (clonal or self) or two parents (cross). In some special cases, there may be more parents, usually when the exact parent is not known.  <br/> If the parameter 'includeParents' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>parents<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">pedigreeString</span></td><td>string</td><td>The string representation of the pedigree for this germplasm in PURDY notation</td></tr>
<tr><td><span style="font-weight:bold;">progeny</span></td><td>array[object]</td><td>A list of germplasm references that are direct children of this germplasm. These represent edges in the tree, connecting to other nodes. <br/> The given germplasm could have a large number of progeny, across a number of different breeding methods. The 'parentType' shows        the type of parent this germplasm is to each of the child germplasm references. <br/> If the parameter 'includeProgeny' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
<tr><td>progeny<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. </td></tr>
<tr><td><span style="font-weight:bold;">siblings</span></td><td>array[object]</td><td>A list of sibling germplasm references in the pedigree tree for this germplasm. These represent edges in the tree, connecting to other nodes. <br/> Siblings share at least one parent with the given germplasm.  <br/> If the parameter 'includeSiblings' is set to false, then this array should be empty, null, or not present in the response.</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>siblings<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>A human readable name for a germplasm</td></tr>
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
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "crossingProjectDbId": "625e745a",
                "crossingYear": 2005,
                "defaultDisplayName": "A0000003",
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
                "familyCode": "F0000203",
                "germplasmDbId": "1098ebaf",
                "germplasmName": "A0021004",
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "parents": [
                    {
                        "germplasmDbId": "b66958de",
                        "germplasmName": "A0000592",
                        "parentType": "MALE"
                    },
                    {
                        "germplasmDbId": "a55847ed",
                        "germplasmName": "A0000592",
                        "parentType": "FEMALE"
                    }
                ],
                "pedigreeString": "A0000001/A0000002",
                "progeny": [
                    {
                        "germplasmDbId": "e8d5dad7",
                        "germplasmName": "A0021011",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "ac07fbd8",
                        "germplasmName": "A0021012",
                        "parentType": "FEMALE"
                    },
                    {
                        "germplasmDbId": "07f45f67",
                        "germplasmName": "A0021013",
                        "parentType": "FEMALE"
                    }
                ],
                "siblings": [
                    {
                        "germplasmDbId": "334f53a3",
                        "germplasmName": "A0021005"
                    },
                    {
                        "germplasmDbId": "7bbbda8c",
                        "germplasmName": "A0021006"
                    },
                    {
                        "germplasmDbId": "ab1d9b26",
                        "germplasmName": "A0021007"
                    }
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

