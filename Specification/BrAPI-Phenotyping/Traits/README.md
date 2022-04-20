
# Group Traits

API to manage the details of observation variable Traits. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Trait describes what property is being observed. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Trait "Leaf length" or "Flower height". 






### Get - /traits [GET /brapi/v2/traits{?traitDbId}{?observationVariableDbId}{?ontologyDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Call to retrieve a list of traits available in the system and their associated variables.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.'



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + traitDbId (Optional, ) ... The unique identifier for a trait
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
                "alternativeAbbreviations": [
                    "H",
                    "PH",
                    "H1"
                ],
                "attribute": "height",
                "attributePUI": "http://my-traits.com/trait/PO:00012345",
                "entity": "Stalk",
                "entityPUI": "http://my-traits.com/trait/PATO:00098765",
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
                "mainAbbreviation": "PH",
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
                },
                "status": "recommended",
                "synonyms": [
                    "Height",
                    "Plant Height",
                    "Stalk Height",
                    "Canopy Height"
                ],
                "traitClass": "phenological",
                "traitDbId": "9b2e34f5",
                "traitDescription": "The height of the plant",
                "traitName": "Height",
                "traitPUI": "http://my-traits.com/trait/CO_123:0000012"
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




### Post - /traits [POST /brapi/v2/traits]

Create new trait objects in the database

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "alternativeAbbreviations": [
            "H",
            "PH",
            "H1"
        ],
        "attribute": "height",
        "attributePUI": "http://my-traits.com/trait/PO:00012345",
        "entity": "Stalk",
        "entityPUI": "http://my-traits.com/trait/PATO:00098765",
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
        "mainAbbreviation": "PH",
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
        },
        "status": "recommended",
        "synonyms": [
            "Height",
            "Plant Height",
            "Stalk Height",
            "Canopy Height"
        ],
        "traitClass": "phenological",
        "traitDescription": "The height of the plant",
        "traitName": "Height",
        "traitPUI": "http://my-traits.com/trait/CO_123:0000012"
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
                "alternativeAbbreviations": [
                    "H",
                    "PH",
                    "H1"
                ],
                "attribute": "height",
                "attributePUI": "http://my-traits.com/trait/PO:00012345",
                "entity": "Stalk",
                "entityPUI": "http://my-traits.com/trait/PATO:00098765",
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
                "mainAbbreviation": "PH",
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
                },
                "status": "recommended",
                "synonyms": [
                    "Height",
                    "Plant Height",
                    "Stalk Height",
                    "Canopy Height"
                ],
                "traitClass": "phenological",
                "traitDbId": "9b2e34f5",
                "traitDescription": "The height of the plant",
                "traitName": "Height",
                "traitPUI": "http://my-traits.com/trait/CO_123:0000012"
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




### Get - /traits/{traitDbId} [GET /brapi/v2/traits/{traitDbId}]

Retrieve the details of a single trait

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + traitDbId (Required, ) ... Id of the trait to retrieve details of.
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
        "alternativeAbbreviations": [
            "H",
            "PH",
            "H1"
        ],
        "attribute": "height",
        "attributePUI": "http://my-traits.com/trait/PO:00012345",
        "entity": "Stalk",
        "entityPUI": "http://my-traits.com/trait/PATO:00098765",
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
        "mainAbbreviation": "PH",
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
        },
        "status": "recommended",
        "synonyms": [
            "Height",
            "Plant Height",
            "Stalk Height",
            "Canopy Height"
        ],
        "traitClass": "phenological",
        "traitDbId": "9b2e34f5",
        "traitDescription": "The height of the plant",
        "traitName": "Height",
        "traitPUI": "http://my-traits.com/trait/CO_123:0000012"
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




### Put - /traits/{traitDbId} [PUT /brapi/v2/traits/{traitDbId}/]

Update an existing trait

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + traitDbId (Required, ) ... Id of the trait to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "alternativeAbbreviations": [
        "H",
        "PH",
        "H1"
    ],
    "attribute": "height",
    "attributePUI": "http://my-traits.com/trait/PO:00012345",
    "entity": "Stalk",
    "entityPUI": "http://my-traits.com/trait/PATO:00098765",
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
    "mainAbbreviation": "PH",
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
    },
    "status": "recommended",
    "synonyms": [
        "Height",
        "Plant Height",
        "Stalk Height",
        "Canopy Height"
    ],
    "traitClass": "phenological",
    "traitDescription": "The height of the plant",
    "traitName": "Height",
    "traitPUI": "http://my-traits.com/trait/CO_123:0000012"
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
        "alternativeAbbreviations": [
            "H",
            "PH",
            "H1"
        ],
        "attribute": "height",
        "attributePUI": "http://my-traits.com/trait/PO:00012345",
        "entity": "Stalk",
        "entityPUI": "http://my-traits.com/trait/PATO:00098765",
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
        "mainAbbreviation": "PH",
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
        },
        "status": "recommended",
        "synonyms": [
            "Height",
            "Plant Height",
            "Stalk Height",
            "Canopy Height"
        ],
        "traitClass": "phenological",
        "traitDbId": "9b2e34f5",
        "traitDescription": "The height of the plant",
        "traitName": "Height",
        "traitPUI": "http://my-traits.com/trait/CO_123:0000012"
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

