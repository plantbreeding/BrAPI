## Variable details [/brapi/v1/variables/{observationVariableDbId}]
Scope: CORE.
Status: ACCEPTED.

Retrieve variable details


### Variable details by id [GET /brapi/v1/variables/{observationVariableDbId}]
+ Parameters
    + observationVariableDbId (required, string, `CO_334:0100622`) ... string id of the variable
    
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "observationVariableDbId": "CO_334:0100622",
                "name": "caro_spectro",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "synonyms": ["Carotenoid content by spectro"],
                "contextOfUse": ["Trial evaluation", "Nursery evaluation"],
                "growthStage": "mature",
                "status": "recommended",
                "xref": "TL_455:0003001",
                "institution": "",
                "scientist": "",
                "submissionTimestamp": "2016-05-13T15:43:41+0100",
                "language": "EN",
                "crop": "Cassava",
                "trait": {
                    "traitDbId": "CO_334:0100620",
                    "name": "Carotenoid content",
                    "class": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": ["carotenoid content measure"],
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": ["CCS"],
                    "entity": "root",
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "xref": "TL_455:0003023"
                },
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "reference": null
                },
                "scale": {
                    "scaleDbId": "CO_334:0100526",
                    "name": "ug/g",
                    "dataType": "Numeric",
                    "decimalPlaces": 2,
                    "xref": null,
                    "validValues": {
                        "min": 1,
                        "max": 3,
                        "categories": ["1=low", "2=medium", "3=high"]
                    }
                },
                "defaultValue": null
            }
        }
