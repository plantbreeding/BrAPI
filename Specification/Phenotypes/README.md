
# Group Phenotypes

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.




## Observationunits [/brapi/v1/observationunits] 




### Get Observationunits  [GET /brapi/v1/observationunits{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?page}{?pageSize}]

Get a set of observation units

 

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
            "totalCount": 22,
            "totalPages": 11
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
            "totalCount": 22,
            "totalPages": 11
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
            }
        ]
    }
}
```





### **Deprecated** Post Phenotypes-search  [POST /brapi/v1/phenotypes-search]

DEPRECATED in v1.3 - See /search/observationunits

 

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
            "totalCount": 11,
            "totalPages": 6
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "10",
                "Y": "12",
                "blockNumber": "0",
                "entryNumber": "1",
                "entryType": "CHECK",
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
                    },
                    {
                        "collector": "string",
                        "observationDbId": "be7ca923-240b-431f-bb01-23b611c25850",
                        "observationTimeStamp": "1970-01-18T14:02:52-05:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "fall 2011",
                        "value": "string"
                    },
                    {
                        "collector": "string",
                        "observationDbId": "83b8ccde-69c7-4cb8-84c8-3ab8b5c5d934",
                        "observationTimeStamp": "1970-01-18T14:02:52-05:00",
                        "observationVariableDbId": "MO_123:100002",
                        "observationVariableName": "Plant height",
                        "season": "fall 2011",
                        "value": "string"
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
            "totalCount": 11,
            "totalPages": 6
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
                "0",
                "CHECK",
                "10",
                "12",
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
                "observationDbId": "5438fc7b-be54-4ed3-847a-ac110735f7fd",
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
            "pageSize": 4,
            "totalCount": 11,
            "totalPages": 3
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
                "2",
                ""
            ],
            [
                "2011",
                "1003",
                "Study 3",
                "2",
                "Location 2",
                "2",
                "Name002",
                "11",
                "6",
                "1",
                "101",
                "FILLER",
                "1",
                "1",
                "11",
                "",
                "12",
                "5",
                "black"
            ],
            [
                "2013",
                "1001",
                "Study 1",
                "1",
                "Location 1",
                "1",
                "Name001",
                "2",
                "1",
                "0",
                "1",
                "TEST",
                "1",
                "1",
                "1.1",
                "5.1",
                "",
                "",
                ""
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
            "MO_123:100004",
            "MO_123:100005"
        ],
        "observationVariableNames": [
            "Plant height",
            "Virus severity",
            "Carotenoid",
            "Root weight",
            "Root color"
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





### Get Search Observationunits SearchResultsDbId  [GET /brapi/v1/search/observationunits/searchResultsDbId{?page}{?pageSize}]

Returns a list of observationUnit with the observed Phenotypes.

See Search Services for additional implementation details.

 

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
            "pageSize": 1000,
            "totalCount": 22,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "1",
                "Y": "2",
                "blockNumber": "1",
                "entryNumber": "8",
                "entryType": "CHECK",
                "germplasmDbId": "3",
                "germplasmName": "Name003",
                "observationLevel": "plant",
                "observationLevels": "block:1;plot:4;plant:4",
                "observationUnitDbId": "8",
                "observationUnitName": "Plant 4",
                "observationUnitXref": [],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "12",
                        "observationTimeStamp": "2013-06-14T22:14:51-04:00",
                        "observationVariableDbId": "MO_123:100005",
                        "observationVariableName": "Root color",
                        "season": "spring 2012",
                        "value": "red"
                    }
                ],
                "plantNumber": "4",
                "plotNumber": "4",
                "programName": "Program 1",
                "replicate": "0",
                "studyDbId": "1002",
                "studyLocation": "Peru",
                "studyLocationDbId": "1",
                "studyName": "Study 2",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "normal"
                    }
                ]
            },
            {
                "X": "1",
                "Y": "2",
                "blockNumber": "1",
                "entryNumber": "7",
                "entryType": "TEST",
                "germplasmDbId": "3",
                "germplasmName": "Name003",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:4",
                "observationUnitDbId": "7",
                "observationUnitName": "Plot 4",
                "observationUnitXref": [],
                "observations": [
                    {
                        "collector": "A. Technician",
                        "observationDbId": "11",
                        "observationTimeStamp": "2013-06-14T22:13:51-04:00",
                        "observationVariableDbId": "MO_123:100003",
                        "observationVariableName": "Carotenoid",
                        "season": "spring 2012",
                        "value": "1.4"
                    }
                ],
                "plantNumber": "null",
                "plotNumber": "4",
                "programName": "Program 1",
                "replicate": "0",
                "studyDbId": "1002",
                "studyLocation": "Peru",
                "studyLocationDbId": "1",
                "studyName": "Study 2",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "normal"
                    }
                ]
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

