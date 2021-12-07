
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

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|commonCropNames|array[string]|The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.|
|externalReferenceIDs|array[string]|**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceIds|array[string]|List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceSources|array[string]|List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm to search for|
|germplasmNames|array[string]|List of human readable names to identify germplasm to search for|
|locationDbIds|array[string]|The location ids to search for|
|locationNames|array[string]|A human readable names to search for|
|observationVariableDbIds|array[string]|List of observation variable IDs to search for|
|observationVariableNames|array[string]|The names of Variables to search for|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.|
|programNames|array[string]|Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.|
|seasonDbIds|array[string]|The ID which uniquely identifies a season|
|sortBy|string|Name of one of the fields within the study object on which results can be sorted|
|sortOrder|string|Order results should be sorted. ex. "ASC" or "DESC"|
|studyCodes|array[string]|A short human readable code for a study|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|studyPUIs|array[string]|Permanent unique identifier associated with study data. For example, a URI or DOI|
|studyTypes|array[string]|The type of study being performed. ex. "Yield Trial", etc|
|trialDbIds|array[string]|The ID which uniquely identifies a trial to search for|
|trialNames|array[string]|The human readable name of a trial to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDbId|string|The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
        "819e508f",
        "f540b703"
    ],
    "observationVariableNames": [
        "Plant Height in meters",
        "Wheat rust score 1-5"
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDbId|string|The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDbId|string|The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
    + programDbId (Optional, ) ... A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. Use this parameter to only return results associated with the given program. Use `GET /programs` to find the list of available programs on a server.
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDbId|string|The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDbId|string|The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this study currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this study|
|contacts|array[object]|List of contact entities associated with this study|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|culturalPractices|string|MIAPPE V1.1 (DM-28) Cultural practices - General description of the cultural practices of the study.|
|dataLinks|array[object]|List of links to extra data files associated with this study. Extra data could include notes, images, and reference data.|
|dataFormat|string|The structure of the data within a file. For example - VCF, table, image archive, multispectral image archives in EDAM ontology (used in Galaxy)  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|description|string|The general description of this data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|fileFormat|string|The MIME type of the file (ie text/csv, application/excel, application/zip).  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|name|string|The name of the external data link  MIAPPE V1.1 (DM-38) Data file description - Description of the format of the data file. May be a standard file format name, or a description of organization of the data in a tabular file.|
|provenance|string|The description of the origin or ownership of this linked data. Could be a formal reference to software, method, or workflow.|
|scientificType|string|The general type of data. For example- Genotyping, Phenotyping raw data, Phenotyping reduced data, Environmental, etc|
|url|string (uri)|URL describing the location of this data file to view or download  MIAPPE V1.1 (DM-37) Data file link - Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.|
|version|string|The version number for this data   MIAPPE V1.1 (DM-39) Data file version - The version of the dataset (the actual data).|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date-time)|The date the study ends  MIAPPE V1.1 (DM-15) End date of study - Date and, if relevant, time when the experiment ended|
|environmentParameters|array[object]|Environmental parameters that were kept constant throughout the study and did not change between observation units.  MIAPPE V1.1 (DM-57) Environment - Environmental parameters that were kept constant throughout the study and did not change between observation units or assays. Environment characteristics that vary over time, i.e. environmental variables, should be recorded as Observed Variables (see below).|
|description|string|Human-readable value of the environment parameter (defined above) constant within the experiment|
|parameterName|string|Name of the environment parameter constant within the experiment  MIAPPE V1.1 (DM-58) Environment parameter - Name of the environment parameter constant within the experiment. |
|parameterPUI|string|URI pointing to an ontology class for the parameter|
|unit|string|Unit of the value for this parameter|
|unitPUI|string|URI pointing to an ontology class for the unit|
|value|string|Numerical or categorical value  MIAPPE V1.1 (DM-59) Environment parameter value - Value of the environment parameter (defined above) constant within the experiment.|
|valuePUI|string|URI pointing to an ontology class for the parameter value|
|experimentalDesign|object|The experimental and statistical design full description plus a category PUI taken from crop research ontology or agronomy ontology|
|PUI|string|MIAPPE V1.1 (DM-23) Type of experimental design - Type of experimental  design of the study, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-22) Description of the experimental design - Short description of the experimental design, possibly including statistical design. In specific cases, e.g. legacy datasets or data computed from several studies, the experimental design can be "unknown"/"NA", "aggregated/reduced data", or simply 'none'.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|growthFacility|object|Short description of the facility in which the study was carried out.|
|PUI|string|MIAPPE V1.1 (DM-27) Type of growth facility - Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology.|
|description|string|MIAPPE V1.1 (DM-26) Description of growth facility - Short description of the facility in which the study was carried out.|
|lastUpdate|object|The date and time when this study was last modified|
|timestamp|string (date-time)||
|version|string||
|license|string|The usage license associated with the study data|
|locationDbId|string|The unique identifier for a Location|
|locationName|string|A human readable name for this location  MIAPPE V1.1 (DM-18) Experimental site name - The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.|
|observationLevels|array[object]|Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). |
|levelName|string|A name for this level  **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).  For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.|
|observationUnitsDescription|string|MIAPPE V1.1 (DM-25) Observation unit description - General description of the observation units in the study.|
|observationVariableDbIds|array[string]|The list of Observation Variables being used in this study.   This list is intended to be the wishlist of variables to collect in this study. It may or may not match the set of variables used in the collected observation records. |
|seasons|array[string]|List of seasons over which this study was performed.|
|startDate|string (date-time)|The date this study started  MIAPPE V1.1 (DM-14) Start date of study - Date and, if relevant, time when the experiment started|
|studyCode|string|A short human readable code for a study|
|studyDbId|string|The ID which uniquely identifies a study within the given database server  MIAPPE V1.1 (DM-11) Study unique ID - Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.|
|studyDescription|string|The description of this study  MIAPPE V1.1 (DM-13) Study description - Human-readable text describing the study|
|studyName|string|The human readable name for a study  MIAPPE V1.1 (DM-12) Study title - Human-readable text summarising the study|
|studyPUI|string|A permanent unique identifier associated with this study data. For example, a URI or DOI|
|studyType|string|The type of study being performed. ex. "Yield Trial", etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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

|Field|Type|Description|
|---|---|---| 
|data|array[string]|the list of all study types available in this server.|


 

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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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

