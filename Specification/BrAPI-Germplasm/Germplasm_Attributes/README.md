# Group Germplasm Attributes
Germplasm "attributes" are simply-inherited characteristics (characterization descriptors) that are not environment-dependent but 
inherent in the germplasm line.  They include genes, QTLs, and genetic "traits" like wheat grain 
hardness.  They are often evaluated by genotyping for diagnostic markers.






### Get - /attributes [GET /brapi/v2/attributes{?attributeCategory}{?attributeDbId}{?attributeName}{?attributePUI}{?methodDbId}{?methodName}{?methodPUI}{?scaleDbId}{?scaleName}{?scalePUI}{?traitDbId}{?traitName}{?traitPUI}{?commonCropName}{?programDbId}{?germplasmDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

List available attributes.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies this attribute within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
</table>


 

+ Parameters
    + attributeCategory (Optional, ) ... The general category for the attribute. very similar to Trait class.
    + attributeDbId (Optional, ) ... The unique id for an attribute
    + attributeName (Optional, ) ... The human readable name for an attribute
    + attributePUI (Optional, ) ... The Permanent Unique Identifier of an Attribute, usually in the form of a URI
    + methodDbId (Optional, ) ... Method unique identifier
    + methodName (Optional, ) ... Human readable name for the method<br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation
    + methodPUI (Optional, ) ... The Permanent Unique Identifier of a Method, usually in the form of a URI
    + scaleDbId (Optional, ) ... Scale unique identifier
    + scaleName (Optional, ) ... Human readable name for the scale<br/>MIAPPE V1.1 (DM-88) Scale  Name of the scale of observation
    + scalePUI (Optional, ) ... The Permanent Unique Identifier of a Scale, usually in the form of a URI
    + traitDbId (Optional, ) ... Trait unique identifier
    + traitName (Optional, ) ... Human readable name for the trait<br/>MIAPPE V1.1 (DM-88) Trait  Name of the trait of observation
    + traitPUI (Optional, ) ... The Permanent Unique Identifier of a Trait, usually in the form of a URI
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + germplasmDbId (Optional, ) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
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
                "attributeCategory": "Morphological",
                "attributeDbId": "2f08b902",
                "attributeDescription": "Height of the plant measured in meters by a tape",
                "attributeName": "Plant Height 1",
                "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": "2.0",
                "documentationURL": "https://wiki.brapi.org/documentation.html",
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
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
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
                },
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
                "scale": {
                    "additionalInfo": {},
                    "dataType": "Numerical",
                    "decimalPlaces": 2,
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
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                    "units": "m",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "maximumValue": "9999",
                        "min": 2,
                        "minimumValue": "2"
                    }
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
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




### Post - /attributes [POST /brapi/v2/attributes]

Create new Germplasm Attributes

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies this attribute within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "attributeCategory": "Morphological",
        "attributeDescription": "Height of the plant measured in meters by a tape",
        "attributeName": "Plant Height 1",
        "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": "2.0",
        "documentationURL": "https://wiki.brapi.org/documentation.html",
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
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
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
        },
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
        "scale": {
            "additionalInfo": {},
            "dataType": "Numerical",
            "decimalPlaces": 2,
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
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
            "units": "m",
            "validValues": {
                "categories": [
                    {
                        "label": "low",
                        "value": "0"
                    },
                    {
                        "label": "medium",
                        "value": "5"
                    },
                    {
                        "label": "high",
                        "value": "10"
                    }
                ],
                "max": 9999,
                "maximumValue": "9999",
                "min": 2,
                "minimumValue": "2"
            }
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
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
                "attributeCategory": "Morphological",
                "attributeDbId": "2f08b902",
                "attributeDescription": "Height of the plant measured in meters by a tape",
                "attributeName": "Plant Height 1",
                "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": "2.0",
                "documentationURL": "https://wiki.brapi.org/documentation.html",
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
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
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
                },
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
                "scale": {
                    "additionalInfo": {},
                    "dataType": "Numerical",
                    "decimalPlaces": 2,
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
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                    "units": "m",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "maximumValue": "9999",
                        "min": 2,
                        "minimumValue": "2"
                    }
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
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




### Get - /attributes/categories [GET /brapi/v2/attributes/categories{?page}{?pageSize}]

List all available attribute categories.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


 

+ Parameters
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
            "Morphological",
            "Agronomic"
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




### Get - /attributes/{attributeDbId} [GET /brapi/v2/attributes/{attributeDbId}]

Get the details for a specific Germplasm Attribute



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies this attribute within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
</table>


 

+ Parameters
    + attributeDbId (Required, ) ... The unique id for an attribute
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
        "attributeCategory": "Morphological",
        "attributeDbId": "2f08b902",
        "attributeDescription": "Height of the plant measured in meters by a tape",
        "attributeName": "Plant Height 1",
        "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": "2.0",
        "documentationURL": "https://wiki.brapi.org/documentation.html",
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
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
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
        },
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
        "scale": {
            "additionalInfo": {},
            "dataType": "Numerical",
            "decimalPlaces": 2,
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
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
            "units": "m",
            "validValues": {
                "categories": [
                    {
                        "label": "low",
                        "value": "0"
                    },
                    {
                        "label": "medium",
                        "value": "5"
                    },
                    {
                        "label": "high",
                        "value": "10"
                    }
                ],
                "max": 9999,
                "maximumValue": "9999",
                "min": 2,
                "minimumValue": "2"
            }
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
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




### Put - /attributes/{attributeDbId} [PUT /brapi/v2/attributes/{attributeDbId}/]

Update an existing Germplasm Attribute

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies this attribute within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
</table>


 

+ Parameters
    + attributeDbId (Required, ) ... The unique id for an attribute
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "attributeCategory": "Morphological",
    "attributeDescription": "Height of the plant measured in meters by a tape",
    "attributeName": "Plant Height 1",
    "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
    "commonCropName": "Maize",
    "contextOfUse": [
        "Trial evaluation",
        "Nursery evaluation"
    ],
    "defaultValue": "2.0",
    "documentationURL": "https://wiki.brapi.org/documentation.html",
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
    "growthStage": "flowering",
    "institution": "The BrAPI Institute",
    "language": "en",
    "method": {
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
    },
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
    "scale": {
        "additionalInfo": {},
        "dataType": "Numerical",
        "decimalPlaces": 2,
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
        "scaleDbId": "af730171",
        "scaleName": "Meters",
        "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
        "units": "m",
        "validValues": {
            "categories": [
                {
                    "label": "low",
                    "value": "0"
                },
                {
                    "label": "medium",
                    "value": "5"
                },
                {
                    "label": "high",
                    "value": "10"
                }
            ],
            "max": 9999,
            "maximumValue": "9999",
            "min": 2,
            "minimumValue": "2"
        }
    },
    "scientist": "Dr. Bob Robertson",
    "status": "recommended",
    "submissionTimestamp": "2018-01-01T14:47:23-0600",
    "synonyms": [
        "Maize Height",
        "Stalk Height",
        "Corn Height"
    ],
    "trait": {
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
        "attributeCategory": "Morphological",
        "attributeDbId": "2f08b902",
        "attributeDescription": "Height of the plant measured in meters by a tape",
        "attributeName": "Plant Height 1",
        "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": "2.0",
        "documentationURL": "https://wiki.brapi.org/documentation.html",
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
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
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
        },
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
        "scale": {
            "additionalInfo": {},
            "dataType": "Numerical",
            "decimalPlaces": 2,
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
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
            "units": "m",
            "validValues": {
                "categories": [
                    {
                        "label": "low",
                        "value": "0"
                    },
                    {
                        "label": "medium",
                        "value": "5"
                    },
                    {
                        "label": "high",
                        "value": "10"
                    }
                ],
                "max": 9999,
                "maximumValue": "9999",
                "min": 2,
                "minimumValue": "2"
            }
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
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




### Post - /search/attributes [POST /brapi/v2/search/attributes]

Submit a search request for Germplasm `Attributes`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/attributes/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeCategories</span></td><td>array[string]</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDbIds</span></td><td>array[string]</td><td>List of Germplasm Attribute IDs to search for</td></tr>
<tr><td><span style="font-weight:bold;">attributeNames</span></td><td>array[string]</td><td>List of human readable Germplasm Attribute names to search for</td></tr>
<tr><td><span style="font-weight:bold;">attributePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">dataTypes</span></td><td>array[string]</td><td>List of scale data types to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">methodDbIds</span></td><td>array[string]</td><td>List of methods to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">methodNames</span></td><td>array[string]</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td><span style="font-weight:bold;">methodPUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyDbIds</span></td><td>array[string]</td><td>List of ontology IDs to search for</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">scaleDbIds</span></td><td>array[string]</td><td>The unique identifier for a Scale</td></tr>
<tr><td><span style="font-weight:bold;">scaleNames</span></td><td>array[string]</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td><span style="font-weight:bold;">scalePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `studyDbIds`. Github issue number #483  <br>The unique ID of a studies to filter on</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">traitAttributePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">traitAttributes</span></td><td>array[string]</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td><span style="font-weight:bold;">traitClasses</span></td><td>array[string]</td><td>List of trait classes to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">traitDbIds</span></td><td>array[string]</td><td>The unique identifier for a Trait</td></tr>
<tr><td><span style="font-weight:bold;">traitEntities</span></td><td>array[string]</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td><span style="font-weight:bold;">traitEntityPUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td><span style="font-weight:bold;">traitNames</span></td><td>array[string]</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td><span style="font-weight:bold;">traitPUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies this attribute within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "attributeCategories": [
        "Morphological",
        "Physical"
    ],
    "attributeDbIds": [
        "2ef15c9f",
        "318e7f7d"
    ],
    "attributeNames": [
        "Plant Height 1",
        "Root Color"
    ],
    "attributePUIs": [
        "http://my-traits.com/trait/CO_123:0008012",
        "http://my-traits.com/trait/CO_123:0007261"
    ],
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "dataTypes": [
        "Numerical",
        "Ordinal",
        "Text"
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
    "methodDbIds": [
        "07e34f83",
        "d3d5517a"
    ],
    "methodNames": [
        "Measuring Tape",
        "Spectrometer"
    ],
    "methodPUIs": [
        "http://my-traits.com/trait/CO_123:0000212",
        "http://my-traits.com/trait/CO_123:0003557"
    ],
    "ontologyDbIds": [
        "f44f7b23",
        "a26b576e"
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
    "scaleDbIds": [
        "a13ecffa",
        "7e1afe4f"
    ],
    "scaleNames": [
        "Meters",
        "Liters"
    ],
    "scalePUIs": [
        "http://my-traits.com/trait/CO_123:0000336",
        "http://my-traits.com/trait/CO_123:0000560"
    ],
    "studyDbId": [
        "5bcac0ae",
        "7f48e22d"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "traitAttributePUIs": [
        "http://my-traits.com/trait/CO_123:0008336",
        "http://my-traits.com/trait/CO_123:0001092"
    ],
    "traitAttributes": [
        "Height",
        "Color"
    ],
    "traitClasses": [
        "morphological",
        "phenological",
        "agronomical"
    ],
    "traitDbIds": [
        "ef81147b",
        "78d82fad"
    ],
    "traitEntities": [
        "Stalk",
        "Root"
    ],
    "traitEntityPUIs": [
        "http://my-traits.com/trait/CO_123:0004098",
        "http://my-traits.com/trait/CO_123:0002366"
    ],
    "traitNames": [
        "Stalk Height",
        "Root Color"
    ],
    "traitPUIs": [
        "http://my-traits.com/trait/CO_123:0000456",
        "http://my-traits.com/trait/CO_123:0000820"
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
                "attributeCategory": "Morphological",
                "attributeDbId": "2f08b902",
                "attributeDescription": "Height of the plant measured in meters by a tape",
                "attributeName": "Plant Height 1",
                "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": "2.0",
                "documentationURL": "https://wiki.brapi.org/documentation.html",
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
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
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
                },
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
                "scale": {
                    "additionalInfo": {},
                    "dataType": "Numerical",
                    "decimalPlaces": 2,
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
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                    "units": "m",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "maximumValue": "9999",
                        "min": 2,
                        "minimumValue": "2"
                    }
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
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




### Get - /search/attributes/{searchResultsDbId} [GET /brapi/v2/search/attributes/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a Germplasm `Attributes` search request <br/>
Clients should submit a search request using the corresponding `POST /search/attributes` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">attributeDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The ID which uniquely identifies this attribute within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">attributeName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this attribute</td></tr>
<tr><td><span style="font-weight:bold;">method</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">attributeCategory</span></td><td>string</td><td>General category for the attribute. very similar to Trait class.</td></tr>
<tr><td><span style="font-weight:bold;">attributeDescription</span></td><td>string</td><td>A human readable description of this attribute</td></tr>
<tr><td><span style="font-weight:bold;">attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of an Attribute, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td><span style="font-weight:bold;">contextOfUse</span></td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td><span style="font-weight:bold;">defaultValue</span></td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">growthStage</span></td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td><span style="font-weight:bold;">institution</span></td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td><span style="font-weight:bold;">language</span></td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
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
                "attributeCategory": "Morphological",
                "attributeDbId": "2f08b902",
                "attributeDescription": "Height of the plant measured in meters by a tape",
                "attributeName": "Plant Height 1",
                "attributePUI": "http://my-traits.com/trait/CO_123:0008012",
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": "2.0",
                "documentationURL": "https://wiki.brapi.org/documentation.html",
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
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
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
                },
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
                "scale": {
                    "additionalInfo": {},
                    "dataType": "Numerical",
                    "decimalPlaces": 2,
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
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                    "units": "m",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "maximumValue": "9999",
                        "min": 2,
                        "minimumValue": "2"
                    }
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
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

