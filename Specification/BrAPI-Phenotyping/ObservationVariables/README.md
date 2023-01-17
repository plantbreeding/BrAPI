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
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">dataTypes</span></td><td>array[string]</td><td>List of scale data types to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">methodDbIds</span></td><td>array[string]</td><td>List of methods to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">methodNames</span></td><td>array[string]</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td><span style="font-weight:bold;">methodPUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbIds</span></td><td>array[string]</td><td>The DbIds of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableNames</span></td><td>array[string]</td><td>The names of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI</td></tr>
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + trialDbId (Optional, ) ... Use this parameter to only return results associated with the given `Trial` unique identifier. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
    + studyDbId (Optional, ) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Human readable name of an Observation Variable  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Human readable name of an Observation Variable  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
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
<tr><td><span style="font-weight:bold;">method</span></td><td>object</td><td>A description of the way an Observation should be collected.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Method "estimation" or "drone image processing". </td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.bibliographicalReference</span></td><td>string</td><td>Bibliographical reference describing the method. <br/>MIAPPE V1.1 (DM-91) Reference associated to the method - URI/DOI of reference describing the method.</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.description</span></td><td>string</td><td>Method description <br/>MIAPPE V1.1 (DM-90) Method description - Textual description of the method, which may extend a method defined in an external reference with specific parameters, e.g. growth stage, inoculation precise organ (leaf number)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>method<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.formula</span></td><td>string</td><td>For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodClass</span></td><td>string</td><td>Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodDbId</span></td><td>string</td><td>Method unique identifier</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodName</span></td><td>string</td><td>Human readable name for the method <br/>MIAPPE V1.1 (DM-88) Method  Name of the method of observation</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.methodPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Method, usually in the form of a URI</td></tr>
<tr><td>method<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>method<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>Variable unique identifier  MIAPPE V1.1 (DM-83) Variable ID - Code used to identify the variable in the data file. We recommend using a variable definition from the Crop Ontology where possible. Otherwise, the Crop Ontology naming convention is recommended: <trait abbreviation>_<method abbreviation>_<scale abbreviation>). A variable ID must be unique within a given investigation.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>Variable name (usually a short name)  MIAPPE V1.1 (DM-84) Variable name - Name of the variable.</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">scale</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>scale<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>scale<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleDbId</span></td><td>string</td><td>Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string</td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>scale<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>scale<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>scale<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td><span style="font-weight:bold;">scientist</span></td><td>string</td><td>Name of scientist submitting the variable.</td></tr>
<tr><td><span style="font-weight:bold;">status</span></td><td>string</td><td>Variable status. (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td><span style="font-weight:bold;">submissionTimestamp</span></td><td>string<br>(date-time)</td><td>Timestamp when the Variable was added (ISO 8601)</td></tr>
<tr><td><span style="font-weight:bold;">synonyms</span></td><td>array[string]</td><td>Other variable names</td></tr>
<tr><td><span style="font-weight:bold;">trait</span></td><td>object</td><td>A Trait describes what property is being observed.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Trait "Leaf length" or "Flower height". </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.alternativeAbbreviations</span></td><td>array[string]</td><td>A list of shortened, human readable, names for a Trait. These abbreviations are acceptable alternatives to the mainAbbreviation and do not need to follow any formatting convention.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attribute</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.attributePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Attribute, usually in the form of a URI <br/>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entity</span></td><td>string</td><td>A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.entityPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait Entity, usually in the form of a URI <br/>A Trait can be decomposed as "Trait" = "Entity" + "Attribute", the Entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain" </td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>trait<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.mainAbbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string</td><td>Ontology database unique identifier</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string</td><td>Ontology name</td></tr>
<tr><td>trait<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>Trait status (examples: "recommended", "obsolete", "legacy", etc.)</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.synonyms</span></td><td>array[string]</td><td>Other trait names</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitClass</span></td><td>string</td><td>A classification to describe the type of trait and the context it should be considered in. <br/> examples- "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDbId</span></td><td>string</td><td>The ID which uniquely identifies a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitDescription</span></td><td>string</td><td>The description of a trait</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitName</span></td><td>string</td><td>The human readable name of a trait <br/>MIAPPE V1.1 (DM-86) Trait - Name of the (plant or environmental) trait under observation</td></tr>
<tr><td>trait<br><span style="font-weight:bold;margin-left:5px">.traitPUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Trait, usually in the form of a URI</td></tr>
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

