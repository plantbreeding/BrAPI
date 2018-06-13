
# Group Study

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).

Note that dates should be provided in extended ISO 8601 format (for example, "YYYY-MM-DD").




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
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 1,
                "studyDbId": "35",
                "replicate": 1,
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "X": 1,
                "germplasmName": "ZIPA_68",
                "Y": 1,
                "observationLevel": "plot"
            },
            {
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 1,
                "studyDbId": "35",
                "replicate": 1,
                "germplasmDbId": "144",
                "observationUnitDbId": "12",
                "X": 1,
                "germplasmName": "ZIPA_69",
                "Y": 2,
                "observationLevel": "plot"
            },
            {
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 1,
                "studyDbId": "35",
                "replicate": 1,
                "germplasmDbId": "145",
                "observationUnitDbId": "13",
                "X": 1,
                "germplasmName": "ZIPA_70",
                "Y": 3,
                "observationLevel": "plot"
            },
            {
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 2,
                "studyDbId": "35",
                "replicate": 2,
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "X": 2,
                "germplasmName": "ZIPA_68",
                "Y": 1,
                "observationLevel": "plot"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

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
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 1,
                "studyDbId": "1",
                "replicate": 1,
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "X": 1,
                "germplasmName": "ZIPA_68",
                "Y": 1,
                "observationLevel": "plot"
            },
            {
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 1,
                "studyDbId": "1",
                "replicate": 1,
                "germplasmDbId": "144",
                "observationUnitDbId": "12",
                "X": 1,
                "germplasmName": "ZIPA_69",
                "Y": 2,
                "observationLevel": "plot"
            },
            {
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 1,
                "studyDbId": "1",
                "replicate": 1,
                "germplasmDbId": "145",
                "observationUnitDbId": "13",
                "X": 1,
                "germplasmName": "ZIPA_70",
                "Y": 3,
                "observationLevel": "plot"
            },
            {
                "entryType": "check/test/filler",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "additionalInfo": {},
                "blockNumber": 2,
                "studyDbId": "1",
                "replicate": 2,
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "X": 2,
                "germplasmName": "ZIPA_68",
                "Y": 1,
                "observationLevel": "plot"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "code": "Error",
                "message": "Could not update values for Observation Units"
            }
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "code": "1",
                "message": "Upload Successful"
            }
        ]
    },
    "results": {
        "observationUnitDbIds": [
            "123abc",
            "456def"
        ]
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
                "uploadedBy": "dbUserId",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationDbId": "12345",
                "studyDbId": "35",
                "operator": "Jane Doe",
                "observationVariableDbId": "CO_334:0100632",
                "observationTimeStamp": "2015-11-05T15:12:56+01:00",
                "value": "5",
                "germplasmDbId": "8383",
                "observationVariableName": "Yield",
                "observationUnitDbId": "11",
                "germplasmName": "Pahang",
                "observationLevel": "plot"
            },
            {
                "uploadedBy": "dbUserId",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationDbId": "23456",
                "studyDbId": "35",
                "operator": "Jane Doe",
                "observationVariableDbId": "CO_334:0100632",
                "observationTimeStamp": "2015-11-05T15:13:56+01:00",
                "value": "22.3",
                "germplasmDbId": "8383",
                "observationVariableName": "Dry Weight",
                "observationUnitDbId": "11",
                "germplasmName": "Pahang",
                "observationLevel": "plot"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "uploadedBy": "dbUserId",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationDbId": "12345",
                "operator": "Jane Doe",
                "studyDbId": "35",
                "observationVariableDbId": "CO_334:0100632",
                "observationTimestamp": "2015-11-05T15:12:56+01:00",
                "value": "5",
                "germplasmDbId": "8383",
                "observationVariableName": "Yield",
                "observationUnitDbId": "11",
                "germplasmName": "Pahang",
                "observationLevel": "plot"
            },
            {
                "uploadedBy": "dbUserId",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationDbId": "23456",
                "operator": "Jane Doe",
                "studyDbId": "35",
                "observationVariableDbId": "CO_334:0100632",
                "observationTimestamp": "2015-11-05T15:13:56+01:00",
                "value": "22.3",
                "germplasmDbId": "8383",
                "observationVariableName": "Dry Weight",
                "observationUnitDbId": "11",
                "germplasmName": "Pahang",
                "observationLevel": "plot"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "seasonDbId": "237",
                "season": "Fall",
                "year": "2015"
            },
            {
                "seasonDbId": "238",
                "season": "Spring",
                "year": "2016"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "observationUnitDbId": "1",
                "observationDbId": "12345",
                "observationVariableDbId": "variable1DbId"
            },
            {
                "observationUnitDbId": "1",
                "observationDbId": "23456",
                "observationVariableDbId": "variable2DbId"
            },
            {
                "observationUnitDbId": "1",
                "observationDbId": "34567",
                "observationVariableDbId": "variable3DbId"
            },
            {
                "observationUnitDbId": "1",
                "observationDbId": "45678",
                "observationVariableDbId": "imagevariable1DbId"
            },
            {
                "observationUnitDbId": "2",
                "observationDbId": "56789",
                "observationVariableDbId": "variable1DbId"
            },
            {
                "observationUnitDbId": "2",
                "observationDbId": "67890",
                "observationVariableDbId": "variable2DbId"
            },
            {
                "observationUnitDbId": "2",
                "observationDbId": "78901",
                "observationVariableDbId": "variable3DbId"
            },
            {
                "observationUnitDbId": "2",
                "observationDbId": "89012",
                "observationVariableDbId": "imagevariable1DbId"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
        ],
        "observationVariableNames": [
            "plant height",
            "fruit weight",
            "root weight"
        ],
        "observationVariableDbIds": [
            "variable1DbId",
            "variable2DbId",
            "variable3DbId"
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
    }
}
```+ Response 200 (application/tsv)
```
"year\tstudyDbId\tstudyName\tlocationDbId\tlocationName\tgermplasmDbId\tgermplasmName\tobservationUnitDbId\tplotNumber\treplicate\tblockNumber\tobservationTimestamp\tentryType\tX\tY\tvariable1DbId\tvariable2DbId\tvariable3DbId\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc123\t1\t1\t1\t2017-06-16T00:53:26Z\tTest Entry\t1\t2\t25.3\t103.4\t50.75\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc124\t1\t1\t1\t2017-06-16T00:54:57Z\tTest Entry\t2\t2\t27.9\t98.65\t45.345\n"
```

## Studies/{studydbid}/observationunits [Post /brapi/v1/studies/{studyDbId}/observationunits{?format}]

This call has been deprecated in V1.1. Use instead: "PUT /studies/{studyDbId}/observationunits" and "PUT /studies/{studyDbId}/observationunits/zip" 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
    + format (Required, string) ... (default is JSON, but can be zip) In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
 
+ Request (application/json)
{
    "title": "newObservationsRequestWrapperDeprecated",
    "properties": {
        "result": {
            "$ref": "#/definitions/newObservationsRequestDeprecated"
        },
        "metadata": {
            "$ref": "#/definitions/metadata"
        }
    }
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "code": "42",
                "message": "Could not update values for Observation Units"
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
                "entryType": "Test entry",
                "observationUnitName": "Test-2016-location-34-575",
                "plantNumber": "0",
                "replicate": "1",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "biosampleEBI"
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
                "X": "1",
                "pedigree": "IR-8-FP/IR-8-MP",
                "plotNumber": "1",
                "entryNumber": "1",
                "blockNumber": "1",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableDbId": "18020",
                        "observationVariableName": "Plant_height",
                        "value": "25.63"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableDbId": "51496",
                        "observationVariableName": "GW100_g",
                        "value": "Light Green"
                    }
                ],
                "germplasmDbId": "1",
                "observationUnitDbId": "abc-123",
                "germplasmName": "IR-8",
                "Y": "1",
                "observationLevel": "plot"
            },
            {
                "pedigree": "IR-9-FP/IR-9-MP",
                "entryType": "Check entry",
                "observationUnitName": "Test-2016-location-34-456",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "3",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableDbId": "18020",
                        "observationVariableName": "Plant_height",
                        "value": "34.95"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "4",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableDbId": "51496",
                        "observationVariableName": "GW100_g",
                        "value": "Blue"
                    }
                ],
                "blockNumber": "2",
                "plotNumber": "2",
                "replicate": "1",
                "germplasmName": "IR-9",
                "plantNumber": "0",
                "germplasmDbId": "2",
                "enrtyNumber": "2",
                "X": "1",
                "observatioUnitDbId": "abc-456",
                "Y": "2",
                "observationLevel": "plot"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

## Studies/{studydbid}/observationunits [Put /brapi/v1/studies/{studyDbId}/observationunits]

Use this call for uploading new Observations as JSON to a system.

Note: If 'observationUnitDbId' or 'observationDbId' is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If 'observationUnitDbId' or 'observationDbId' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds. 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
 
+ Request (application/json)
{
    "title": "newObservationUnitRequestList",
    "items": {
        "$ref": "#/definitions/newObservationUnitRequest"
    },
    "type": "array"
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "code": "Error",
                "message": "Could not update values for Observation Units"
            }
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "code": "1",
                "message": "Upload Successful"
            }
        ]
    },
    "results": {
        "observationUnitDbIds": [
            "123abc",
            "456def"
        ]
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
        "contacts": [
            {
                "name": "John Doe",
                "instituteName": "IRRI",
                "contactDbId": "C025",
                "type": "Scientist",
                "email": "j.doe@mail.com",
                "orcid": "0000-0002-0607-8728"
            },
            {
                "name": "Dave Peters",
                "instituteName": "IRRI",
                "contactDbId": "C026",
                "type": null,
                "email": null,
                "orcid": null
            }
        ],
        "license": "https://creativecommons.org/licenses/by/4.0",
        "trialDbId": "57",
        "trialName": "International Yield Trial",
        "lastUpdate": {
            "timestamp": "2015-06-16T00:53:26Z",
            "version": "1.1"
        },
        "location": {
            "latitude": -21.5,
            "instituteAddress": "route foo, Clermont Ferrand, France",
            "additionalInfo": {
                "property1Name": "property1Value",
                "property2Name": "property2Value",
                "AnnualMeanRain": "value",
                "SoilDescription": "23"
            },
            "abbreviation": "IB",
            "countryCode": "NGA",
            "locationDbId": "1",
            "altitude": 12,
            "name": "Ibadan",
            "countryName": "Nigeria",
            "longitude": 165.5,
            "instituteName": "INRA - GDEC"
        },
        "studyName": "Earlygenerationtesting",
        "startDate": "2005-06-01",
        "active": "true",
        "studyDescription": "some free text description that could include scientific goal, some tracability and whatever makes sense",
        "additionalInfo": {
            "publications": "pmid:24039865287545",
            "property1Name": "property1Value",
            "principalInvestigator": "Dr. Breeder",
            "property2Name": "property2Value",
            "studyObjective": "Increase yield"
        },
        "studyDbId": "35",
        "dataLinks": [
            {
                "name": "image-archive12.zip",
                "url": "http://data.inra.fr/archive/multi-spect-flowering.zip",
                "type": "Image archive"
            }
        ],
        "seasons": [
            "2005 Winter",
            "2008 Summer"
        ],
        "studyType": "Yield study",
        "endDate": "2008-12-31"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
        "data": [
            {
                "pedigree": "TOBA97/SW90.1057",
                "entryNumber": "1",
                "synonyms": [
                    "01BEL084609"
                ],
                "seedSource": "SS1",
                "germplasmDbId": "382",
                "germplasmName": "Pahang",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "accessionNumber": "ITC0609"
            },
            {
                "pedigree": "TOBA97/SW90.1057",
                "entryNumber": "2",
                "synonyms": [
                    "01BEL084727"
                ],
                "seedSource": "SS2",
                "germplasmDbId": "394",
                "germplasmName": "Pahang",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084727",
                "accessionNumber": "ITC0727"
            }
        ],
        "studyDbId": "35",
        "trialName": "myBestTrial"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "name": "Crossing Nursery",
                "description": "Description for Nursery study type"
            },
            {
                "name": "Yield Trial",
                "description": "Description for Trial study type"
            },
            {
                "name": "Genotype",
                "description": "Description for Genotyping study type"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 3,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "startDate": "2007-06-01",
                "active": "true",
                "locationName": "Kenya",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "35",
                "programDbId": "27",
                "locationDbId": "23",
                "trialDbId": "7",
                "programName": "Drought Resistance Program A",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "name": "Earlygenerationtesting",
                "trialName": "InternationalTrialA",
                "studyType": "Trial",
                "endDate": "2008-12-31"
            },
            {
                "startDate": "2005-06-01",
                "active": "true",
                "locationName": "Zimbabwe",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "345",
                "programDbId": "58",
                "locationDbId": "33",
                "trialDbId": "7",
                "programName": "Drought Resistance Program B",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "name": "Earlygenerationtesting",
                "trialName": "InternationalTrialA",
                "studyType": "Trial",
                "endDate": "2008-12-31"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
                "startDate": "2007-06-01",
                "active": "true",
                "locationName": "Kenya",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "35",
                "programDbId": "27",
                "locationDbId": "23",
                "trialDbId": "7",
                "programName": "Drought Resistance Program A",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "name": "Earlygenerationtesting",
                "trialName": "InternationalTrialA",
                "studyType": "Trial",
                "endDate": "2008-12-31"
            },
            {
                "startDate": "2005-06-01",
                "active": "true",
                "locationName": "Zimbabwe",
                "additionalInfo": {
                    "property1Name": "property1Value",
                    "property2Name": "property2Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "345",
                "programDbId": "58",
                "locationDbId": "33",
                "trialDbId": "7",
                "programName": "Drought Resistance Program B",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "name": "Earlygenerationtesting",
                "trialName": "InternationalTrialA",
                "studyType": "Trial",
                "endDate": "2008-12-31"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
        "data": [
            {
                "defaultValue": "0",
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "xref": null,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    }
                },
                "ontologyName": "Cassava",
                "name": "CT_M_C",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "reference": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                }
            },
            {
                "defaultValue": "0",
                "growthStage": "mature",
                "date": "2016-05-13",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "ontologyDbId": "CO_334",
                "xref": "TL_455:0003001",
                "ontologyName": "Cassava",
                "scientist": "",
                "institution": "",
                "language": "EN",
                "status": "recommended",
                "crop": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "xref": null,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    }
                },
                "name": "caro_spectro",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "reference": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "trait": {
                    "class": "physiological trait",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "attribute": "carotenoid",
                    "xref": "TL_455:0003023",
                    "mainAbbreviation": "CC",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "entity": "root",
                    "status": "recommended",
                    "alternativeAbbreviations": [
                        "CCS"
                    ]
                }
            }
        ],
        "studyDbId": "35",
        "trialName": "myBestTrial"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
        "data": [
            {
                "defaultValue": null,
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": null,
                "ontologyName": "Cassava",
                "name": "CT_M_C",
                "method": null,
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                }
            },
            {
                "defaultValue": null,
                "growthStage": "mature",
                "date": "2016-05-13",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "ontologyDbId": "CO_334",
                "xref": "TL_455:0003001",
                "ontologyName": "Cassava",
                "scientist": "",
                "institution": "",
                "language": "EN",
                "status": "recommended",
                "crop": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "xref": null,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    }
                },
                "name": "caro_spectro",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "reference": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "trait": {
                    "class": "physiological trait",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "attribute": "carotenoid",
                    "xref": "TL_455:0003023",
                    "mainAbbreviation": "CC",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "entity": "root",
                    "status": "recommended",
                    "alternativeAbbreviations": [
                        "CCS"
                    ]
                }
            }
        ],
        "studyDbId": "123",
        "trialName": "myBestTrial"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
    }
}
```