
# Group Methods

API to manage the details of observation variable Methods. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Method describes the way an observation should be collected. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Method "estimation" or "drone image processing". 






### Get - /methods [GET /brapi/v2/methods{?methodDbId}{?observationVariableDbId}{?ontologyDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Returns a list of Methods available on a server.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.'



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + methodDbId (Optional, ) ... The unique identifier for a method
    + observationVariableDbId (Optional, ) ... The unique identifier for an observation variable
    + ontologyDbId (Optional, ) ... The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology Use `GET /ontologies` to find the list of available ontologies on a server.
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
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
                "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
                "description": "A measuring tape was used",
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
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "methodPUI": "http://my-traits.com/trait/CO_123:0000212",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": "OBO"
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
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




### Post - /methods [POST /brapi/v2/methods]

Create new method objects in the database

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
        "description": "A measuring tape was used",
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
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodName": "Measuring Tape",
        "methodPUI": "http://my-traits.com/trait/CO_123:0000212",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        }
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
                "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
                "description": "A measuring tape was used",
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
                "formula": "a^2 + b^2 = c^2",
                "methodClass": "Measurement",
                "methodDbId": "0adb2764",
                "methodName": "Measuring Tape",
                "methodPUI": "http://my-traits.com/trait/CO_123:0000212",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": "OBO"
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
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




### Get - /methods/{methodDbId} [GET /brapi/v2/methods/{methodDbId}]

Retrieve details about a specific method

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
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
        "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
        "description": "A measuring tape was used",
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
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "methodPUI": "http://my-traits.com/trait/CO_123:0000212",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
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




### Put - /methods/{methodDbId} [PUT /brapi/v2/methods/{methodDbId}/]

Update the details of an existing method

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
    "description": "A measuring tape was used",
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
    "formula": "a^2 + b^2 = c^2",
    "methodClass": "Measurement",
    "methodName": "Measuring Tape",
    "methodPUI": "http://my-traits.com/trait/CO_123:0000212",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                "type": "OBO"
            }
        ],
        "ontologyDbId": "6b071868",
        "ontologyName": "The Crop Ontology",
        "version": "7.2.3"
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
        "additionalInfo": {},
        "bibliographicalReference": "Smith, 1893, Really Cool Paper, Popular Journal",
        "description": "A measuring tape was used",
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
        "formula": "a^2 + b^2 = c^2",
        "methodClass": "Measurement",
        "methodDbId": "0adb2764",
        "methodName": "Measuring Tape",
        "methodPUI": "http://my-traits.com/trait/CO_123:0000212",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": "OBO"
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
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

