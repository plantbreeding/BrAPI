## Variables by category [/brapi/v1/variables/category/{categoryName}]
Scope: CORE.
Status: ACCEPTED.

Call to retrieve a list of variables for a given category as defined in the crop ontology (Phenology, stress, etc.).
+ Parameters
    + categoryName (required, string, `Phenology`) ... string containing the name of the category

### Variables by category [GET]
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
                        "observationVariableDbId": "123",
                        "observationVariableId": "CO_334:0100622",
                        "name": "caro_spectro",
                        "fullName": "Carotenoid content by spectro",
                        "trait": {
                            "traitDbId": "123",
                            "traitId": "CO_334:0100620",
                            "name": "Carotenoid content",
                            "description": "Cassava storage root pulp carotenoid content"
                        },
                        "measurementMethod": {
                            "methodId": "CO_334:0010320",
                            "name": "Visual Rating:total carotenoid by chart_method",
                            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                        },
                        "scale": {
                            "scaleId": "CO_334:0100526",
                            "name": "ug/g",
                            "dataType": "Numeric",
                            "validValues": {
                                "min": "0",
                                "max": "100",
                                "categories": null
                            }
                        },
                        "defaultValue": null
                    },
                    {
                        "observationVariableDbId": "124",
                        "observationVariableId": "CO_334:0100621",
                        "name": "Carot_chart",
                        "fullName": "Carotenoid content by chart",
                        "trait": {
                            "traitDbId": "124",
                            "traitId": "CO_334:0100620",
                            "name": "Carotenoid content",
                            "description": "Cassava storage root pulp carotenoid content"
                        },                 
                        "measurementMethod": {
                            "methodId": "CO_334:0010319",
                            "name": "Visual Rating:total carotenoid by chart_method",
                            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                        },
                        "scale": {
                            "scaleId": "CO_334:0100525",
                            "name": "8pt scale",
                            "dataType": "Categorical",
                            "validValues": {
                                "min": null,
                                "max": null,
                                "categories": [
                                    "white", 
                                    "light cream", 
                                    "cream", 
                                    "light yellow", 
                                    "yellow", 
                                    "deep yellow", 
                                    "orange", 
                                    "pink"
                                ]
                            }
                        },
                        "defaultValue": null
                    }
                ]
            }
        }
