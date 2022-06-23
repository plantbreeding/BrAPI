
# Group Scales

API to manage the details of observation variable Scales. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Scale describes the units and acceptable values for a Variable. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Scale "inches" or "pixels". 






### Get - /scales [GET /brapi/v2/scales{?scaleDbId}{?observationVariableDbId}{?ontologyDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Returns a list of Scales available on a server.

An Observation Variable has 3 critical parts; A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td><span style="font-weight:bold;">decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td><span style="font-weight:bold;">scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td><span style="font-weight:bold;">scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td><span style="font-weight:bold;">validValues</span></td><td>object</td><td></td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
</table>


 

+ Parameters
    + scaleDbId (Optional, ) ... The unique identifier for a scale
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




### Post - /scales [POST /brapi/v2/scales]

Create new scale objects in the database

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td><span style="font-weight:bold;">decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td><span style="font-weight:bold;">scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td><span style="font-weight:bold;">validValues</span></td><td>object</td><td></td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td><span style="font-weight:bold;">decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td><span style="font-weight:bold;">scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td><span style="font-weight:bold;">scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td><span style="font-weight:bold;">validValues</span></td><td>object</td><td></td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
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




### Get - /scales/{scaleDbId} [GET /brapi/v2/scales/{scaleDbId}]

Retrieve details about a specific scale

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td><span style="font-weight:bold;">decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td><span style="font-weight:bold;">scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td><span style="font-weight:bold;">scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td><span style="font-weight:bold;">validValues</span></td><td>object</td><td></td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
</table>


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
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




### Put - /scales/{scaleDbId} [PUT /brapi/v2/scales/{scaleDbId}/]

Update the details of an existing scale

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td><span style="font-weight:bold;">decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td><span style="font-weight:bold;">scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td><span style="font-weight:bold;">validValues</span></td><td>object</td><td></td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td><span style="font-weight:bold;">decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td><span style="font-weight:bold;">scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td><span style="font-weight:bold;">scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td><span style="font-weight:bold;">validValues</span></td><td>object</td><td></td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
</table>


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
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

