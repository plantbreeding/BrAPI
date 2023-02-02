# Group VariantSets





### Post - /search/variantsets [POST /brapi/v2/search/variantsets]

Submit a search request for `VariantSets`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/variantsets/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>The unique identifier representing a CallSet</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">referenceDbIds</span></td><td>array[string]</td><td>The unique identifier representing a genotype Reference</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbIds</span></td><td>array[string]</td><td>The unique identifier representing a genotype ReferenceSet</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>The unique identifier representing a Variant</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>The unique identifier representing a VariantSet</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">analysis</span></td><td>array[object]</td><td>Set of Analysis descriptors for this VariantSet</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisDbId</span></td><td>string</td><td>Unique identifier for this analysis description</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisName</span></td><td>string</td><td>A human readable name for this analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.created</span></td><td>string<br>(date-time)</td><td>The time at which this record was created, in ISO 8601 format.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>A human readable description of the analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.software</span></td><td>array[string]</td><td>The software run to generate this analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.updated</span></td><td>string<br>(date-time)</td><td>The time at which this record was last updated, in ISO 8601 format.</td></tr>
<tr><td><span style="font-weight:bold;">availableFormats</span></td><td>array[object]</td><td>When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.  <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc) <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.dataFormat</span></td><td>string</td><td>dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileFormat</span></td><td>string</td><td>fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string<br>(uri)</td><td>A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">callSetCount</span></td><td>integer</td><td>The number of CallSets included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">metadataFields</span></td><td>array[object]</td><td>The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet.  <br> When possible, these field names and abbreviations should follow the VCF standard </td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The ID of the reference set that describes the sequences used by the variants in this set.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID of the dataset this variant set belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantCount</span></td><td>integer</td><td>The number of Variants included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "9569cfc4",
        "da1e888c"
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
        "89ab4d17",
        "74d3b63d"
    ],
    "referenceSetDbIds": [
        "d3b63d4d",
        "3b63d74b"
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
    "variantDbIds": [
        "c80f068b",
        "eb7c5f50"
    ],
    "variantSetDbIds": [
        "b2903842",
        "dcbb8558"
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
                "analysis": [
                    {
                        "analysisDbId": "6191a6bd",
                        "analysisName": "Standard QC",
                        "created": "2018-01-01T14:47:23-0600",
                        "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                        "software": [
                            "https://github.com/genotyping/QC"
                        ],
                        "type": "QC",
                        "updated": "2018-01-01T14:47:23-0600"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "expandHomozygotes": true,
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": "",
                        "sepPhased": "|",
                        "sepUnphased": "/",
                        "unknownString": "."
                    }
                ],
                "callSetCount": 341,
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
                "metadataFields": [
                    {
                        "dataType": "integer",
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality"
                    }
                ],
                "referenceSetDbId": "57eae639",
                "studyDbId": "2fc3b034",
                "variantCount": 250,
                "variantSetDbId": "87a6ac1e",
                "variantSetName": "Maize QC DataSet 002334"
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




### Get - /search/variantsets/{searchResultsDbId} [GET /brapi/v2/search/variantsets/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `VariantSets` search request <br/>
Clients should submit a search request using the corresponding `POST /search/variantsets` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">analysis</span></td><td>array[object]</td><td>Set of Analysis descriptors for this VariantSet</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisDbId</span></td><td>string</td><td>Unique identifier for this analysis description</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisName</span></td><td>string</td><td>A human readable name for this analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.created</span></td><td>string<br>(date-time)</td><td>The time at which this record was created, in ISO 8601 format.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>A human readable description of the analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.software</span></td><td>array[string]</td><td>The software run to generate this analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.updated</span></td><td>string<br>(date-time)</td><td>The time at which this record was last updated, in ISO 8601 format.</td></tr>
<tr><td><span style="font-weight:bold;">availableFormats</span></td><td>array[object]</td><td>When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.  <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc) <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.dataFormat</span></td><td>string</td><td>dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileFormat</span></td><td>string</td><td>fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string<br>(uri)</td><td>A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">callSetCount</span></td><td>integer</td><td>The number of CallSets included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">metadataFields</span></td><td>array[object]</td><td>The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet.  <br> When possible, these field names and abbreviations should follow the VCF standard </td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The ID of the reference set that describes the sequences used by the variants in this set.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID of the dataset this variant set belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantCount</span></td><td>integer</td><td>The number of Variants included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
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
                "analysis": [
                    {
                        "analysisDbId": "6191a6bd",
                        "analysisName": "Standard QC",
                        "created": "2018-01-01T14:47:23-0600",
                        "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                        "software": [
                            "https://github.com/genotyping/QC"
                        ],
                        "type": "QC",
                        "updated": "2018-01-01T14:47:23-0600"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "expandHomozygotes": true,
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": "",
                        "sepPhased": "|",
                        "sepUnphased": "/",
                        "unknownString": "."
                    }
                ],
                "callSetCount": 341,
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
                "metadataFields": [
                    {
                        "dataType": "integer",
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality"
                    }
                ],
                "referenceSetDbId": "57eae639",
                "studyDbId": "2fc3b034",
                "variantCount": 250,
                "variantSetDbId": "87a6ac1e",
                "variantSetName": "Maize QC DataSet 002334"
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




### Get - /variantsets [GET /brapi/v2/variantsets{?variantSetDbId}{?variantDbId}{?callSetDbId}{?referenceSetDbId}{?commonCropName}{?programDbId}{?studyDbId}{?studyName}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Will return a filtered list of `VariantSet`.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">analysis</span></td><td>array[object]</td><td>Set of Analysis descriptors for this VariantSet</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisDbId</span></td><td>string</td><td>Unique identifier for this analysis description</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisName</span></td><td>string</td><td>A human readable name for this analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.created</span></td><td>string<br>(date-time)</td><td>The time at which this record was created, in ISO 8601 format.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>A human readable description of the analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.software</span></td><td>array[string]</td><td>The software run to generate this analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.updated</span></td><td>string<br>(date-time)</td><td>The time at which this record was last updated, in ISO 8601 format.</td></tr>
<tr><td><span style="font-weight:bold;">availableFormats</span></td><td>array[object]</td><td>When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.  <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc) <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.dataFormat</span></td><td>string</td><td>dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileFormat</span></td><td>string</td><td>fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string<br>(uri)</td><td>A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">callSetCount</span></td><td>integer</td><td>The number of CallSets included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">metadataFields</span></td><td>array[object]</td><td>The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet.  <br> When possible, these field names and abbreviations should follow the VCF standard </td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The ID of the reference set that describes the sequences used by the variants in this set.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID of the dataset this variant set belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantCount</span></td><td>integer</td><td>The number of Variants included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
</table>


 

+ Parameters
    + variantSetDbId (Optional, ) ... The ID of the `VariantSet` to be retrieved.
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + referenceSetDbId (Optional, ) ... The ID of the reference set that describes the sequences used by the variants in this set.
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + studyDbId (Optional, ) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + studyName (Optional, ) ... Use this parameter to only return results associated with the given `Study` by its human readable name. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
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
                "analysis": [
                    {
                        "analysisDbId": "6191a6bd",
                        "analysisName": "Standard QC",
                        "created": "2018-01-01T14:47:23-0600",
                        "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                        "software": [
                            "https://github.com/genotyping/QC"
                        ],
                        "type": "QC",
                        "updated": "2018-01-01T14:47:23-0600"
                    }
                ],
                "availableFormats": [
                    {
                        "dataFormat": [
                            "DartSeq",
                            "VCF",
                            "Hapmap",
                            "tabular",
                            "JSON"
                        ],
                        "expandHomozygotes": true,
                        "fileFormat": [
                            "text/csv",
                            "text/tsv",
                            "application/excel",
                            "application/zip",
                            "application/json"
                        ],
                        "fileURL": "",
                        "sepPhased": "|",
                        "sepUnphased": "/",
                        "unknownString": "."
                    }
                ],
                "callSetCount": 341,
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
                "metadataFields": [
                    {
                        "dataType": "integer",
                        "fieldAbbreviation": "GQ",
                        "fieldName": "Genotype Quality"
                    }
                ],
                "referenceSetDbId": "57eae639",
                "studyDbId": "2fc3b034",
                "variantCount": 250,
                "variantSetDbId": "87a6ac1e",
                "variantSetName": "Maize QC DataSet 002334"
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




### Post - /variantsets/extract [POST /brapi/v2/variantsets/extract]

Will perform a search for `Calls` which match the search criteria in `variantSetsExtractRequest`. The results of the search will be used to create a new `VariantSet` on the server. The new `VariantSet` will be returned.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">callSetDbIds</span></td><td>array[string]</td><td>The CallSet to search.</td></tr>
<tr><td><span style="font-weight:bold;">expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td><span style="font-weight:bold;">sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">variantDbIds</span></td><td>array[string]</td><td>The Variant to search.</td></tr>
<tr><td><span style="font-weight:bold;">variantSetDbIds</span></td><td>array[string]</td><td>The VariantSet to search.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">analysis</span></td><td>array[object]</td><td>Set of Analysis descriptors for this VariantSet</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisDbId</span></td><td>string</td><td>Unique identifier for this analysis description</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisName</span></td><td>string</td><td>A human readable name for this analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.created</span></td><td>string<br>(date-time)</td><td>The time at which this record was created, in ISO 8601 format.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>A human readable description of the analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.software</span></td><td>array[string]</td><td>The software run to generate this analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.updated</span></td><td>string<br>(date-time)</td><td>The time at which this record was last updated, in ISO 8601 format.</td></tr>
<tr><td><span style="font-weight:bold;">availableFormats</span></td><td>array[object]</td><td>When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.  <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc) <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.dataFormat</span></td><td>string</td><td>dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileFormat</span></td><td>string</td><td>fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string<br>(uri)</td><td>A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">callSetCount</span></td><td>integer</td><td>The number of CallSets included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">metadataFields</span></td><td>array[object]</td><td>The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet.  <br> When possible, these field names and abbreviations should follow the VCF standard </td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The ID of the reference set that describes the sequences used by the variants in this set.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID of the dataset this variant set belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantCount</span></td><td>integer</td><td>The number of Variants included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "callSetDbIds": [
        "9569cfc4",
        "da1e888c"
    ],
    "expandHomozygotes": true,
    "sepPhased": "~",
    "sepUnphased": "|",
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "unknownString": "-",
    "variantDbIds": [
        "c80f068b",
        "eb7c5f50"
    ],
    "variantSetDbIds": [
        "b2903842",
        "dcbb8558"
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
        "additionalInfo": {},
        "analysis": [
            {
                "analysisDbId": "6191a6bd",
                "analysisName": "Standard QC",
                "created": "2018-01-01T14:47:23-0600",
                "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                "software": [
                    "https://github.com/genotyping/QC"
                ],
                "type": "QC",
                "updated": "2018-01-01T14:47:23-0600"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": [
                    "DartSeq",
                    "VCF",
                    "Hapmap",
                    "tabular",
                    "JSON"
                ],
                "expandHomozygotes": true,
                "fileFormat": [
                    "text/csv",
                    "text/tsv",
                    "application/excel",
                    "application/zip",
                    "application/json"
                ],
                "fileURL": "",
                "sepPhased": "|",
                "sepUnphased": "/",
                "unknownString": "."
            }
        ],
        "callSetCount": 341,
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
        "metadataFields": [
            {
                "dataType": "integer",
                "fieldAbbreviation": "GQ",
                "fieldName": "Genotype Quality"
            }
        ],
        "referenceSetDbId": "57eae639",
        "studyDbId": "2fc3b034",
        "variantCount": 250,
        "variantSetDbId": "87a6ac1e",
        "variantSetName": "Maize QC DataSet 002334"
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




### Get - /variantsets/{variantSetDbId} [GET /brapi/v2/variantsets/{variantSetDbId}]

This call will return a JSON version of a `VariantSet`.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">variantSetDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">analysis</span></td><td>array[object]</td><td>Set of Analysis descriptors for this VariantSet</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisDbId</span></td><td>string</td><td>Unique identifier for this analysis description</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.analysisName</span></td><td>string</td><td>A human readable name for this analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.created</span></td><td>string<br>(date-time)</td><td>The time at which this record was created, in ISO 8601 format.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>A human readable description of the analysis</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.software</span></td><td>array[string]</td><td>The software run to generate this analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of analysis.</td></tr>
<tr><td>analysis<br><span style="font-weight:bold;margin-left:5px">.updated</span></td><td>string<br>(date-time)</td><td>The time at which this record was last updated, in ISO 8601 format.</td></tr>
<tr><td><span style="font-weight:bold;">availableFormats</span></td><td>array[object]</td><td>When the data for a VariantSet is retrieved, it can be retrieved in a variety of data formats and file formats.  <br/>'dataFormat' defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc) <br/>'fileFormat' defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.dataFormat</span></td><td>string</td><td>dataFormat defines the structure of the data within a file (ie DartSeq, VCF, Hapmap, tabular, etc)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.expandHomozygotes</span></td><td>boolean</td><td>Should homozygotes be expanded (true) or collapsed into a single occurrence (false)</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileFormat</span></td><td>string</td><td>fileFormat defines the MIME type of the file (ie text/csv, application/excel, application/zip). This should also be reflected in the Accept and ContentType HTTP headers for every relevant request and response.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string<br>(uri)</td><td>A URL which indicates the location of the file version of this VariantSet. Could be a static file URL or an API endpoint which generates the file.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepPhased</span></td><td>string</td><td>The string used as a separator for phased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.sepUnphased</span></td><td>string</td><td>The string used as a separator for unphased allele calls.</td></tr>
<tr><td>availableFormats<br><span style="font-weight:bold;margin-left:5px">.unknownString</span></td><td>string</td><td>The string used as a representation for missing data.</td></tr>
<tr><td><span style="font-weight:bold;">callSetCount</span></td><td>integer</td><td>The number of CallSets included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">metadataFields</span></td><td>array[object]</td><td>The 'metadataFields' array indicates which types of genotyping data and metadata are available in the VariantSet.  <br> When possible, these field names and abbreviations should follow the VCF standard </td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The type of field represented in this Genotype Field. This is intended to help parse the data out of JSON.</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldAbbreviation</span></td><td>string</td><td>The abbreviated code of the field represented in this Genotype Field. These codes should match the VCF standard when possible. Examples include: "GQ", "RD", and "HQ"</td></tr>
<tr><td>metadataFields<br><span style="font-weight:bold;margin-left:5px">.fieldName</span></td><td>string</td><td>The name of the field represented in this Genotype Field. Examples include: "Genotype Quality", "Read Depth", and "Haplotype Quality"</td></tr>
<tr><td><span style="font-weight:bold;">referenceSetDbId</span></td><td>string</td><td>The ID of the reference set that describes the sequences used by the variants in this set.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID of the dataset this variant set belongs to.</td></tr>
<tr><td><span style="font-weight:bold;">variantCount</span></td><td>integer</td><td>The number of Variants included in this VariantSet</td></tr>
<tr><td><span style="font-weight:bold;">variantSetName</span></td><td>string</td><td>The human readable name for a VariantSet</td></tr>
</table>


 

+ Parameters
    + variantSetDbId (Required, ) ... The ID of the `Variant` to be retrieved.
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
        "analysis": [
            {
                "analysisDbId": "6191a6bd",
                "analysisName": "Standard QC",
                "created": "2018-01-01T14:47:23-0600",
                "description": "This is a formal description of a QC methodology. Blah blah blah ...",
                "software": [
                    "https://github.com/genotyping/QC"
                ],
                "type": "QC",
                "updated": "2018-01-01T14:47:23-0600"
            }
        ],
        "availableFormats": [
            {
                "dataFormat": [
                    "DartSeq",
                    "VCF",
                    "Hapmap",
                    "tabular",
                    "JSON"
                ],
                "expandHomozygotes": true,
                "fileFormat": [
                    "text/csv",
                    "text/tsv",
                    "application/excel",
                    "application/zip",
                    "application/json"
                ],
                "fileURL": "",
                "sepPhased": "|",
                "sepUnphased": "/",
                "unknownString": "."
            }
        ],
        "callSetCount": 341,
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
        "metadataFields": [
            {
                "dataType": "integer",
                "fieldAbbreviation": "GQ",
                "fieldName": "Genotype Quality"
            }
        ],
        "referenceSetDbId": "57eae639",
        "studyDbId": "2fc3b034",
        "variantCount": 250,
        "variantSetDbId": "87a6ac1e",
        "variantSetName": "Maize QC DataSet 002334"
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




### Get - /variantsets/{variantSetDbId}/calls [GET /brapi/v2/variantsets/{variantSetDbId}/calls{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageToken}{?page}{?pageSize}]

Gets a list of `Calls` associated with a `VariantSet`.



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
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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




### Get - /variantsets/{variantSetDbId}/callsets [GET /brapi/v2/variantsets/{variantSetDbId}/callsets{?callSetDbId}{?callSetName}{?page}{?pageSize}]

Gets a list of `CallSets` associated with a `VariantSet`.



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
    + callSetDbId (Optional, ) ... The ID of the `CallSet` to be retrieved.
    + callSetName (Optional, ) ... The human readable name of the `CallSet` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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




### Get - /variantsets/{variantSetDbId}/variants [GET /brapi/v2/variantsets/{variantSetDbId}/variants{?variantDbId}{?pageToken}{?page}{?pageSize}]

This call will return an array of `Variants`.



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
    + variantDbId (Optional, ) ... The ID of the `Variant` to be retrieved.
    + variantSetDbId (Required, ) ... The ID of the `VariantSet` to be retrieved.
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

