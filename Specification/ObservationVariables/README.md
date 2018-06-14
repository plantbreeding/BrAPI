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
        "pagination": {
            "currentPage": 0,
            "totalCount": 6,
            "pageSize": 1000,
            "totalPages": 1
        },
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
                "ontologyName": "Wheat ontology",
                "licence": "CC BY-SA 4.0",
                "copyright": "2016, INRA",
                "version": "v1.2",
                "authors": "J. Snow, H. Peterson",
                "ontologyDbId": "CO_334",
                "description": "developped for European genetic studies projects"
            },
            {
                "ontologyName": "Rice ontology",
                "licence": "CC BY-SA 4.0",
                "copyright": "2017, IRRI",
                "version": "v2",
                "authors": "J. Doe",
                "ontologyDbId": "CO_335",
                "description": "developped for IRRI and amended with partners needs"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
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
                "scale": {
                    "scaleDbId": "CO_334:0100526",
                    "xref": null,
                    "name": "ug/g",
                    "decimalPlaces": 2,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "dataType": "Numeric"
                },
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100632",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630",
                    "class": "physiological trait"
                },
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320"
                },
                "defaultValue": null
            },
            {
                "crop": "Cassava",
                "submissionTimestamp": "2016-05-13T17:43:11+01:00",
                "language": "EN",
                "status": "recommended",
                "name": "caro_spectro",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "scientist": "",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "institution": "",
                "scale": {
                    "scaleDbId": "CO_334:0100526",
                    "xref": null,
                    "name": "ug/g",
                    "decimalPlaces": 2,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "dataType": "Numeric"
                },
                "growthStage": "mature",
                "ontologyName": "Cassava",
                "xref": "TL_455:0003001",
                "observationVariableDbId": "CO_334:0100622",
                "trait": {
                    "class": "physiological trait",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "entity": "root",
                    "description": "Cassava storage root pulp carotenoid content",
                    "xref": "TL_455:0003023",
                    "status": "recommended",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "ontologyDbId": "CO_334",
                "method": {
                    "reference": null,
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null
                },
                "defaultValue": null
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        },
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
        "crop": "Cassava",
        "submissionTimestamp": "2016-05-13T15:43:41+01:00",
        "language": "EN",
        "status": "recommended",
        "name": "caro_spectro",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "scientist": "",
        "synonyms": [
            "Carotenoid content by spectro"
        ],
        "institution": "",
        "scale": {
            "scaleDbId": "CO_334:0100526",
            "xref": null,
            "name": "ug/g",
            "decimalPlaces": 2,
            "validValues": {
                "min": 1,
                "categories": [
                    "1=low",
                    "2=medium",
                    "3=high"
                ],
                "max": 3
            },
            "dataType": "Numeric"
        },
        "growthStage": "mature",
        "ontologyName": "Cassava",
        "xref": "TL_455:0003001",
        "observationVariableDbId": "CO_334:0100632",
        "trait": {
            "class": "physiological trait",
            "alternativeAbbreviations": [
                "CCS"
            ],
            "synonyms": [
                "carotenoid content measure"
            ],
            "entity": "root",
            "description": "Cassava storage root pulp carotenoid content",
            "xref": "TL_455:0003023",
            "status": "recommended",
            "name": "Carotenoid content",
            "mainAbbreviation": "CC",
            "attribute": "carotenoid",
            "traitDbId": "CO_334:0100620"
        },
        "ontologyDbId": "CO_334",
        "method": {
            "reference": null,
            "class": "Estimation",
            "methodDbId": "CO_334:0010320",
            "name": "Visual Rating:total carotenoid by chart_method",
            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
            "formula": null
        },
        "defaultValue": null
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        },
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
                "scale": null,
                "ontologyName": "Cassava",
                "observationVariableDbId": "CO_334:0100632",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                },
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "method": null,
                "defaultValue": null
            },
            {
                "crop": "Cassava",
                "submissionTimestamp": "2016-05-13T23:21:56+01:00",
                "language": "EN",
                "status": "recommended",
                "name": "caro_spectro",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "scientist": "",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "institution": "",
                "scale": {
                    "scaleDbId": "CO_334:0100526",
                    "xref": null,
                    "name": "ug/g",
                    "decimalPlaces": 2,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "dataType": "Numeric"
                },
                "growthStage": "mature",
                "ontologyName": "Cassava",
                "xref": "TL_455:0003001",
                "observationVariableDbId": "CO_334:0100622",
                "trait": {
                    "class": "physiological trait",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "entity": "root",
                    "description": "Cassava storage root pulp carotenoid content",
                    "xref": "TL_455:0003023",
                    "status": "recommended",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "attribute": "carotenoid",
                    "traitDbId": "CO_334:0100620"
                },
                "ontologyDbId": "CO_334",
                "method": {
                    "reference": null,
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null
                },
                "defaultValue": null
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 300,
            "pageSize": 2,
            "totalPages": 150
        },
        "status": []
    }
}
```