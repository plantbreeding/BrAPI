
# Group Traits

API to manage the details of observation variable Traits. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Trait describes what property is being observed. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Trait "Leaf length" or "Flower height". 






### Get - /traits [GET /brapi/v2/traits{?traitDbId}{?observationVariableDbId}{?ontologyDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Call to retrieve a list of traits available in the system and their associated variables.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.'



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">traitDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td><span style="font-weight:bold;">attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td><span style="font-weight:bold;">entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td><span style="font-weight:bold;">traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td><span style="font-weight:bold;">traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + traitDbId (Optional, ) ... The unique identifier for a trait
    + observationVariableDbId (Optional, ) ... The unique identifier for an observation variable
    + ontologyDbId (Optional, ) ... The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology Use `GET /ontologies` to find the list of available ontologies on a server.
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
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
<tr><td><span style="font-weight:bold;">traitName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td><span style="font-weight:bold;">attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td><span style="font-weight:bold;">entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td><span style="font-weight:bold;">traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td><span style="font-weight:bold;">traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">traitDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td><span style="font-weight:bold;">attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td><span style="font-weight:bold;">entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td><span style="font-weight:bold;">traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td><span style="font-weight:bold;">traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
<tr><td><span style="font-weight:bold;">traitDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td><span style="font-weight:bold;">attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td><span style="font-weight:bold;">entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td><span style="font-weight:bold;">traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td><span style="font-weight:bold;">traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
<tr><td><span style="font-weight:bold;">traitName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td><span style="font-weight:bold;">attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td><span style="font-weight:bold;">entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td><span style="font-weight:bold;">traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td><span style="font-weight:bold;">traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">traitDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td><span style="font-weight:bold;">attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td><span style="font-weight:bold;">entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td><span style="font-weight:bold;">traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td><span style="font-weight:bold;">traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td><span style="font-weight:bold;">traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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

