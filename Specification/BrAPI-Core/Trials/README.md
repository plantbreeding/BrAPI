
# Group Trials

Services related to trials. Trials comprise of multiple studies. 

A "trial" in BrAPI represents an "investigation" in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).





### Post - /search/trials [POST /brapi/v2/search/trials]

Advanced searching for the programs resource.
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|commonCropNames|array[string]|Common name for the crop which this program is for|
|contactDbIds|array[string]|List of contact entities associated with this trial|
|externalReferenceIDs|array[string]|List of external references for the trait to search for|
|externalReferenceSources|array[string]|List of external references sources for the trait to search for|
|locationDbIds|array[string]|The location ids to search for|
|locationNames|array[string]|A human readable names to search for|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A program identifier to search for|
|programNames|array[string]|A name of a program to search for|
|searchDateRangeEnd|string (date)|The end of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.  Return a Trial entity if any of the following cases are true  - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null   - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`|
|searchDateRangeStart|string (date)|The start of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.  Return a Trial entity if any of the following cases are true  - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null   - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|trialDbIds|array[string]|The ID which uniquely identifies a trial to search for|
|trialNames|array[string]|The human readable name of a trial to search for|
|trialPUIs|array[string]|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


 

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
    "contactDbIds": [
        "e0f70c2a",
        "b82f0967"
    ],
    "externalReferenceIDs": [
        "http://purl.obolibrary.org/obo/ro.owl",
        "14a19841"
    ],
    "externalReferenceSources": [
        "OBO Library",
        "Field App Name"
    ],
    "locationDbIds": [
        "b28911cf",
        "5071d1e4"
    ],
    "locationNames": [
        "Location Alpha",
        "The Large Hadron Collider"
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
    "searchDateRangeEnd": "2018-01-01",
    "searchDateRangeStart": "2018-01-01",
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
    "trialPUIs": [
        "https://doi.org/01093190",
        "https://doi.org/11192409"
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
                "commonCropName": "Wheat",
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
                "datasetAuthorships": [
                    {
                        "datasetPUI": "doi:10.15454/312953986E3",
                        "license": "https://CreativeCommons.org/licenses/by/4.0",
                        "publicReleaseDate": "2018-01-01",
                        "submissionDate": "2018-01-01"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "programDbId": "673f378a",
                "programName": "Tomatillo_Breeding_Program",
                "publications": [
                    {
                        "publicationPUI": "doi:10.15454/312953986E3",
                        "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
                    }
                ],
                "startDate": "2018-01-01",
                "trialDbId": "1883b402",
                "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
                "trialName": "Peru Yield Trial 1",
                "trialPUI": "https://doi.org/101093190"
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




### Get - /search/trials/{searchResultsDbId} [GET /brapi/v2/search/trials/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the trials resource.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "commonCropName": "Wheat",
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
                "datasetAuthorships": [
                    {
                        "datasetPUI": "doi:10.15454/312953986E3",
                        "license": "https://CreativeCommons.org/licenses/by/4.0",
                        "publicReleaseDate": "2018-01-01",
                        "submissionDate": "2018-01-01"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "programDbId": "673f378a",
                "programName": "Tomatillo_Breeding_Program",
                "publications": [
                    {
                        "publicationPUI": "doi:10.15454/312953986E3",
                        "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
                    }
                ],
                "startDate": "2018-01-01",
                "trialDbId": "1883b402",
                "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
                "trialName": "Peru Yield Trial 1",
                "trialPUI": "https://doi.org/101093190"
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




### Get - /trials [GET /brapi/v2/trials{?active}{?commonCropName}{?contactDbId}{?programDbId}{?locationDbId}{?searchDateRangeStart}{?searchDateRangeEnd}{?studyDbId}{?trialDbId}{?trialName}{?trialPUI}{?sortBy}{?sortOrder}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Retrieve a filtered list of breeding Trials. A Trial is a collection of Studies



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


 

+ Parameters
    + active (Optional, ) ... Filter active status true/false.
    + commonCropName (Optional, ) ... Common name for the crop associated with this trial
    + contactDbId (Optional, ) ... Contact entities associated with this trial
    + programDbId (Optional, ) ... Program filter to only return trials associated with given program id.
    + locationDbId (Optional, ) ... Filter by location
    + searchDateRangeStart (Optional, ) ... The start of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.Return a Trial entity if any of the following cases are true- `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`
    + searchDateRangeEnd (Optional, ) ... The start of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.Return a Trial entity if any of the following cases are true- `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`
    + studyDbId (Optional, ) ... Filter by connected studyDbId
    + trialDbId (Optional, ) ... Filter by trialDbId
    + trialName (Optional, ) ... Filter by trial name
    + trialPUI (Optional, ) ... Filter by trial PUI
    + sortBy (Optional, ) ... Sort order. Name of the field to sort by.
    + sortOrder (Optional, ) ... Sort order direction: asc/desc
    + externalReferenceID (Optional, ) ... Search for Germplasm by an external reference
    + externalReferenceSource (Optional, ) ... Search for Germplasm by an external reference
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
                "commonCropName": "Wheat",
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
                "datasetAuthorships": [
                    {
                        "datasetPUI": "doi:10.15454/312953986E3",
                        "license": "https://CreativeCommons.org/licenses/by/4.0",
                        "publicReleaseDate": "2018-01-01",
                        "submissionDate": "2018-01-01"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "programDbId": "673f378a",
                "programName": "Tomatillo_Breeding_Program",
                "publications": [
                    {
                        "publicationPUI": "doi:10.15454/312953986E3",
                        "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
                    }
                ],
                "startDate": "2018-01-01",
                "trialDbId": "1883b402",
                "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
                "trialName": "Peru Yield Trial 1",
                "trialPUI": "https://doi.org/101093190"
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




### Post - /trials [POST /brapi/v2/trials]

Create new breeding Trials. A Trial represents a collection of related Studies. `trialDbId` is generated by the server.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "active": true,
        "additionalInfo": {},
        "commonCropName": "Wheat",
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
        "datasetAuthorships": [
            {
                "datasetPUI": "doi:10.15454/312953986E3",
                "license": "https://CreativeCommons.org/licenses/by/4.0",
                "publicReleaseDate": "2018-01-01",
                "submissionDate": "2018-01-01"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "programDbId": "673f378a",
        "programName": "Tomatillo_Breeding_Program",
        "publications": [
            {
                "publicationPUI": "doi:10.15454/312953986E3",
                "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
            }
        ],
        "startDate": "2018-01-01",
        "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
        "trialName": "Peru Yield Trial 1",
        "trialPUI": "https://doi.org/101093190"
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
                "commonCropName": "Wheat",
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
                "datasetAuthorships": [
                    {
                        "datasetPUI": "doi:10.15454/312953986E3",
                        "license": "https://CreativeCommons.org/licenses/by/4.0",
                        "publicReleaseDate": "2018-01-01",
                        "submissionDate": "2018-01-01"
                    }
                ],
                "documentationURL": "https://wiki.brapi.org",
                "endDate": "2018-01-01",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "programDbId": "673f378a",
                "programName": "Tomatillo_Breeding_Program",
                "publications": [
                    {
                        "publicationPUI": "doi:10.15454/312953986E3",
                        "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
                    }
                ],
                "startDate": "2018-01-01",
                "trialDbId": "1883b402",
                "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
                "trialName": "Peru Yield Trial 1",
                "trialPUI": "https://doi.org/101093190"
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




### Get - /trials/{trialDbId} [GET /brapi/v2/trials/{trialDbId}]

Get the details of a specific Trial



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


 

+ Parameters
    + trialDbId (Required, ) ... The internal trialDbId
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
        "commonCropName": "Wheat",
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
        "datasetAuthorships": [
            {
                "datasetPUI": "doi:10.15454/312953986E3",
                "license": "https://CreativeCommons.org/licenses/by/4.0",
                "publicReleaseDate": "2018-01-01",
                "submissionDate": "2018-01-01"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "programDbId": "673f378a",
        "programName": "Tomatillo_Breeding_Program",
        "publications": [
            {
                "publicationPUI": "doi:10.15454/312953986E3",
                "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
            }
        ],
        "startDate": "2018-01-01",
        "trialDbId": "1883b402",
        "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
        "trialName": "Peru Yield Trial 1",
        "trialPUI": "https://doi.org/101093190"
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




### Put - /trials/{trialDbId} [PUT /brapi/v2/trials/{trialDbId}/]

Update the details of an existing Trial

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|active|boolean|Is this trail currently active|
|additionalInfo|object|Additional arbitrary info|
|commonCropName|string|Common name for the crop associated with this trial|
|contacts|array[object]|List of contact entities associated with this trial|
|contactDbId|string|The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|email|string|The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.|
|instituteName|string|The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to|
|name|string|The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)|
|orcid|string|The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.|
|type|string|The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation|
|datasetAuthorships|array[object]|License and citation information for the data in this trial|
|datasetPUI|string||
|license|string|MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.|
|publicReleaseDate|string (date)|MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.|
|submissionDate|string (date)|MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|endDate|string (date)|The date this trial ends|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|programDbId|string|A program identifier to search for|
|programName|string|Human readable name of the program|
|publications|array[object]|MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.|
|publicationPUI|string||
|publicationReference|string||
|startDate|string (date)|The date this trial started|
|trialDbId|string|The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.|
|trialDescription|string|The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.|
|trialName|string|The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.|
|trialPUI|string|A permanent identifier for a trial. Could be DOI or other URI formatted identifier.|


 

+ Parameters
    + trialDbId (Required, ) ... The internal trialDbId
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "active": true,
    "additionalInfo": {},
    "commonCropName": "Wheat",
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
    "datasetAuthorships": [
        {
            "datasetPUI": "doi:10.15454/312953986E3",
            "license": "https://CreativeCommons.org/licenses/by/4.0",
            "publicReleaseDate": "2018-01-01",
            "submissionDate": "2018-01-01"
        }
    ],
    "documentationURL": "https://wiki.brapi.org",
    "endDate": "2018-01-01",
    "externalReferences": [
        {
            "referenceID": "doi:10.155454/12349537E12",
            "referenceSource": "DOI"
        },
        {
            "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
            "referenceSource": "OBO Library"
        },
        {
            "referenceID": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        }
    ],
    "programDbId": "673f378a",
    "programName": "Tomatillo_Breeding_Program",
    "publications": [
        {
            "publicationPUI": "doi:10.15454/312953986E3",
            "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
        }
    ],
    "startDate": "2018-01-01",
    "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
    "trialName": "Peru Yield Trial 1",
    "trialPUI": "https://doi.org/101093190"
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
        "commonCropName": "Wheat",
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
        "datasetAuthorships": [
            {
                "datasetPUI": "doi:10.15454/312953986E3",
                "license": "https://CreativeCommons.org/licenses/by/4.0",
                "publicReleaseDate": "2018-01-01",
                "submissionDate": "2018-01-01"
            }
        ],
        "documentationURL": "https://wiki.brapi.org",
        "endDate": "2018-01-01",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "programDbId": "673f378a",
        "programName": "Tomatillo_Breeding_Program",
        "publications": [
            {
                "publicationPUI": "doi:10.15454/312953986E3",
                "publicationReference": "Selby, BrAPI - An application programming interface for plant breeding applications, Bioinformatics, https://doi.org/10.1093/bioinformatics/190"
            }
        ],
        "startDate": "2018-01-01",
        "trialDbId": "1883b402",
        "trialDescription": "General drought resistance trial initiated in Peru before duplication in Africa",
        "trialName": "Peru Yield Trial 1",
        "trialPUI": "https://doi.org/101093190"
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

