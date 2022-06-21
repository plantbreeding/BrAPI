
# Group Observations

API to manage the details of observation variable Traits. An observation variable is composed by the unique combination of one Trait, one Method and one Scale. A Trait describes what property is being observed. For example, an Observation Variable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This Variable would be distinct from a Variable with the Trait "Leaf length" or "Flower height". 






### Post - /delete/observations [POST /brapi/v2/delete/observations]

Submit a delete request for `Observations`

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">locationDbIds</span></td><td>array[string]</td><td>The location ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">locationNames</span></td><td>array[string]</td><td>A human readable names to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>The unique id of an Observation</td></tr>
<tr><td><span style="font-weight:bold;">observationLevelRelationships</span></td><td>array[object]</td><td>Searches for values in ObservationUnit->observationUnitPosition->observationLevelRelationships</td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td><span style="font-weight:bold;">observationLevels</span></td><td>array[object]</td><td>Searches for values in ObservationUnit->observationUnitPosition->observationLevel</td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStampRangeEnd</span></td><td>string<br>(date-time)</td><td>Timestamp range end</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStampRangeStart</span></td><td>string<br>(date-time)</td><td>Timestamp range start</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbIds</span></td><td>array[string]</td><td>The unique id of an Observation Unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbIds</span></td><td>array[string]</td><td>The DbIds of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableNames</span></td><td>array[string]</td><td>The names of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">seasonDbIds</span></td><td>array[string]</td><td>The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>The unique ids of the Observation records which have been successfully deleted</td></tr>
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
        "observationDbIds": [
            "6a4a59d8",
            "3ff067e0"
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




### Get - /observations [GET /brapi/v2/observations{?observationDbId}{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?seasonDbId}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?observationUnitLevelName}{?observationUnitLevelOrder}{?observationUnitLevelCode}{?observationUnitLevelRelationshipName}{?observationUnitLevelRelationshipOrder}{?observationUnitLevelRelationshipCode}{?observationUnitLevelRelationshipDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Retrieve all observations where there are measurements for the given observation variables. 

observationTimestamp should be ISO8601 format with timezone -> YYYY-MM-DDThh:mm:ss+hhmm 



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


 

+ Parameters
    + observationDbId (Optional, ) ... The unique ID of an Observation
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + observationUnitLevelName (Optional, ) ... The Observation Unit Level. Returns only the observation unit of the specified Level. <br/>References ObservationUnit->observationUnitPosition->observationLevel->levelName <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelOrder (Optional, ) ... The Observation Unit Level Order Number. Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelCode (Optional, ) ... The Observation Unit Level Code. This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipName (Optional, ) ... The Observation Unit Level Relationship is a connection that this observation unit has to another level of the hierarchy. <br/>For example, if you have several observation units at a 'plot' level, they might all share a relationship to the same 'field' level.  <br/>Use this parameter to identify groups of observation units that share a relationship level. <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipOrder (Optional, ) ... The Observation Unit Level Order Number. <br/>Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipCode (Optional, ) ... The Observation Unit Level Code. <br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipDbId (Optional, ) ... The observationUnitDbId associated with a particular level and code.<br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->observationUnitDbId <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
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
                "collector": "917d3ae0",
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
                "geoCoordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
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
                    "seasonName": "Spring",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


 

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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "geoCoordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
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
            "seasonName": "Spring",
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
                "collector": "917d3ae0",
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
                "geoCoordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
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
                    "seasonName": "Spring",
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




### Put - /observations [PUT /brapi/v2/observations/]

Update multiple Observation entities simultaneously with a single call 

Include as many `observationDbIds` in the request as needed. 

Note - In strictly typed languages, this structure can be represented as a Map or Dictionary of objects and parsed directly from JSON. 

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "<observationDbId_1>": {
        "additionalInfo": {},
        "collector": "917d3ae0",
        "externalReferences": [
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "germplasmDbId": "2408ab11",
        "germplasmName": "A0000003",
        "observationTimeStamp": "2020-08-12T18:10:40.413Z",
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
    },
    "<observationDbId_2>": {
        "additionalInfo": {},
        "collector": "03ba8c2c",
        "externalReferences": [
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "germplasmDbId": "69310ca4",
        "germplasmName": "A0000438",
        "observationTimeStamp": "2020-08-12T18:10:40.413Z",
        "observationUnitDbId": "1177a714",
        "observationUnitName": "Plot 13",
        "observationVariableDbId": "e4f8ba8c",
        "observationVariableName": "Carotenoid",
        "season": {
            "season": "Spring",
            "seasonDbId": "Spring_2018",
            "year": 2018
        },
        "studyDbId": "6f9e267d",
        "uploadedBy": "182c72ad",
        "value": "2.5"
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
        "data": [
            {
                "additionalInfo": {},
                "collector": "917d3ae0",
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
                "geoCoordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
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
                    "seasonName": "Spring",
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




### Get - /observations/table [GET /brapi/v2/observations/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?searchResultsDbId}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?observationUnitLevelName}{?observationUnitLevelOrder}{?observationUnitLevelCode}{?observationUnitLevelRelationshipName}{?observationUnitLevelRelationshipOrder}{?observationUnitLevelRelationshipCode}{?observationUnitLevelRelationshipDbId}]

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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">data</span></td><td>array[array]</td><td>Matrix of observation data recorded for different observation variables across different observation units</td></tr>
<tr><td><span style="font-weight:bold;">headerRow</span></td><td>array[string]</td><td><p>The table is REQUIRED to have the following columns</p> <ul>   <li>observationUnitDbId - Each row is related to one Observation Unit</li>   <li>observationTimeStamp - Each row is has a time stamp for when the observation was taken</li>   <li>At least one column with an observationVariableDbId</li> </ul> <p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p> <ul>   <li>observationUnitName</li>   <li>studyDbId</li>   <li>studyName</li>   <li>germplasmDbId</li>   <li>germplasmName</li>   <li>positionCoordinateX</li>   <li>positionCoordinateY</li>   <li>year</li> </ul> <p>The table also may have any number of Observation Unit Hierarchy Level columns. For example:</p> <ul>   <li>field</li>   <li>plot</li>   <li>sub-plot</li>   <li>plant</li>   <li>pot</li>   <li>block</li>   <li>entry</li>   <li>rep</li> </ul> <p>The JSON representation provides a pair of extra arrays for defining the headers of the table.  The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names.  The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table.  By appending the two arrays, you can construct the complete header row of the table. </p></td></tr>
<tr><td><span style="font-weight:bold;">observationVariables</span></td><td>array[object]</td><td>The list of observation variables which have values recorded for them in the data matrix. Append to the 'headerRow' for complete header row of the table.</td></tr>
<tr><td>observationVariables<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>Variable unique identifier</td></tr>
<tr><td>observationVariables<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>Variable name (usually a short name)</td></tr>
</table>


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... **Deprecated in v2.1** Please use `observationUnitLevelName`. Github issue number #464 <br>The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure. 
    + searchResultsDbId (Optional, ) ... Permanent unique identifier which references the search results
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + observationUnitLevelName (Optional, ) ... The Observation Unit Level. Returns only the observation unit of the specified Level. <br/>References ObservationUnit->observationUnitPosition->observationLevel->levelName <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelOrder (Optional, ) ... The Observation Unit Level Order Number. Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelCode (Optional, ) ... The Observation Unit Level Code. This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipName (Optional, ) ... The Observation Unit Level Relationship is a connection that this observation unit has to another level of the hierarchy. <br/>For example, if you have several observation units at a 'plot' level, they might all share a relationship to the same 'field' level.  <br/>Use this parameter to identify groups of observation units that share a relationship level. <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipOrder (Optional, ) ... The Observation Unit Level Order Number. <br/>Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipCode (Optional, ) ... The Observation Unit Level Code. <br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipDbId (Optional, ) ... The observationUnitDbId associated with a particular level and code.<br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->observationUnitDbId <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + Accept (Required, ) ... The requested content type which should be returned by the server
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


 

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
        "collector": "917d3ae0",
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
        "geoCoordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
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
            "seasonName": "Spring",
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




### Put - /observations/{observationDbId} [PUT /brapi/v2/observations/{observationDbId}/]

Update an existing Observation

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


 

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
            "referenceId": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceId": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        }
    ],
    "geoCoordinates": {
        "geometry": {
            "coordinates": [
                -76.506042,
                42.417373,
                123
            ],
            "type": "Point"
        },
        "type": "Feature"
    },
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
        "seasonName": "Spring",
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
        "collector": "917d3ae0",
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
        "geoCoordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373,
                    123
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
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
            "seasonName": "Spring",
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

Submit a search request for `Observations`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/observations/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">locationDbIds</span></td><td>array[string]</td><td>The location ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">locationNames</span></td><td>array[string]</td><td>A human readable names to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationDbIds</span></td><td>array[string]</td><td>The unique id of an Observation</td></tr>
<tr><td><span style="font-weight:bold;">observationLevelRelationships</span></td><td>array[object]</td><td>Searches for values in ObservationUnit->observationUnitPosition->observationLevelRelationships</td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td><span style="font-weight:bold;">observationLevels</span></td><td>array[object]</td><td>Searches for values in ObservationUnit->observationUnitPosition->observationLevel</td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStampRangeEnd</span></td><td>string<br>(date-time)</td><td>Timestamp range end</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStampRangeStart</span></td><td>string<br>(date-time)</td><td>Timestamp range start</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbIds</span></td><td>array[string]</td><td>The unique id of an Observation Unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbIds</span></td><td>array[string]</td><td>The DbIds of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableNames</span></td><td>array[string]</td><td>The names of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">seasonDbIds</span></td><td>array[string]</td><td>The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
<tr><td><span style="font-weight:bold;">trialDbIds</span></td><td>array[string]</td><td>The ID which uniquely identifies a trial to search for</td></tr>
<tr><td><span style="font-weight:bold;">trialNames</span></td><td>array[string]</td><td>The human readable name of a trial to search for</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
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
                "collector": "917d3ae0",
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
                "geoCoordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
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
                    "seasonName": "Spring",
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




### Get - /search/observations/{searchResultsDbId} [GET /brapi/v2/search/observations/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Observations` search request <br/>
Clients should submit a search request using the corresponding `POST /search/observations` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td><span style="font-weight:bold;">observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td><span style="font-weight:bold;">season</span></td><td>object</td><td></td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456  <br>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
</table>


 

+ Parameters
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




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
                "collector": "917d3ae0",
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
                "geoCoordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                },
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
                    "seasonName": "Spring",
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

