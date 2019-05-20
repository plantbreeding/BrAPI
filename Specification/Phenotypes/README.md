
# Group Phenotypes

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.




## Observationunits [/brapi/v1/observationunits] 




### Get Observationunits  [GET /brapi/v1/observationunits{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?page}{?pageSize}]

Get a set of observation units



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationLevels|string|Concatenation of the levels of this observationUnit. Used to handle non canonical level structures. Format levelType:levelID,levelType:levelID|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|observations|array[object]|List of observations associated with this observation unit|
|collector|string|The name or identifier of the entity which collected the observation|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|string|The season when the observation data was collected|
|value|string|The value of the data collected as an observation|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|programName|string|The human readable name of a program|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyLocation|string|The human readable name of a location associated with this study|
|studyLocationDbId|string|The ID which uniquely identifies a location, associated with this study|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|


 

+ Parameters
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + observationVariableDbId (Optional, ) ... The unique ID of an observation variable
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "1",
                "entryNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239865",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "1",
                        "observationTimeStamp": "2013-06-14T22:03:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "fall 2011",
                        "value": "1.2"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "2",
                        "observationTimeStamp": "2013-06-14T22:04:51-04:00",
                        "observationVariableDbId": "MO_123:100006",
                        "observationVariableName": "Virus severity",
                        "season": "fall 2011",
                        "value": "4.5"
                    }
                ],
                "plantNumber": "null",
                "plotNumber": "1",
                "programName": "Program 1",
                "replicate": "0",
                "studyDbId": "1001",
                "studyLocation": "Peru",
                "studyLocationDbId": "1",
                "studyName": "Study 1",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "deficit"
                    }
                ]
            },
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "101",
                "entryNumber": "1",
                "entryType": "FILLER",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "observationLevel": "plant",
                "observationLevels": "block:101;plot:5;plant:5",
                "observationUnitDbId": "10",
                "observationUnitName": "Plant 5",
                "observationUnitXref": [],
                "observations": [
                    {
                        "collector": "B. Tech",
                        "observationDbId": "16",
                        "observationTimeStamp": "2011-06-14T22:06:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "winter 2012",
                        "value": "100"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "17",
                        "observationTimeStamp": "2011-06-14T22:07:51-04:00",
                        "observationVariableDbId": "MO_123:100003",
                        "observationVariableName": "Carotenoid",
                        "season": "winter 2012",
                        "value": "9"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "18",
                        "observationTimeStamp": "2011-06-14T22:08:51-04:00",
                        "observationVariableDbId": "MO_123:100004",
                        "observationVariableName": "Root weight",
                        "season": "winter 2012",
                        "value": "2"
                    }
                ],
                "plantNumber": "5",
                "plotNumber": "5",
                "programName": "Program 1",
                "replicate": "1",
                "studyDbId": "1003",
                "studyLocation": "Peru",
                "studyLocationDbId": "2",
                "studyName": "Study 3",
                "treatments": []
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```



## Phenotypes-search [/brapi/v1/phenotypes-search] 




### **Deprecated** Post Phenotypes-search Csv  [POST /brapi/v1/phenotypes-search/csv]

DEPRECATED in v1.3 - See /search/observationtables

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|list of programs to search across|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|




 

+ Parameters


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationLevel": "observationLevel0",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "seasonDbIds": [
        "seasonDbIds0",
        "seasonDbIds1"
    ],
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{}
```

+ Response 200 (text/csv)
```
{}
```





### **Deprecated** Get Phenotypes-search  [GET /brapi/v1/phenotypes-search{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?page}{?pageSize}]

DEPRECATED in v1.3 - See GET /observationunits



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationLevels|string|Concatenation of the levels of this observationUnit. Used to handle non canonical level structures. Format levelType:levelID,levelType:levelID|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|observations|array[object]|List of observations associated with this observation unit|
|collector|string|The name or identifier of the entity which collected the observation|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|string|The season when the observation data was collected|
|value|string|The value of the data collected as an observation|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|programName|string|The human readable name of a program|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyLocation|string|The human readable name of a location associated with this study|
|studyLocationDbId|string|The ID which uniquely identifies a location, associated with this study|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|


 

+ Parameters
    + germplasmDbId (Optional, ) ... The name or synonym of external genebank accession identifiers
    + observationVariableDbId (Optional, ) ... The ID of traits, could be ontology ID, database ID or PUI
    + studyDbId (Optional, ) ... The database ID / PK of the studies search parameter
    + locationDbId (Optional, ) ... locations these traits were collected
    + trialDbId (Optional, ) ... trial to search across
    + programDbId (Optional, ) ... program that have phenotyped this trait
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + observationTimeStampRangeStart (Optional, ) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, ) ... Timestamp range end
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "1",
                "entryNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239865",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "1",
                        "observationTimeStamp": "2013-06-14T22:03:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "fall 2011",
                        "value": "1.2"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "2",
                        "observationTimeStamp": "2013-06-14T22:04:51-04:00",
                        "observationVariableDbId": "MO_123:100006",
                        "observationVariableName": "Virus severity",
                        "season": "fall 2011",
                        "value": "4.5"
                    }
                ],
                "plantNumber": "null",
                "plotNumber": "1",
                "programName": "Program 1",
                "replicate": "0",
                "studyDbId": "1001",
                "studyLocation": "Peru",
                "studyLocationDbId": "1",
                "studyName": "Study 1",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "deficit"
                    }
                ]
            },
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "101",
                "entryNumber": "1",
                "entryType": "FILLER",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "observationLevel": "plant",
                "observationLevels": "block:101;plot:5;plant:5",
                "observationUnitDbId": "10",
                "observationUnitName": "Plant 5",
                "observationUnitXref": [],
                "observations": [
                    {
                        "collector": "B. Tech",
                        "observationDbId": "16",
                        "observationTimeStamp": "2011-06-14T22:06:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "winter 2012",
                        "value": "100"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "17",
                        "observationTimeStamp": "2011-06-14T22:07:51-04:00",
                        "observationVariableDbId": "MO_123:100003",
                        "observationVariableName": "Carotenoid",
                        "season": "winter 2012",
                        "value": "9"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "18",
                        "observationTimeStamp": "2011-06-14T22:08:51-04:00",
                        "observationVariableDbId": "MO_123:100004",
                        "observationVariableName": "Root weight",
                        "season": "winter 2012",
                        "value": "2"
                    }
                ],
                "plantNumber": "5",
                "plotNumber": "5",
                "programName": "Program 1",
                "replicate": "1",
                "studyDbId": "1003",
                "studyLocation": "Peru",
                "studyLocationDbId": "2",
                "studyName": "Study 3",
                "treatments": []
            }
        ]
    }
}
```





### **Deprecated** Post Phenotypes-search  [POST /brapi/v1/phenotypes-search]

DEPRECATED in v1.3 - See /search/observationunits

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|list of programs to search across|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationLevels|string|Concatenation of the levels of this observationUnit. Used to handle non canonical level structures. Format levelType:levelID,levelType:levelID|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|observations|array[object]|List of observations associated with this observation unit|
|collector|string|The name or identifier of the entity which collected the observation|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|string|The season when the observation data was collected|
|value|string|The value of the data collected as an observation|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|programName|string|The human readable name of a program|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyLocation|string|The human readable name of a location associated with this study|
|studyLocationDbId|string|The ID which uniquely identifies a location, associated with this study|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|


 

+ Parameters


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationLevel": "observationLevel0",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "seasonDbIds": [
        "seasonDbIds0",
        "seasonDbIds1"
    ],
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "1",
                "entryNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239865",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "1",
                        "observationTimeStamp": "2013-06-14T22:03:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "fall 2011",
                        "value": "1.2"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "2",
                        "observationTimeStamp": "2013-06-14T22:04:51-04:00",
                        "observationVariableDbId": "MO_123:100006",
                        "observationVariableName": "Virus severity",
                        "season": "fall 2011",
                        "value": "4.5"
                    }
                ],
                "plantNumber": "null",
                "plotNumber": "1",
                "programName": "Program 1",
                "replicate": "0",
                "studyDbId": "1001",
                "studyLocation": "Peru",
                "studyLocationDbId": "1",
                "studyName": "Study 1",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "deficit"
                    }
                ]
            },
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "101",
                "entryNumber": "1",
                "entryType": "FILLER",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "observationLevel": "plant",
                "observationLevels": "block:101;plot:5;plant:5",
                "observationUnitDbId": "10",
                "observationUnitName": "Plant 5",
                "observationUnitXref": [],
                "observations": [
                    {
                        "collector": "B. Tech",
                        "observationDbId": "16",
                        "observationTimeStamp": "2011-06-14T22:06:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "winter 2012",
                        "value": "100"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "17",
                        "observationTimeStamp": "2011-06-14T22:07:51-04:00",
                        "observationVariableDbId": "MO_123:100003",
                        "observationVariableName": "Carotenoid",
                        "season": "winter 2012",
                        "value": "9"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "18",
                        "observationTimeStamp": "2011-06-14T22:08:51-04:00",
                        "observationVariableDbId": "MO_123:100004",
                        "observationVariableName": "Root weight",
                        "season": "winter 2012",
                        "value": "2"
                    }
                ],
                "plantNumber": "5",
                "plotNumber": "5",
                "programName": "Program 1",
                "replicate": "1",
                "studyDbId": "1003",
                "studyLocation": "Peru",
                "studyLocationDbId": "2",
                "studyName": "Study 3",
                "treatments": []
            }
        ]
    }
}
```





### **Deprecated** Post Phenotypes-search Tsv  [POST /brapi/v1/phenotypes-search/tsv]

DEPRECATED in v1.3 - See /search/observationtables

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|list of programs to search across|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|




 

+ Parameters


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationLevel": "observationLevel0",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "seasonDbIds": [
        "seasonDbIds0",
        "seasonDbIds1"
    ],
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{}
```

+ Response 200 (text/csv)
```
{}
```





### **Deprecated** Post Phenotypes-search Table  [POST /brapi/v1/phenotypes-search/table]

DEPRECATED in v1.3 - See /search/observationtables

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|list of programs to search across|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation meta-data and recorded values. Each inner array represents 1 row of data.|
|headerRow|array[string]|Names of the columns included in the data matrix. Any or All of [ "year","studyDbId","studyName","locationDbId","locationName","germplasmDbId","germplasmName","observationUnitDbId","plotNumber","replicate","blockNumber", "entryType", "X", "Y"]|
|observationVariableDbIds|array[string]|Array of observation variable DbIds for the collected data. This array is appended to the "headerRow" to get the complete header of the data matrix|
|observationVariableNames|array[string]|Human readable names of the observation variables for the collected data. This array should match 1 to 1 with the "observationVariableDbIds" array.|


 

+ Parameters


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationLevel": "observationLevel0",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "seasonDbIds": [
        "seasonDbIds0",
        "seasonDbIds1"
    ],
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            [
                "2013",
                "1001",
                "Study 1",
                "1",
                "Location 1",
                "1",
                "Name001",
                "1",
                "1",
                "0",
                "1",
                "TEST",
                "1",
                "1",
                "1.2",
                "4.5",
                "",
                ""
            ],
            [
                "2011",
                "1003",
                "Study 3",
                "2",
                "Location 2",
                "4",
                "Name004",
                "10",
                "5",
                "1",
                "101",
                "FILLER",
                "1",
                "1",
                "100",
                "",
                "9",
                "2"
            ]
        ],
        "headerRow": [
            "year",
            "studyDbId",
            "studyName",
            "locationDbId",
            "locationName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "plotNumber",
            "replicate",
            "blockNumber",
            "entryType",
            "X",
            "Y"
        ],
        "observationVariableDbIds": [
            "MO_123:100002",
            "MO_123:100006",
            "MO_123:100003",
            "MO_123:100004"
        ],
        "observationVariableNames": [
            "Plant height",
            "Virus severity",
            "Carotenoid",
            "Root weight"
        ]
    }
}
```



## Phenotypes [/brapi/v1/phenotypes] 




### Post Phenotypes  [POST /brapi/v1/phenotypes{?format}]

Notes: 

Along with the study specific phenotype saving calls (in the observationUnit and table formats), this call allows phenotypes to be saved and images to optionally be transferred as well.

Call to invoke for saving the measurements (observations) collected\nfrom field for all the observation units.

Observation timestamp should be ISO 8601 https://www.w3.org/TR/NOTE-datetime 

In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call. In this case a format parameter should be passed as well. 

Images can be optionally be uploaded using this call by providing a zipfile of all images in the datafiles, along with the actual zipfile in multi-part form data."

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]|Matrix of observation data recorded for different observation variables across different observation units|
|observatioUnitDbId|string||
|observations|array[object]||
|collector|string|The name or identifier of the entity which collected the observation|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationVariableDbId|string|Variable unique identifier|
|observationVariableName|string|A human readable name for an observation variable|
|season|string|The season when the observation data was collected|
|value|string|The value of the data collected as an observation|
|studyDbId|string||


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|observations|array[object]|List of observation references which have been created or updated|
|observationDbId|string||
|observationUnitDbId|string||
|observationVariableDbId|string||


 

+ Parameters
    + format (Optional, ) ... In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "data": [
        {
            "observatioUnitDbId": "observatioUnitDbId0",
            "observations": [
                {
                    "collector": "collector0",
                    "observationDbId": "observationDbId0",
                    "observationTimeStamp": "2018-01-01T14:47:23-0600",
                    "observationVariableDbId": "observationVariableDbId0",
                    "observationVariableName": "observationVariableName0",
                    "season": "season0",
                    "value": "value0"
                },
                {
                    "collector": "collector1",
                    "observationDbId": "observationDbId1",
                    "observationTimeStamp": "2018-01-01T14:47:23-0600",
                    "observationVariableDbId": "observationVariableDbId1",
                    "observationVariableName": "observationVariableName1",
                    "season": "season1",
                    "value": "value1"
                }
            ],
            "studyDbId": "studyDbId0"
        },
        {
            "observatioUnitDbId": "observatioUnitDbId1",
            "observations": [
                {
                    "collector": "collector0",
                    "observationDbId": "observationDbId0",
                    "observationTimeStamp": "2018-01-01T14:47:23-0600",
                    "observationVariableDbId": "observationVariableDbId0",
                    "observationVariableName": "observationVariableName0",
                    "season": "season0",
                    "value": "value0"
                },
                {
                    "collector": "collector1",
                    "observationDbId": "observationDbId1",
                    "observationTimeStamp": "2018-01-01T14:47:23-0600",
                    "observationVariableDbId": "observationVariableDbId1",
                    "observationVariableName": "observationVariableName1",
                    "season": "season1",
                    "value": "value1"
                }
            ],
            "studyDbId": "studyDbId1"
        }
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "observations": [
            {
                "observationDbId": "bb989815-86bf-430b-9d87-054df8919767",
                "observationUnitDbId": "1",
                "observationVariableDbId": "MO_123:100002"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```



## Search [/brapi/v1/search] 




### Post Search Observationtables  [POST /brapi/v1/search/observationtables]

Returns a list of observationUnit with the observed Phenotypes.

observationTimeStamp - Iso Standard 8601.

observationValue data type inferred from the ontology

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|list of programs to search across|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationLevel": "observationLevel0",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "seasonDbIds": [
        "seasonDbIds0",
        "seasonDbIds1"
    ],
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "searchResultDbId": "551ae08c-4548-4bde-ad70-f23beb25e2ea"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Search Observationtables by searchResultsDbId  [GET /brapi/v1/search/observationtables/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of observationUnit with the observed Phenotypes.

observationTimeStamp - Iso Standard 8601.

observationValue data type inferred from the ontology




**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[array]|Matrix of observation meta-data and recorded values. Each inner array represents 1 row of data.|
|headerRow|array[string]|Names of the columns included in the data matrix. Any or All of [ "year","studyDbId","studyName","locationDbId","locationName","germplasmDbId","germplasmName","observationUnitDbId","plotNumber","replicate","blockNumber", "entryType", "X", "Y"]|
|observationVariableDbIds|array[string]|Array of observation variable DbIds for the collected data. This array is appended to the "headerRow" to get the complete header of the data matrix|
|observationVariableNames|array[string]|Human readable names of the observation variables for the collected data. This array should match 1 to 1 with the "observationVariableDbIds" array.|


 

+ Parameters
    + Accept (Required, ) ... The requested content type which should be returned by the server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            [
                "2013",
                "1001",
                "Study 1",
                "1",
                "Location 1",
                "1",
                "Name001",
                "1",
                "1",
                "0",
                "1",
                "TEST",
                "1",
                "1",
                "1.2",
                "4.5",
                "",
                ""
            ],
            [
                "2011",
                "1003",
                "Study 3",
                "2",
                "Location 2",
                "4",
                "Name004",
                "10",
                "5",
                "1",
                "101",
                "FILLER",
                "1",
                "1",
                "100",
                "",
                "9",
                "2"
            ]
        ],
        "headerRow": [
            "year",
            "studyDbId",
            "studyName",
            "locationDbId",
            "locationName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "plotNumber",
            "replicate",
            "blockNumber",
            "entryType",
            "X",
            "Y"
        ],
        "observationVariableDbIds": [
            "MO_123:100002",
            "MO_123:100006",
            "MO_123:100003",
            "MO_123:100004"
        ],
        "observationVariableNames": [
            "Plant height",
            "Virus severity",
            "Carotenoid",
            "Root weight"
        ]
    }
}
```

+ Response 200 (text/csv)
```
"\"year\", \"studyDbId\", \"studyName\", \"locationDbId\", \"locationName\", \"germplasmDbId\", \"germplasmName\", \"observationUnitDbId\", \"plotNumber\", \"replicate\", \"blockNumber\", \"entryType\", \"X\", \"Y\", \"MO_123:100002\", \"MO_123:100006\", \"MO_123:100003\", \"MO_123:100004\", \"MO_123:100005\"\n\"2013\", \"1001\", \"Study 1\", \"1\", \"Location 1\", \"1\", \"Name001\", \"1\", \"1\", \"0\", \"1\", \"TEST\", \"1\", \"1\", \"1.2\", \"4.5\", \"\", \"\", \"\"\n\"2011\", \"1003\", \"Study 3\", \"2\", \"Location 2\", \"4\", \"Name004\", \"10\", \"5\", \"1\", \"101\", \"FILLER\", \"1\", \"1\", \"100\", \"\", \"9\", \"2\", \"\"\n\"2011\", \"1003\", \"Study 3\", \"2\", \"Location 2\", \"2\", \"Name002\", \"11\", \"6\", \"1\", \"101\", \"FILLER\", \"1\", \"1\", \"11\", \"\", \"12\", \"5\", \"black\"\n\"2013\", \"1001\", \"Study 1\", \"1\", \"Location 1\", \"1\", \"Name001\", \"2\", \"1\", \"0\", \"1\", \"TEST\", \"1\", \"1\", \"1.1\", \"5.1\", \"\", \"\", \"\""
```

+ Response 200 (text/tsv)
```
"\"year\"\t\"studyDbId\"\t\"studyName\"\t\"locationDbId\"\t\"locationName\"\t\"germplasmDbId\"\t\"germplasmName\"\t\"observationUnitDbId\"\t\"plotNumber\"\t\"replicate\"\t\"blockNumber\"\t\"entryType\"\t\"X\"\t\"Y\"\t\"MO_123:100002\"\t\"MO_123:100006\"\t\"MO_123:100003\"\t\"MO_123:100004\"\t\"MO_123:100005\"\n\"2013\"\t\"1001\"\t\"Study 1\"\t\"1\"\t\"Location 1\"\t\"1\"\t\"Name001\"\t\"1\"\t\"1\"\t\"0\"\t\"1\"\t\"TEST\"\t\"1\"\t\"1\"\t\"1.2\"\t\"4.5\"\t\"\"\t\"\"\t\"\"\n\"2011\"\t\"1003\"\t\"Study 3\"\t\"2\"\t\"Location 2\"\t\"4\"\t\"Name004\"\t\"10\"\t\"5\"\t\"1\"\t\"101\"\t\"FILLER\"\t\"1\"\t\"1\"\t\"100\"\t\"\"\t\"9\"\t\"2\"\t\"\"\n\"2011\"\t\"1003\"\t\"Study 3\"\t\"2\"\t\"Location 2\"\t\"2\"\t\"Name002\"\t\"11\"\t\"6\"\t\"1\"\t\"101\"\t\"FILLER\"\t\"1\"\t\"1\"\t\"11\"\t\"\"\t\"12\"\t\"5\"\t\"black\"\n\"2013\"\t\"1001\"\t\"Study 1\"\t\"1\"\t\"Location 1\"\t\"1\"\t\"Name001\"\t\"2\"\t\"1\"\t\"0\"\t\"1\"\t\"TEST\"\t\"1\"\t\"1\"\t\"1.1\"\t\"5.1\"\t\"\"\t\"\"\t\"\""
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Post Search Observationunits  [POST /brapi/v1/search/observationunits]

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.

Use case - this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.

Refactor note - This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below.

Example Use cases 

- Study a panel of germplasm accross multiple studies

    '{"germplasmDbIds": ["Syrah", "34Mtp362"]}'

- Get all data for a specific study (same as "/studies/{studyDbId}/observationunits")

    '{"studyDbIds" : ["383"]}'

- Get simple atomic phenotyping values 

    '{

       "germplasmDbIds" : [ "Syrah", "34Mtp362" ], 

       "observationVariableDbIds" : [ "CO_345:0000043"]

     }'

- Study Locations for adaptation to climate change

    '{

       "locationDbIds" : ["383838", "MONTPELLIER"], 

       "germplasmDbIds" : [ "14Mtp361", "24Mtp362", "34Mtp363", "44Mtp364"]

     }'

- Find phenotypes that are from after a certain timestamp

    '{

       "observationTimeStampRangeStart" : "2013-06-14T23:59:59-04:00", 

       "observationTimeStampRangeEnd" : "2013-06-15T23:59:59-04:00"

     }'
     
observationTimeStampRangeStart and observationTimeStampRangeEnd use Iso Standard 8601.

observationValue data type inferred from the ontology

**Request Fields** 
 |Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationTimeStampRangeEnd|string (date-time)|Timestamp range end|
|observationTimeStampRangeStart|string (date-time)|Timestamp range start|
|observationVariableDbIds|array[string]|The IDs of traits, could be ontology ID, database ID or PUI|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|programDbIds|array[string]|list of programs to search across|
|seasonDbIds|array[string]|The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|


**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "locationDbIds": [
        "locationDbIds0",
        "locationDbIds1"
    ],
    "observationLevel": "observationLevel0",
    "observationTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "observationTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "programDbIds": [
        "programDbIds0",
        "programDbIds1"
    ],
    "seasonDbIds": [
        "seasonDbIds0",
        "seasonDbIds1"
    ],
    "studyDbIds": [
        "studyDbIds0",
        "studyDbIds1"
    ],
    "trialDbIds": [
        "trialDbIds0",
        "trialDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "searchResultDbId": "551ae08c-4548-4bde-ad70-f23beb25e2ea"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Search Observationunits by searchResultsDbId  [GET /brapi/v1/search/observationunits/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.



**Response Fields** 
 |Field|Type|Description|
|---|---|---| 
|data|array[object]||
|X|string|DEPRECATED - use "positionCoordinateX"|
|Y|string|DEPRECATED - use "positionCoordinateY"|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "check", "test", "filler"|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationLevels|string|Concatenation of the levels of this observationUnit. Used to handle non canonical level structures. Format levelType:levelID,levelType:levelID|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|observations|array[object]|List of observations associated with this observation unit|
|collector|string|The name or identifier of the entity which collected the observation|
|observationDbId|string|The ID which uniquely identifies an observation|
|observationTimeStamp|string (date-time)|The date and time  when this observation was made |
|observationVariableDbId|string|The ID which uniquely identifies an observation variable|
|observationVariableName|string|A human readable name for an observation variable|
|season|object||
|season|string|Name of the season. ex. 'Spring', 'Q2', 'Season A', etc.|
|seasonDbId|string|The ID which uniquely identifies a season|
|year|string|The 4 digit year of the season.|
|value|string|The value of the data collected as an observation|
|pedigree|string|The string representation of the pedigree of this observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See "Location Coordinate Encoding" for details PLANTED_ROW - The physical planted row number  PLANTED_INDIVIDUAl - The physical counted number, could be independant or within a planted row GRID_ROW - The row index number of a square grid overlay GRID_COL - The column index number of a square grid overlay MEASURED_ROW - The distance in meters from a defined 0th row MEASURED_COL - The distance in meters from a defined 0th column |
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyLocation|string|DEPRECATED in v1.3 - see "locationName"|
|studyLocationDbId|string|DEPRECATED in v1.3 - see "locationDbId"|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor descritpion. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "1",
                "entryNumber": "1",
                "entryType": "TEST",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "observationUnitDbId": "1",
                "observationUnitName": "Plot 1",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239865",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "1",
                        "observationTimeStamp": "2013-06-14T22:03:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "1.2"
                    },
                    {
                        "collector": "A. Technician",
                        "observationDbId": "2",
                        "observationTimeStamp": "2013-06-14T22:04:51-04:00",
                        "observationVariableDbId": "MO_123:100006",
                        "observationVariableName": "Virus severity",
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "4.5"
                    },
                    {
                        "collector": "string",
                        "observationDbId": "bb989815-86bf-430b-9d87-054df8919767",
                        "observationTimeStamp": "1970-01-18T14:02:52-05:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": {
                            "season": "fall",
                            "seasonDbId": "1",
                            "year": "2011"
                        },
                        "value": "string"
                    }
                ],
                "pedigree": "",
                "plantNumber": "null",
                "plotNumber": "1",
                "replicate": "0"
            },
            {
                "X": "1",
                "Y": "1",
                "blockNumber": "101",
                "entryNumber": "1",
                "entryType": "FILLER",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "observationUnitDbId": "10",
                "observationUnitName": "Plant 5",
                "observationUnitXref": [],
                "observations": [
                    {
                        "collector": "B. Tech",
                        "observationDbId": "16",
                        "observationTimeStamp": "2011-06-14T22:06:51-04:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": {
                            "season": "winter",
                            "seasonDbId": "2",
                            "year": "2012"
                        },
                        "value": "100"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "17",
                        "observationTimeStamp": "2011-06-14T22:07:51-04:00",
                        "observationVariableDbId": "MO_123:100003",
                        "observationVariableName": "Carotenoid",
                        "season": {
                            "season": "winter",
                            "seasonDbId": "2",
                            "year": "2012"
                        },
                        "value": "9"
                    },
                    {
                        "collector": "B. Tech",
                        "observationDbId": "18",
                        "observationTimeStamp": "2011-06-14T22:08:51-04:00",
                        "observationVariableDbId": "MO_123:100004",
                        "observationVariableName": "Root weight",
                        "season": {
                            "season": "winter",
                            "seasonDbId": "2",
                            "year": "2012"
                        },
                        "value": "2"
                    }
                ],
                "pedigree": "",
                "plantNumber": "5",
                "plotNumber": "5",
                "replicate": "1"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

