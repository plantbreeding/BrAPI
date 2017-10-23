## Variable list [/brapi/v1/variables?page={page}&pageSize={pageSize}&traitClass={traitClass}]
Scope: CORE.
Status: ACCEPTED.

Call to retrieve a list of observationVariables available in the system.

### Variable list [GET]

+ Parameters
    + pageSize (optional, integer, `100`)
    + page (optional, integer, `0`)
    + traitClass (optional, string, `Phenological`) ... Variable's trait class (phenological, physiological, morphological, etc.)

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
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
                  "submissionTimestamp": "2016-05-13T17:43:11+0100",
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
