
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
                "studyDbId": "35",
                "Y": 1,
                "germplasmName": "ZIPA_68",
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "X": 1,
                "additionalInfo": {}
            },
            {
                "studyDbId": "35",
                "Y": 2,
                "germplasmName": "ZIPA_69",
                "germplasmDbId": "144",
                "observationUnitDbId": "12",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "X": 1,
                "additionalInfo": {}
            },
            {
                "studyDbId": "35",
                "Y": 3,
                "germplasmName": "ZIPA_70",
                "germplasmDbId": "145",
                "observationUnitDbId": "13",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "X": 1,
                "additionalInfo": {}
            },
            {
                "studyDbId": "35",
                "Y": 1,
                "germplasmName": "ZIPA_68",
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 2,
                "observationLevel": "plot",
                "replicate": 2,
                "X": 2,
                "additionalInfo": {}
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "studyDbId": "1",
                "Y": 1,
                "germplasmName": "ZIPA_68",
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "X": 1,
                "additionalInfo": {}
            },
            {
                "studyDbId": "1",
                "Y": 2,
                "germplasmName": "ZIPA_69",
                "germplasmDbId": "144",
                "observationUnitDbId": "12",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "X": 1,
                "additionalInfo": {}
            },
            {
                "studyDbId": "1",
                "Y": 3,
                "germplasmName": "ZIPA_70",
                "germplasmDbId": "145",
                "observationUnitDbId": "13",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 1,
                "observationLevel": "plot",
                "replicate": 1,
                "X": 1,
                "additionalInfo": {}
            },
            {
                "studyDbId": "1",
                "Y": 1,
                "germplasmName": "ZIPA_68",
                "germplasmDbId": "143",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "entryType": "check/test/filler",
                "blockNumber": 2,
                "observationLevel": "plot",
                "replicate": 2,
                "X": 2,
                "additionalInfo": {}
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 4,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "code": "1",
                "message": "Upload Successful"
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
                "code": "Error",
                "message": "Could not update values for Observation Units"
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
                "studyDbId": "35",
                "observationTimeStamp": "2015-11-05T15:12:56+01:00",
                "germplasmName": "Pahang",
                "germplasmDbId": "8383",
                "value": "5",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationVariableName": "Yield",
                "observationLevel": "plot",
                "operator": "Jane Doe",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "observationDbId": "12345"
            },
            {
                "studyDbId": "35",
                "observationTimeStamp": "2015-11-05T15:13:56+01:00",
                "germplasmName": "Pahang",
                "germplasmDbId": "8383",
                "value": "22.3",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationVariableName": "Dry Weight",
                "observationLevel": "plot",
                "operator": "Jane Doe",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "observationDbId": "23456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "studyDbId": "35",
                "germplasmName": "Pahang",
                "germplasmDbId": "8383",
                "observationTimestamp": "2015-11-05T15:12:56+01:00",
                "value": "5",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationVariableName": "Yield",
                "observationLevel": "plot",
                "operator": "Jane Doe",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "observationDbId": "12345"
            },
            {
                "studyDbId": "35",
                "germplasmName": "Pahang",
                "germplasmDbId": "8383",
                "observationTimestamp": "2015-11-05T15:13:56+01:00",
                "value": "22.3",
                "observationUnitDbId": "11",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationVariableName": "Dry Weight",
                "observationLevel": "plot",
                "operator": "Jane Doe",
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "observationDbId": "23456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "year": "2015",
                "seasonDbId": "237"
            },
            {
                "season": "Spring",
                "year": "2016",
                "seasonDbId": "238"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
```+ Response 200 (application/tsv)
```
"year\tstudyDbId\tstudyName\tlocationDbId\tlocationName\tgermplasmDbId\tgermplasmName\tobservationUnitDbId\tplotNumber\treplicate\tblockNumber\tobservationTimestamp\tentryType\tX\tY\tvariable1DbId\tvariable2DbId\tvariable3DbId\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc123\t1\t1\t1\t2017-06-16T00:53:26Z\tTest Entry\t1\t2\t25.3\t103.4\t50.75\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc124\t1\t1\t1\t2017-06-16T00:54:57Z\tTest Entry\t2\t2\t27.9\t98.65\t45.345\n"
```+ Response 200 (application/json)
```
{
    "result": {
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
        ],
        "observationVariableDbIds": [
            "variable1DbId",
            "variable2DbId",
            "variable3DbId"
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
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
                "observationVariableDbId": "variable1DbId",
                "observationDbId": "12345"
            },
            {
                "observationUnitDbId": "1",
                "observationVariableDbId": "variable2DbId",
                "observationDbId": "23456"
            },
            {
                "observationUnitDbId": "1",
                "observationVariableDbId": "variable3DbId",
                "observationDbId": "34567"
            },
            {
                "observationUnitDbId": "1",
                "observationVariableDbId": "imagevariable1DbId",
                "observationDbId": "45678"
            },
            {
                "observationUnitDbId": "2",
                "observationVariableDbId": "variable1DbId",
                "observationDbId": "56789"
            },
            {
                "observationUnitDbId": "2",
                "observationVariableDbId": "variable2DbId",
                "observationDbId": "67890"
            },
            {
                "observationUnitDbId": "2",
                "observationVariableDbId": "variable3DbId",
                "observationDbId": "78901"
            },
            {
                "observationUnitDbId": "2",
                "observationVariableDbId": "imagevariable1DbId",
                "observationDbId": "89012"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
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
                "plotNumber": "1",
                "entryNumber": "1",
                "plantNumber": "0",
                "pedigree": "IR-8-FP/IR-8-MP",
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
                "observationUnitName": "Test-2016-location-34-575",
                "blockNumber": "1",
                "replicate": "1",
                "observationUnitDbId": "abc-123",
                "Y": "1",
                "germplasmName": "IR-8",
                "germplasmDbId": "1",
                "observationLevel": "plot",
                "entryType": "Test entry",
                "observations": [
                    {
                        "observationDbId": "153453453",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableName": "Plant_height",
                        "observationVariableDbId": "18020",
                        "collector": "Mr. Technician",
                        "value": "25.63"
                    },
                    {
                        "observationDbId": "23453454345",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableName": "GW100_g",
                        "observationVariableDbId": "51496",
                        "collector": "Mr. Technician",
                        "value": "Light Green"
                    }
                ],
                "X": "1"
            },
            {
                "plotNumber": "2",
                "Y": "2",
                "enrtyNumber": "2",
                "plantNumber": "0",
                "germplasmName": "IR-9",
                "germplasmDbId": "2",
                "pedigree": "IR-9-FP/IR-9-MP",
                "observationUnitName": "Test-2016-location-34-456",
                "observatioUnitDbId": "abc-456",
                "entryType": "Check entry",
                "blockNumber": "2",
                "observationLevel": "plot",
                "replicate": "1",
                "observations": [
                    {
                        "observationDbId": "3",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableName": "Plant_height",
                        "observationVariableDbId": "18020",
                        "collector": "Mr. Technician",
                        "value": "34.95"
                    },
                    {
                        "observationDbId": "4",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationVariableName": "GW100_g",
                        "observationVariableDbId": "51496",
                        "collector": "Mr. Technician",
                        "value": "Blue"
                    }
                ],
                "X": "1"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "code": "42",
                "message": "Could not update values for Observation Units"
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
    "type": "array",
    "title": "newObservationUnitRequestList",
    "items": {
        "$ref": "#/definitions/newObservationUnitRequest"
    }
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
                "code": "1",
                "message": "Upload Successful"
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
                "code": "Error",
                "message": "Could not update values for Observation Units"
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
        "active": "true",
        "dataLinks": [
            {
                "type": "Image archive",
                "name": "image-archive12.zip",
                "url": "http://data.inra.fr/archive/multi-spect-flowering.zip"
            }
        ],
        "trialName": "International Yield Trial",
        "studyType": "Yield study",
        "studyName": "Earlygenerationtesting",
        "studyDescription": "some free text description that could include scientific goal, some tracability and whatever makes sense",
        "additionalInfo": {
            "publications": "pmid:24039865287545",
            "principalInvestigator": "Dr. Breeder",
            "property2Name": "property2Value",
            "property1Name": "property1Value",
            "studyObjective": "Increase yield"
        },
        "license": "https://creativecommons.org/licenses/by/4.0",
        "trialDbId": "57",
        "startDate": "2005-06-01",
        "endDate": "2008-12-31",
        "lastUpdate": {
            "timestamp": "2015-06-16T00:53:26Z",
            "version": "1.1"
        },
        "studyDbId": "35",
        "location": {
            "abbreviation": "IB",
            "latitude": -21.5,
            "longitude": 165.5,
            "name": "Ibadan",
            "countryCode": "NGA",
            "locationDbId": "1",
            "altitude": 12,
            "instituteName": "INRA - GDEC",
            "countryName": "Nigeria",
            "instituteAddress": "route foo, Clermont Ferrand, France",
            "additionalInfo": {
                "AnnualMeanRain": "value",
                "property2Name": "property2Value",
                "property1Name": "property1Value",
                "SoilDescription": "23"
            }
        },
        "contacts": [
            {
                "email": "j.doe@mail.com",
                "instituteName": "IRRI",
                "type": "Scientist",
                "name": "John Doe",
                "contactDbId": "C025",
                "orcid": "0000-0002-0607-8728"
            },
            {
                "email": null,
                "instituteName": "IRRI",
                "type": null,
                "name": "Dave Peters",
                "contactDbId": "C026",
                "orcid": null
            }
        ],
        "seasons": [
            "2005 Winter",
            "2008 Summer"
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
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
                "entryNumber": "1",
                "germplasmName": "Pahang",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "germplasmDbId": "382",
                "accessionNumber": "ITC0609",
                "pedigree": "TOBA97/SW90.1057",
                "synonyms": [
                    "01BEL084609"
                ],
                "seedSource": "SS1"
            },
            {
                "entryNumber": "2",
                "germplasmName": "Pahang",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084727",
                "germplasmDbId": "394",
                "accessionNumber": "ITC0727",
                "pedigree": "TOBA97/SW90.1057",
                "synonyms": [
                    "01BEL084727"
                ],
                "seedSource": "SS2"
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studytypes [Get /brapi/v1/studytypes{?pageSize}{?page}]

 Call to retrieve the list of study types.
Scope: PHENOTYPING. Implementation target date: PAG2016
<a href="https://test-server.brapi.org/brapi/v1/studytypes"> test-server.brapi.org/brapi/v1/studytypes</a> 

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
            "currentPage": 0,
            "totalCount": 3,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "studyDbId": "35",
                "locationName": "Kenya",
                "active": "true",
                "programDbId": "27",
                "locationDbId": "23",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "studyType": "Trial",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property2Name": "property2Value",
                    "property1Name": "property1Value"
                },
                "programName": "Drought Resistance Program A",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "trialDbId": "7",
                "startDate": "2007-06-01",
                "endDate": "2008-12-31"
            },
            {
                "studyDbId": "345",
                "locationName": "Zimbabwe",
                "active": "true",
                "programDbId": "58",
                "locationDbId": "33",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "studyType": "Trial",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property2Name": "property2Value",
                    "property1Name": "property1Value"
                },
                "programName": "Drought Resistance Program B",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "trialDbId": "7",
                "startDate": "2005-06-01",
                "endDate": "2008-12-31"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "studyDbId": "35",
                "locationName": "Kenya",
                "active": "true",
                "programDbId": "27",
                "locationDbId": "23",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "studyType": "Trial",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property2Name": "property2Value",
                    "property1Name": "property1Value"
                },
                "programName": "Drought Resistance Program A",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "trialDbId": "7",
                "startDate": "2007-06-01",
                "endDate": "2008-12-31"
            },
            {
                "studyDbId": "345",
                "locationName": "Zimbabwe",
                "active": "true",
                "programDbId": "58",
                "locationDbId": "33",
                "trialName": "InternationalTrialA",
                "name": "Earlygenerationtesting",
                "studyType": "Trial",
                "additionalInfo": {
                    "property3Name": "property3Value",
                    "property2Name": "property2Value",
                    "property1Name": "property1Value"
                },
                "programName": "Drought Resistance Program B",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "trialDbId": "7",
                "startDate": "2005-06-01",
                "endDate": "2008-12-31"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "ontologyName": "Cassava",
                "defaultValue": "0",
                "name": "CT_M_C",
                "method": {
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "reference": null,
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation"
                },
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": {
                    "xref": null,
                    "validValues": {
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "min": 1
                    },
                    "decimalPlaces": 2,
                    "scaleDbId": "CO_334:0100526",
                    "datatype": "Numeric",
                    "name": "ug/g"
                },
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                }
            },
            {
                "scientist": "",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "date": "2016-05-13",
                "xref": "TL_455:0003001",
                "defaultValue": "0",
                "crop": "Cassava",
                "name": "caro_spectro",
                "scale": {
                    "xref": null,
                    "validValues": {
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "min": 1
                    },
                    "decimalPlaces": 2,
                    "scaleDbId": "CO_334:0100526",
                    "datatype": "Numeric",
                    "name": "ug/g"
                },
                "ontologyName": "Cassava",
                "institution": "",
                "language": "EN",
                "status": "recommended",
                "method": {
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "reference": null,
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation"
                },
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "observationVariableDbId": "CO_334:0100622",
                "ontologyDbId": "CO_334",
                "growthStage": "mature",
                "trait": {
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "attribute": "carotenoid",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "mainAbbreviation": "CC",
                    "class": "physiological trait",
                    "entity": "root"
                }
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
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
                "ontologyName": "Cassava",
                "defaultValue": null,
                "name": "CT_M_C",
                "method": null,
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": null,
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                }
            },
            {
                "scientist": "",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "date": "2016-05-13",
                "xref": "TL_455:0003001",
                "defaultValue": null,
                "crop": "Cassava",
                "name": "caro_spectro",
                "scale": {
                    "xref": null,
                    "validValues": {
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "min": 1
                    },
                    "decimalPlaces": 2,
                    "scaleDbId": "CO_334:0100526",
                    "datatype": "Numeric",
                    "name": "ug/g"
                },
                "ontologyName": "Cassava",
                "institution": "",
                "language": "EN",
                "status": "recommended",
                "method": {
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "reference": null,
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation"
                },
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "observationVariableDbId": "CO_334:0100622",
                "ontologyDbId": "CO_334",
                "growthStage": "mature",
                "trait": {
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "attribute": "carotenoid",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "mainAbbreviation": "CC",
                    "class": "physiological trait",
                    "entity": "root"
                }
            }
        ],
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
    }
}
```