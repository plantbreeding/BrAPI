
# Group Observation Units

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.





### Get - /observationlevels [GET /brapi/v2/observationlevels{?studyDbId}{?trialDbId}{?programDbId}{?page}{?pageSize}]

Call to retrieve the list of supported observation levels. 

Observation levels indicate the granularity level at which the measurements are taken. `levelName` defines the level, `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6). 

The values are used to supply the `observationLevel` parameter in the observation unit details call.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|


 

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




### Get - /observationunits [GET /brapi/v2/observationunits{?germplasmDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationUnitLevelName}{?observationUnitLevelOrder}{?observationUnitLevelCode}{?includeObservations}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered set of Observation Units



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|observations|array[object]|All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.|
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
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationUnitLevelName (Optional, ) ... The Observation Unit Level. Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelName
    + observationUnitLevelOrder (Optional, ) ... The Observation Unit Level Order Number. Returns only the observation unit of the specified Level. References ObservationUnit->observationUnitPosition->observationLevel->levelOrder
    + observationUnitLevelCode (Optional, ) ... The Observation Unit Level Code. This parameter should be used together with `observationUnitLevelName` or `observationUnitLevelOrder`. References ObservationUnit->observationUnitPosition->observationLevel->levelCode
    + includeObservations (Optional, ) ... Use this parameter to include a list of observations embedded in each ObservationUnit object. CAUTION - Use this parameter at your own risk. It may return large, unpaginated lists of observation data. Only set this value to True if you are sure you need to.
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
                ],
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

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|observations|array[object]|All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.|
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
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
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
                ],
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

|Field|Type|Description|
|---|---|---| 


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|observations|array[object]|All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.|
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
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
                ],
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




### Get - /observationunits/table [GET /brapi/v2/observationunits/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}]

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

|Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation data recorded for different observation variables across different observation units|
|headerRow|array[string]|<p>The table is REQUIRED to have the following columns</p> <ul>   <li>observationUnitDbId - Each row is related to one Observation Unit</li>   <li>At least one column with an observationVariableDbId</li> </ul> <p>The table may have any or all of the following OPTIONAL columns. Included columns are decided by the server developer</p> <ul>   <li>observationUnitName</li>   <li>studyDbId</li>   <li>studyName</li>   <li>germplasmDbId</li>   <li>germplasmName</li>   <li>positionCoordinateX</li>   <li>positionCoordinateY</li>   <li>year</li> </ul> <p>The table also may have any number of Observation Unit Hierarchy Level columns. For example:</p> <ul>   <li>field</li>   <li>plot</li>   <li>sub-plot</li>   <li>plant</li>   <li>pot</li>   <li>block</li>   <li>entry</li>   <li>rep</li> </ul> <p>The JSON representation provides a pair of extra arrays for defining the headers of the table.  The first array "headerRow" will always contain "observationUnitDbId" and any or all of the OPTIONAL column header names.  The second array "observationVariables" contains the names and DbIds for the Observation Variables represented in the table.  By appending the two arrays, you can construct the complete header row of the table. </p>|
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

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|observations|array[object]|All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.|
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
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
        ],
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

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|observations|array[object]|All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.|
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
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + observationUnitDbId (Required, ) ... The unique ID of the specific Observation Unit
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
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
        ],
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

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.

Use case - this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.

Example Use cases 

- Study a panel of germplasm across multiple studies

- Get all data for a specific study 

- Get simple atomic phenotyping values 

- Study Locations for adaptation to climate change

- Find phenotypes that are from after a certain timestamp

observationTimeStampRangeStart and observationTimeStampRangeEnd use Iso Standard 8601.

observationValue data type inferred from the ontology

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|externalReferenceIDs|array[string]|List of external references for the trait to search for|
|externalReferenceSources|array[string]|List of external references sources for the trait to search for|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm to search for|
|germplasmNames|array[string]|List of human readable names to identify germplasm to search for|
|includeObservations|boolean|Use this parameter to include a list of observations embedded in each ObservationUnit object.   CAUTION - Use this parameter at your own risk. It may return large, unpaginated lists of observation data. Only set this value to True if you are sure you need to.|
|locationDbIds|array[string]|The location ids to search for|
|locationNames|array[string]|A human readable names to search for|
|observationLevelRelationships|array[object]|Searches for values in ObservationUnit->observationUnitPosition->observationLevelRelationships|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevels|array[object]|Searches for values in ObservationUnit->observationUnitPosition->observationLevel|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationUnitDbIds|array[string]|The unique id of an observation unit|
|observationVariableDbIds|array[string]|The DbIds of Variables to search for|
|observationVariableNames|array[string]|The names of Variables to search for|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A program identifier to search for|
|programNames|array[string]|A name of a program to search for|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|trialDbIds|array[string]|The ID which uniquely identifies a trial to search for|
|trialNames|array[string]|The human readable name of a trial to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|observations|array[object]|All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.|
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
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
                ],
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




### Get - /search/observationunits/{searchResultsDbId} [GET /brapi/v2/search/observationunits/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit  MIAPPE V1.1 (DM-70) Observation unit ID - Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique. |
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPUI|string|A Permanent Unique Identifier for an observation unit  MIAPPE V1.1 (DM-72) External ID - Identifier for the observation unit in a persistent repository, comprises the name of the repository and the identifier of the observation unit therein. The EBI Biosamples repository can be used. URI are recommended when possible.|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit  MIAPPE V1.1 (DM-73) Spatial distribution - Type and value of a spatial coordinate (georeference or relative) or level of observation (plot 45, subblock 7, block 2) provided as a key-value pair of the form type:value. Levels of observation must be consistent with those listed in the Study section.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|observationLevel|object|The exact level and level code of an observation unit.   MIAPPE V1.1 DM-71 Observation unit type "Type of observation unit in textual form, usually one of the following: study, block, sub-block, plot, sub-plot, pot, plant. Use of other observation unit types is possible but not recommended.  The observation unit type can not be used to indicate sub-plant levels. However, observations can still be made on the sub-plant level, as long as the details are indicated in the associated observed variable (see observed variables). Alternatively, it is possible to use samples for more detailed tracing of sub-plant units, attaching the observations to them instead."|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|observationLevelRelationships|array[object]|Observation levels indicate the granularity level at which the measurements are taken.   `levelName` defines the level   `levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`s lower numbers are at the top of the hierarchy (ie field > 0) and higher numbers are at the bottom of the hierarchy (ie plant > 6).   `levelCode` is an ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelCode|string|An ID code for this level tag. Identify this observation unit by each level of the hierarchy where it exists|
|levelName|string|A name for this level|
|levelOrder|integer|`levelOrder` defines where that level exists in the hierarchy of levels. `levelOrder`'s lower numbers are at the top of the hierarchy (ie field -> 1) and higher numbers are at the bottom of the hierarchy (ie plant -> 9).|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|observations|array[object]|All observations attached to this observation unit.   Default for this field is null or omitted. Do NOT include data in this field unless the 'includeObservations' flag is explicitly set to True.|
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
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|seedLotDbId|string|The unique identifier for the originating Seed Lot|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.  MIAPPE V1.1 (DM-74) Observation Unit factor value - List of values for each factor applied to the observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc  MIAPPE V1.1 (DM-61) Experimental Factor type - Name/Acronym of the experimental factor.|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc  MIAPPE V1.1 (DM-62) Experimental Factor description - Free text description of the experimental factor. This includes all relevant treatments planned and protocol planned for all the plants targeted by a given experimental factor. |
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

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
                "additionalInfo": {},
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
                ],
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

