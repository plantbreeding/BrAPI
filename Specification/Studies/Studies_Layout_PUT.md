
### Update plot layout details [PUT /brapi/v1/studies/{studyDbId}/layout]

Update the layout data for a set of observation units within a study. Each layout object is a subset of fields within an observationUnit, so it doesn't make sense to create a new layout object by itself. 

Implementation Notes:

+ If any of the fields in the request object is missing, that piece of data will not be updated.
+ If an observationUnitDbId can not be found within the given study, an error will be returned.
+ `entryType` can have the values "check", "test", or "filler".
+ The response should match the structure of the response from `GET studies/{studyDbId}/layout`, but it should only contain the layout objects which have been updated by the PUT request. Also, pagination is not available in the response.

+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study.

+ Request

        {
            "layout" : [ 
                {
                    "observationUnitDbId": "11",
                    "replicate": 1,
                    "blockNumber": 1,
                    "X": 1,
                    "Y": 1,
                    "entryType": "check/test/filler"
                },
                {
                    "observationUnitDbId": "12",
                    "replicate": 1,
                    "blockNumber": 1,
                    "X": 1,
                    "Y": 2,
                    "entryType": "check/test/filler"
                },
                {
                    "observationUnitDbId": "13",
                    "replicate": 2,
                    "blockNumber": 2,
                    "X": 2,
                    "Y": 1,
                    "entryType": "check/test/filler"
                },
                {
                    "observationUnitDbId": "11",
                    "replicate": 1,
                    "blockNumber": 1,
                    "X": 1,
                    "Y": 3,
                    "entryType": "check/test/filler"
                }
            ]
        }

+ Response 200 (application/json)
    
        {
            "metadata" : {
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data" : [ 
                    {
                        "studyDbId": "1",
                        "observationUnitDbId": "11",
                        "observationUnitName": "ZIPA_68_Ibadan_2014",
                        "observationLevel": "plot",
                        "germplasmDbId": "143",
                        "germplasmName": "ZIPA_68",
                        "replicate": 1,
                        "blockNumber": 1,
                        "X": 1,
                        "Y": 1,
                        "entryType": "check/test/filler",
                        "additionalInfo" : { 
                        }
                    },
                    {
                        "studyDbId": "1",
                        "observationUnitDbId": "12",
                        "observationUnitName": "ZIPA_69_Ibadan_2014",
                        "observationLevel": "plot",
                        "germplasmDbId": "144",
                        "germplasmName": "ZIPA_69",
                        "replicate": 1,
                        "blockNumber": 1,
                        "X": 1,
                        "Y": 2,
                        "entryType": "check/test/filler",
                        "additionalInfo" : { 
                        }
                    },
                    {
                        "studyDbId": "1",
                        "observationUnitDbId": "13",
                        "observationUnitName": "ZIPA_70_Ibadan_2014",
                        "observationLevel": "plot",
                        "germplasmDbId": "145",
                        "germplasmName": "ZIPA_70",
                        "replicate": 2,
                        "blockNumber": 2,
                        "X": 2,
                        "Y": 1,
                        "entryType": "check/test/filler",
                        "additionalInfo" : { 
                        }
                    },
                    {
                        "studyDbId": "1",
                        "observationUnitDbId": "11",
                        "observationUnitName": "ZIPA_68_Ibadan_2014",
                        "observationLevel": "plot",
                        "germplasmDbId": "143",
                        "germplasmName": "ZIPA_68",
                        "replicate": 1,
                        "blockNumber": 1,
                        "X": 1,
                        "Y": 3,
                        "entryType": "check/test/filler",
                        "additionalInfo" : { 
                        }
                    }
                ]
            }
        }

