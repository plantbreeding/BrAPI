
# Group Observation Units

API to retrieve and submit data regarding Observation Units. An Observation Unit is anything that is being observed. Typically, this is a Plot or a Plant, but it could include things like Fields or Samples. The Observation Level defines the type of Observation Unit. For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.






### Get - /observationlevels [GET /brapi/v2/observationlevels{?studyDbId}{?trialDbId}{?programDbId}{?page}{?pageSize}]

Call to retrieve the list of supported observation levels. 

Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). 

The values are used to supply the `observationLevel` parameter in the observation unit details call.
      
For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td><span style="font-weight:bold;">levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
</table>


 

+ Parameters
    + studyDbId (Optional, ) ... Filter by study DbId
    + trialDbId (Optional, ) ... Filter by trial DbId
    + programDbId (Optional, ) ... Filter by program DbId
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
            },
            {
                "levelName": "sub-plot",
                "levelOrder": 3
            },
            {
                "levelName": "plant",
                "levelOrder": 4
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




### Get - /observationunits [GET /brapi/v2/observationunits{?observationUnitDbId}{?observationUnitName}{?germplasmDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?seasonDbId}{?includeObservations}{?observationUnitLevelName}{?observationUnitLevelOrder}{?observationUnitLevelCode}{?observationUnitLevelRelationshipName}{?observationUnitLevelRelationshipOrder}{?observationUnitLevelRelationshipCode}{?observationUnitLevelRelationshipDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered set of Observation Units



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">observations</span></td><td>array[object]</td><td>All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>object</td><td></td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456   Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + observationUnitDbId (Optional, ) ... The unique ID of an Observation Unit
    + observationUnitName (Optional, ) ... The human readable identifier for an Observation Unit
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + includeObservations (Optional, ) ... Use this parameter to include a list of observations embedded in each ObservationUnit object. CAUTION - Use this parameter at your own risk. It may return large, unpaginated lists of observation data. Only set this value to True if you are sure you need to. 
    + observationUnitLevelName (Optional, ) ... The Observation Unit Level. Returns only the observation unit of the specified Level. <br/>References ObservationUnit->observationUnitPosition->observationLevel->levelName <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelOrder (Optional, ) ... The Observation Unit Level Order Number. Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelCode (Optional, ) ... The Observation Unit Level Code. This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipName (Optional, ) ... The Observation Unit Level Relationship is a connection that this observation unit has to another level of the hierarchy. <br/>For example, if you have several observation units at a 'plot' level, they might all share a relationship to the same 'field' level.  <br/>Use this parameter to identify groups of observation units that share a relationship level. <br/>**Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipOrder (Optional, ) ... The Observation Unit Level Order Number. <br/>Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipCode (Optional, ) ... The Observation Unit Level Code. <br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
    + observationUnitLevelRelationshipDbId (Optional, ) ... The observationUnitDbId associated with a particular level and code.<br/>This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->observationUnitDbId <br/>For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. 
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
                "additionalInfo": {},
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "entryType": "TEST",
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
                    "observationLevel": {
                        "levelCode": "Plot_123",
                        "levelName": "plot",
                        "levelOrder": 2
                    },
                    "observationLevelRelationships": [
                        {
                            "levelCode": "Field_1",
                            "levelName": "field",
                            "levelOrder": 0
                        },
                        {
                            "levelCode": "Block_12",
                            "levelName": "block",
                            "levelOrder": 1
                        },
                        {
                            "levelCode": "Plot_123",
                            "levelName": "plot",
                            "levelOrder": 2
                        }
                    ],
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW"
                },
                "observations": [
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
                ],
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "seedLotDbId": "261ecb09",
                "seedLotName": "Seed Lot Alpha",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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




### Post - /observationunits [POST /brapi/v2/observationunits]

Add new Observation Units

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">observations</span></td><td>array[object]</td><td>All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>object</td><td></td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456   Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "crossDbId": "d105fd6f",
        "crossName": "my_Crosses_2018_01",
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
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationUnitName": "Plot 1",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "entryType": "TEST",
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
            "observationLevel": {
                "levelCode": "Plot_123",
                "levelName": "plot",
                "levelOrder": 2
            },
            "observationLevelRelationships": [
                {
                    "levelCode": "Field_1",
                    "levelName": "field",
                    "levelOrder": 0
                },
                {
                    "levelCode": "Block_12",
                    "levelName": "block",
                    "levelOrder": 1
                },
                {
                    "levelCode": "Plot_123",
                    "levelName": "plot",
                    "levelOrder": 2
                }
            ],
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW"
        },
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "seedLotDbId": "261ecb09",
        "seedLotName": "Seed Lot Alpha",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
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
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "entryType": "TEST",
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
                    "observationLevel": {
                        "levelCode": "Plot_123",
                        "levelName": "plot",
                        "levelOrder": 2
                    },
                    "observationLevelRelationships": [
                        {
                            "levelCode": "Field_1",
                            "levelName": "field",
                            "levelOrder": 0
                        },
                        {
                            "levelCode": "Block_12",
                            "levelName": "block",
                            "levelOrder": 1
                        },
                        {
                            "levelCode": "Plot_123",
                            "levelName": "plot",
                            "levelOrder": 2
                        }
                    ],
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW"
                },
                "observations": [
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
                ],
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "seedLotDbId": "261ecb09",
                "seedLotName": "Seed Lot Alpha",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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




### Put - /observationunits [PUT /brapi/v2/observationunits/]

Update a set of Observation Units 

Note - In strictly typed languages, this structure can be represented as a Map or Dictionary of objects and parsed directly to JSON. 

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">observations</span></td><td>array[object]</td><td>All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>object</td><td></td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456   Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "<observationUnitDbId_1>": {
        "additionalInfo": {},
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            }
        ],
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationUnitName": "Plot 31",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "entryType": "TEST",
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
            "observationLevel": {
                "levelCode": "Plot_456",
                "levelName": "plot",
                "levelOrder": 2
            },
            "observationLevelRelationships": [
                {
                    "levelCode": "Field_1",
                    "levelName": "field",
                    "levelOrder": 0
                },
                {
                    "levelCode": "Block_6",
                    "levelName": "block",
                    "levelOrder": 1
                },
                {
                    "levelCode": "Plot_456",
                    "levelName": "plot",
                    "levelOrder": 2
                }
            ],
            "positionCoordinateX": "78",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "08",
            "positionCoordinateYType": "GRID_ROW"
        },
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "seedLotDbId": "261ecb09",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
    },
    "<observationUnitDbId_2>": {
        "additionalInfo": {},
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            }
        ],
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationUnitName": "Plot 17",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "entryType": "TEST",
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
            "observationLevel": {
                "levelCode": "Plot_123",
                "levelName": "plot",
                "levelOrder": 2
            },
            "observationLevelRelationships": [
                {
                    "levelCode": "Field_1",
                    "levelName": "field",
                    "levelOrder": 0
                },
                {
                    "levelCode": "Block_12",
                    "levelName": "block",
                    "levelOrder": 1
                },
                {
                    "levelCode": "Plot_123",
                    "levelName": "plot",
                    "levelOrder": 2
                }
            ],
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW"
        },
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "seedLotDbId": "261ecb09",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
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
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "entryType": "TEST",
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
                    "observationLevel": {
                        "levelCode": "Plot_123",
                        "levelName": "plot",
                        "levelOrder": 2
                    },
                    "observationLevelRelationships": [
                        {
                            "levelCode": "Field_1",
                            "levelName": "field",
                            "levelOrder": 0
                        },
                        {
                            "levelCode": "Block_12",
                            "levelName": "block",
                            "levelOrder": 1
                        },
                        {
                            "levelCode": "Plot_123",
                            "levelName": "plot",
                            "levelOrder": 2
                        }
                    ],
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW"
                },
                "observations": [
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
                ],
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "seedLotDbId": "261ecb09",
                "seedLotName": "Seed Lot Alpha",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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




### Get - /observationunits/table [GET /brapi/v2/observationunits/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationUnitLevelName}{?observationUnitLevelOrder}{?observationUnitLevelCode}{?observationUnitLevelRelationshipName}{?observationUnitLevelRelationshipOrder}{?observationUnitLevelRelationshipCode}{?observationUnitLevelRelationshipDbId}]

<p>This service is designed to retrieve a table for observation values as a matrix of Observation Units and Observation Variables.</p>
<p>The table may be represented by JSON, CSV, or TSV. The "Accept" HTTP header is used for the client to request different return formats. 
By default, if the "Accept" header is not included in the request, the server should return JSON as described below.</p>
<p>The table is REQUIRED to have the following columns</p>
<ul>
  <li>observationUnitDbId - Each row is related to one Observation Unit</li>
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
<tr><td><span style="font-weight:bold;">headerRow</span></td><td>array[string]</td><td><p>The table is REQUIRED to have the following columns</p> <ul>   <li>observationUnitDbId - Each row is related to one Observation Unit</li>   <li>At least one column with an observationVariableDbId</li> </ul> <p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p> <ul>   <li>observationUnitName</li>   <li>studyDbId</li>   <li>studyName</li>   <li>germplasmDbId</li>   <li>germplasmName</li>   <li>positionCoordinateX</li>   <li>positionCoordinateY</li>   <li>year</li> </ul> <p>The table also may have any number of Observation Unit Hierarchy Level columns. For example:</p> <ul>   <li>field</li>   <li>plot</li>   <li>sub-plot</li>   <li>plant</li>   <li>pot</li>   <li>block</li>   <li>entry</li>   <li>rep</li> </ul> <p>The JSON representation provides a pair of extra arrays for defining the headers of the table.  The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names.  The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table.  By appending the two arrays, you can construct the complete header row of the table. </p></td></tr>
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
    + observationLevel (Optional, ) ... **Deprecated in v2.1** Please use `observationUnitLevelName`. Github issue number #464 The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure. 
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
                "3",
                "50.75"
            ],
            [
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
                "1",
                "45.345"
            ],
            [
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
                "3",
                "50.76"
            ],
            [
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
                "0",
                "46.5"
            ]
        ],
        "headerRow": [
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
"\"observationUnitDbId\",\"observationUnitName\",\"studyDbId\",\"studyName\",\"germplasmDbId\",\"germplasmName\",\"positionCoordinateX\",\"positionCoordinateY\",\"year\",\"field\",\"plot\",\"sub-plot\",\"plant\",\"pot\",\"block\",\"entry\",\"rep\",\"f959a77d\",\"8341dee0\",\"84c9fd86\"\n\n\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"Plant Height\",\"Virus severity\",\"Carotenoid\"\n\n\"f3a8a3db\",\"Plant Alpha\",  \"0fe3e48b\",\"2017 Plant Study\",\"06307ec0\",\"A0043001\",\"76.50106681\",\"42.44409301\",\"2017\",\"Field_1\",\"Plot_11\",\"SubPlot_111\",\"Plant_1111\",\"Pot_1111\",\"Block_11\",\"Entry_11\",\"Rep_11\",\"25.3\",\"3\",\"50.75\"\n\n\"05d1b011\",\"Plant Beta\",   \"0fe3e48b\",\"2017 Plant Study\",\"59d435cd\",\"A0043002\",\"76.50106683\",\"42.44409301\",\"2017\",\"Field_1\",\"Plot_11\",\"SubPlot_112\",\"Plant_1122\",\"Pot_1122\",\"Block_11\",\"Entry_11\",\"Rep_12\",\"27.9\",\"1\",\"45.345\"\n\n\"67e2d87c\",\"Plant Gamma\",  \"0fe3e48b\",\"2017 Plant Study\",\"06307ec0\",\"A0043001\",\"76.50106681\",\"42.44409356\",\"2017\",\"Field_1\",\"Plot_12\",\"SubPlot_123\",\"Plant_1233\",\"Pot_1233\",\"Block_12\",\"Entry_12\",\"Rep_11\",\"25.5\",\"3\",\"50.76\"\n\n\"d98d0d4c\",\"Plant Epsilon\",\"0fe3e48b\",\"2017 Plant Study\",\"59d435cd\",\"A0043002\",\"76.50106683\",\"42.44409356\",\"2017\",\"Field_1\",\"Plot_12\",\"SubPlot_124\",\"Plant_1244\",\"Pot_1244\",\"Block_12\",\"Entry_12\",\"Rep_12\",\"28.9\",\"0\",\"46.5\""
```

+ Response 200 (text/tsv)
```
"\"observationUnitDbId\"\\t\"observationUnitName\"\\t\"studyDbId\"\\t\"studyName\"\\t\"germplasmDbId\"\\t\"germplasmName\"\\t\"positionCoordinateX\"\\t\"positionCoordinateY\"\\t\"year\"\\t\"field\"\\t\"plot\"\\t\"sub-plot\"\\t\"plant\"\\t\"pot\"\\t\"block\"\\t\"entry\"\\t\"rep\"\\t\"f959a77d\"\\t\"8341dee0\"\\t\"84c9fd86\"\n\n\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"\"\\t\"Plant Height\"\\t\"Virus severity\"\\t\"Carotenoid\"\n\n\"f3a8a3db\"\\t\"Plant Alpha\"\\t  \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"06307ec0\"\\t\"A0043001\"\\t\"76.50106681\"\\t\"42.44409301\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_11\"\\t\"SubPlot_111\"\\t\"Plant_1111\"\\t\"Pot_1111\"\\t\"Block_11\"\\t\"Entry_11\"\\t\"Rep_11\"\\t\"25.3\"\\t\"3\"\\t\"50.75\"\n\n\"05d1b011\"\\t\"Plant Beta\"\\t   \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"59d435cd\"\\t\"A0043002\"\\t\"76.50106683\"\\t\"42.44409301\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_11\"\\t\"SubPlot_112\"\\t\"Plant_1122\"\\t\"Pot_1122\"\\t\"Block_11\"\\t\"Entry_11\"\\t\"Rep_12\"\\t\"27.9\"\\t\"1\"\\t\"45.345\"\n\n\"67e2d87c\"\\t\"Plant Gamma\"\\t  \"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"06307ec0\"\\t\"A0043001\"\\t\"76.50106681\"\\t\"42.44409356\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_12\"\\t\"SubPlot_123\"\\t\"Plant_1233\"\\t\"Pot_1233\"\\t\"Block_12\"\\t\"Entry_12\"\\t\"Rep_11\"\\t\"25.5\"\\t\"3\"\\t\"50.76\"\n\n\"d98d0d4c\"\\t\"Plant Epsilon\"\\t\"0fe3e48b\"\\t\"2017 Plant Study\"\\t\"59d435cd\"\\t\"A0043002\"\\t\"76.50106683\"\\t\"42.44409356\"\\t\"2017\"\\t\"Field_1\"\\t\"Plot_12\"\\t\"SubPlot_124\"\\t\"Plant_1244\"\\t\"Pot_1244\"\\t\"Block_12\"\\t\"Entry_12\"\\t\"Rep_12\"\\t\"28.9\"\\t\"0\"\\t\"46.5\""
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




### Get - /observationunits/{observationUnitDbId} [GET /brapi/v2/observationunits/{observationUnitDbId}]

Get the details of a specific Observation Unit



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">observations</span></td><td>array[object]</td><td>All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>object</td><td></td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456   Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + observationUnitDbId (Required, ) ... The unique ID of the specific Observation Unit
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
        "crossDbId": "d105fd6f",
        "crossName": "my_Crosses_2018_01",
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
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationUnitDbId": "8c67503c",
        "observationUnitName": "Plot 1",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "entryType": "TEST",
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
            "observationLevel": {
                "levelCode": "Plot_123",
                "levelName": "plot",
                "levelOrder": 2
            },
            "observationLevelRelationships": [
                {
                    "levelCode": "Field_1",
                    "levelName": "field",
                    "levelOrder": 0
                },
                {
                    "levelCode": "Block_12",
                    "levelName": "block",
                    "levelOrder": 1
                },
                {
                    "levelCode": "Plot_123",
                    "levelName": "plot",
                    "levelOrder": 2
                }
            ],
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW"
        },
        "observations": [
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
        ],
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "seedLotDbId": "261ecb09",
        "seedLotName": "Seed Lot Alpha",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
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




### Put - /observationunits/{observationUnitDbId} [PUT /brapi/v2/observationunits/{observationUnitDbId}/]

Update an existing Observation Units

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">observations</span></td><td>array[object]</td><td>All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>object</td><td></td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456   Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
</table>


 

+ Parameters
    + observationUnitDbId (Required, ) ... The unique ID of the specific Observation Unit
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "crossDbId": "d105fd6f",
    "crossName": "my_Crosses_2018_01",
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
    "germplasmDbId": "e9d9ed57",
    "germplasmName": "A0000001",
    "locationDbId": "0e208b20",
    "locationName": "Field Station Alpha",
    "observationUnitName": "Plot 1",
    "observationUnitPUI": "http://pui.per/plot/1a9afc14",
    "observationUnitPosition": {
        "entryType": "TEST",
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
        "observationLevel": {
            "levelCode": "Plot_123",
            "levelName": "plot",
            "levelOrder": 2
        },
        "observationLevelRelationships": [
            {
                "levelCode": "Field_1",
                "levelName": "field",
                "levelOrder": 0
            },
            {
                "levelCode": "Block_12",
                "levelName": "block",
                "levelOrder": 1
            },
            {
                "levelCode": "Plot_123",
                "levelName": "plot",
                "levelOrder": 2
            }
        ],
        "positionCoordinateX": "74",
        "positionCoordinateXType": "GRID_COL",
        "positionCoordinateY": "03",
        "positionCoordinateYType": "GRID_ROW"
    },
    "programDbId": "2d763a7a",
    "programName": "The Perfect Breeding Program",
    "seedLotDbId": "261ecb09",
    "seedLotName": "Seed Lot Alpha",
    "studyDbId": "9865addc",
    "studyName": "Purple_Tomato_1",
    "treatments": [
        {
            "factor": "fertilizer",
            "modality": "low fertilizer"
        }
    ],
    "trialDbId": "776a609c",
    "trialName": "Purple Tomato"
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
        "crossDbId": "d105fd6f",
        "crossName": "my_Crosses_2018_01",
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
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationUnitDbId": "8c67503c",
        "observationUnitName": "Plot 1",
        "observationUnitPUI": "http://pui.per/plot/1a9afc14",
        "observationUnitPosition": {
            "entryType": "TEST",
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
            "observationLevel": {
                "levelCode": "Plot_123",
                "levelName": "plot",
                "levelOrder": 2
            },
            "observationLevelRelationships": [
                {
                    "levelCode": "Field_1",
                    "levelName": "field",
                    "levelOrder": 0
                },
                {
                    "levelCode": "Block_12",
                    "levelName": "block",
                    "levelOrder": 1
                },
                {
                    "levelCode": "Plot_123",
                    "levelName": "plot",
                    "levelOrder": 2
                }
            ],
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW"
        },
        "observations": [
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
        ],
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
        "seedLotDbId": "261ecb09",
        "seedLotName": "Seed Lot Alpha",
        "studyDbId": "9865addc",
        "studyName": "Purple_Tomato_1",
        "treatments": [
            {
                "factor": "fertilizer",
                "modality": "low fertilizer"
            }
        ],
        "trialDbId": "776a609c",
        "trialName": "Purple Tomato"
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




### Post - /search/observationunits [POST /brapi/v2/search/observationunits]

Submit a search request for `ObservationUnits`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/observationunits/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">includeObservations</span></td><td>boolean</td><td>Use this parameter to include a list of observations embedded in each ObservationUnit object.   CAUTION - Use this parameter at your own risk. It may return large, unpaginated lists of observation data. Only set this value to True if you are sure you need to.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbIds</span></td><td>array[string]</td><td>The location ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">locationNames</span></td><td>array[string]</td><td>A human readable names to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationLevelRelationships</span></td><td>array[object]</td><td>Searches for values in ObservationUnit->observationUnitPosition->observationLevelRelationships</td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td><span style="font-weight:bold;">observationLevels</span></td><td>array[object]</td><td>Searches for values in ObservationUnit->observationUnitPosition->observationLevel</td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationLevels<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbIds</span></td><td>array[string]</td><td>The unique id of an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitNames</span></td><td>array[string]</td><td>The human readable identifier for an Observation Unit</td></tr>
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
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">observations</span></td><td>array[object]</td><td>All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>object</td><td></td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456   Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
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
    "includeObservations": false,
    "locationDbIds": [
        "b28911cf",
        "5071d1e4"
    ],
    "locationNames": [
        "Location Alpha",
        "The Large Hadron Collider"
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
    "observationUnitDbIds": [
        "66bab7e3",
        "0e5e7f99"
    ],
    "observationUnitNames": [
        "FieldA_PlotB",
        "SpecialPlantName"
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
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "entryType": "TEST",
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
                    "observationLevel": {
                        "levelCode": "Plot_123",
                        "levelName": "plot",
                        "levelOrder": 2
                    },
                    "observationLevelRelationships": [
                        {
                            "levelCode": "Field_1",
                            "levelName": "field",
                            "levelOrder": 0
                        },
                        {
                            "levelCode": "Block_12",
                            "levelName": "block",
                            "levelOrder": 1
                        },
                        {
                            "levelCode": "Plot_123",
                            "levelName": "plot",
                            "levelOrder": 2
                        }
                    ],
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW"
                },
                "observations": [
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
                ],
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "seedLotDbId": "261ecb09",
                "seedLotName": "Seed Lot Alpha",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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




### Get - /search/observationunits/{searchResultsDbId} [GET /brapi/v2/search/observationunits/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `ObservationUnits` search request <br/>
Clients should submit a search request using the corresponding `POST /search/observationunits` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The ID which uniquely identifies a location, associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>The human readable name of a location associated with this study</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. </td></tr>
<tr><td><span style="font-weight:bold;">observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPUI</span></td><td>string</td><td>A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitPosition</span></td><td>object</td><td>All positional and layout information related to this Observation Unit   MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative)  or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value.  Levels of observation must be consistent with those listed in the Study section.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.entryType</span></td><td>string</td><td>The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observationUnitPosition<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevel</span></td><td>object</td><td>The exact level and level code of an observation unit.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables).  Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead." </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevel<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.observationLevelRelationships</span></td><td>array[object]</td><td>Observation levels indicate the granularity level at which the measurements are taken. `levelName`  defines the level, `levelOrder` defines where that level exists in the hierarchy of levels.  `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are  at the bottom of the hierarchy (ie plant > 6). `levelCode` is an ID code for this level tag. Identify  this observation unit by each level of the hierarchy where it exists.   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>.   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample** </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelCode</span></td><td>string</td><td>An ID code or number to represent a real thing that may or may not be an an observation unit. <br/>For example, if the 'levelName' is 'plot', then the 'levelCode' would be the plot number or plot barcode. If this plot is also considered an ObservationUnit, then the appropriate observationUnitDbId should also be recorded. <br/>If the 'levelName' is 'field', then the 'levelCode' might be something like '3' or 'F3' to indicate the third field at a research station. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelName</span></td><td>string</td><td>A name for this level   **Standard Level Names: study, field, entry, rep, block, sub-block, plot, sub-plot, plant, pot, sample**   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.levelOrder</span></td><td>integer</td><td>`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers  are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).   For more information on Observation Levels, please review the <a target="_blank" href="https://wiki.brapi.org/index.php/Observation_Levels">Observation Levels documentation</a>. </td></tr>
<tr><td>observationUnitPosition<br>.observationLevelRelationships<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit <br/>If this level has on ObservationUnit associated with it, record the observationUnitDbId here. This is intended to construct a strict hierarchy of observationUnits.  <br/>If there is no ObservationUnit associated with this level, this field can set to NULL or omitted from the response.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateX</span></td><td>string</td><td>The X position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateXType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateY</span></td><td>string</td><td>The Y position coordinate for an observation unit. Different systems may use different coordinate systems.</td></tr>
<tr><td>observationUnitPosition<br><span style="font-weight:bold;margin-left:5px">.positionCoordinateYType</span></td><td>string</td><td>The type of positional coordinate used. Must be one of the following values   LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details   PLANTED_ROW - The physical planted row number    PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row   GRID_ROW - The row index number of a square grid overlay   GRID_COL - The column index number of a square grid overlay   MEASURED_ROW - The distance in meters from a defined 0-th row   MEASURED_COL - The distance in meters from a defined 0-th column </td></tr>
<tr><td><span style="font-weight:bold;">observations</span></td><td>array[object]</td><td>All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.collector</span></td><td>string</td><td>The name or identifier of the entity which collected the observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>observations<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.geoCoordinates</span></td><td>object</td><td>One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.geometry</span></td><td>object</td><td>A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.</td></tr>
<tr><td>observations<br>.geoCoordinates<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td>The literal string "Feature"</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The ID which uniquely identifies a germplasm</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>Name of the germplasm. It can be the preferred name and does not have to be unique.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time when this observation was made</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>A human readable name for an observation unit</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableDbId</span></td><td>string</td><td>The ID which uniquely identifies an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.observationVariableName</span></td><td>string</td><td>A human readable name for an observation variable</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>object</td><td></td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.season</span></td><td>string</td><td>**Deprecated in v2.1** Please use `seasonName`. Github issue number #456   Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonDbId</span></td><td>string</td><td>The ID which uniquely identifies a season. For backward compatibility it can be a string like '2012', '1957-2004'</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.seasonName</span></td><td>string</td><td>Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.</td></tr>
<tr><td>observations<br>.season<br><span style="font-weight:bold;margin-left:5px">.year</span></td><td>integer</td><td>The 4 digit year of the season.</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.uploadedBy</span></td><td>string</td><td>The name or id of the user who uploaded the observation to the database system</td></tr>
<tr><td>observations<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The value of the data collected as an observation</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies a program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of a program</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string</td><td>The unique identifier for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string</td><td>A human readable name for the originating Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The ID which uniquely identifies a study within the given database server</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name for a study</td></tr>
<tr><td><span style="font-weight:bold;">treatments</span></td><td>array[object]</td><td>List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.factor</span></td><td>string</td><td>The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.</td></tr>
<tr><td>treatments<br><span style="font-weight:bold;margin-left:5px">.modality</span></td><td>string</td><td>The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. </td></tr>
<tr><td><span style="font-weight:bold;">trialDbId</span></td><td>string</td><td>The ID which uniquely identifies a trial</td></tr>
<tr><td><span style="font-weight:bold;">trialName</span></td><td>string</td><td>The human readable name of a trial</td></tr>
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
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPUI": "http://pui.per/plot/1a9afc14",
                "observationUnitPosition": {
                    "entryType": "TEST",
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
                    "observationLevel": {
                        "levelCode": "Plot_123",
                        "levelName": "plot",
                        "levelOrder": 2
                    },
                    "observationLevelRelationships": [
                        {
                            "levelCode": "Field_1",
                            "levelName": "field",
                            "levelOrder": 0
                        },
                        {
                            "levelCode": "Block_12",
                            "levelName": "block",
                            "levelOrder": 1
                        },
                        {
                            "levelCode": "Plot_123",
                            "levelName": "plot",
                            "levelOrder": 2
                        }
                    ],
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW"
                },
                "observations": [
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
                ],
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
                "seedLotDbId": "261ecb09",
                "seedLotName": "Seed Lot Alpha",
                "studyDbId": "9865addc",
                "studyName": "Purple_Tomato_1",
                "treatments": [
                    {
                        "factor": "fertilizer",
                        "modality": "low fertilizer"
                    }
                ],
                "trialDbId": "776a609c",
                "trialName": "Purple Tomato"
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

