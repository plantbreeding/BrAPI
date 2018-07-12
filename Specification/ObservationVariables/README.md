# Group Observation Variables

Implemented by: GnpIS

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.




## Get Ontologies  [GET /brapi/v1/ontologies{?pageSize}{?page}]

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
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "authors": "J. Snow, H. Peterson",
                "copyright": "2016, INRA",
                "description": "developped for European genetic studies projects",
                "licence": "CC BY-SA 4.0",
                "ontologyDbId": "CO_334",
                "ontologyName": "Wheat ontology",
                "version": "v1.2"
            },
            {
                "authors": "J. Doe",
                "copyright": "2017, IRRI",
                "description": "developped for IRRI and amended with partners needs",
                "licence": "CC BY-SA 4.0",
                "ontologyDbId": "CO_335",
                "ontologyName": "Rice ontology",
                "version": "v2"
            }
        ]
    }
}
```



## Post Variables-search  [POST /brapi/v1/variables-search]

Search observation variables.
See <a href="https://brapi.docs.apiary.io/#introduction/search-services">Search Services</a> for additional implementation details. <br>
<strong>Scope:</strong> CORE.
<strong>Status:</strong> ACCEPTED. 

+ Parameters
 
+ Request (application/json)
```
/definitions/observationVariableSearchRequest
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 300,
            "totalPages": 150
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "defaultValue": null,
                "method": null,
                "name": "CT_M_C",
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": null,
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                }
            },
            {
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "Cassava",
                "defaultValue": null,
                "growthStage": "mature",
                "institution": "",
                "language": "EN",
                "method": {
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null
                },
                "name": "caro_spectro",
                "observationVariableDbId": "CO_334:0100622",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": {
                    "dataType": "Numeric",
                    "decimalPlaces": 2,
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "xref": null
                },
                "scientist": "",
                "status": "recommended",
                "submissionTimestamp": "2016-05-13T23:21:56+01:00",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "class": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "entity": "root",
                    "mainAbbreviation": "CC",
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "traitDbId": "CO_334:0100620",
                    "xref": "TL_455:0003023"
                },
                "xref": "TL_455:0003001"
            }
        ]
    }
}
```



## Get Variables Datatypes  [GET /brapi/v1/variables/datatypes{?pageSize}{?page}]

Call to retrieve a list of data types the variable can have. 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 6,
            "totalPages": 1
        },
        "status": []
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



## Get Variables  [GET /brapi/v1/variables{?pageSize}{?page}{?traitClass}]

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
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "defaultValue": null,
                "method": {
                    "class": "Estimation",
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method"
                },
                "name": "CT_M_C",
                "observationVariableDbId": "CO_334:0100632",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": {
                    "dataType": "Numeric",
                    "decimalPlaces": 2,
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "xref": null
                },
                "trait": {
                    "class": "physiological trait",
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                }
            },
            {
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "Cassava",
                "defaultValue": null,
                "growthStage": "mature",
                "institution": "",
                "language": "EN",
                "method": {
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null
                },
                "name": "caro_spectro",
                "observationVariableDbId": "CO_334:0100622",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "scale": {
                    "dataType": "Numeric",
                    "decimalPlaces": 2,
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "xref": null
                },
                "scientist": "",
                "status": "recommended",
                "submissionTimestamp": "2016-05-13T17:43:11+01:00",
                "synonyms": [
                    "Carotenoid content by spectro"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "class": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "entity": "root",
                    "mainAbbreviation": "CC",
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "traitDbId": "CO_334:0100620",
                    "xref": "TL_455:0003023"
                },
                "xref": "TL_455:0003001"
            }
        ]
    }
}
```



## Get Variables by observationVariableDbId  [GET /brapi/v1/variables/{observationVariableDbId}]

Retrieve variable details <br>
<strong>Scope:</strong> CORE
<strong>Status:</strong> ACCEPTED 

+ Parameters
    + observationVariableDbId (Required, string) ... string id of the variable


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "crop": "Cassava",
        "defaultValue": null,
        "growthStage": "mature",
        "institution": "",
        "language": "EN",
        "method": {
            "class": "Estimation",
            "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
            "formula": null,
            "methodDbId": "CO_334:0010320",
            "name": "Visual Rating:total carotenoid by chart_method",
            "reference": null
        },
        "name": "caro_spectro",
        "observationVariableDbId": "CO_334:0100632",
        "ontologyDbId": "CO_334",
        "ontologyName": "Cassava",
        "scale": {
            "dataType": "Numeric",
            "decimalPlaces": 2,
            "name": "ug/g",
            "scaleDbId": "CO_334:0100526",
            "validValues": {
                "categories": [
                    "1=low",
                    "2=medium",
                    "3=high"
                ],
                "max": 3,
                "min": 1
            },
            "xref": null
        },
        "scientist": "",
        "status": "recommended",
        "submissionTimestamp": "2016-05-13T15:43:41+01:00",
        "synonyms": [
            "Carotenoid content by spectro"
        ],
        "trait": {
            "alternativeAbbreviations": [
                "CCS"
            ],
            "attribute": "carotenoid",
            "class": "physiological trait",
            "description": "Cassava storage root pulp carotenoid content",
            "entity": "root",
            "mainAbbreviation": "CC",
            "name": "Carotenoid content",
            "status": "recommended",
            "synonyms": [
                "carotenoid content measure"
            ],
            "traitDbId": "CO_334:0100620",
            "xref": "TL_455:0003023"
        },
        "xref": "TL_455:0003001"
    }
}
```

