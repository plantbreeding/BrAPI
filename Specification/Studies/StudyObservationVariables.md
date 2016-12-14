## Study Observation Variables [/brapi/v1/studies/{studyDbId}/observationVariables]

List all the observation variables measured in the study.

Refer to the data type definition of variables in `/Specification/ObservationVariables/README.md`.

### Retrieve study observation variables [GET]

+ Parameters
    + studyDbId (required, string, `ST012`) ... string database unique identifier

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
                "studyDbId": "123",
                "trialName": "myBestTrial",
                "data": [
                  {
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
                  }
                ]
            }
        }
