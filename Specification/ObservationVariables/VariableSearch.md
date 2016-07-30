## Variable Search [/brapi/v1/variables-search]
Scope: CORE.
Status: ACCEPTED.

Search observation variables.

### Variable Search [POST]

+ Request (application/json)

        {
            "observationVariableIds" : ["obs-variable-id1", "obs-variable-id1"],
            "cropOntologyXrefs" : ["CO:123", "CO:456"],
            "methodIds" : ["method-1", "method=2"],
            "scaleIds" : ["sclae-1", "scale-2"],
            "names" : [],
            "cropOntologyIds" : [],
            "dataTypes" : [],
            "variableTypes" : [],
            "classes" : []
        }

+ Response 200 (application/json)
        
        {
        "metadata": {
            "pagination": {
                "pageSize": 10,
                "currentPage": 1,
                "totalCount": 2,
                "totalPages": 1
            },
            "status": {},
            "datafiles": []
        },
        "result": {
            "data" : [ 
                {
                    "traitDbId": "123",
                    "observationVariableId": "CO_334:0100622",
                    "name": "carot_spectro",
                    "fullName": "Carotenoid content by spectro",
                    "trait": {
                        "traitId": "CO_334:0100620",
                        "name": "Estimation :Total Carotenoid Content_method",
                        "description": "Total extracted carotenoids in cassava storage root as estimated by spectrophotometer"
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
                }
            ]
        }
