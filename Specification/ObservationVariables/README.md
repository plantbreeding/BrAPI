# Group Observation Variables

Implemented by: GnpIS

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.




## Variables/datatypes [Get /brapi/v1/variables/datatypes{?pageSize}{?page}]

Call to retrieve a list of data types the variable can have. 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            "Numeric",
            "Categorical",
            "Date",
            "Text",
            "Picture",
            "Boolean"
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 6,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

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
    "result": {
        "data": [
            {
                "version": "v1.2",
                "licence": "CC BY-SA 4.0",
                "ontologyDbId": "CO_334",
                "authors": "J. Snow, H. Peterson",
                "copyright": "2016, INRA",
                "ontologyName": "Wheat ontology",
                "description": "developped for European genetic studies projects"
            },
            {
                "version": "v2",
                "licence": "CC BY-SA 4.0",
                "ontologyDbId": "CO_335",
                "authors": "J. Doe",
                "copyright": "2017, IRRI",
                "ontologyName": "Rice ontology",
                "description": "developped for IRRI and amended with partners needs"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
    "result": {
        "data": [
            {
                "defaultValue": null,
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "dataType": "Numeric",
                    "decimalPlaces": 2,
                    "xref": null,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    }
                },
                "ontologyName": "Cassava",
                "name": "CT_M_C",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "class": "Estimation"
                },
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630",
                    "class": "physiological trait"
                }
            },
            {
                "growthStage": "mature",
                "defaultValue": null,
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "ontologyDbId": "CO_334",
                "xref": "TL_455:0003001",
                "ontologyName": "Cassava",
                "submissionTimestamp": "2016-05-13T17:43:11+01:00",
                "scientist": "",
                "institution": "",
                "language": "EN",
                "status": "recommended",
                "crop": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "dataType": "Numeric",
                    "decimalPlaces": 2,
                    "xref": null,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    }
                },
                "name": "caro_spectro",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "reference": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "trait": {
                    "class": "physiological trait",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "attribute": "carotenoid",
                    "xref": "TL_455:0003023",
                    "mainAbbreviation": "CC",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "entity": "root",
                    "status": "recommended",
                    "alternativeAbbreviations": [
                        "CCS"
                    ]
                }
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
    "result": {
        "growthStage": "mature",
        "defaultValue": null,
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "synonyms": [
            "Carotenoid content by spectro"
        ],
        "ontologyDbId": "CO_334",
        "xref": "TL_455:0003001",
        "ontologyName": "Cassava",
        "submissionTimestamp": "2016-05-13T15:43:41+01:00",
        "scientist": "",
        "institution": "",
        "language": "EN",
        "status": "recommended",
        "crop": "Cassava",
        "observationVariableDbId": "CO_334:0100632",
        "scale": {
            "name": "ug/g",
            "scaleDbId": "CO_334:0100526",
            "dataType": "Numeric",
            "decimalPlaces": 2,
            "xref": null,
            "validValues": {
                "categories": [
                    "1=low",
                    "2=medium",
                    "3=high"
                ],
                "max": 3,
                "min": 1
            }
        },
        "name": "caro_spectro",
        "method": {
            "name": "Visual Rating:total carotenoid by chart_method",
            "methodDbId": "CO_334:0010320",
            "formula": null,
            "reference": null,
            "class": "Estimation",
            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
        },
        "trait": {
            "class": "physiological trait",
            "synonyms": [
                "carotenoid content measure"
            ],
            "attribute": "carotenoid",
            "xref": "TL_455:0003023",
            "mainAbbreviation": "CC",
            "description": "Cassava storage root pulp carotenoid content",
            "name": "Carotenoid content",
            "traitDbId": "CO_334:0100620",
            "entity": "root",
            "status": "recommended",
            "alternativeAbbreviations": [
                "CCS"
            ]
        }
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
    "result": {
        "data": [
            {
                "defaultValue": null,
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": null,
                "ontologyName": "Cassava",
                "name": "CT_M_C",
                "method": null,
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                }
            },
            {
                "growthStage": "mature",
                "defaultValue": null,
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "ontologyDbId": "CO_334",
                "xref": "TL_455:0003001",
                "ontologyName": "Cassava",
                "submissionTimestamp": "2016-05-13T23:21:56+01:00",
                "scientist": "",
                "institution": "",
                "language": "EN",
                "status": "recommended",
                "crop": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "dataType": "Numeric",
                    "decimalPlaces": 2,
                    "xref": null,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    }
                },
                "name": "caro_spectro",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "reference": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "trait": {
                    "class": "physiological trait",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "attribute": "carotenoid",
                    "xref": "TL_455:0003023",
                    "mainAbbreviation": "CC",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "entity": "root",
                    "status": "recommended",
                    "alternativeAbbreviations": [
                        "CCS"
                    ]
                }
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 300,
            "pageSize": 2,
            "totalPages": 150
        }
    }
}
```