## Study Observation Variables [/brapi/v1/studies/{studyDbId}/observationVariables]

List all the observation variables measured in the study.

### Retrieve study observation variables [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":2, 
                    "currentPage":0, 
                    "totalCount":10, 
                    "totalPages":5 
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "studyDbId": 123,
                "trialName": "myBestTrial",
                "data": [
                    
                    {
                        "observationVariableId": "CO_334:0100622",
                        "observationVariableName": "carot_spectro",
                        "trait": "TraitName",
                        "method" : "Root to tip at maturity",
                        "scale" : "cm",
                        "dataType": "Numeric",
                        "scaleValidValues": {
                            "min": "0",
                            "max": "100",
                            "categories": null
                          }
                    },
                    
                    {
                        "observationVariableId": "CO_334:112233",
                        "observationVariableName": "Flower Color",
                        "trait": "TraitName",
                        "method" : "Record manually",
                        "scale" : "Color",
                        "dataType": "Text",
                        "scaleValidValues": {
                            "min": null,
                            "max": null,
                            "categories": ["Red", "Blue", "Yellow"]
                          }
                    }
                
                ]
            }
        }

