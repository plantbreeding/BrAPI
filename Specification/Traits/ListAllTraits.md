## List all Traits [/brapi/v1/traits]
Scope: CORE.
Status: ACCEPTED.

Implemented by: Germinate, Cassavabase

Call to retrieve a list of traits available in the system and their associated variables.

### List all traits [GET]
+ Response 200 (application/json)
    
        {
            "metadata" : {
                "pagination" : {    
                    "pageSize": 3, 
                    "currentPage": 0, 
                    "totalCount": 300, 
                    "totalPages": 100 
                }
                "status" : [],
                "datafiles": []
            },
        
            "result" : {
                "data" : [
                    {
                        "traitDbId": "123",
                        "traitId": "CO:123000007",
                        "name": "Plant Height",
                        "description": "Description of Plant Height",
                        "observationVariables": [
                            "CO_334:0100121", 
                            "CO_334:0100122", 
                            "CO_334:0100123" 
                        ],
                        "defaultValue": null
                    },
                    {
                        "traitDbId": "123",
                        "traitId": "CO_334:0100620",
                        "name": "Carotenoid content",
                        "description": "Cassava storage root pulp carotenoid content",
                        "observationVariables": [
                            "CO_334:0100621", 
                            "CO_334:0100622", 
                            "CO_334:0100623" 
                        ],
                        "defaultValue": null
                    }
                ],

            ]
        }

