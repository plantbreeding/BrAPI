# Group Observation Variables

Implemented by: GnpIS

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.




## Ontologies [Get /brapi/v1/ontologies{?pageSize}{?page}]

Call to retrieve a list of observation variable ontologies available in the system. <br>
<strong>Scope:</strong> CORE. 
<strong>Status:</strong> ACCEPTED. 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
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
        "data": [
            {
                "ontologyDbId": "CO_334",
                "ontologyName": "Wheat ontology",
                "authors": "J. Snow, H. Peterson",
                "version": "v1.2",
                "description": "developped for European genetic studies projects",
                "copyright": "2016, INRA",
                "licence": "CC BY-SA 4.0"
            },
            {
                "ontologyDbId": "CO_335",
                "ontologyName": "Rice ontology",
                "authors": "J. Doe",
                "description": "developped for IRRI and amended with partners needs",
                "version": "v2",
                "copyright": "2017, IRRI",
                "licence": "CC BY-SA 4.0"
            }
        ]
    }
}
```

## Variables-search [Post /brapi/v1/variables-search]

Search observation variables.
See <a href="https://brapi.docs.apiary.io/#introduction/search-services">Search Services</a> for additional implementation details. <br>
<strong>Scope:</strong> CORE.
<strong>Status:</strong> ACCEPTED. 

+ Parameters
 
+ Request (application/json)
/definitions/observationVariableSearchRequest

+ Response 200 (application/json)
```
{
    "metadata": {
        "pagination": {
            "pageSize": 2,
            "currentPage": 0,
            "totalCount": 300,
            "totalPages": 150
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                },
                "method": null,
                "scale": null,
                "defaultValue": null
            },
            {
                "observationVariableDbId": "CO_334:0100622",
                "name": "caro_spectro",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature",
                "status": "recommended",
                "xref": "TL_455:0003001",
                "institution": "",
                "scientist": "",
                "submissionTimestamp": "2016-05-13T23:21:56+01:00",
                "language": "EN",
                "crop": "Cassava",
                "trait": {
                    "traitDbId": "CO_334:0100620",
                    "name": "Carotenoid content",
                    "class": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
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
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    }
                },
                "defaultValue": null
            }
        ]
    }
}
```

## Variables/datatypes [Get /brapi/v1/variables/datatypes{?pageSize}{?page}]

Call to retrieve a list of data types the variable can have. 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalCount": 6,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            "Numeric",
            "Categorical",
            "Date",
            "Text",
            "Picture",
            "Boolean"
        ]
    }
}
```

## Variables [Get /brapi/v1/variables{?pageSize}{?page}{?traitClass}]

Call to retrieve a list of observationVariables available in the system. <br>
<strong>Scope:</strong> CORE.
<strong>Status:</strong> ACCEPTED. 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + traitClass (Optional, string) ... Variable's trait class (phenological, physiological, morphological, etc.)


+ Response 200 (application/json)
```
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
        "data": [
            {
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature",
                    "class": "physiological trait"
                },
                "defaultValue": null,
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation"
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
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    }
                }
            },
            {
                "observationVariableDbId": "CO_334:0100622",
                "name": "caro_spectro",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature",
                "status": "recommended",
                "xref": "TL_455:0003001",
                "institution": "",
                "scientist": "",
                "submissionTimestamp": "2016-05-13T17:43:11+01:00",
                "language": "EN",
                "crop": "Cassava",
                "trait": {
                    "traitDbId": "CO_334:0100620",
                    "name": "Carotenoid content",
                    "class": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
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
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    }
                },
                "defaultValue": null
            }
        ]
    }
}
```

## Variables/{observationvariabledbid} [Get /brapi/v1/variables/{observationVariableDbId}]

Retrieve variable details <br>
<strong>Scope:</strong> CORE
<strong>Status:</strong> ACCEPTED 

+ Parameters
    + observationVariableDbId (Required, string) ... string id of the variable


+ Response 200 (application/json)
```
{
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "observationVariableDbId": "CO_334:0100632",
        "name": "caro_spectro",
        "ontologyDbId": "CO_334",
        "ontologyName": "Cassava",
        "synonyms": [
            "Carotenoid content by spectro"
        ],
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "growthStage": "mature",
        "status": "recommended",
        "xref": "TL_455:0003001",
        "institution": "",
        "scientist": "",
        "submissionTimestamp": "2016-05-13T15:43:41+01:00",
        "language": "EN",
        "crop": "Cassava",
        "trait": {
            "traitDbId": "CO_334:0100620",
            "name": "Carotenoid content",
            "class": "physiological trait",
            "description": "Cassava storage root pulp carotenoid content",
            "synonyms": [
                "carotenoid content measure"
            ],
            "mainAbbreviation": "CC",
            "alternativeAbbreviations": [
                "CCS"
            ],
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
                "categories": [
                    "1=low",
                    "2=medium",
                    "3=high"
                ]
            }
        },
        "defaultValue": null
    }
}
```