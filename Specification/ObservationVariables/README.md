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
    "result": {
        "data": [
            {
                "licence": "CC BY-SA 4.0",
                "ontologyDbId": "CO_334",
                "ontologyName": "Wheat ontology",
                "version": "v1.2",
                "authors": "J. Snow, H. Peterson",
                "copyright": "2016, INRA",
                "description": "developped for European genetic studies projects"
            },
            {
                "licence": "CC BY-SA 4.0",
                "ontologyDbId": "CO_335",
                "ontologyName": "Rice ontology",
                "version": "v2",
                "authors": "J. Doe",
                "copyright": "2017, IRRI",
                "description": "developped for IRRI and amended with partners needs"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
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
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                },
                "defaultValue": null,
                "ontologyName": "Cassava",
                "method": null,
                "scale": null
            },
            {
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "name": "caro_spectro",
                "trait": {
                    "mainAbbreviation": "CC",
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620",
                    "class": "physiological trait",
                    "entity": "root",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content"
                },
                "ontologyName": "Cassava",
                "scientist": "",
                "scale": {
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "xref": null,
                    "decimalPlaces": 2,
                    "name": "ug/g",
                    "dataType": "Numeric",
                    "scaleDbId": "CO_334:0100526"
                },
                "observationVariableDbId": "CO_334:0100622",
                "crop": "Cassava",
                "ontologyDbId": "CO_334",
                "status": "recommended",
                "language": "EN",
                "institution": "",
                "submissionTimestamp": "2016-05-13T23:21:56+01:00",
                "growthStage": "mature",
                "defaultValue": null,
                "xref": "TL_455:0003001",
                "method": {
                    "reference": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "synonyms": [
                    "Carotenoid content by spectro"
                ]
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 2,
            "currentPage": 0,
            "totalPages": 150,
            "totalCount": 300
        },
        "status": [],
        "datafiles": []
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
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 6
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
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630",
                    "class": "physiological trait"
                },
                "defaultValue": null,
                "ontologyName": "Cassava",
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation"
                },
                "scale": {
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "xref": null,
                    "decimalPlaces": 2,
                    "name": "ug/g",
                    "dataType": "Numeric",
                    "scaleDbId": "CO_334:0100526"
                }
            },
            {
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "name": "caro_spectro",
                "trait": {
                    "mainAbbreviation": "CC",
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620",
                    "class": "physiological trait",
                    "entity": "root",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content"
                },
                "ontologyName": "Cassava",
                "scientist": "",
                "scale": {
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "xref": null,
                    "decimalPlaces": 2,
                    "name": "ug/g",
                    "dataType": "Numeric",
                    "scaleDbId": "CO_334:0100526"
                },
                "observationVariableDbId": "CO_334:0100622",
                "crop": "Cassava",
                "ontologyDbId": "CO_334",
                "status": "recommended",
                "language": "EN",
                "institution": "",
                "submissionTimestamp": "2016-05-13T17:43:11+01:00",
                "growthStage": "mature",
                "defaultValue": null,
                "xref": "TL_455:0003001",
                "method": {
                    "reference": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "synonyms": [
                    "Carotenoid content by spectro"
                ]
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
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
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "name": "caro_spectro",
        "trait": {
            "mainAbbreviation": "CC",
            "name": "Carotenoid content",
            "status": "recommended",
            "attribute": "carotenoid",
            "traitDbId": "CO_334:0100620",
            "class": "physiological trait",
            "entity": "root",
            "alternativeAbbreviations": [
                "CCS"
            ],
            "xref": "TL_455:0003023",
            "synonyms": [
                "carotenoid content measure"
            ],
            "description": "Cassava storage root pulp carotenoid content"
        },
        "ontologyName": "Cassava",
        "scientist": "",
        "scale": {
            "validValues": {
                "min": 1,
                "categories": [
                    "1=low",
                    "2=medium",
                    "3=high"
                ],
                "max": 3
            },
            "xref": null,
            "decimalPlaces": 2,
            "name": "ug/g",
            "dataType": "Numeric",
            "scaleDbId": "CO_334:0100526"
        },
        "observationVariableDbId": "CO_334:0100632",
        "crop": "Cassava",
        "ontologyDbId": "CO_334",
        "status": "recommended",
        "language": "EN",
        "institution": "",
        "submissionTimestamp": "2016-05-13T15:43:41+01:00",
        "growthStage": "mature",
        "defaultValue": null,
        "xref": "TL_455:0003001",
        "method": {
            "reference": null,
            "name": "Visual Rating:total carotenoid by chart_method",
            "methodDbId": "CO_334:0010320",
            "formula": null,
            "class": "Estimation",
            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
        },
        "synonyms": [
            "Carotenoid content by spectro"
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [],
        "datafiles": []
    }
}
```