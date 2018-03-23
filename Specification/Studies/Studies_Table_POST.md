### Save study Observation Units as table [POST /brapi/v1/studies/{studyDbId}/table]

This call can be used to create new observations in bulk. 

Note: If you need to update any existing observation, please use `PUT /studies/{studyDbId}/observations`. This call should only be used to create NEW observations.

Implementation Guidelines: 

+ All observations submitted through this call should create NEW observation records in the database under the given observation unit. 
+ Each 'observationUnitDbId' listed should already exist in the database. If the server can not find a given 'observationUnitDbId', it should report an error. (see Error Handling)
+ The response of this call should be the set of 'observationDbIds' created from this call, along with the associated 'observationUnitDbId' and 'observationVariableDbId' that each observation is associated with.


Images can optionally be saved using this call by providing a zipped file of all images in the datafiles. The physical zipped file should be transferred as well in the mulit-part form data.

Scope: PHENOTYPING

+ Parameters
    + studyDbId (required, string, `1`) ... Identifier of the study. Usually a number, could be alphanumeric.
    
+ Request
    
        {
            "headerRow": [ "observationUnitDbId", "collector", "observationTimestamp"],
            "observationVariableDbIds": ["variable1DbId", "variable2DbId", "variable3DbId", "imagevariable1DbId" ],
            "data" :[
                ["1", "Mr. Technician1", "2015-06-16T10:00:00Z", "variable1Value", "variable2Value", "variable3Value", "image1.jpg" ],
                ["2", "Mr. Technician2", "2015-06-16T11:00:01Z", "variable1Value", "variable2Value", "variable3Value", "image2.jpg" ]
            ]
        }
        
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status": [],
                "datafiles": []
            },
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
            }
        }