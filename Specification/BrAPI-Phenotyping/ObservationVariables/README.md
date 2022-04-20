# Group Observation Variables

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.





### Post - /search/variables [POST /brapi/v2/search/variables]

Submit a search request for Observation `Variables`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/variables/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>commonCropNames</td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td>dataTypes</td><td>array[string]</td><td>List of scale data types to filter search results</td></tr>
<tr><td>externalReferenceIDs</td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td>externalReferenceIds</td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td>externalReferenceSources</td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td>methodDbIds</td><td>array[string]</td><td>List of methods to filter search results</td></tr>
<tr><td>methodNames</td><td>array[string]</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>methodPUIs</td><td>array[string]</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The DbIds of Variables to search for</td></tr>
<tr><td>observationVariableNames</td><td>array[string]</td><td>The names of Variables to search for</td></tr>
<tr><td>observationVariablePUIs</td><td>array[string]</td><td>The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI</td></tr>
<tr><td>ontologyDbIds</td><td>array[string]</td><td>List of ontology IDs to search for</td></tr>
<tr><td>page</td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td>pageSize</td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td>programDbIds</td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td>programNames</td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td>scaleDbIds</td><td>array[string]</td><td>The unique identifier for a Scale</td></tr>
<tr><td>scaleNames</td><td>array[string]</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scalePUIs</td><td>array[string]</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>studyDbId</td><td>array[string]</td><td>**Deprecated in v2.1** Please use `studyDbIds`. Github issue number #483  The unique ID of a studies to filter on</td></tr>
<tr><td>studyDbIds</td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td>studyNames</td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td>traitAttributePUIs</td><td>array[string]</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>traitAttributes</td><td>array[string]</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>traitClasses</td><td>array[string]</td><td>List of trait classes to filter search results</td></tr>
<tr><td>traitDbIds</td><td>array[string]</td><td>The unique identifier for a Trait</td></tr>
<tr><td>traitEntities</td><td>array[string]</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>traitEntityPUIs</td><td>array[string]</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>traitNames</td><td>array[string]</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>traitPUIs</td><td>array[string]</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
<tr><td>trialDbIds</td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td>trialNames</td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableDbId</td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
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
    "observationVariableDbIds": [
        "a646187d",
        "6d23513b"
    ],
    "observationVariableNames": [
        "Plant Height in meters",
        "Wheat rust score 1-5"
    ],
    "observationVariablePUIs": [
        "http://my-traits.com/trait/CO_123:0008012",
        "http://my-traits.com/trait/CO_123:0007261"
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
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
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




### Get - /search/variables/{searchResultsDbId} [GET /brapi/v2/search/variables/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a Observation `variables` search request <br/>
Clients should submit a search request using the corresponding `POST /search/variables` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableDbId</td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
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




### Get - /variables [GET /brapi/v2/variables{?observationVariableDbId}{?observationVariableName}{?observationVariablePUI}{?traitClass}{?methodDbId}{?methodName}{?methodPUI}{?scaleDbId}{?scaleName}{?scalePUI}{?traitDbId}{?traitName}{?traitPUI}{?ontologyDbId}{?commonCropName}{?programDbId}{?trialDbId}{?studyDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Call to retrieve a list of observationVariables available in the system.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableDbId</td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + observationVariableDbId (Optional, ) ... Variable's unique ID
    + observationVariableName (Optional, ) ... Human readable name of an Observation Variable
    + observationVariablePUI (Optional, ) ... The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI
    + traitClass (Optional, ) ... Variable's trait class (phenological, physiological, morphological, etc.)
    + methodDbId (Optional, ) ... Method unique identifier
    + methodName (Optional, ) ... Human readable name for the method<br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation
    + methodPUI (Optional, ) ... The Permanent Unique Identifier of a Method, usually in the form of a URI
    + scaleDbId (Optional, ) ... Scale unique identifier
    + scaleName (Optional, ) ... Human readable name for the scale<br/>MIAPPE V1.1 (DM-88) Scale  Name of the scale of observation
    + scalePUI (Optional, ) ... The Permanent Unique Identifier of a Scale, usually in the form of a URI
    + traitDbId (Optional, ) ... Trait unique identifier
    + traitName (Optional, ) ... Human readable name for the trait<br/>MIAPPE V1.1 (DM-88) Trait  Name of the trait of observation
    + traitPUI (Optional, ) ... The Permanent Unique Identifier of a Trait, usually in the form of a URI
    + ontologyDbId (Optional, ) ... The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology Use `GET /ontologies` to find the list of available ontologies on a server.
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
    + trialDbId (Optional, ) ... Use this parameter to only return results associated with the given Trial unique identifier. <br/>Use `GET /trials` to find the list of available Trials on a server.
    + studyDbId (Optional, ) ... Use this parameter to only return results associated with the given Study unique identifier. <br/>Use `GET /studies` to find the list of available Studies on a server.
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
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
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




### Post - /variables [POST /brapi/v2/variables]

Add new Observation Variables to the system.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Human readable name of an Observation Variable</td></tr>
<tr><td>observationVariablePUI</td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableDbId</td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
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
        "observationVariableName": "Variable Name",
        "observationVariablePUI": "http://my-traits.com/trait/CO_123:0009012",
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
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
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




### Get - /variables/{observationVariableDbId} [GET /brapi/v2/variables/{observationVariableDbId}]

Retrieve variable details



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableDbId</td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + observationVariableDbId (Required, ) ... string id of the variable
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
        "observationVariableDbId": "b9b7edd1",
        "observationVariableName": "Variable Name",
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Put - /variables/{observationVariableDbId} [PUT /brapi/v2/variables/{observationVariableDbId}/]

Update an existing Observation Variable

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Human readable name of an Observation Variable</td></tr>
<tr><td>observationVariablePUI</td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Crop name (examples: "Maize", "Wheat")</td></tr>
<tr><td>contextOfUse</td><td>array[string]</td><td>Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])</td></tr>
<tr><td>defaultValue</td><td>string</td><td>Variable default value. (examples: "red", "2.3", etc.)</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthStage</td><td>string</td><td>Growth stage at which measurement is made (examples: "flowering")</td></tr>
<tr><td>institution</td><td>string</td><td>Name of institution submitting the variable</td></tr>
<tr><td>language</td><td>string</td><td>2 letter ISO 639-1 code for the language of submission of the variable.</td></tr>
<tr><td>method</td><td>object</td><td></td></tr>
<tr><td>method.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>method.<br>bibliographicalReference</td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method.<br>description</td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method.<br>formula</td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method.<br>methodClass</td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method.<br>methodDbId</td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method.<br>methodName</td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method.<br>methodPUI</td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>method.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>observationVariableDbId</td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td>observationVariableName</td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale</td><td>object</td><td>Scale metadata</td></tr>
<tr><td>scale.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>scale.<br>dataType</td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale.<br>decimalPlaces</td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale.<br>scaleDbId</td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale.<br>scaleName</td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale.<br>scalePUI</td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale.<br>units</td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale.<br>validValues</td><td>object</td><td></td></tr>
<tr><td>scale.<br>validValues.<br>categories</td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>label</td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale.<br>validValues.<br>categories.<br>value</td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale.<br>validValues.<br>max</td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450   Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>maximumValue</td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>min</td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br/>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale.<br>validValues.<br>minimumValue</td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scientist</td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td>status</td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>submissionTimestamp</td><td>string (date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td>synonyms</td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td>trait</td><td>object</td><td></td></tr>
<tr><td>trait.<br>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>trait.<br>alternativeAbbreviations</td><td>array[string]</td><td>Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention</td></tr>
<tr><td>trait.<br>attribute</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>attributePUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait.<br>entity</td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait.<br>entityPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait.<br>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait.<br>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait.<br>mainAbbreviation</td><td>string</td><td>Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")</td></tr>
<tr><td>trait.<br>ontologyReference</td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks</td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>URL</td><td>string (uri)</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>documentationLinks.<br>type</td><td>string</td><td></td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyDbId</td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait.<br>ontologyReference.<br>ontologyName</td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait.<br>ontologyReference.<br>version</td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait.<br>status</td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait.<br>synonyms</td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait.<br>traitClass</td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait.<br>traitDbId</td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait.<br>traitDescription</td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait.<br>traitName</td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait.<br>traitPUI</td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


 

+ Parameters
    + observationVariableDbId (Required, ) ... string id of the variable
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
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
    "observationVariableName": "Variable Name",
    "observationVariablePUI": "http://my-traits.com/trait/CO_123:0009012",
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
        "observationVariableDbId": "b9b7edd1",
        "observationVariableName": "Variable Name",
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

