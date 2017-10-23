### Search Studies (POST) [POST /brapi/v1/studies-search] 

+ Request (application/json)

        {
           "studyType" : "Trial",
           "studyNames" : ["Study A", "StydyB"], 
           "studyLocations" : ["Kenya", "Zimbabwe"], 
           "programNames": ["Test Program", "Program2"],
           "germplasmDbIds" : [ "CML123", "CWL123"],
           "observationVariableDbIds": ["CO-PH-123", "Var-123"]
           "active" : "true",
           "sortBy" : "studyDbId",
           "sortOrder" : "desc"
        }

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 2,
                    "currentPage": 0,
                    "totalCount": 100,
                    "totalPages": 50
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "data": [ 
                    {
                        "studyDbId": 35,
                        "name": "Earlygenerationtesting",
                        "trialDbId" : 1,
                        "trialName" : "InternationalTrialA",
                        "studyType": "Trial",
                        "seasons": ["2007 Spring", "2008 Fall"],
                        "locationDbId": 23,
                        "locationName": "Kenya",
                        "programDbId": 27,
                        "programName": "Drought Resistance Program A",
                        "startDate": "2007-06-01",
                        "endDate"  : "2008-12-31",
                        "studyType": "Trial",
                        "active" : "true",
                        "additionalInfo" : {
                            "property1Name" : "property1Value",
                            "property2Name" : "property2Value",
                            "property3Name" : "property3Value"
                        }
                    }
                    ,
                    {
                        "studyDbId": 345,
                        "name": "Earlygenerationtesting",
                        "trialDbId" : 1,
                        "trialName" : "InternationalTrialA",
                        "seasons": ["2005 Winter", "2006 Summer"],
                        "locationDbId": 33,
                        "locationName": "Zimbabwe",
                        "programDbId": 58,
                        "programName": "Drought Resistance Program B",
                        "startDate": "2005-06-01",
                        "endDate"  : "2008-12-31",
                        "studyType": "Trial",
                        "active" : "true",
                        "additionalInfo" : {
                            "property1Name" : "property1Value",
                            "property2Name" : "property2Value",
                            "property3Name" : "property3Value"
                        }
                    }
                ]
            }
        }        
