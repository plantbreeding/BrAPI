
# Group Study

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).

Note that dates should be provided in extended ISO 8601 format (for example, "YYYY-MM-DD").

A "study" in BrAPI represents an "study" in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).





### Post - /search/studies [POST /brapi/v2/search/studies]

Submit a search request for `Studies`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/studies/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>commonCropNames</td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td>externalReferenceIDs</td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td>externalReferenceIds</td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td>externalReferenceSources</td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td>germplasmDbIds</td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td>germplasmNames</td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td>locationDbIds</td><td>array[string]</td><td>The location ids to search for</td></tr>
<tr><td>locationNames</td><td>array[string]</td><td>A human readable names to search for</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The DbIds of Variables to search for</td></tr>
<tr><td>observationVariableNames</td><td>array[string]</td><td>The names of Variables to search for</td></tr>
<tr><td>observationVariablePUIs</td><td>array[string]</td><td>The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI</td></tr>
<tr><td>page</td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td>pageSize</td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td>programDbIds</td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td>programNames</td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td>seasonDbIds</td><td>array[string]</td><td>The ID which uniquely identifies a season</td></tr>
<tr><td>sortBy</td><td>string</td><td>Name of one of the fields within the study object on which results can be sorted</td></tr>
<tr><td>sortOrder</td><td>string</td><td>Order results should be sorted. ex. "ASC" or "DESC"</td></tr>
<tr><td>studyCodes</td><td>array[string]</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDbIds</td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td>studyNames</td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td>studyPUIs</td><td>array[string]</td><td>Permanent unique identifier associated with study data. For example, a URI or DOI</td></tr>
<tr><td>studyTypes</td><td>array[string]</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbIds</td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td>trialNames</td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "active": true,
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
    "locationDbIds": [
        "b28911cf",
        "5071d1e4"
    ],
    "locationNames": [
        "Location Alpha",
        "The Large Hadron Collider"
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
    "seasonDbIds": [
        "Harvest Two 2017",
        "Summer 2018"
    ],
    "sortBy": [
        "studyDbId",
        "trialDbId",
        "programDbId",
        "locationDbId",
        "seasonDbId",
        "studyType",
        "studyName",
        "studyLocation",
        "programName",
        "germplasmDbId",
        "observationVariableDbId"
    ],
    "sortOrder": [
        "ASC",
        "DESC"
    ],
    "studyCodes": [
        "Grape_Yield_Spring_2018",
        "Walnut_Kenya"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "studyPUIs": [
        "doi:10.155454/12349537312",
        "https://pui.per/d8dd35e1"
    ],
    "studyTypes": [
        "Yield Trial",
        "Disease Resistance Trial"
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
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Grape",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
                "dataLinks": [
                    {
                        "dataFormat": "Image Archive",
                        "description": "Raw drone images collected for this study",
                        "fileFormat": "application/zip",
                        "name": "image-archive.zip",
                        "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
                        "scientificType": "Environmental",
                        "url": "https://brapi.org/image-archive.zip",
                        "version": "1.0.3"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01T14:47:23-0600",
                "environmentParameters": [
                    {
                        "description": "the soil type was clay",
                        "parameterName": "soil type",
                        "parameterPUI": "PECO:0007155",
                        "unit": "pH",
                        "unitPUI": "PECO:0007059",
                        "value": "clay soil",
                        "valuePUI": "ENVO:00002262"
                    }
                ],
                "experimentalDesign": {
                    "PUI": "CO_715:0000145",
                    "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
                },
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
                "growthFacility": {
                    "PUI": "CO_715:0000162",
                    "description": "field environment condition, greenhouse"
                },
                "lastUpdate": {
                    "timestamp": "2018-01-01T14:47:23-0600",
                    "version": "1.2.3"
                },
                "license": "MIT License",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "observationLevels": [
                    {
                        "levelName": "field",
                        "levelOrder": 0
                    },
                    {
                        "levelName": "block",
                        "levelOrder": 1
                    },
                    {
                        "levelName": "plot",
                        "levelOrder": 2
                    }
                ],
                "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
                "observationVariableDbIds": [
                    "57c236f9",
                    "48b327ea",
                    "a5b367c5"
                ],
                "seasons": [
                    "Spring_2018"
                ],
                "startDate": "2018-01-01T14:47:23-0600",
                "studyCode": "Grape_Yield_Spring_2018",
                "studyDbId": "175ac75a",
                "studyDescription": "This is a yield study for Spring 2018",
                "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
                "studyPUI": "doi:10.155454/12349537312",
                "studyType": "Phenotyping",
                "trialDbId": "48b327ea",
                "trialName": "Grape_Yield_Trial"
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




### Get - /search/studies/{searchResultsDbId} [GET /brapi/v2/search/studies/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Studies` search request <br/>
Clients should submit a search request using the corresponding `POST /search/studies` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
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
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Grape",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
                "dataLinks": [
                    {
                        "dataFormat": "Image Archive",
                        "description": "Raw drone images collected for this study",
                        "fileFormat": "application/zip",
                        "name": "image-archive.zip",
                        "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
                        "scientificType": "Environmental",
                        "url": "https://brapi.org/image-archive.zip",
                        "version": "1.0.3"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01T14:47:23-0600",
                "environmentParameters": [
                    {
                        "description": "the soil type was clay",
                        "parameterName": "soil type",
                        "parameterPUI": "PECO:0007155",
                        "unit": "pH",
                        "unitPUI": "PECO:0007059",
                        "value": "clay soil",
                        "valuePUI": "ENVO:00002262"
                    }
                ],
                "experimentalDesign": {
                    "PUI": "CO_715:0000145",
                    "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
                },
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
                "growthFacility": {
                    "PUI": "CO_715:0000162",
                    "description": "field environment condition, greenhouse"
                },
                "lastUpdate": {
                    "timestamp": "2018-01-01T14:47:23-0600",
                    "version": "1.2.3"
                },
                "license": "MIT License",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "observationLevels": [
                    {
                        "levelName": "field",
                        "levelOrder": 0
                    },
                    {
                        "levelName": "block",
                        "levelOrder": 1
                    },
                    {
                        "levelName": "plot",
                        "levelOrder": 2
                    }
                ],
                "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
                "observationVariableDbIds": [
                    "57c236f9",
                    "48b327ea",
                    "a5b367c5"
                ],
                "seasons": [
                    "Spring_2018"
                ],
                "startDate": "2018-01-01T14:47:23-0600",
                "studyCode": "Grape_Yield_Spring_2018",
                "studyDbId": "175ac75a",
                "studyDescription": "This is a yield study for Spring 2018",
                "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
                "studyPUI": "doi:10.155454/12349537312",
                "studyType": "Phenotyping",
                "trialDbId": "48b327ea",
                "trialName": "Grape_Yield_Trial"
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




### Get - /studies [GET /brapi/v2/studies{?studyType}{?locationDbId}{?seasonDbId}{?trialDbId}{?studyDbId}{?studyName}{?studyCode}{?studyPUI}{?germplasmDbId}{?observationVariableDbId}{?active}{?sortBy}{?sortOrder}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get list of studies

StartDate and endDate should be ISO-8601 format for dates



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + studyType (Optional, ) ... Filter based on study type unique identifier
    + locationDbId (Optional, ) ... Filter by location
    + seasonDbId (Optional, ) ... Filter by season or year
    + trialDbId (Optional, ) ... Filter by trial
    + studyDbId (Optional, ) ... Filter by study DbId
    + studyName (Optional, ) ... Filter by study name
    + studyCode (Optional, ) ... Filter by study code
    + studyPUI (Optional, ) ... Filter by study PUI
    + germplasmDbId (Optional, ) ... Filter by germplasm DbId
    + observationVariableDbId (Optional, ) ... Filter by observation variable DbId
    + active (Optional, ) ... Filter active status true/false.
    + sortBy (Optional, ) ... Name of the field to sort by.
    + sortOrder (Optional, ) ... Sort order direction. Ascending/Descending.
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
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Grape",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
                "dataLinks": [
                    {
                        "dataFormat": "Image Archive",
                        "description": "Raw drone images collected for this study",
                        "fileFormat": "application/zip",
                        "name": "image-archive.zip",
                        "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
                        "scientificType": "Environmental",
                        "url": "https://brapi.org/image-archive.zip",
                        "version": "1.0.3"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01T14:47:23-0600",
                "environmentParameters": [
                    {
                        "description": "the soil type was clay",
                        "parameterName": "soil type",
                        "parameterPUI": "PECO:0007155",
                        "unit": "pH",
                        "unitPUI": "PECO:0007059",
                        "value": "clay soil",
                        "valuePUI": "ENVO:00002262"
                    }
                ],
                "experimentalDesign": {
                    "PUI": "CO_715:0000145",
                    "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
                },
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
                "growthFacility": {
                    "PUI": "CO_715:0000162",
                    "description": "field environment condition, greenhouse"
                },
                "lastUpdate": {
                    "timestamp": "2018-01-01T14:47:23-0600",
                    "version": "1.2.3"
                },
                "license": "MIT License",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "observationLevels": [
                    {
                        "levelName": "field",
                        "levelOrder": 0
                    },
                    {
                        "levelName": "block",
                        "levelOrder": 1
                    },
                    {
                        "levelName": "plot",
                        "levelOrder": 2
                    }
                ],
                "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
                "observationVariableDbIds": [
                    "57c236f9",
                    "48b327ea",
                    "a5b367c5"
                ],
                "seasons": [
                    "Spring_2018"
                ],
                "startDate": "2018-01-01T14:47:23-0600",
                "studyCode": "Grape_Yield_Spring_2018",
                "studyDbId": "175ac75a",
                "studyDescription": "This is a yield study for Spring 2018",
                "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
                "studyPUI": "doi:10.155454/12349537312",
                "studyType": "Phenotyping",
                "trialDbId": "48b327ea",
                "trialName": "Grape_Yield_Trial"
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




### Post - /studies [POST /brapi/v2/studies]

Create new studies

Implementation Notes

StartDate and endDate should be ISO-8601 format for dates

`studDbId` is generated by the server.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataFormat": "Image Archive",
                "description": "Raw drone images collected for this study",
                "fileFormat": "application/zip",
                "name": "image-archive.zip",
                "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
                "scientificType": "Environmental",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.3"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01T14:47:23-0600",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
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
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "observationLevels": [
            {
                "levelName": "field",
                "levelOrder": 0
            },
            {
                "levelName": "block",
                "levelOrder": 1
            },
            {
                "levelName": "plot",
                "levelOrder": 2
            }
        ],
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "observationVariableDbIds": [
            "57c236f9",
            "48b327ea",
            "a5b367c5"
        ],
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01T14:47:23-0600",
        "studyCode": "Grape_Yield_Spring_2018",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
        "studyPUI": "doi:10.155454/12349537312",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
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
                "active": true,
                "additionalInfo": {},
                "commonCropName": "Grape",
                "contacts": [
                    {
                        "contactDbId": "5f4e5509",
                        "email": "bob@bob.com",
                        "instituteName": "The BrAPI Institute",
                        "name": "Bob Robertson",
                        "orcid": "http://orcid.org/0000-0001-8640-1750",
                        "type": "PI"
                    }
                ],
                "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
                "dataLinks": [
                    {
                        "dataFormat": "Image Archive",
                        "description": "Raw drone images collected for this study",
                        "fileFormat": "application/zip",
                        "name": "image-archive.zip",
                        "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
                        "scientificType": "Environmental",
                        "url": "https://brapi.org/image-archive.zip",
                        "version": "1.0.3"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01T14:47:23-0600",
                "environmentParameters": [
                    {
                        "description": "the soil type was clay",
                        "parameterName": "soil type",
                        "parameterPUI": "PECO:0007155",
                        "unit": "pH",
                        "unitPUI": "PECO:0007059",
                        "value": "clay soil",
                        "valuePUI": "ENVO:00002262"
                    }
                ],
                "experimentalDesign": {
                    "PUI": "CO_715:0000145",
                    "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
                },
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
                "growthFacility": {
                    "PUI": "CO_715:0000162",
                    "description": "field environment condition, greenhouse"
                },
                "lastUpdate": {
                    "timestamp": "2018-01-01T14:47:23-0600",
                    "version": "1.2.3"
                },
                "license": "MIT License",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "observationLevels": [
                    {
                        "levelName": "field",
                        "levelOrder": 0
                    },
                    {
                        "levelName": "block",
                        "levelOrder": 1
                    },
                    {
                        "levelName": "plot",
                        "levelOrder": 2
                    }
                ],
                "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
                "observationVariableDbIds": [
                    "57c236f9",
                    "48b327ea",
                    "a5b367c5"
                ],
                "seasons": [
                    "Spring_2018"
                ],
                "startDate": "2018-01-01T14:47:23-0600",
                "studyCode": "Grape_Yield_Spring_2018",
                "studyDbId": "175ac75a",
                "studyDescription": "This is a yield study for Spring 2018",
                "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
                "studyPUI": "doi:10.155454/12349537312",
                "studyType": "Phenotyping",
                "trialDbId": "48b327ea",
                "trialName": "Grape_Yield_Trial"
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




### Get - /studies/{studyDbId} [GET /brapi/v2/studies/{studyDbId}]

Retrieve the information of the study required for field data collection

An additionalInfo field was added to provide a controlled vocabulary for less common data fields.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
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
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataFormat": "Image Archive",
                "description": "Raw drone images collected for this study",
                "fileFormat": "application/zip",
                "name": "image-archive.zip",
                "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
                "scientificType": "Environmental",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.3"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01T14:47:23-0600",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
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
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "observationLevels": [
            {
                "levelName": "field",
                "levelOrder": 0
            },
            {
                "levelName": "block",
                "levelOrder": 1
            },
            {
                "levelName": "plot",
                "levelOrder": 2
            }
        ],
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "observationVariableDbIds": [
            "57c236f9",
            "48b327ea",
            "a5b367c5"
        ],
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01T14:47:23-0600",
        "studyCode": "Grape_Yield_Spring_2018",
        "studyDbId": "175ac75a",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
        "studyPUI": "doi:10.155454/12349537312",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
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




### Put - /studies/{studyDbId} [PUT /brapi/v2/studies/{studyDbId}/]

Update an existing Study with new data

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>active</td><td>boolean</td><td>Is this study currently active</td></tr>
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>commonCropName</td><td>string</td><td>Common name for the crop associated with this study</td></tr>
<tr><td>contacts</td><td>array[object]</td><td>List of contact entities associated with this study</td></tr>
<tr><td>contacts.<br>contactDbId</td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>email</td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts.<br>instituteName</td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts.<br>name</td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts.<br>orcid</td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts.<br>type</td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td>culturalPractices</td><td>string</td><td>MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.</td></tr>
<tr><td>dataLinks</td><td>array[object]</td><td>List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.</td></tr>
<tr><td>dataLinks.<br>dataFormat</td><td>string</td><td>The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>description</td><td>string</td><td>The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>fileFormat</td><td>string</td><td>The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>name</td><td>string</td><td>The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.</td></tr>
<tr><td>dataLinks.<br>provenance</td><td>string</td><td>The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.</td></tr>
<tr><td>dataLinks.<br>scientificType</td><td>string</td><td>The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc</td></tr>
<tr><td>dataLinks.<br>url</td><td>string (uri)</td><td>URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.</td></tr>
<tr><td>dataLinks.<br>version</td><td>string</td><td>The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).</td></tr>
<tr><td>documentationURL</td><td>string (uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td>endDate</td><td>string (date-time)</td><td>The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended</td></tr>
<tr><td>environmentParameters</td><td>array[object]</td><td>Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).</td></tr>
<tr><td>environmentParameters.<br>description</td><td>string</td><td>Human-readable value of the environment parameter (defined above) constant within the experiment</td></tr>
<tr><td>environmentParameters.<br>parameterName</td><td>string</td><td>Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. </td></tr>
<tr><td>environmentParameters.<br>parameterPUI</td><td>string</td><td>URI pointing to an ontology class for the parameter</td></tr>
<tr><td>environmentParameters.<br>unit</td><td>string</td><td>Unit of the value for this parameter</td></tr>
<tr><td>environmentParameters.<br>unitPUI</td><td>string</td><td>URI pointing to an ontology class for the unit</td></tr>
<tr><td>environmentParameters.<br>value</td><td>string</td><td>Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.</td></tr>
<tr><td>environmentParameters.<br>valuePUI</td><td>string</td><td>URI pointing to an ontology class for the parameter value</td></tr>
<tr><td>experimentalDesign</td><td>object</td><td>The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology</td></tr>
<tr><td>experimentalDesign.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>experimentalDesign.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>growthFacility</td><td>object</td><td>Short description of the facility in which the study was carried out.</td></tr>
<tr><td>growthFacility.<br>PUI</td><td>string</td><td>MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.</td></tr>
<tr><td>growthFacility.<br>description</td><td>string</td><td>MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.</td></tr>
<tr><td>lastUpdate</td><td>object</td><td>The date and time when this study was last modified</td></tr>
<tr><td>lastUpdate.<br>timestamp</td><td>string (date-time)</td><td></td></tr>
<tr><td>lastUpdate.<br>version</td><td>string</td><td></td></tr>
<tr><td>license</td><td>string</td><td>The usage license associated with the study data</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.</td></tr>
<tr><td>observationLevels</td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). </td></tr>
<tr><td>observationLevels.<br>levelName</td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels.<br>levelOrder</td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitsDescription</td><td>string</td><td>MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.</td></tr>
<tr><td>observationVariableDbIds</td><td>array[string]</td><td>The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. </td></tr>
<tr><td>seasons</td><td>array[string]</td><td>List of seasons over which this study was performed.</td></tr>
<tr><td>startDate</td><td>string (date-time)</td><td>The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started</td></tr>
<tr><td>studyCode</td><td>string</td><td>A short human readable code for a study</td></tr>
<tr><td>studyDbId</td><td>string</td><td>The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.</td></tr>
<tr><td>studyDescription</td><td>string</td><td>The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study</td></tr>
<tr><td>studyName</td><td>string</td><td>The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study</td></tr>
<tr><td>studyPUI</td><td>string</td><td>A permanent unique identifier associated with this study data. For example, a URI or DOI</td></tr>
<tr><td>studyType</td><td>string</td><td>The type of study being performed. ex. "Yield Trial", etc</td></tr>
<tr><td>trialDbId</td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td>trialName</td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + studyDbId (Required, ) ... Identifier of the study. Usually a number, could be alphanumeric.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "active": true,
    "additionalInfo": {},
    "commonCropName": "Grape",
    "contacts": [
        {
            "contactDbId": "5f4e5509",
            "email": "bob@bob.com",
            "instituteName": "The BrAPI Institute",
            "name": "Bob Robertson",
            "orcid": "http://orcid.org/0000-0001-8640-1750",
            "type": "PI"
        }
    ],
    "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
    "dataLinks": [
        {
            "dataFormat": "Image Archive",
            "description": "Raw drone images collected for this study",
            "fileFormat": "application/zip",
            "name": "image-archive.zip",
            "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
            "scientificType": "Environmental",
            "url": "https://brapi.org/image-archive.zip",
            "version": "1.0.3"
        }
    ],
    "documentationURL": "https://wiki.brapi.org",
    "endDate": "2018-01-01T14:47:23-0600",
    "environmentParameters": [
        {
            "description": "the soil type was clay",
            "parameterName": "soil type",
            "parameterPUI": "PECO:0007155",
            "unit": "pH",
            "unitPUI": "PECO:0007059",
            "value": "clay soil",
            "valuePUI": "ENVO:00002262"
        }
    ],
    "experimentalDesign": {
        "PUI": "CO_715:0000145",
        "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
    },
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
    "growthFacility": {
        "PUI": "CO_715:0000162",
        "description": "field environment condition, greenhouse"
    },
    "lastUpdate": {
        "timestamp": "2018-01-01T14:47:23-0600",
        "version": "1.2.3"
    },
    "license": "MIT License",
    "locationDbId": "3cfdd67d",
    "locationName": "Location 1",
    "observationLevels": [
        {
            "levelName": "field",
            "levelOrder": 0
        },
        {
            "levelName": "block",
            "levelOrder": 1
        },
        {
            "levelName": "plot",
            "levelOrder": 2
        }
    ],
    "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
    "observationVariableDbIds": [
        "57c236f9",
        "48b327ea",
        "a5b367c5"
    ],
    "seasons": [
        "Spring_2018"
    ],
    "startDate": "2018-01-01T14:47:23-0600",
    "studyCode": "Grape_Yield_Spring_2018",
    "studyDescription": "This is a yield study for Spring 2018",
    "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
    "studyPUI": "doi:10.155454/12349537312",
    "studyType": "Phenotyping",
    "trialDbId": "48b327ea",
    "trialName": "Grape_Yield_Trial"
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
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Grape",
        "contacts": [
            {
                "contactDbId": "5f4e5509",
                "email": "bob@bob.com",
                "instituteName": "The BrAPI Institute",
                "name": "Bob Robertson",
                "orcid": "http://orcid.org/0000-0001-8640-1750",
                "type": "PI"
            }
        ],
        "culturalPractices": "Irrigation was applied according needs during summer to prevent water stress.",
        "dataLinks": [
            {
                "dataFormat": "Image Archive",
                "description": "Raw drone images collected for this study",
                "fileFormat": "application/zip",
                "name": "image-archive.zip",
                "provenance": "Image Processing Pipeline, built at the University of Antarctica: https://github.com/antarctica/pipeline",
                "scientificType": "Environmental",
                "url": "https://brapi.org/image-archive.zip",
                "version": "1.0.3"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01T14:47:23-0600",
        "environmentParameters": [
            {
                "description": "the soil type was clay",
                "parameterName": "soil type",
                "parameterPUI": "PECO:0007155",
                "unit": "pH",
                "unitPUI": "PECO:0007059",
                "value": "clay soil",
                "valuePUI": "ENVO:00002262"
            }
        ],
        "experimentalDesign": {
            "PUI": "CO_715:0000145",
            "description": "Lines were repeated twice at each location using a complete block design. In order to limit competition effects, each block was organized into four sub-blocks corresponding to earliest groups based on a prior information."
        },
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
        "growthFacility": {
            "PUI": "CO_715:0000162",
            "description": "field environment condition, greenhouse"
        },
        "lastUpdate": {
            "timestamp": "2018-01-01T14:47:23-0600",
            "version": "1.2.3"
        },
        "license": "MIT License",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "observationLevels": [
            {
                "levelName": "field",
                "levelOrder": 0
            },
            {
                "levelName": "block",
                "levelOrder": 1
            },
            {
                "levelName": "plot",
                "levelOrder": 2
            }
        ],
        "observationUnitsDescription": "Observation units consisted in individual plots themselves consisting of a row of 15 plants at a density of approximately six plants per square meter.",
        "observationVariableDbIds": [
            "57c236f9",
            "48b327ea",
            "a5b367c5"
        ],
        "seasons": [
            "Spring_2018"
        ],
        "startDate": "2018-01-01T14:47:23-0600",
        "studyCode": "Grape_Yield_Spring_2018",
        "studyDbId": "175ac75a",
        "studyDescription": "This is a yield study for Spring 2018",
        "studyName": "INRA's Walnut Genetic Resources Observation at Kenya",
        "studyPUI": "doi:10.155454/12349537312",
        "studyType": "Phenotyping",
        "trialDbId": "48b327ea",
        "trialName": "Grape_Yield_Trial"
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




### Get - /studytypes [GET /brapi/v2/studytypes{?page}{?pageSize}]

Call to retrieve the list of study types.



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
            "Crossing Nursery",
            "Yield study"
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

