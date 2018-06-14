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
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 6
        },
        "datafiles": [],
        "status": []
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
                "ontologyDbId": "CO_334",
                "ontologyName": "Wheat ontology",
                "description": "developped for European genetic studies projects",
                "licence": "CC BY-SA 4.0",
                "version": "v1.2",
                "authors": "J. Snow, H. Peterson",
                "copyright": "2016, INRA"
            },
            {
                "ontologyDbId": "CO_335",
                "ontologyName": "Rice ontology",
                "description": "developped for IRRI and amended with partners needs",
                "licence": "CC BY-SA 4.0",
                "version": "v2",
                "authors": "J. Doe",
                "copyright": "2017, IRRI"
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
        "datafiles": [],
        "status": []
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
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": {
                    "validValues": {
                        "min": 1,
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "decimalPlaces": 2,
                    "dataType": "Numeric",
                    "name": "ug/g",
                    "xref": null,
                    "scaleDbId": "CO_334:0100526"
                },
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "method": {
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method"
                },
                "defaultValue": null,
                "trait": {
                    "class": "physiological trait",
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                }
            },
            {
                "submissionTimestamp": "2016-05-13T17:43:11+01:00",
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "defaultValue": null,
                "status": "recommended",
                "language": "EN",
                "trait": {
                    "class": "physiological trait",
                    "entity": "root",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "scientist": "",
                "ontologyDbId": "CO_334",
                "scale": {
                    "validValues": {
                        "min": 1,
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "decimalPlaces": 2,
                    "dataType": "Numeric",
                    "name": "ug/g",
                    "xref": null,
                    "scaleDbId": "CO_334:0100526"
                },
                "name": "caro_spectro",
                "method": {
                    "class": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "institution": "",
                "xref": "TL_455:0003001",
                "crop": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature"
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
        "datafiles": [],
        "status": []
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
        "submissionTimestamp": "2016-05-13T15:43:41+01:00",
        "ontologyName": "Cassava",
        "observationVariableDbId": "CO_334:0100632",
        "defaultValue": null,
        "status": "recommended",
        "language": "EN",
        "trait": {
            "class": "physiological trait",
            "entity": "root",
            "name": "Carotenoid content",
            "mainAbbreviation": "CC",
            "status": "recommended",
            "xref": "TL_455:0003023",
            "synonyms": [
                "carotenoid content measure"
            ],
            "description": "Cassava storage root pulp carotenoid content",
            "alternativeAbbreviations": [
                "CCS"
            ],
            "attribute": "carotenoid",
            "traitDbId": "CO_334:0100620"
        },
        "scientist": "",
        "ontologyDbId": "CO_334",
        "scale": {
            "validValues": {
                "min": 1,
                "max": 3,
                "categories": [
                    "1=low",
                    "2=medium",
                    "3=high"
                ]
            },
            "decimalPlaces": 2,
            "dataType": "Numeric",
            "name": "ug/g",
            "xref": null,
            "scaleDbId": "CO_334:0100526"
        },
        "name": "caro_spectro",
        "method": {
            "class": "Estimation",
            "reference": null,
            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
            "formula": null,
            "name": "Visual Rating:total carotenoid by chart_method",
            "methodDbId": "CO_334:0010320"
        },
        "institution": "",
        "xref": "TL_455:0003001",
        "crop": "Cassava",
        "synonyms": [
            "Carotenoid content by spectro"
        ],
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "growthStage": "mature"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
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
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": null,
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "method": null,
                "defaultValue": null,
                "trait": {
                    "traitDbId": "CO_334:0100630",
                    "name": "Canopy temperature"
                }
            },
            {
                "submissionTimestamp": "2016-05-13T23:21:56+01:00",
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100622",
                "defaultValue": null,
                "status": "recommended",
                "language": "EN",
                "trait": {
                    "class": "physiological trait",
                    "entity": "root",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "scientist": "",
                "ontologyDbId": "CO_334",
                "scale": {
                    "validValues": {
                        "min": 1,
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "decimalPlaces": 2,
                    "dataType": "Numeric",
                    "name": "ug/g",
                    "xref": null,
                    "scaleDbId": "CO_334:0100526"
                },
                "name": "caro_spectro",
                "method": {
                    "class": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "institution": "",
                "xref": "TL_455:0003001",
                "crop": "Cassava",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature"
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
        "datafiles": [],
        "status": []
    }
}
```