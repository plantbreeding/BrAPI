## List all Variables [/brapi/v1/variables]
Scope: CORE.
Status: ACCEPTED.

Call to retrieve a list of observationVariables available in the system.
`required` means the key has to be provided, but the value may be null.

### List all variables [GET]
+ Response 200 (application/json)
    
        {
            "metadata" : {
                "pagination" : {    
                    "pageSize": 3, 
                    "currentPage": 1, 
                    "totalCount": 300, 
                    "totalPages": 100 
                }
                "status" : {},
                "datafiles": []
            },
        
            "result" : {
                "data" : [
                            {
                                "observationVariableDbId": "123",    // required
                                "observationVariableOntologyId": "CO_334",  // required
                                "observationVariableOntologyName": "Cassava",  //required
                                "observationVariableId": "CO_334:0100622",  // required
                                "observationVariableName": "caro_spectro",   // required
                                "observationVariableSynonyms": ["Carotenoid content by spectro", ""],  
                                "observationVariableContextOfUse": ["", ""],
                                "observationVariableGrowthStage": "",
                                "observationVariableStatus": "recommended",
                                "observationVariableXref": "",
                                "observationVariableInstitution": "",
                                "observationVariableScientist": "",
                                "observationVariableDate": "",
                                "observationVariableLanguage": "EN",
                                "observationVariableCrop": "Cassava",
                                "trait": {                               // required
                                    "traitDbId": "123",   // required
                                    "traitId": "CO_334:0100620",   // required
                                    "traitName": "Carotenoid content",   // required
                                    "traitDescription": "Cassava storage root pulp carotenoid content",
                                    "traitClass": "", 
                                    "traitSynonyms": ["", ""],
                                    "traitMainAbbreviation": "",
                                    "traitAlternativeAbbreviations": ["", ""],
                                    "traitEntity": "root",
                                    "traitAttribute": "carotenoid",
                                    "traitStatus": "recommended",
                                    "traitXref": ""
                                },
                                "measurementMethod": {   // required
                                    "methodId": "CO_334:0010320",
                                    "methodName": "Visual Rating:total carotenoid by chart_method",
                                    "methodDescription": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                                    "methodClass": "", 
                                    "methodFormula": "",
                                    "methodReference": ""
                                },
                                "scale": {    // required
                                    "scaleId": "CO_334:0100526",
                                    "scaleName": "ug/g",
                                    "scaleClass": "",
                                    "dataType" : "numeric", 
                                    "scaleDecimalPlaces": 2,
                                    "scaleXref": "",
                                    "scaleValidValues": {
                                        "min": "0",
                                        "max": "100",
                                        "categories": null
                                    }
                                },
                                "defaultValue": null    // required
                            }
                        ]
            }
        }

