
# Group Observations

API to manage the details of observation variable Traits. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Trait describes what property is being observed. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Trait "Leaf length" or "Flower height". 






### Get - /observations [GET /brapi/v2/observations{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationUnitLevelName}{?observationUnitLevelOrder}{?observationUnitLevelCode}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Retrieve all observations where there are measurements for the given observation variables.

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationUnitLevelName (Optional, ) ... The Observation Unit Level. Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelName
    + observationUnitLevelOrder (Optional, ) ... The Observation Unit Level Order Number. Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder
    + observationUnitLevelCode (Optional, ) ... The Observation Unit Level Code. This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
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
                "additionalInfo": {},
                "collector": "917d3ae0",
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
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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




### Post - /observations [POST /brapi/v2/observations]

Add new Observation entities

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "collector": "917d3ae0",
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
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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
                "additionalInfo": {},
                "collector": "917d3ae0",
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
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Put - /observations [PUT /brapi/v2/observations]

Update multiple Observation entities simultaneously with a single call

Include as many `observationDbIds` in the request as needed.

Note - In strictly typed languages, this structure can be represented as a Map or Dictionary of objects and parsed directly from JSON.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{}
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
                "additionalInfo": {},
                "collector": "917d3ae0",
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
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```




### Get - /observations/table [GET /brapi/v2/observations/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?searchResultsDbId}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}]

<p>This service is designed to retrieve a table of time dependant observation values as a matrix of Observation Units and Observation Variables.
This is also sometimes called a Time Series. This service takes the "Sparse Table" approach for representing this time dependant data.</p>
<p>The table may be represented by JSON, CSV, or TSV. The "Accept" HTTP header is used for the client to request different return formats. 
By default, if the "Accept" header is not included in the request, the server should return JSON as described below.</p>
<p>The table is REQUIRED to have the following columns</p>
<ul>
  <li>observationUnitDbId - Each row is related to one Observation Unit</li>
  <li>observationTimeStamp - Each row is has a time stamp for when the observation was taken</li>
  <li>At least one column with an observationVariableDbId</li>
</ul>
<p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p>
<ul>
  <li>observationUnitName</li>
  <li>studyDbId</li>
  <li>studyName</li>
  <li>germplasmDbId</li>
  <li>germplasmName</li>
  <li>positionCoordinateX</li>
  <li>positionCoordinateY</li>
  <li>year</li>
</ul>
<p>The table also may have any number of Observation Unit Hierarchy Level columns. For example:</p>
<ul>
  <li>field</li>
  <li>plot</li>
  <li>sub-plot</li>
  <li>plant</li>
  <li>pot</li>
  <li>block</li>
  <li>entry</li>
  <li>rep</li>
</ul>
<p>The JSON representation provides a pair of extra arrays for defining the headers of the table. 
The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names. 
The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table. 
By appending the two arrays, you can construct the complete header row of the table. </p>
<p>For CSV and TSV representations of the table, an extra header row is needed to describe both the Observation Variable DbId and the Observation Variable Name for each data column. 
See the example responses below</p> 



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation data recorded for different observation variables across different observation units|
|headerRow|array[string]|<p>The table is REQUIRED to have the following columns</p> <ul>   <li>observationUnitDbId - Each row is related to one Observation Unit</li>   <li>observationTimeStamp - Each row is has a time stamp for when the observation was taken</li>   <li>At least one column with an observationVariableDbId</li> </ul> <p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p> <ul>   <li>observationUnitName</li>   <li>studyDbId</li>   <li>studyName</li>   <li>germplasmDbId</li>   <li>germplasmName</li>   <li>positionCoordinateX</li>   <li>positionCoordinateY</li>   <li>year</li> </ul> <p>The table also may have any number of Observation Unit Hierarchy Level columns. For example:</p> <ul>   <li>field</li>   <li>plot</li>   <li>sub-plot</li>   <li>plant</li>   <li>pot</li>   <li>block</li>   <li>entry</li>   <li>rep</li> </ul> <p>The JSON representation provides a pair of extra arrays for defining the headers of the table.  The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names.  The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table.  By appending the two arrays, you can construct the complete header row of the table. </p>|
|observationVariables|array[object]|The list of observation variables which have values recorded for them in the data matrix. Append to the 'headerRow' for complete header row of the table.|
|observationVariableDbId|string|Variable unique identifier|
|observationVariableName|string|Variable name (usually a short name)|


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + searchResultsDbId (Optional, ) ... Permanent unique identifier which references the search results
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + Accept (Required, ) ... The requested content type which should be returned by the server
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
            [
                "2019-09-10T18:13:27.223Z",
                "f3a8a3db",
                "Plant Alpha",
                "0fe3e48b",
                "2017 Plant Study",
                "06307ec0",
                "A0043001",
                "76.50106681",
                "42.44409301",
                "2017",
                "Field_1",
                "Plot_11",
                "SubPlot_111",
                "Plant_1111",
                "Pot_1111",
                "Block_11",
                "Entry_11",
                "Rep_11",
                "25.3",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:14:27.223Z",
                "f3a8a3db",
                "Plant Alpha",
                "0fe3e48b",
                "2017 Plant Study",
                "06307ec0",
                "A0043001",
                "76.50106681",
                "42.44409301",
                "2017",
                "Field_1",
                "Plot_11",
                "SubPlot_111",
                "Plant_1111",
                "Pot_1111",
                "Block_11",
                "Entry_11",
                "Rep_11",
                "",
                "3",
                "",
                ""
            ],
            [
                "2019-09-10T18:15:54.868Z",
                "05d1b011",
                "Plant Beta",
                "0fe3e48b",
                "2017 Plant Study",
                "59d435cd",
                "A0043002",
                "76.50106683",
                "42.44409301",
                "2017",
                "Field_1",
                "Plot_11",
                "SubPlot_112",
                "Plant_1122",
                "Pot_1122",
                "Block_11",
                "Entry_11",
                "Rep_12",
                "27.9",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:16:54.868Z",
                "05d1b011",
                "Plant Beta",
                "0fe3e48b",
                "2017 Plant Study",
                "59d435cd",
                "A0043002",
                "76.50106683",
                "42.44409301",
                "2017",
                "Field_1",
                "Plot_11",
                "SubPlot_112",
                "Plant_1122",
                "Pot_1122",
                "Block_11",
                "Entry_11",
                "Rep_12",
                "",
                "1",
                "",
                ""
            ],
            [
                "2019-09-10T18:17:34.433Z",
                "67e2d87c",
                "Plant Gamma",
                "0fe3e48b",
                "2017 Plant Study",
                "06307ec0",
                "A0043001",
                "76.50106681",
                "42.44409356",
                "2017",
                "Field_1",
                "Plot_12",
                "SubPlot_123",
                "Plant_1233",
                "Pot_1233",
                "Block_12",
                "Entry_12",
                "Rep_11",
                "",
                "3",
                "",
                ""
            ],
            [
                "2019-09-10T18:18:34.433Z",
                "67e2d87c",
                "Plant Gamma",
                "0fe3e48b",
                "2017 Plant Study",
                "06307ec0",
                "A0043001",
                "76.50106681",
                "42.44409356",
                "2017",
                "Field_1",
                "Plot_12",
                "SubPlot_123",
                "Plant_1233",
                "Pot_1233",
                "Block_12",
                "Entry_12",
                "Rep_11",
                "25.5",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:19:15.629Z",
                "d98d0d4c",
                "Plant Epsilon",
                "0fe3e48b",
                "2017 Plant Study",
                "59d435cd",
                "A0043002",
                "76.50106683",
                "42.44409356",
                "2017",
                "Field_1",
                "Plot_12",
                "SubPlot_124",
                "Plant_1244",
                "Pot_1244",
                "Block_12",
                "Entry_12",
                "Rep_12",
                "28.9",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:20:15.629Z",
                "d98d0d4c",
                "Plant Epsilon",
                "0fe3e48b",
                "2017 Plant Study",
                "59d435cd",
                "A0043002",
                "76.50106683",
                "42.44409356",
                "2017",
                "Field_1",
                "Plot_12",
                "SubPlot_124",
                "Plant_1244",
                "Pot_1244",
                "Block_12",
                "Entry_12",
                "Rep_12",
                "",
                "0",
                "",
                ""
            ]
        ],
        "headerRow": [
            "observationTimeStamp",
            "observationUnitDbId",
            "observationUnitName",
            "studyDbId",
            "studyName",
            "germplasmDbId",
            "germplasmName",
            "positionCoordinateX",
            "positionCoordinateY",
            "year",
            "field",
            "plot",
            "sub-plot",
            "plant",
            "pot",
            "block",
            "entry",
            "rep"
        ],
        "observationVariables": [
            {
                "observationVariableDbId": "367aa1a9",
                "observationVariableName": "Plant height"
            },
            {
                "observationVariableDbId": "2acb934c",
                "observationVariableName": "Carotenoid"
            },
            {
                "observationVariableDbId": "85a21ce1",
                "observationVariableName": "Root color"
            },
            {
                "observationVariableDbId": "46f590e5",
                "observationVariableName": "Virus severity"
            }
        ]
    }
}
```

+ Response 200 (text/csv)
```
"\"observationUnitDbId\",\"observationUnitName\",\"studyDbId\",\"studyName\",\"germplasmDbId\",\"germplasmName\",\"positionCoordinateX\",\"positionCoordinateY\",\"year\",\"field\",\"plot\",\"sub-plot\",\"plant\",\"pot\",\"block\",\"entry\",\"rep\",\"f959a77d\",\"8341dee0\",\"84c9fd86\",\"93d80c95\"\n\n\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"Plant height\",\"Carotenoid\",\"Root color\",\"Virus severity\"\n      \n\"2019-09-10T18:13:27.223Z\",\"f3a8a3db\",\"Plant Alpha\",  \"0fe3e48b\",\"2017 Plant Study\",\"06307ec0\",\"A0043001\",\"76.50106681\",\"42.44409301\",\"2017\",\"Field_1\",\"Plot_11\",\"SubPlot_111\",\"Plant_1111\",\"Pot_1111\",\"Block_11\",\"Entry_11\",\"Rep_11\",\"25.3\",\"\", \"\",\"\"\n\n\"2019-09-10T18:14:27.223Z\",\"f3a8a3db\",\"Plant Alpha\",  \"0fe3e48b\",\"2017 Plant Study\",\"06307ec0\",\"A0043001\",\"76.50106681\",\"42.44409301\",\"2017\",\"Field_1\",\"Plot_11\",\"SubPlot_111\",\"Plant_1111\",\"Pot_1111\",\"Block_11\",\"Entry_11\",\"Rep_11\",\"\",    \"3\",\"\",\"\"\n\n\"2019-09-10T18:15:54.868Z\",\"05d1b011\",\"Plant Beta\",   \"0fe3e48b\",\"2017 Plant Study\",\"59d435cd\",\"A0043002\",\"76.50106683\",\"42.44409301\",\"2017\",\"Field_1\",\"Plot_11\",\"SubPlot_112\",\"Plant_1122\",\"Pot_1122\",\"Block_11\",\"Entry_11\",\"Rep_12\",\"27.9\",\"\", \"\",\"\"\n\n\"2019-09-10T18:16:54.868Z\",\"05d1b011\",\"Plant Beta\",   \"0fe3e48b\",\"2017 Plant Study\",\"59d435cd\",\"A0043002\",\"76.50106683\",\"42.44409301\",\"2017\",\"Field_1\",\"Plot_11\",\"SubPlot_112\",\"Plant_1122\",\"Pot_1122\",\"Block_11\",\"Entry_11\",\"Rep_12\",\"\",    \"1\",\"\",\"\"\n\n\"2019-09-10T18:17:34.433Z\",\"67e2d87c\",\"Plant Gamma\",  \"0fe3e48b\",\"2017 Plant Study\",\"06307ec0\",\"A0043001\",\"76.50106681\",\"42.44409356\",\"2017\",\"Field_1\",\"Plot_12\",\"SubPlot_123\",\"Plant_1233\",\"Pot_1233\",\"Block_12\",\"Entry_12\",\"Rep_11\",\"\",    \"3\",\"\",\"\"\n\n\"2019-09-10T18:18:34.433Z\",\"67e2d87c\",\"Plant Gamma\",  \"0fe3e48b\",\"2017 Plant Study\",\"06307ec0\",\"A0043001\",\"76.50106681\",\"42.44409356\",\"2017\",\"Field_1\",\"Plot_12\",\"SubPlot_123\",\"Plant_1233\",\"Pot_1233\",\"Block_12\",\"Entry_12\",\"Rep_11\",\"25.5\",\"\", \"\",\"\"\n\n\"2019-09-10T18:19:15.629Z\",\"d98d0d4c\",\"Plant Epsilon\",\"0fe3e48b\",\"2017 Plant Study\",\"59d435cd\",\"A0043002\",\"76.50106683\",\"42.44409356\",\"2017\",\"Field_1\",\"Plot_12\",\"SubPlot_124\",\"Plant_1244\",\"Pot_1244\",\"Block_12\",\"Entry_12\",\"Rep_12\",\"28.9\",\"\", \"\",\"\"\n\n\"2019-09-10T18:20:15.629Z\",\"d98d0d4c\",\"Plant Epsilon\",\"0fe3e48b\",\"2017 Plant Study\",\"59d435cd\",\"A0043002\",\"76.50106683\",\"42.44409356\",\"2017\",\"Field_1\",\"Plot_12\",\"SubPlot_124\",\"Plant_1244\",\"Pot_1244\",\"Block_12\",\"Entry_12\",\"Rep_12\",\"\",    \"0\",\"\",\"\""
```

+ Response 200 (text/tsv)
```
"\"observationUnitDbId\"\\t\"observationUnitName\"\\t\"studyDbId\"\\t\"studyName\"\\t\"germplasmDbId\"\\t\"germplasmName\"\\t\"positionCoordinateX\"\\t\"positionCoordinateY\"\\t\"year\"\\t\"field\"\\t\"plot\"\\t\"sub-plot\"\\t\"plant\"\\t\"pot\"\\t\"block\"\\t\"entry\"\\t\"rep\"\\t\"f959a77d\"\\t\"8341dee0\"\\t\"84c9fd86\"\\t\"93d80c95\"\n\n\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"Plant height\"\\t\"Carotenoid\"\\t\"Root color\"\\t\"Virus severity\"\n      \n\"2019-09-10T18:13:27.223Z\"\\t\"f3a8a3db\"\\t\"Plant Alpha\"\\t  \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"06307ec0\"\\t\"A0043001\"\\t\"76.50106681\"\\t\"42.44409301\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_11\"\\t\"SubPlot_111\"\\t\"Plant_1111\"\\t\"Pot_1111\"\\t\"Block_11\"\\t\"Entry_11\"\\t\"Rep_11\"\\t\"25.3\"\\t\"\"\\t \"\"\\t\"\"\n\n\"2019-09-10T18:14:27.223Z\"\\t\"f3a8a3db\"\\t\"Plant Alpha\"\\t  \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"06307ec0\"\\t\"A0043001\"\\t\"76.50106681\"\\t\"42.44409301\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_11\"\\t\"SubPlot_111\"\\t\"Plant_1111\"\\t\"Pot_1111\"\\t\"Block_11\"\\t\"Entry_11\"\\t\"Rep_11\"\\t\"\"\\t    \"3\"\\t\"\"\\t\"\"\n\n\"2019-09-10T18:15:54.868Z\"\\t\"05d1b011\"\\t\"Plant Beta\"\\t   \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"59d435cd\"\\t\"A0043002\"\\t\"76.50106683\"\\t\"42.44409301\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_11\"\\t\"SubPlot_112\"\\t\"Plant_1122\"\\t\"Pot_1122\"\\t\"Block_11\"\\t\"Entry_11\"\\t\"Rep_12\"\\t\"27.9\"\\t\"\"\\t \"\"\\t\"\"\n\n\"2019-09-10T18:16:54.868Z\"\\t\"05d1b011\"\\t\"Plant Beta\"\\t   \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"59d435cd\"\\t\"A0043002\"\\t\"76.50106683\"\\t\"42.44409301\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_11\"\\t\"SubPlot_112\"\\t\"Plant_1122\"\\t\"Pot_1122\"\\t\"Block_11\"\\t\"Entry_11\"\\t\"Rep_12\"\\t\"\"\\t    \"1\"\\t\"\"\\t\"\"\n\n\"2019-09-10T18:17:34.433Z\"\\t\"67e2d87c\"\\t\"Plant Gamma\"\\t  \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"06307ec0\"\\t\"A0043001\"\\t\"76.50106681\"\\t\"42.44409356\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_12\"\\t\"SubPlot_123\"\\t\"Plant_1233\"\\t\"Pot_1233\"\\t\"Block_12\"\\t\"Entry_12\"\\t\"Rep_11\"\\t\"\"\\t    \"3\"\\t\"\"\\t\"\"\n\n\"2019-09-10T18:18:34.433Z\"\\t\"67e2d87c\"\\t\"Plant Gamma\"\\t  \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"06307ec0\"\\t\"A0043001\"\\t\"76.50106681\"\\t\"42.44409356\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_12\"\\t\"SubPlot_123\"\\t\"Plant_1233\"\\t\"Pot_1233\"\\t\"Block_12\"\\t\"Entry_12\"\\t\"Rep_11\"\\t\"25.5\"\\t\"\"\\t \"\"\\t\"\"\n\n\"2019-09-10T18:19:15.629Z\"\\t\"d98d0d4c\"\\t\"Plant Epsilon\"\\t\"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"59d435cd\"\\t\"A0043002\"\\t\"76.50106683\"\\t\"42.44409356\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_12\"\\t\"SubPlot_124\"\\t\"Plant_1244\"\\t\"Pot_1244\"\\t\"Block_12\"\\t\"Entry_12\"\\t\"Rep_12\"\\t\"28.9\"\\t\"\"\\t \"\"\\t\"\"\n\n\"2019-09-10T18:20:15.629Z\"\\t\"d98d0d4c\"\\t\"Plant Epsilon\"\\t\"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"59d435cd\"\\t\"A0043002\"\\t\"76.50106683\"\\t\"42.44409356\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_12\"\\t\"SubPlot_124\"\\t\"Plant_1244\"\\t\"Pot_1244\"\\t\"Block_12\"\\t\"Entry_12\"\\t\"Rep_12\"\\t\"\"\\t    \"0\"\\t\"\"\\t\"\""
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




### Get - /observations/{observationDbId} [GET /brapi/v2/observations/{observationDbId}]

Get the details of a specific Observations

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + observationDbId (Required, ) ... The unique ID of an observation
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
        "additionalInfo": {},
        "collector": "917d3ae0",
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
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationDbId": "ef24b615",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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




### Put - /observations/{observationDbId} [PUT /brapi/v2/observations/{observationDbId}]

Update an existing Observation

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + observationDbId (Required, ) ... The unique ID of an observation
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "collector": "917d3ae0",
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
    "germplasmDbId": "2408ab11",
    "germplasmName": "A0000003",
    "observationTimeStamp": "2018-01-01T14:47:23-0600",
    "observationUnitDbId": "598111d4",
    "observationUnitName": "Plot 1",
    "observationVariableDbId": "c403d107",
    "observationVariableName": "Plant Height in meters",
    "season": {
        "season": "Spring",
        "seasonDbId": "Spring_2018",
        "year": 2018
    },
    "studyDbId": "ef2829db",
    "uploadedBy": "a2f7f60b",
    "value": "2.3"
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
        "additionalInfo": {},
        "collector": "917d3ae0",
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
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationDbId": "ef24b615",
        "observationTimeStamp": "2018-01-01T14:47:23-0600",
        "observationUnitDbId": "598111d4",
        "observationUnitName": "Plot 1",
        "observationVariableDbId": "c403d107",
        "observationVariableName": "Plant Height in meters",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "ef2829db",
        "uploadedBy": "a2f7f60b",
        "value": "2.3"
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




### Post - /search/observations [POST /brapi/v2/search/observations]

Submit a search request for a set of Observations. Returns an Id which reference the results of this search

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|externalReferenceIDs|array[string]|List of external references for the trait to search for|
|externalReferenceSources|array[string]|List of external references sources for the trait to search for|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm to search for|
|germplasmNames|array[string]|List of human readable names to identify germplasm to search for|
|locationDbIds|array[string]|The location ids to search for|
|locationNames|array[string]|A human readable names to search for|
|observationDbIds|array[string]|The unique id of an Observation|
|observationLevelRelationships|array[object]|Searches for values in ObservationUnit->observationUnitPosition->observationLevelRelationships|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevels|array[object]|Searches for values in ObservationUnit->observationUnitPosition->observationLevel|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationUnitDbIds|array[string]|The unique id of an Observation Unit|
|observationVariableDbIds|array[string]|The DbIds of Variables to search for|
|observationVariableNames|array[string]|The names of Variables to search for|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A program identifier to search for|
|programNames|array[string]|A name of a program to search for|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|trialDbIds|array[string]|The ID which uniquely identifies a trial to search for|
|trialNames|array[string]|The human readable name of a trial to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "externalReferenceIDs": [
        "http://purl.obolibrary.org/obo/ro.owl",
        "14a19841"
    ],
    "externalReferenceSources": [
        "OBO Library",
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
    "observationDbIds": [
        "6a4a59d8",
        "3ff067e0"
    ],
    "observationLevelRelationships": [
        {
            "levelCode": "Field_1",
            "levelName": "field"
        }
    ],
    "observationLevels": [
        {
            "levelCode": "Plot_123",
            "levelName": "plot"
        },
        {
            "levelCode": "Plot_456",
            "levelName": "plot"
        },
        {
            "levelCode": "Plot_789",
            "levelName": "plot"
        }
    ],
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationUnitDbIds": [
        "76f559b5",
        "066bc5d3"
    ],
    "observationVariableDbIds": [
        "a646187d",
        "6d23513b"
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
        "Spring 2018",
        "Season A"
    ],
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
                "additionalInfo": {},
                "collector": "917d3ae0",
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
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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




### Get - /search/observations/{searchResultsDbId} [GET /brapi/v2/search/observations/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of Observations based on search criteria.

observationTimeStamp - Iso Standard 8601.

observationValue data type inferred from the ontology



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|collector|string|The name or identifier of the entity which collected the observation|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'|
|year|integer|The 4 digit year of the season.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|uploadedBy|string|The name or id of the user who uploaded the observation to the database system|
|value|string|The value of the data collected as an observation|


 

+ Parameters
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 102 (application/json)
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
                "additionalInfo": {},
                "collector": "917d3ae0",
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
                "germplasmDbId": "2408ab11",
                "germplasmName": "A0000003",
                "observationDbId": "ef24b615",
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "598111d4",
                "observationUnitName": "Plot 1",
                "observationVariableDbId": "c403d107",
                "observationVariableName": "Plant Height in meters",
                "season": {
                    "season": "Spring",
                    "seasonDbId": "Spring_2018",
                    "year": 2018
                },
                "studyDbId": "ef2829db",
                "uploadedBy": "a2f7f60b",
                "value": "2.3"
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

