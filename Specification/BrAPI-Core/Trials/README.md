
# Group Trials

Services related to trials. Trials comprise of multiple studies. 

A "trial" in BrAPI represents an "investigation" in MIAPPE (Minimal Information about a Plant Phenotyping Experiment).





### Post - /search/trials [POST /brapi/v2/search/trials]

Submit a search request for `Trials`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/trials/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trail currently active</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">contactDbIds</span></td><td>array[string]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">locationDbIds</span></td><td>array[string]</td><td>The location ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">locationNames</span></td><td>array[string]</td><td>A human readable names to search for</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">searchDateRangeEnd</span></td><td>string<br>(date)</td><td>The end of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.  Return a Trial entity if any of the following cases are true  - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null   - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`</td></tr>
<tr><td><span style="font-weight:bold;">searchDateRangeStart</span></td><td>string<br>(date)</td><td>The start of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.  Return a Trial entity if any of the following cases are true  - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null   - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null  - `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialPUIs</span></td><td>array[string]</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
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
    "contactDbIds": [
        "e0f70c2a",
        "b82f0967"
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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




### Get - /search/trials/{searchResultsDbId} [GET /brapi/v2/search/trials/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Trials` search request <br/>
Clients should submit a search request using the corresponding `POST /search/trials` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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




### Get - /trials [GET /brapi/v2/trials{?active}{?contactDbId}{?locationDbId}{?searchDateRangeStart}{?searchDateRangeEnd}{?trialPUI}{?sortBy}{?sortOrder}{?commonCropName}{?programDbId}{?trialDbId}{?trialName}{?studyDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Retrieve a filtered list of breeding Trials. A Trial is a collection of Studies



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
</table>


 

+ Parameters
    + active (Optional, ) ... Filter active status true/false.
    + contactDbId (Optional, ) ... Contact entities associated with this trial
    + locationDbId (Optional, ) ... Filter by location
    + searchDateRangeStart (Optional, ) ... The start of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.Return a Trial entity if any of the following cases are true- `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`
    + searchDateRangeEnd (Optional, ) ... The start of the overlapping search date range. `searchDateRangeStart` must be before `searchDateRangeEnd`.Return a Trial entity if any of the following cases are true- `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is null - `searchDateRangeStart` is before `trial.endDate` AND `searchDateRangeEnd` is after `trial.startDate`- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is null- `searchDateRangeEnd` is after `trial.startDate` AND `searchDateRangeStart` is before `trial.endDate`
    + trialPUI (Optional, ) ... Filter by trial PUI
    + sortBy (Optional, ) ... Sort order. Name of the field to sort by.
    + sortOrder (Optional, ) ... Sort order direction: asc/desc
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + trialDbId (Optional, ) ... Use this parameter to only return results associated with the given `Trial` unique identifier. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
    + trialName (Optional, ) ... Use this parameter to only return results associated with the given `Trial` by its human readable name. <br/>Use `GET /trials` to find the list of available `Trials` on a server.
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
</table>


 

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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
</table>


 

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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">active</span></td><td>boolean</td><td>Is this trial currently active</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop associated with this trial</td></tr>
<tr><td><span style="font-weight:bold;">contacts</span></td><td>array[object]</td><td>List of contact entities associated with this trial</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.contactDbId</span></td><td>string</td><td>The ID which uniquely identifies this contact  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.email</span></td><td>string</td><td>The contacts email address  MIAPPE V1.1 (DM-32) Person email - The electronic mail address of the person.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.instituteName</span></td><td>string</td><td>The name of the institution which this contact is part of  MIAPPE V1.1 (DM-35) Person affiliation - The institution the person belongs to</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of this contact person  MIAPPE V1.1 (DM-31) Person name - The name of the person (either full name or as used in scientific publications)</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.orcid</span></td><td>string</td><td>The Open Researcher and Contributor ID for this contact person (orcid.org)  MIAPPE V1.1 (DM-33) Person ID - An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.</td></tr>
<tr><td>contacts<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The type of person this contact represents (ex: Coordinator, Scientist, PI, etc.)  MIAPPE V1.1 (DM-34) Person role - Type of contribution of the person to the investigation</td></tr>
<tr><td><span style="font-weight:bold;">datasetAuthorships</span></td><td>array[object]</td><td>License and citation information for the data in this trial</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.datasetPUI</span></td><td>string</td><td></td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.license</span></td><td>string</td><td>MIAPPE V1.1 (DM-7) License - License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.publicReleaseDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-6) Public release date - Date of first public release of the dataset presently being described.</td></tr>
<tr><td>datasetAuthorships<br><span style="font-weight:bold;margin-left:5px">.submissionDate</span></td><td>string<br>(date)</td><td>MIAPPE V1.1 (DM-5) Submission date - Date of submission of the dataset presently being described to a host repository.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">endDate</span></td><td>string<br>(date)</td><td>The date this trial ends</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>A program identifier to search for</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">publications</span></td><td>array[object]</td><td>MIAPPE V1.1 (DM-9) Associated publication - An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.</td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationPUI</span></td><td>string</td><td></td></tr>
<tr><td>publications<br><span style="font-weight:bold;margin-left:5px">.publicationReference</span></td><td>string</td><td></td></tr>
<tr><td><span style="font-weight:bold;">startDate</span></td><td>string<br>(date)</td><td>The date this trial started</td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial  MIAPPE V1.1 (DM-2) Investigation unique ID - Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.</td></tr>
<tr><td><span style="font-weight:bold;">trialDescription</span></td><td>string</td><td>The human readable description of a trial  MIAPPE V1.1 (DM-4) Investigation description - Human-readable text describing the investigation in more detail.</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial  MIAPPE V1.1 (DM-3) Investigation title - Human-readable string summarising the investigation.</td></tr>
<tr><td><span style="font-weight:bold;">trialPUI</span></td><td>string</td><td>A permanent identifier for a trial. Could be DOI or other URI formatted identifier.</td></tr>
</table>


 

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
            "referenceId": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceId": "75a50e76",
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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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

