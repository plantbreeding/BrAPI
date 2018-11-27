# Group Germplasm Attributes
Germplasm "attributes" are simply-inherited characteristics (characterization descriptors) that are not environment-dependent but 
inherent in the germplasm line.  They include genes, QTLs, and genetic "traits" like wheat grain 
hardness.  They are often evaluated by genotyping for diagnostic markers.





## Attributes [/brapi/v1/attributes] 




### Get Attributes Categories  [GET /brapi/v1/attributes/categories{?page}{?pageSize}]

List all available attribute categories.

 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCategoryDbId": "1",
                "attributeCategoryName": "Morphological",
                "name": "Morphological"
            },
            {
                "attributeCategoryDbId": "2",
                "attributeCategoryName": "Agronomic",
                "name": "Agronomic"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Attributes  [GET /brapi/v1/attributes{?attributeCategoryDbId}{?page}{?pageSize}]

List available attributes.

 

+ Parameters
    + attributeCategoryDbId (Optional, ) ... Unique identifier for the general category for the attribute. very similar to Trait class.
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 5,
            "totalPages": 3
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCategoryDbId": "2",
                "attributeDbId": "ATT01",
                "attributeName": "Rht-B1b",
                "code": "RHT",
                "contextOfUse": [],
                "crop": "maize",
                "datatype": "Categorical",
                "defaultValue": "10",
                "description": "Allele of marker 11_4769",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Standard rolled measuring tape",
                    "formula": "a^2 + b^2 = c^2",
                    "methodDbId": "m1",
                    "methodName": "Tape Measure",
                    "name": "Tape Measure",
                    "ontologyRefernce": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "google.com"
                },
                "name": "Rht-B1b",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 1,
                    "name": "Centimeter",
                    "ontologyRefernce": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s1",
                    "scaleName": "Centimeter",
                    "validValues": {
                        "categories": [],
                        "max": 99999,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "plant height",
                    "class": "Numeric",
                    "description": "plant height",
                    "entity": "entity",
                    "mainAbbreviation": "H",
                    "name": "Plant Height",
                    "ontologyRefernce": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t1",
                    "traitName": "Plant Height",
                    "xref": "xref"
                },
                "uri": "http://www.brapi.org/ontology/MO_123:1000001",
                "values": "Present",
                "xref": "MO_123:100002"
            },
            {
                "attributeCategoryDbId": "3",
                "attributeDbId": "ATT02",
                "attributeName": "Weevil Resistance",
                "code": "WEV",
                "contextOfUse": [],
                "crop": "maize",
                "datatype": "Categorical",
                "defaultValue": "10",
                "description": "Resistance allele",
                "documentationURL": "https://brapi.org",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": "Standard Color Palette",
                    "name": "Standard Color Palette",
                    "ontologyRefernce": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "reference": "google.com"
                },
                "name": "Weevil Resistance",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scale": {
                    "dataType": "Nominal",
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyRefernce": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "scaleDbId": "s3",
                    "scaleName": "Color",
                    "validValues": {
                        "categories": [
                            "dark red",
                            "red",
                            "dark blue",
                            "blue",
                            "black"
                        ],
                        "max": 0,
                        "min": 0
                    },
                    "xref": "xref"
                },
                "scientist": "Bob",
                "status": "active",
                "submissionTimestamp": "2011-06-14T22:12:51-04:00",
                "synonyms": [],
                "trait": {
                    "alternativeAbbreviations": [],
                    "attribute": "leaf color",
                    "class": "Categorical",
                    "description": "color of leaf sample",
                    "entity": "entity",
                    "mainAbbreviation": "LC",
                    "name": "Leaf Color",
                    "ontologyRefernce": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org"
                            }
                        ],
                        "ontologyDbId": "MO_123",
                        "ontologyName": "Ontology.org",
                        "version": "17"
                    },
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t3",
                    "traitName": "Leaf Color",
                    "xref": "xref"
                },
                "uri": "http://www.brapi.org/ontology/MO_123:1000002",
                "values": "Absent",
                "xref": "MO_123:100003"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

