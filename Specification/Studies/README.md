
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
                "observationUnitDbId": "11",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "35",
                "Y": 1,
                "germplasmDbId": "143",
                "X": 1,
                "additionalInfo": {}
            },
            {
                "entryType": "check/test/filler",
                "observationUnitDbId": "12",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmName": "ZIPA_69",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "studyDbId": "35",
                "Y": 2,
                "germplasmDbId": "144",
                "X": 1,
                "additionalInfo": {}
            },
            {
                "entryType": "check/test/filler",
                "observationUnitDbId": "13",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmName": "ZIPA_70",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "studyDbId": "35",
                "Y": 3,
                "germplasmDbId": "145",
                "X": 1,
                "additionalInfo": {}
            },
            {
                "entryType": "check/test/filler",
                "observationUnitDbId": "11",
                "blockNumber": 2,
                "observationLevel": "plot",
                "replicate": 2,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "35",
                "Y": 1,
                "germplasmDbId": "143",
                "X": 2,
                "additionalInfo": {}
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
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
                "observationUnitDbId": "11",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "1",
                "Y": 1,
                "germplasmDbId": "143",
                "X": 1,
                "additionalInfo": {}
            },
            {
                "entryType": "check/test/filler",
                "observationUnitDbId": "12",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmName": "ZIPA_69",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "studyDbId": "1",
                "Y": 2,
                "germplasmDbId": "144",
                "X": 1,
                "additionalInfo": {}
            },
            {
                "entryType": "check/test/filler",
                "observationUnitDbId": "13",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmName": "ZIPA_70",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "studyDbId": "1",
                "Y": 3,
                "germplasmDbId": "145",
                "X": 1,
                "additionalInfo": {}
            },
            {
                "entryType": "check/test/filler",
                "observationUnitDbId": "11",
                "blockNumber": 2,
                "observationLevel": "plot",
                "replicate": 2,
                "germplasmName": "ZIPA_68",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "studyDbId": "1",
                "Y": 1,
                "germplasmDbId": "143",
                "X": 2,
                "additionalInfo": {}
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        },
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

+ Response 200 (application/json)
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
```+ Response 400 (application/json)
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
                "observationDbId": "12345",
                "observationVariableName": "Yield",
                "observationUnitDbId": "11",
                "observationLevel": "plot",
                "studyDbId": "35",
                "uploadedBy": "dbUserId",
                "operator": "Jane Doe",
                "germplasmDbId": "8383",
                "value": "5",
                "observationTimeStamp": "2015-11-05T15:12:56+01:00",
                "germplasmName": "Pahang",
                "observationVariableDbId": "CO_334:0100632",
                "observationUnitName": "ZIPA_68_Ibadan_2014"
            },
            {
                "observationDbId": "23456",
                "observationVariableName": "Dry Weight",
                "observationUnitDbId": "11",
                "observationLevel": "plot",
                "studyDbId": "35",
                "uploadedBy": "dbUserId",
                "operator": "Jane Doe",
                "germplasmDbId": "8383",
                "value": "22.3",
                "observationTimeStamp": "2015-11-05T15:13:56+01:00",
                "germplasmName": "Pahang",
                "observationVariableDbId": "CO_334:0100632",
                "observationUnitName": "ZIPA_68_Ibadan_2014"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
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
                "observationDbId": "12345",
                "observationVariableName": "Yield",
                "observationUnitDbId": "11",
                "observationLevel": "plot",
                "studyDbId": "35",
                "uploadedBy": "dbUserId",
                "operator": "Jane Doe",
                "germplasmDbId": "8383",
                "value": "5",
                "germplasmName": "Pahang",
                "observationVariableDbId": "CO_334:0100632",
                "observationTimestamp": "2015-11-05T15:12:56+01:00",
                "observationUnitName": "ZIPA_68_Ibadan_2014"
            },
            {
                "observationDbId": "23456",
                "observationVariableName": "Dry Weight",
                "observationUnitDbId": "11",
                "observationLevel": "plot",
                "studyDbId": "35",
                "uploadedBy": "dbUserId",
                "operator": "Jane Doe",
                "germplasmDbId": "8383",
                "value": "22.3",
                "germplasmName": "Pahang",
                "observationVariableDbId": "CO_334:0100632",
                "observationTimestamp": "2015-11-05T15:13:56+01:00",
                "observationUnitName": "ZIPA_68_Ibadan_2014"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
    }
}
```

## Observationlevels [Get /brapi/v1/observationlevels{?pageSize}{?page}]

 Call to retrieve the list of supported observation levels. Observation levels indicate the granularity level at which the measurements are taken. The values are used to supply the `observationLevel` parameter in the observation unit details call.
<a href="https://test-server.brapi.org/brapi/v1/observationlevels"> test-server.brapi.org/brapi/v1/observationlevels</a> 

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
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
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
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
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


+ Response 200 (application/json)
```
{
    "result": {
        "observationVariableDbIds": [
            "variable1DbId",
            "variable2DbId",
            "variable3DbId"
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
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": []
    }
}
```+ Response 200 (application/csv)
```
"year,studyDbId,studyName,locationDbId,locationName,germplasmDbId,germplasmName,observationUnitDbId,plotNumber,replicate,blockNumber,observationTimestamp,entryType,X,Y,variable1DbId,variable2DbId,variable3DbId\n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc123,1,1,1,2017-06-16T00:53:26Z,Test Entry,1,2,25.3,103.4,50.75 \n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc124,1,1,1,2017-06-16T00:54:57Z,Test Entry,2,2,27.9,98.65,45.345\n"
```+ Response 200 (application/tsv)
```
"year\tstudyDbId\tstudyName\tlocationDbId\tlocationName\tgermplasmDbId\tgermplasmName\tobservationUnitDbId\tplotNumber\treplicate\tblockNumber\tobservationTimestamp\tentryType\tX\tY\tvariable1DbId\tvariable2DbId\tvariable3DbId\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc123\t1\t1\t1\t2017-06-16T00:53:26Z\tTest Entry\t1\t2\t25.3\t103.4\t50.75\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc124\t1\t1\t1\t2017-06-16T00:54:57Z\tTest Entry\t2\t2\t27.9\t98.65\t45.345\n"
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
                "observationUnitDbId": "1",
                "observationVariableDbId": "variable1DbId"
            },
            {
                "observationDbId": "23456",
                "observationUnitDbId": "1",
                "observationVariableDbId": "variable2DbId"
            },
            {
                "observationDbId": "34567",
                "observationUnitDbId": "1",
                "observationVariableDbId": "variable3DbId"
            },
            {
                "observationDbId": "45678",
                "observationUnitDbId": "1",
                "observationVariableDbId": "imagevariable1DbId"
            },
            {
                "observationDbId": "56789",
                "observationUnitDbId": "2",
                "observationVariableDbId": "variable1DbId"
            },
            {
                "observationDbId": "67890",
                "observationUnitDbId": "2",
                "observationVariableDbId": "variable2DbId"
            },
            {
                "observationDbId": "78901",
                "observationUnitDbId": "2",
                "observationVariableDbId": "variable3DbId"
            },
            {
                "observationDbId": "89012",
                "observationUnitDbId": "2",
                "observationVariableDbId": "imagevariable1DbId"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": []
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
                "plantNumber": "0",
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
                "blockNumber": "1",
                "observationLevel": "plot",
                "observations": [
                    {
                        "observationDbId": "153453453",
                        "collector": "Mr. Technician",
                        "observationVariableDbId": "18020",
                        "value": "25.63",
                        "observationVariableName": "Plant_height",
                        "observationTimeStamp": "2015-06-16T00:53:26Z"
                    },
                    {
                        "observationDbId": "23453454345",
                        "collector": "Mr. Technician",
                        "observationVariableDbId": "51496",
                        "value": "Light Green",
                        "observationVariableName": "GW100_g",
                        "observationTimeStamp": "2015-06-16T00:53:26Z"
                    }
                ],
                "germplasmDbId": "1",
                "X": "1",
                "observationUnitDbId": "abc-123",
                "entryNumber": "1",
                "replicate": "1",
                "plotNumber": "1",
                "germplasmName": "IR-8",
                "observationUnitName": "Test-2016-location-34-575",
                "pedigree": "IR-8-FP/IR-8-MP",
                "Y": "1"
            },
            {
                "entryType": "Check entry",
                "enrtyNumber": "2",
                "blockNumber": "2",
                "observationLevel": "plot",
                "replicate": "1",
                "germplasmName": "IR-9",
                "observatioUnitDbId": "abc-456",
                "germplasmDbId": "2",
                "plotNumber": "2",
                "plantNumber": "0",
                "observationUnitName": "Test-2016-location-34-456",
                "observations": [
                    {
                        "observationDbId": "3",
                        "collector": "Mr. Technician",
                        "observationVariableDbId": "18020",
                        "value": "34.95",
                        "observationVariableName": "Plant_height",
                        "observationTimeStamp": "2015-06-16T00:53:26Z"
                    },
                    {
                        "observationDbId": "4",
                        "collector": "Mr. Technician",
                        "observationVariableDbId": "51496",
                        "value": "Blue",
                        "observationVariableName": "GW100_g",
                        "observationTimeStamp": "2015-06-16T00:53:26Z"
                    }
                ],
                "pedigree": "IR-9-FP/IR-9-MP",
                "X": "1",
                "Y": "2"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": []
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
                "message": "Could not update values for Observation Units",
                "code": "42"
            }
        ]
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

+ Response 200 (application/json)
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
```+ Response 400 (application/json)
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
        "lastUpdate": {
            "timestamp": "2015-06-16T00:53:26Z",
            "version": "1.1"
        },
        "studyDescription": "some free text description that could include scientific goal, some tracability and whatever makes sense",
        "trialName": "International Yield Trial",
        "license": "https://creativecommons.org/licenses/by/4.0",
        "seasons": [
            "2005 Winter",
            "2008 Summer"
        ],
        "studyType": "Yield study",
        "startDate": "2005-06-01",
        "additionalInfo": {
            "property2Name": "property2Value",
            "principalInvestigator": "Dr. Breeder",
            "studyObjective": "Increase yield",
            "publications": "pmid:24039865287545",
            "property1Name": "property1Value"
        },
        "studyDbId": "35",
        "active": "true",
        "dataLinks": [
            {
                "name": "image-archive12.zip",
                "type": "Image archive",
                "url": "http://data.inra.fr/archive/multi-spect-flowering.zip"
            }
        ],
        "location": {
            "countryCode": "NGA",
            "altitude": 12,
            "additionalInfo": {
                "AnnualMeanRain": "value",
                "SoilDescription": "23",
                "property1Name": "property1Value",
                "property2Name": "property2Value"
            },
            "instituteName": "INRA - GDEC",
            "abbreviation": "IB",
            "instituteAddress": "route foo, Clermont Ferrand, France",
            "locationDbId": "1",
            "longitude": 165.5,
            "name": "Ibadan",
            "latitude": -21.5,
            "countryName": "Nigeria"
        },
        "endDate": "2008-12-31",
        "contacts": [
            {
                "name": "John Doe",
                "orcid": "0000-0002-0607-8728",
                "type": "Scientist",
                "instituteName": "IRRI",
                "contactDbId": "C025",
                "email": "j.doe@mail.com"
            },
            {
                "name": "Dave Peters",
                "orcid": null,
                "type": null,
                "instituteName": "IRRI",
                "contactDbId": "C026",
                "email": null
            }
        ],
        "trialDbId": "57",
        "studyName": "Earlygenerationtesting"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
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
                "synonyms": [
                    "01BEL084609"
                ],
                "entryNumber": "1",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "germplasmDbId": "382",
                "germplasmName": "Pahang",
                "seedSource": "SS1",
                "accessionNumber": "ITC0609",
                "pedigree": "TOBA97/SW90.1057"
            },
            {
                "synonyms": [
                    "01BEL084727"
                ],
                "entryNumber": "2",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084727",
                "germplasmDbId": "394",
                "germplasmName": "Pahang",
                "seedSource": "SS2",
                "accessionNumber": "ITC0727",
                "pedigree": "TOBA97/SW90.1057"
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
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
        "pagination": {
            "currentPage": 0,
            "totalCount": 3,
            "pageSize": 1000,
            "totalPages": 1
        },
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
                "startDate": "2007-06-01",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "studyDbId": "35",
                "active": "true",
                "programName": "Drought Resistance Program A",
                "programDbId": "27",
                "endDate": "2008-12-31",
                "locationDbId": "23",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "trialDbId": "7",
                "locationName": "Kenya",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "studyType": "Trial"
            },
            {
                "startDate": "2005-06-01",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "studyDbId": "345",
                "active": "true",
                "programName": "Drought Resistance Program B",
                "programDbId": "58",
                "endDate": "2008-12-31",
                "locationDbId": "33",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "trialDbId": "7",
                "locationName": "Zimbabwe",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "studyType": "Trial"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
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
                "startDate": "2007-06-01",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "studyDbId": "35",
                "active": "true",
                "programName": "Drought Resistance Program A",
                "programDbId": "27",
                "endDate": "2008-12-31",
                "locationDbId": "23",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "trialDbId": "7",
                "locationName": "Kenya",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "studyType": "Trial"
            },
            {
                "startDate": "2005-06-01",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property1Name": "property1Value",
                    "property2Name": "property2Value"
                },
                "studyDbId": "345",
                "active": "true",
                "programName": "Drought Resistance Program B",
                "programDbId": "58",
                "endDate": "2008-12-31",
                "locationDbId": "33",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "trialDbId": "7",
                "locationName": "Zimbabwe",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "studyType": "Trial"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
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
                "scale": {
                    "scaleDbId": "CO_334:0100526",
                    "xref": null,
                    "name": "ug/g",
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    }
                },
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100632",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                },
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "method": {
                    "reference": null,
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null
                },
                "defaultValue": "0"
            },
            {
                "scientist": "",
                "date": "2016-05-13",
                "language": "EN",
                "status": "recommended",
                "name": "caro_spectro",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "institution": "",
                "scale": {
                    "scaleDbId": "CO_334:0100526",
                    "xref": null,
                    "name": "ug/g",
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    }
                },
                "growthStage": "mature",
                "ontologyName": "Cassava",
                "xref": "TL_455:0003001",
                "observationVariableDbId": "CO_334:0100622",
                "trait": {
                    "class": "physiological trait",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "entity": "root",
                    "description": "Cassava storage root pulp carotenoid content",
                    "xref": "TL_455:0003023",
                    "status": "recommended",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "ontologyDbId": "CO_334",
                "method": {
                    "reference": null,
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null
                },
                "defaultValue": "0"
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
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
                "scale": null,
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100632",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                },
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "method": null,
                "defaultValue": null
            },
            {
                "scientist": "",
                "date": "2016-05-13",
                "language": "EN",
                "status": "recommended",
                "name": "caro_spectro",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "institution": "",
                "scale": {
                    "scaleDbId": "CO_334:0100526",
                    "xref": null,
                    "name": "ug/g",
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    }
                },
                "growthStage": "mature",
                "ontologyName": "Cassava",
                "xref": "TL_455:0003001",
                "observationVariableDbId": "CO_334:0100622",
                "trait": {
                    "class": "physiological trait",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "entity": "root",
                    "description": "Cassava storage root pulp carotenoid content",
                    "xref": "TL_455:0003023",
                    "status": "recommended",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "ontologyDbId": "CO_334",
                "method": {
                    "reference": null,
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null
                },
                "defaultValue": null
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": []
    }
}
```