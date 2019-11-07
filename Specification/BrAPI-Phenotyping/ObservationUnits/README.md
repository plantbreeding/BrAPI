
# Group Observation Units

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.





### Get - /observationlevels [GET /brapi/v1/observationlevels{?page}{?pageSize}]

Call to retrieve the list of supported observation levels. 

Observation levels indicate the granularity level at which the measurements are taken. 

The values are used to supply the `observationLevel` parameter in the observation unit details call.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[string]||


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
            "field",
            "plot",
            "plant"
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




### Get - /observationunits [GET /brapi/v1/observationunits{?germplasmDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?page}{?pageSize}]

Get a filtered set of Observation Units



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + germplasmDbId (Optional, ) ... The unique ID of a germplasm (accession) to filter on
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + locationDbId (Optional, ) ... The unique ID of a location where these observations were collected
    + trialDbId (Optional, ) ... The unique ID of a trial to filter on
    + programDbId (Optional, ) ... The unique ID of a program to filter on
    + seasonDbId (Optional, ) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, ) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
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




### Post - /observationunits [POST /brapi/v1/observationunits]

Add new Observation Units

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationLevel": "plot",
        "observationUnitName": "Plot 1",
        "observationUnitPosition": {
            "blockNumber": "6",
            "entryNumber": "3",
            "entryType": [
                "CHECK",
                "TEST",
                "FILLER"
            ],
            "geoCoordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW",
            "replicate": "1"
        },
        "observationUnitXref": [
            {
                "id": "SAMEA179865230",
                "source": "ebi.biosample"
            },
            {
                "id": "INRA:CoeSt6 _SMH03",
                "source": "gnpis.lot"
            }
        ],
        "plantNumber": "1",
        "plotNumber": "01",
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
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




### Put - /observationunits [PUT /brapi/v1/observationunits]

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
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
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




### Get - /observationunits/table [GET /brapi/v1/observationunits/table{?observationUnitDbId}{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}]

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
  <li>plotNumber</li>
  <li>plantNumber</li>
  <li>blockNumber</li>
  <li>entryNumber</li>
  <li>replicate</li>
  <li>positionCoordinateX</li>
  <li>positionCoordinateY</li>
  <li>year</li>
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
|headerRow|array[string]|The header row describing observation unit fields. Append "observationVariableDbIds" for complete header row of the table.  This array should contain any or all of the following strings; year, studyDbId, studyName, locationDbId, locationName, germplasmDbId, germplasmName, observationUnitDbId, plotNumber, replicate, blockNumber, entryType, X, Y|
|observationVariableDbIds|array[string]|The list of observation variables which have values recorded for them in the data matrix. Append to the "headerRow" for complete header row.|
|observationVariableNames|array[string]|The list of observation variable names which have values recorded for them in the data matrix. Order should match "observationVariableDbIds".|


 

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




+ Response 200 (application/csv)
```
"\"observationTimeStamp\",\"studyDbId\",\"studyName\",\"germplasmDbId\",\"germplasmName\",\"observationUnitDbId\",\"observationUnitName\",\"plotNumber\",\"plantNumber\",\"blockNumber\",\"entryNumber\",\"replicate\",\"positionCoordinateX\",\"positionCoordinateY\",\"2d599b04\",\"a0e84c5c\",\"35c5670a\",\"0144dea8\"\n\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"Plant height\",\"Carotenoid\",\"Root color\",\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"1.1\", \"\",    \"\", \"\"\n\"2019-09-10T18:14:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"1.9\", \"\",    \"\", \"\"\n\"2019-09-10T18:15:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"1.4\", \"\",    \"\", \"\"\n\"2019-09-10T18:16:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"1.5\", \"\",    \"\", \"\"\n\"2019-09-10T18:17:27.223Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"d64dd058\", \"Plant alpha\",   \"1\", \"1\", \"1\", \"1\", \"1\",\"76.50106681\",\"42.44409301\", \"\",    \"2.6\", \"\", \"\"\n\"2019-09-10T18:18:54.868Z\", \"f753a83c\", \"Study 1\", \"67c3cf0c\", \"A0000001\", \"f9adff3c\", \"Plant beta\",    \"2\", \"2\", \"1\", \"1\", \"2\",\"76.50106683\",\"42.44409301\", \"\",    \"2.3\", \"\", \"\"\n\"2019-09-10T18:19:34.433Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"67102b8f\", \"Plant gamma\",   \"1\", \"3\", \"1\", \"2\", \"1\",\"76.50106685\",\"42.44409301\", \"\",    \"3.1\", \"\", \"\"\n\"2019-09-10T18:20:15.629Z\", \"f753a83c\", \"Study 1\", \"40498c3c\", \"A0000002\", \"2869d94a\", \"Plant epsilon\", \"2\", \"4\", \"1\", \"2\", \"2\",\"76.50106687\",\"42.44409301\", \"\",    \"3.2\", \"\", \"\""
```

+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1.1",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:14:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "1.9",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:15:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "1.4",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:16:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "1.5",
                "",
                "",
                ""
            ],
            [
                "2019-09-10T18:17:27.223Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "d64dd058",
                "Plant alpha",
                "1",
                "1",
                "1",
                "1",
                "1",
                "",
                "2.6",
                "",
                ""
            ],
            [
                "2019-09-10T18:18:54.868Z",
                "f753a83c",
                "Study 1",
                "67c3cf0c",
                "A0000001",
                "f9adff3c",
                "Plant beta",
                "2",
                "2",
                "1",
                "1",
                "2",
                "",
                "2.3",
                "",
                ""
            ],
            [
                "2019-09-10T18:19:34.433Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "67102b8f",
                "Plant gamma",
                "1",
                "3",
                "1",
                "2",
                "1",
                "",
                "3.1",
                "",
                ""
            ],
            [
                "2019-09-10T18:20:15.629Z",
                "f753a83c",
                "Study 1",
                "40498c3c",
                "A0000002",
                "2869d94a",
                "Plant epsilon",
                "2",
                "4",
                "1",
                "2",
                "2",
                "",
                "3.2",
                "",
                ""
            ]
        ],
        "headerRow": [
            "observationTimeStamp",
            "studyDbId",
            "studyName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "observationUnitName",
            "plotNumber",
            "plantNumber",
            "blockNumber",
            "entryNumber",
            "replicate",
            "positionCoordinateX",
            "positionCoordinateY"
        ],
        "observationVariableDbIds": [
            "367aa1a9",
            "2acb934c",
            "85a21ce1",
            "46f590e5"
        ],
        "observationVariableNames": [
            "Plant height",
            "Carotenoid",
            "Root color",
            "Virus severity"
        ]
    }
}
```

+ Response 200 (application/tsv)
```
"\"observationTimeStamp\"\t\"studyDbId\"\t\"studyName\"\t\"germplasmDbId\"\t\"germplasmName\"\t\"observationUnitDbId\"\t\"observationUnitName\"\t\"plotNumber\"\t\"plantNumber\"\t\"blockNumber\"\t\"entryNumber\"\t\"replicate\"\t\"positionCoordinateX\"\t\"positionCoordinateY\"\t\"2d599b04\"\t\"a0e84c5c\"\t\"35c5670a\"\t\"0144dea8\"\n\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"\"\t\"Plant height\"\t\"Carotenoid\"\t\"Root color\"\t\"Virus severity\"\n\"2019-09-10T18:13:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"1.1\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:14:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"1.9\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:15:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"1.4\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:16:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"1.5\"\t\"\"\t\"\"\t\"\"\n\"2019-09-10T18:17:27.223Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"d64dd058\"\t\"Plant alpha\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"1\"\t\"76.50106681\"\t\"42.44409301\"\t\"\"\t\"2.6\"\t\"\"\t\"\"\n\"2019-09-10T18:18:54.868Z\"\t\"f753a83c\"\t\"Study 1\"\t\"67c3cf0c\"\t\"A0000001\"\t\"f9adff3c\"\t\"Plant beta\"\t\"2\"\t\"2\"\t\"1\"\t\"1\"\t\"2\"\t\"76.50106683\"\t\"42.44409301\"\t\"\"\t\"2.3\"\t\"\"\t\"\"\n\"2019-09-10T18:19:34.433Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"67102b8f\"\t\"Plant gamma\"\t\"1\"\t\"3\"\t\"1\"\t\"2\"\t\"1\"\t\"76.50106685\"\t\"42.44409301\"\t\"\"\t\"3.1\"\t\"\"\t\"\"\n\"2019-09-10T18:20:15.629Z\"\t\"f753a83c\"\t\"Study 1\"\t\"40498c3c\"\t\"A0000002\"\t\"2869d94a\"\t\"Plant epsilon\"\t\"2\"\t\"4\"\t\"1\"\t\"2\"\t\"2\"\t\"76.50106687\"\t\"42.44409301\"\t\"\"\t\"3.2\"\t\"\"\t\"\""
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




### Get - /observationunits/{observationUnitDbId} [GET /brapi/v1/observationunits/{observationUnitDbId}]

Get the details of a specific Observation Unit



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + observationUnitDbId (Required, ) ... The unique ID of the specific Observation Unit
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationLevel": "plot",
        "observationUnitDbId": "8c67503c",
        "observationUnitName": "Plot 1",
        "observationUnitPosition": {
            "blockNumber": "6",
            "entryNumber": "3",
            "entryType": [
                "CHECK",
                "TEST",
                "FILLER"
            ],
            "geoCoordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW",
            "replicate": "1"
        },
        "observationUnitXref": [
            {
                "id": "SAMEA179865230",
                "source": "ebi.biosample"
            },
            {
                "id": "INRA:CoeSt6 _SMH03",
                "source": "gnpis.lot"
            }
        ],
        "plantNumber": "1",
        "plotNumber": "01",
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
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




### Put - /observationunits/{observationUnitDbId} [PUT /brapi/v1/observationunits/{observationUnitDbId}]

Update an existing Observation Units

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + observationUnitDbId (Required, ) ... The unique ID of the specific Observation Unit
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "germplasmDbId": "e9d9ed57",
    "germplasmName": "A0000001",
    "locationDbId": "0e208b20",
    "locationName": "Field Station Alpha",
    "observationLevel": "plot",
    "observationUnitName": "Plot 1",
    "observationUnitPosition": {
        "blockNumber": "6",
        "entryNumber": "3",
        "entryType": [
            "CHECK",
            "TEST",
            "FILLER"
        ],
        "geoCoordinates": {
            "geometry": {
                "coordinates": [
                    -76.506042,
                    42.417373
                ],
                "type": "Point"
            },
            "type": "Feature"
        },
        "positionCoordinateX": "74",
        "positionCoordinateXType": "GRID_COL",
        "positionCoordinateY": "03",
        "positionCoordinateYType": "GRID_ROW",
        "replicate": "1"
    },
    "observationUnitXref": [
        {
            "id": "SAMEA179865230",
            "source": "ebi.biosample"
        },
        {
            "id": "INRA:CoeSt6 _SMH03",
            "source": "gnpis.lot"
        }
    ],
    "plantNumber": "1",
    "plotNumber": "01",
    "programDbId": "2d763a7a",
    "programName": "The Perfect Breeding Program",
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
        "germplasmDbId": "e9d9ed57",
        "germplasmName": "A0000001",
        "locationDbId": "0e208b20",
        "locationName": "Field Station Alpha",
        "observationLevel": "plot",
        "observationUnitDbId": "8c67503c",
        "observationUnitName": "Plot 1",
        "observationUnitPosition": {
            "blockNumber": "6",
            "entryNumber": "3",
            "entryType": [
                "CHECK",
                "TEST",
                "FILLER"
            ],
            "geoCoordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            },
            "positionCoordinateX": "74",
            "positionCoordinateXType": "GRID_COL",
            "positionCoordinateY": "03",
            "positionCoordinateYType": "GRID_ROW",
            "replicate": "1"
        },
        "observationUnitXref": [
            {
                "id": "SAMEA179865230",
                "source": "ebi.biosample"
            },
            {
                "id": "INRA:CoeSt6 _SMH03",
                "source": "gnpis.lot"
            }
        ],
        "plantNumber": "1",
        "plotNumber": "01",
        "programDbId": "2d763a7a",
        "programName": "The Perfect Breeding Program",
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




### Post - /search/observationunits [POST /brapi/v1/search/observationunits]

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
|germplasmDbIds|array[string]|The name or synonym of external genebank accession identifiers|
|locationDbIds|array[string]|locations these traits were collected|
|observationLevel|string|The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.|
|observationUnitDbIds|array[string]|The unique id of an observation unit|
|programDbIds|array[string]|list of programs to search across|
|studyDbIds|array[string]|The database ID / PK of the studies search parameter|
|trialDbIds|array[string]|list of trials to search across|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "621b6f1b",
        "cdb7a727"
    ],
    "locationDbIds": [
        "88da535f",
        "1554486a"
    ],
    "observationLevel": "plant",
    "observationUnitDbIds": [
        "66bab7e3",
        "0e5e7f99"
    ],
    "programDbIds": [
        "ea41cd20",
        "f03f211a"
    ],
    "studyDbIds": [
        "c74f8370",
        "dd021ad9"
    ],
    "trialDbIds": [
        "4688d49c",
        "3c90127d"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
        "searchResultDbId": "551ae08c"
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




### Get - /search/observationunits/{searchResultsDbId} [GET /brapi/v1/search/observationunits/{searchResultsDbId}{?page}{?pageSize}]

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|locationDbId|string|The ID which uniquely identifies a location, associated with this study|
|locationName|string|The human readable name of a location associated with this study|
|observationLevel|string|The level of an observation unit. ex. "plot", "plant"|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|observationUnitName|string|A human readable name for an observation unit|
|observationUnitPosition|object|All positional and layout information related to this Observation Unit|
|blockNumber|string|The block number for an observation unit. Different systems may use different block designs.|
|entryNumber|string|The entry number for an observation unit. Different systems may use different entry systems.|
|entryType|string|The type of entry for this observation unit. ex. "CHECK", "TEST", "FILLER"|
|geoCoordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.|
|geometry|object||
|type|string|Feature|
|positionCoordinateX|string|The X position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateXType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|positionCoordinateY|string|The Y position coordinate for an observation unit. Different systems may use different coordinate systems.|
|positionCoordinateYType|string|The type of positional coordinate used. Must be one of the following values  LONGITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  LATITUDE - ISO 6709 standard, WGS84 geodetic datum. See 'Location Coordinate Encoding' for details  PLANTED_ROW - The physical planted row number   PLANTED_INDIVIDUAL - The physical counted number, could be independant or within a planted row  GRID_ROW - The row index number of a square grid overlay  GRID_COL - The column index number of a square grid overlay  MEASURED_ROW - The distance in meters from a defined 0-th row  MEASURED_COL - The distance in meters from a defined 0-th column|
|replicate|string|The replicate number of an observation unit. May be the same as blockNumber.|
|observationUnitXref|array[object]|A list of external references to this observation unit|
|id|string|The unique ID in the external reference 'source' system|
|source|string|The system identifier (name, URL, etc) which has an external reference to the observation unit|
|plantNumber|string|The plant number in a field. Applicable for observationLevel: "plant"|
|plotNumber|string|The plot number in a field. Applicable for observationLevel: "plot"|
|programDbId|string|The ID which uniquely identifies a program|
|programName|string|The human readable name of a program|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|studyName|string|The human readable name for a study|
|treatments|array[object]|List of treatments applied to an observation unit.|
|factor|string|The type of treatment/factor. ex. 'fertilizer', 'inoculation', 'irrigation', etc|
|modality|string|The treatment/factor description. ex. 'low fertilizer', 'yellow rust inoculation', 'high water', etc|
|trialDbId|string|The ID which uniquely identifies a trial|
|trialName|string|The human readable name of a trial|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "germplasmDbId": "e9d9ed57",
                "germplasmName": "A0000001",
                "locationDbId": "0e208b20",
                "locationName": "Field Station Alpha",
                "observationLevel": "plot",
                "observationUnitDbId": "8c67503c",
                "observationUnitName": "Plot 1",
                "observationUnitPosition": {
                    "blockNumber": "6",
                    "entryNumber": "3",
                    "entryType": [
                        "CHECK",
                        "TEST",
                        "FILLER"
                    ],
                    "geoCoordinates": {
                        "geometry": {
                            "coordinates": [
                                -76.506042,
                                42.417373
                            ],
                            "type": "Point"
                        },
                        "type": "Feature"
                    },
                    "positionCoordinateX": "74",
                    "positionCoordinateXType": "GRID_COL",
                    "positionCoordinateY": "03",
                    "positionCoordinateYType": "GRID_ROW",
                    "replicate": "1"
                },
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "ebi.biosample"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    }
                ],
                "plantNumber": "1",
                "plotNumber": "01",
                "programDbId": "2d763a7a",
                "programName": "The Perfect Breeding Program",
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

