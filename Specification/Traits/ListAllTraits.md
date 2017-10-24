## List all Traits [/brapi/v1/traits?pageSize={pageSize}&page={page}]
Scope: CORE.
Status: ACCEPTED.

Implemented by: Germinate, Cassavabase

Call to retrieve a list of traits available in the system and their associated variables.

### List all traits [GET]
+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)
    
        {
            "metadata" : {
                "pagination" : {    
                    "pageSize": 1000, 
                    "currentPage": 0, 
                    "totalCount": 2, 
                    "totalPages": 1 
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

