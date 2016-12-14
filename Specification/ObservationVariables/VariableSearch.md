## Variable search [/brapi/v1/variables-search]
Scope: CORE.
Status: ACCEPTED.

Search observation variables.

### Variable search [POST]

+ Request (application/json)

        {
            "page": 0,
            "pageSize": 2,
            "observationVariableDbIds" : ["obs-variable-id1", "obs-variable-id1"],
            "ontologyXrefs" : ["CO:123", "CO:456"],
            "ontologyDbIds" : ["CO_334:0100632"],
            "methodDbIds" : ["method-1", "method=2"],
            "scaleDbIds" : ["scale-1", "scale-2"],
            "names" : ["caro_spectro"],
            "datatypes" : ["numeric"],
            "traitClasses" : ["Phenological", "Physiological"]
        }

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 2,
                    "currentPage": 0,
                    "totalCount": 300,
                    "totalPages": 100
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": [{
                    "observationVariableDbId": "CO_334:0100632",
                    "name": "CT_M_C",
                    "ontologyDbId": "CO_334",
                    "ontologyName": "Cassava",
                    "trait": {
                        "traiDbId": "CO_334:0100630",
                        "name": "Canopy temperature"
                    },
                    "method": null,
                    "scale": null,
                    "defaultValue": null
                }, {
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
                  "date": "2016-05-13",
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
                      "datatype": "Numeric",
                      "decimalPlaces": 2,
                      "xref": null,
                      "validValues": {
                          "min": 1,
                          "max": 3,
                          "categories": ["1=low", "2=medium", "3=high"]
                      }
                  },
                  "defaultValue": null
                }]
            }
        }
