
# Group Study

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).

Note that dates should be provided in extended ISO 8601 format (for example, "YYYY-MM-DD").




## Studies/{studydbid}/layout [Put /brapi/v1/studies/{studyDbId}/layout]

 Modify a study layout
Update the layout data for a set of observation units within a study. Each layout object is a subset of fields within an observationUnit, so it doesnt make sense to create a new layout object by itself.
Implementation Notes:
+ If any of the fields in the request object is missing, that piece of data will not be updated. + If an observationUnitDbId can not be found within the given study, an error will be returned. + `entryType` can have the values "check", "test", or "filler". + The response should match the structure of the response from `GET studies/{studyDbId}/layout`, but it should only contain the layout objects which have been updated by the PUT request. Also, pagination is not available in the response.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/layout</a>  

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
 
+ Request (application/json)
/definitions/studyLayoutRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "143",
                "Y": 1,
                "replicate": 1,
                "additionalInfo": {},
                "X": 1,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "blockNumber": 1,
                "studyDbId": "1",
                "observationUnitDbId": "11"
            },
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "144",
                "Y": 2,
                "replicate": 1,
                "additionalInfo": {},
                "X": 1,
                "germplasmName": "ZIPA_69",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "blockNumber": 1,
                "studyDbId": "1",
                "observationUnitDbId": "12"
            },
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "145",
                "Y": 3,
                "replicate": 1,
                "additionalInfo": {},
                "X": 1,
                "germplasmName": "ZIPA_70",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "blockNumber": 1,
                "studyDbId": "1",
                "observationUnitDbId": "13"
            },
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "143",
                "Y": 1,
                "replicate": 2,
                "additionalInfo": {},
                "X": 2,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "blockNumber": 2,
                "studyDbId": "1",
                "observationUnitDbId": "11"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 4
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/layout [Get /brapi/v1/studies/{studyDbId}/layout{?pageSize}{?page}]

 Retrive the layout details for a study. Returns an array of observation unit position data which describes where each unit and germplasm is located within the study layout
Retrieve the plot layout of the study with id {id}.
For each observationUnit within a study, return the `block`, `replicate`, and `entryType` values as well as the `X` and `Y` coordinates. `entryType` can be "check", "test", or "filler".
Also return some human readable meta data about the observationUnit and germplasm.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/layout</a>  

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "143",
                "Y": 1,
                "replicate": 1,
                "additionalInfo": {},
                "X": 1,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "blockNumber": 1,
                "studyDbId": "35",
                "observationUnitDbId": "11"
            },
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "144",
                "Y": 2,
                "replicate": 1,
                "additionalInfo": {},
                "X": 1,
                "germplasmName": "ZIPA_69",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "blockNumber": 1,
                "studyDbId": "35",
                "observationUnitDbId": "12"
            },
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "145",
                "Y": 3,
                "replicate": 1,
                "additionalInfo": {},
                "X": 1,
                "germplasmName": "ZIPA_70",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "blockNumber": 1,
                "studyDbId": "35",
                "observationUnitDbId": "13"
            },
            {
                "observationLevel": "plot",
                "entryType": "check/test/filler",
                "germplasmDbId": "143",
                "Y": 1,
                "replicate": 2,
                "additionalInfo": {},
                "X": 2,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "blockNumber": 2,
                "studyDbId": "35",
                "observationUnitDbId": "11"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 4
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/observationunits/zip [Post /brapi/v1/studies/{studyDbId}/observationunits/zip]

Note: If 'observationUnitDbId' or 'observationDbId' is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If 'observationUnitDbId' or 'observationDbId' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds. 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
 
+ Request (application/json)
{
    "format": "binary",
    "type": "string"
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "message": "Could not update values for Observation Units",
                "code": "Error"
            }
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "results": {
        "observationUnitDbIds": [
            "123abc",
            "456def"
        ]
    },
    "metadata": {
        "status": [
            {
                "message": "Upload Successful",
                "code": "1"
            }
        ]
    }
}
```

## Studies/{studydbid}/observations [Put /brapi/v1/studies/{studyDbId}/observations]

 Implementation Guidelines: + If an `observationDbId` is "null" or an empty string in the request, a NEW observation should be created for the given study and observationUnit + If an `observationDbId` is populated but not found in the database, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client. + If an `observationDbId` is populated and found in the database, but the existing entry is not associated with the given study or observationUnit, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client. + If an `observationDbId` is populated and found in the database and is associated with the given study and observationUnit, then it should be updated with the new data given.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observations</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
 
+ Request (application/json)
/definitions/newObservationsRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationLevel": "plot",
                "observationTimestamp": "2015-11-05T15:12:56+01:00",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "germplasmDbId": "8383",
                "value": "5",
                "observationVariableName": "Yield",
                "germplasmName": "Pahang",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "35",
                "observationUnitDbId": "11",
                "operator": "Jane Doe",
                "observationDbId": "12345"
            },
            {
                "observationLevel": "plot",
                "observationTimestamp": "2015-11-05T15:13:56+01:00",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "germplasmDbId": "8383",
                "value": "22.3",
                "observationVariableName": "Dry Weight",
                "germplasmName": "Pahang",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "35",
                "observationUnitDbId": "11",
                "operator": "Jane Doe",
                "observationDbId": "23456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/observations [Get /brapi/v1/studies/{studyDbId}/observations{?observationVariableDbIds}{?pageSize}{?page}]


Retrieve all observations where there are measurements for the given observation variables.
observationTimestamp should be ISO8601 format with timezone: YYYY-MM-DDThh:mm:ss+hhmm
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observations</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + observationVariableDbIds (Optional, array) ... Numeric `id` of that variable (combination of trait, unit and method)
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationLevel": "plot",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "observationTimeStamp": "2015-11-05T15:12:56+01:00",
                "germplasmDbId": "8383",
                "value": "5",
                "observationVariableName": "Yield",
                "germplasmName": "Pahang",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "35",
                "observationUnitDbId": "11",
                "operator": "Jane Doe",
                "observationDbId": "12345"
            },
            {
                "observationLevel": "plot",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "observationTimeStamp": "2015-11-05T15:13:56+01:00",
                "germplasmDbId": "8383",
                "value": "22.3",
                "observationVariableName": "Dry Weight",
                "germplasmName": "Pahang",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "35",
                "observationUnitDbId": "11",
                "operator": "Jane Doe",
                "observationDbId": "23456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Observationlevels [Get /brapi/v1/observationLevels{?pageSize}{?page}]

 Call to retrieve the list of supported observation levels. Observation levels indicate the granularity level at which the measurements are taken. The values are used to supply the `observationLevel` parameter in the observation unit details call.  

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            "plant",
            "plot"
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Seasons [Get /brapi/v1/seasons{?year}{?pageSize}{?page}]

 Call to retrive all seasons (or years) in the database. (Added by Jan-Erik and Lukas 5/26/2016) Scope: PHENOTYPING.
<a href="https://test-server.brapi.org/brapi/v1/seasons"> test-server.brapi.org/brapi/v1/seasons</a> 

+ Parameters
    + year (Optional, string) ... 
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "season": "Fall",
                "seasonDbId": "237",
                "year": "2015"
            },
            {
                "season": "Spring",
                "seasonDbId": "238",
                "year": "2016"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/table [Post /brapi/v1/studies/{studyDbId}/table]

 This call can be used to create new observations in bulk.
Note: If you need to update any existing observation, please use `PUT /studies/{studyDbId}/observations`. This call should only be used to create NEW observations.
Implementation Guidelines:
+ All observations submitted through this call should create NEW observation records in the database under the given observation unit. + Each "observationUnitDbId" listed should already exist in the database. If the server can not find a given "observationUnitDbId", it should report an error. (see Error Handling) + The response of this call should be the set of "observationDbIds" created from this call, along with the associated "observationUnitDbId" and "observationVariableDbId" that each observation is associated with.
Images can optionally be saved using this call by providing a zipped file of all images in the datafiles. The physical zipped file should be transferred as well in the mulit-part form data.
Scope: PHENOTYPING  

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
 
+ Request (application/json)
/definitions/newObservationsTableRequest

+ Response 200 (application/json)
```
{
    "result": {
        "observations": [
            {
                "observationDbId": "12345",
                "observationVariableDbId": "variable1DbId",
                "observationUnitDbId": "1"
            },
            {
                "observationDbId": "23456",
                "observationVariableDbId": "variable2DbId",
                "observationUnitDbId": "1"
            },
            {
                "observationDbId": "34567",
                "observationVariableDbId": "variable3DbId",
                "observationUnitDbId": "1"
            },
            {
                "observationDbId": "45678",
                "observationVariableDbId": "imagevariable1DbId",
                "observationUnitDbId": "1"
            },
            {
                "observationDbId": "56789",
                "observationVariableDbId": "variable1DbId",
                "observationUnitDbId": "2"
            },
            {
                "observationDbId": "67890",
                "observationVariableDbId": "variable2DbId",
                "observationUnitDbId": "2"
            },
            {
                "observationDbId": "78901",
                "observationVariableDbId": "variable3DbId",
                "observationUnitDbId": "2"
            },
            {
                "observationDbId": "89012",
                "observationVariableDbId": "imagevariable1DbId",
                "observationUnitDbId": "2"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/table [Get /brapi/v1/studies/{studyDbId}/table{?format}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implemented in Cassavabase, HIDAP and Germinate. Notes: Implementation target date: after PAG2016 Retrieve the details of the study required for field data collection. Includes actual trait data.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/table</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + format (Optional, string) ... The format parameter will cause the data to be dumped to a file in the specified format. Currently, tsv and csv are supported.


+ Response 200 (application/csv)
```
"year,studyDbId,studyName,locationDbId,locationName,germplasmDbId,germplasmName,observationUnitDbId,plotNumber,replicate,blockNumber,observationTimestamp,entryType,X,Y,variable1DbId,variable2DbId,variable3DbId\n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc123,1,1,1,2017-06-16T00:53:26Z,Test Entry,1,2,25.3,103.4,50.75 \n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc124,1,1,1,2017-06-16T00:54:57Z,Test Entry,2,2,27.9,98.65,45.345\n"
```+ Response 200 (application/json)
```
{
    "result": {
        "observationVariableDbIds": [
            "variable1DbId",
            "variable2DbId",
            "variable3DbId"
        ],
        "observationVariableNames": [
            "plant height",
            "fruit weight",
            "root weight"
        ],
        "data": [
            [
                "2017",
                "stu1",
                "Study Name",
                "loc1",
                "Location Name",
                "CIP1",
                "CIP Name",
                "abc123",
                1,
                1,
                1,
                "2017-06-16T00:53:26Z",
                "Test Entry",
                "1",
                "2",
                "25.3",
                "103.4",
                "50.75"
            ],
            [
                "2017",
                "stu1",
                "Study Name",
                "loc1",
                "Location Name",
                "CIP1",
                "CIP Name",
                "abc124",
                1,
                1,
                1,
                "2017-06-16T00:54:57Z",
                "Test Entry",
                "2",
                "2",
                "27.9",
                "98.65",
                "45.345"
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
            "observationTimestamp",
            "entryType",
            "X",
            "Y"
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```+ Response 200 (application/tsv)
```
"year\tstudyDbId\tstudyName\tlocationDbId\tlocationName\tgermplasmDbId\tgermplasmName\tobservationUnitDbId\tplotNumber\treplicate\tblockNumber\tobservationTimestamp\tentryType\tX\tY\tvariable1DbId\tvariable2DbId\tvariable3DbId\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc123\t1\t1\t1\t2017-06-16T00:53:26Z\tTest Entry\t1\t2\t25.3\t103.4\t50.75\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc124\t1\t1\t1\t2017-06-16T00:54:57Z\tTest Entry\t2\t2\t27.9\t98.65\t45.345\n"
```

## Studies/{studydbid}/observationunits [Put /brapi/v1/studies/{studyDbId}/observationunits]

Use this call for uploading new Observations as JSON to a system.

Note: If 'observationUnitDbId' or 'observationDbId' is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If 'observationUnitDbId' or 'observationDbId' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds. 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
 
+ Request (application/json)
{
    "items": {
        "$ref": "#/definitions/newObservationUnitRequest"
    },
    "title": "newObservationUnitRequestList",
    "type": "array"
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "message": "Could not update values for Observation Units",
                "code": "Error"
            }
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "results": {
        "observationUnitDbIds": [
            "123abc",
            "456def"
        ]
    },
    "metadata": {
        "status": [
            {
                "message": "Upload Successful",
                "code": "1"
            }
        ]
    }
}
```

## Studies/{studydbid}/observationunits [Post /brapi/v1/studies/{studyDbId}/observationunits{?format}]

This call has been deprecated in V1.1. Use instead: "PUT /studies/{studyDbId}/observationunits" and "PUT /studies/{studyDbId}/observationunits/zip" 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
    + format (Required, string) ... (default is JSON, but can be zip) In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
 
+ Request (application/json)
{
    "properties": {
        "result": {
            "$ref": "#/definitions/newObservationsRequestDeprecated"
        },
        "metadata": {
            "$ref": "#/definitions/metadata"
        }
    },
    "title": "newObservationsRequestWrapperDeprecated"
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "message": "Could not update values for Observation Units",
                "code": "42"
            }
        ]
    }
}
```

## Studies/{studydbid}/observationunits [Get /brapi/v1/studies/{studyDbId}/observationunits{?observationLevel}{?pageSize}{?page}]

 The main API call for field data collection, to retrieve all the observation units within a study.
Scope: PHENOTYPING
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationunits</a> 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
    + observationLevel (Optional, string) ... The granularity level of observation units. Either `plotNumber` or `plantNumber` fields will be relavant depending on whether granularity is plot or plant respectively.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "entryNumber": "1",
                "Y": "1",
                "plantNumber": "0",
                "replicate": "1",
                "plotNumber": "1",
                "observationUnitXref": [
                    {
                        "source": "biosampleEBI",
                        "id": "SAMEA179865230"
                    },
                    {
                        "source": "gnpis.lot",
                        "id": "INRA:CoeSt6 _SMH03"
                    },
                    {
                        "source": "kernelDB",
                        "id": "239865"
                    }
                ],
                "X": "1",
                "observationUnitName": "Test-2016-location-34-575",
                "observationLevel": "plot",
                "pedigree": "IR-8-FP/IR-8-MP",
                "entryType": "Test entry",
                "germplasmName": "IR-8",
                "observationUnitDbId": "abc-123",
                "observations": [
                    {
                        "observationVariableDbId": "18020",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "value": "25.63",
                        "collector": "Mr. Technician",
                        "observationVariableName": "Plant_height",
                        "observationDbId": "153453453"
                    },
                    {
                        "observationVariableDbId": "51496",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "value": "Light Green",
                        "collector": "Mr. Technician",
                        "observationVariableName": "GW100_g",
                        "observationDbId": "23453454345"
                    }
                ],
                "germplasmDbId": "1",
                "blockNumber": "1"
            },
            {
                "observationLevel": "plot",
                "pedigree": "IR-9-FP/IR-9-MP",
                "entryType": "Check entry",
                "enrtyNumber": "2",
                "germplasmDbId": "2",
                "Y": "2",
                "replicate": "1",
                "plantNumber": "0",
                "plotNumber": "2",
                "observations": [
                    {
                        "observationVariableDbId": "18020",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "value": "34.95",
                        "collector": "Mr. Technician",
                        "observationVariableName": "Plant_height",
                        "observationDbId": "3"
                    },
                    {
                        "observationVariableDbId": "51496",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "value": "Blue",
                        "collector": "Mr. Technician",
                        "observationVariableName": "GW100_g",
                        "observationDbId": "4"
                    }
                ],
                "X": "1",
                "germplasmName": "IR-9",
                "observationUnitName": "Test-2016-location-34-456",
                "blockNumber": "2",
                "observatioUnitDbId": "abc-456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid} [Get /brapi/v1/studies/{studyDbId}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implemented by: Germinate, GnpIS
Notes: an additionalInfo field was added to provide a controlled vocabulary for less common data fields.
Retrieve the information of the study required for field data collection
More linked data: * observation variables: ```/brapi/v1/studies/{studyDbId}/observationVariables``` * germplasm: ```/brapi/v1/studies/{studyDbId}/germplasm``` * observation units: ```/brapi/v1/studies/{studyDbId}/observationUnits``` * layout: ```brapi/v1/studies/{studyDbId}/layout```
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.


+ Response 200 (application/json)
```
{
    "result": {
        "dataLinks": [
            {
                "url": "http://data.inra.fr/archive/multi-spect-flowering.zip",
                "type": "Image archive",
                "name": "image-archive12.zip"
            }
        ],
        "studyType": "Yield study",
        "endDate": "2008-12-31",
        "studyDescription": "some free text description that could include scientific goal, some tracability and whatever makes sense",
        "additionalInfo": {
            "principalInvestigator": "Dr. Breeder",
            "publications": "pmid:24039865287545",
            "property1Name": "property1Value",
            "studyObjective": "Increase yield",
            "property2Name": "property2Value"
        },
        "startDate": "2005-06-01",
        "studyName": "Earlygenerationtesting",
        "trialDbId": "57",
        "studyDbId": "35",
        "contacts": [
            {
                "instituteName": "IRRI",
                "type": "Scientist",
                "name": "John Doe",
                "contactDbId": "C025",
                "email": "j.doe@mail.com",
                "orcid": "0000-0002-0607-8728"
            },
            {
                "instituteName": "IRRI",
                "type": null,
                "name": "Dave Peters",
                "contactDbId": "C026",
                "email": null,
                "orcid": null
            }
        ],
        "trialName": "International Yield Trial",
        "license": "https://creativecommons.org/licenses/by/4.0",
        "lastUpdate": {
            "version": "1.1",
            "timestamp": "2015-06-16T00:53:26Z"
        },
        "seasons": [
            "2005 Winter",
            "2008 Summer"
        ],
        "location": {
            "abbreviation": "IB",
            "name": "Ibadan",
            "instituteName": "INRA - GDEC",
            "altitude": 12,
            "countryName": "Nigeria",
            "countryCode": "NGA",
            "additionalInfo": {
                "AnnualMeanRain": "value",
                "property1Name": "property1Value",
                "SoilDescription": "23",
                "property2Name": "property2Value"
            },
            "latitude": -21.5,
            "longitude": 165.5,
            "instituteAddress": "route foo, Clermont Ferrand, France",
            "locationDbId": "1"
        },
        "active": "true"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/germplasm [Get /brapi/v1/studies/{studyDbId}/germplasm{?pageSize}{?page}]

 Scope: PHENOTYPING
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/germplasm</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "studyDbId": "35",
        "data": [
            {
                "accessionNumber": "ITC0609",
                "entryNumber": "1",
                "pedigree": "TOBA97/SW90.1057",
                "germplasmName": "Pahang",
                "synonyms": [
                    "01BEL084609"
                ],
                "seedSource": "SS1",
                "germplasmDbId": "382",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609"
            },
            {
                "accessionNumber": "ITC0727",
                "entryNumber": "2",
                "pedigree": "TOBA97/SW90.1057",
                "germplasmName": "Pahang",
                "synonyms": [
                    "01BEL084727"
                ],
                "seedSource": "SS2",
                "germplasmDbId": "394",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084727"
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studytypes [Get /brapi/v1/studyTypes{?pageSize}{?page}]

 Call to retrieve the list of study types.
Scope: PHENOTYPING. Implementation target date: PAG2016  

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "description": "Description for Nursery study type",
                "name": "Crossing Nursery"
            },
            {
                "description": "Description for Trial study type",
                "name": "Yield Trial"
            },
            {
                "description": "Description for Genotyping study type",
                "name": "Genotype"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 3
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies-search [Post /brapi/v1/studies-search]

 Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016.
Implemented by: Germinate
Used by: Flapjack, Cassavabase
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Get list of studies
StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies-search</a> 

+ Parameters
 
+ Request (application/json)
/definitions/studySearchRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "locationName": "Kenya",
                "studyType": "Trial",
                "name": "Earlygenerationtesting",
                "endDate": "2008-12-31",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "startDate": "2007-06-01",
                "trialDbId": "7",
                "programDbId": "27",
                "studyDbId": "35",
                "active": "true",
                "locationDbId": "23",
                "programName": "Drought Resistance Program A",
                "trialName": "InternationalTrialA"
            },
            {
                "locationName": "Zimbabwe",
                "studyType": "Trial",
                "name": "Earlygenerationtesting",
                "endDate": "2008-12-31",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "startDate": "2005-06-01",
                "trialDbId": "7",
                "programDbId": "58",
                "studyDbId": "345",
                "active": "true",
                "locationDbId": "33",
                "programName": "Drought Resistance Program B",
                "trialName": "InternationalTrialA"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies-search [Get /brapi/v1/studies-search{?studyType}{?programDbId}{?locationDbId}{?seasonDbId}{?trialDbId}{?studyDbId}{?germplasmDbIds}{?observationVariableDbIds}{?pageSize}{?page}{?active}{?sortBy}{?sortOrder}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016.
Implemented by: Germinate
Used by: Flapjack, Cassavabase
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Get list of studies
StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies-search</a> 

+ Parameters
    + studyType (Optional, string) ... Filter based on study type e.g. Nursery, Trial or Genotype.
    + programDbId (Optional, string) ... Program filter to only return studies associated with given program id.
    + locationDbId (Optional, string) ... Filter by location
    + seasonDbId (Optional, string) ... Filter by season or year
    + trialDbId (Optional, string) ... Filter by trial
    + studyDbId (Optional, string) ... Filter by study DbId
    + germplasmDbIds (Optional, array) ... Filter studies where specified germplasm have been used/tested
    + observationVariableDbIds (Optional, array) ... Filter studies where specified observation variables have been measured
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + active (Optional, boolean) ... Filter active status true/false.
    + sortBy (Optional, string) ... Sort order. Name of the field to sort by.
    + sortOrder (Optional, string) ... Sort order direction. Ascending/Descending.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "locationName": "Kenya",
                "studyType": "Trial",
                "name": "Earlygenerationtesting",
                "endDate": "2008-12-31",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "startDate": "2007-06-01",
                "trialDbId": "7",
                "programDbId": "27",
                "studyDbId": "35",
                "active": "true",
                "locationDbId": "23",
                "programName": "Drought Resistance Program A",
                "trialName": "InternationalTrialA"
            },
            {
                "locationName": "Zimbabwe",
                "studyType": "Trial",
                "name": "Earlygenerationtesting",
                "endDate": "2008-12-31",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "startDate": "2005-06-01",
                "trialDbId": "7",
                "programDbId": "58",
                "studyDbId": "345",
                "active": "true",
                "locationDbId": "33",
                "programName": "Drought Resistance Program B",
                "trialName": "InternationalTrialA"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/observationvariables [Get /brapi/v1/studies/{studyDbId}/observationvariables{?pageSize}{?page}]

 Scope: PHENOTYPING
List all the observation variables measured in the study.
Refer to the data type definition of variables in `/Specification/ObservationVariables/README.md`.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationvariables</a> 

+ Parameters
    + studyDbId (Required, string) ... string database unique identifier
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "studyDbId": "35",
        "data": [
            {
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": {
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "name": "ug/g",
                    "xref": null,
                    "scaleDbId": "CO_334:0100526"
                },
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "method": {
                    "class": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "defaultValue": "0",
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                }
            },
            {
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "defaultValue": "0",
                "institution": "",
                "language": "EN",
                "trait": {
                    "class": "physiological trait",
                    "entity": "root",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "date": "2016-05-13",
                "scientist": "",
                "ontologyDbId": "CO_334",
                "scale": {
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "name": "ug/g",
                    "xref": null,
                    "scaleDbId": "CO_334:0100526"
                },
                "name": "caro_spectro",
                "method": {
                    "class": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "status": "recommended",
                "xref": "TL_455:0003001",
                "crop": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature"
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```

## Studies/{studydbid}/observationvariables [Get /brapi/v1/studies/{studyDbId}/observationVariables]



<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationVariables</a> 

+ Parameters
    + studyDbId (Required, string) ... string database unique identifier


+ Response 200 (application/json)
```
{
    "result": {
        "studyDbId": "123",
        "data": [
            {
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": null,
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "method": null,
                "defaultValue": null,
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                }
            },
            {
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "defaultValue": null,
                "institution": "",
                "language": "EN",
                "trait": {
                    "class": "physiological trait",
                    "entity": "root",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "date": "2016-05-13",
                "scientist": "",
                "ontologyDbId": "CO_334",
                "scale": {
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "name": "ug/g",
                    "xref": null,
                    "scaleDbId": "CO_334:0100526"
                },
                "name": "caro_spectro",
                "method": {
                    "class": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "status": "recommended",
                "xref": "TL_455:0003001",
                "crop": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature"
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```