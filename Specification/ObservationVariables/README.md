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
        "pagination": {
            "currentPage": 0,
            "totalCount": 6,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "ontologyName": "Wheat ontology",
                "authors": "J. Snow, H. Peterson",
                "description": "developped for European genetic studies projects",
                "licence": "CC BY-SA 4.0",
                "version": "v1.2",
                "ontologyDbId": "CO_334",
                "copyright": "2016, INRA"
            },
            {
                "ontologyName": "Rice ontology",
                "authors": "J. Doe",
                "description": "developped for IRRI and amended with partners needs",
                "licence": "CC BY-SA 4.0",
                "version": "v2",
                "ontologyDbId": "CO_335",
                "copyright": "2017, IRRI"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
                "ontologyName": "Cassava",
                "defaultValue": null,
                "name": "CT_M_C",
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature",
                    "class": "physiological trait"
                },
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": {
                    "xref": null,
                    "validValues": {
                        "max": 3,
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "decimalPlaces": 2,
                    "scaleDbId": "CO_334:0100526",
                    "dataType": "Numeric",
                    "name": "ug/g"
                },
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation"
                }
            },
            {
                "scientist": "",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "xref": "TL_455:0003001",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "crop": "Cassava",
                "name": "caro_spectro",
                "scale": {
                    "xref": null,
                    "validValues": {
                        "max": 3,
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "decimalPlaces": 2,
                    "scaleDbId": "CO_334:0100526",
                    "dataType": "Numeric",
                    "name": "ug/g"
                },
                "ontologyName": "Cassava",
                "institution": "",
                "language": "EN",
                "submissionTimestamp": "2016-05-13T17:43:11+01:00",
                "status": "recommended",
                "trait": {
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "attribute": "carotenoid",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "mainAbbreviation": "CC",
                    "class": "physiological trait",
                    "entity": "root"
                },
                "defaultValue": null,
                "observationVariableDbId": "CO_334:0100622",
                "ontologyDbId": "CO_334",
                "growthStage": "mature",
                "method": {
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "reference": null,
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "class": "Estimation",
                    "name": "Visual Rating:total carotenoid by chart_method"
                }
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
        "status": [],
        "datafiles": []
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
        "scientist": "",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "xref": "TL_455:0003001",
        "synonyms": [
            "Carotenoid content by spectro"
        ],
        "crop": "Cassava",
        "name": "caro_spectro",
        "scale": {
            "xref": null,
            "validValues": {
                "max": 3,
                "min": 1,
                "categories": [
                    "1=low",
                    "2=medium",
                    "3=high"
                ]
            },
            "decimalPlaces": 2,
            "scaleDbId": "CO_334:0100526",
            "dataType": "Numeric",
            "name": "ug/g"
        },
        "ontologyName": "Cassava",
        "institution": "",
        "language": "EN",
        "submissionTimestamp": "2016-05-13T15:43:41+01:00",
        "status": "recommended",
        "trait": {
            "xref": "TL_455:0003023",
            "description": "Cassava storage root pulp carotenoid content",
            "traitDbId": "CO_334:0100620",
            "attribute": "carotenoid",
            "synonyms": [
                "carotenoid content measure"
            ],
            "alternativeAbbreviations": [
                "CCS"
            ],
            "name": "Carotenoid content",
            "status": "recommended",
            "mainAbbreviation": "CC",
            "class": "physiological trait",
            "entity": "root"
        },
        "defaultValue": null,
        "observationVariableDbId": "CO_334:0100632",
        "ontologyDbId": "CO_334",
        "growthStage": "mature",
        "method": {
            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
            "reference": null,
            "formula": null,
            "methodDbId": "CO_334:0010320",
            "class": "Estimation",
            "name": "Visual Rating:total carotenoid by chart_method"
        }
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
        "status": [],
        "datafiles": []
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
                "ontologyName": "Cassava",
                "defaultValue": null,
                "name": "CT_M_C",
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                },
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "scale": null,
                "method": null
            },
            {
                "scientist": "",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "xref": "TL_455:0003001",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "crop": "Cassava",
                "name": "caro_spectro",
                "scale": {
                    "xref": null,
                    "validValues": {
                        "max": 3,
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "decimalPlaces": 2,
                    "scaleDbId": "CO_334:0100526",
                    "dataType": "Numeric",
                    "name": "ug/g"
                },
                "ontologyName": "Cassava",
                "institution": "",
                "language": "EN",
                "submissionTimestamp": "2016-05-13T23:21:56+01:00",
                "status": "recommended",
                "trait": {
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitDbId": "CO_334:0100620",
                    "attribute": "carotenoid",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "mainAbbreviation": "CC",
                    "class": "physiological trait",
                    "entity": "root"
                },
                "defaultValue": null,
                "observationVariableDbId": "CO_334:0100622",
                "ontologyDbId": "CO_334",
                "growthStage": "mature",
                "method": {
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "reference": null,
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "class": "Estimation",
                    "name": "Visual Rating:total carotenoid by chart_method"
                }
            }
        ]
    },
    "metadata": {
        "pagination": {
            "currentPage": 0,
            "totalCount": 300,
            "pageSize": 2,
            "totalPages": 150
        },
        "status": [],
        "datafiles": []
    }
}
```