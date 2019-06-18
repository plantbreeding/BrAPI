# Group Germplasm Attributes
Germplasm "attributes" are simply-inherited characteristics (characterization descriptors) that are not environment-dependent but 
inherent in the germplasm line.  They include genes, QTLs, and genetic "traits" like wheat grain 
hardness.  They are often evaluated by genotyping for diagnostic markers.





## Attributes [/brapi/v1/attributes] 




### Get Attributes Categories  [GET /brapi/v1/attributes/categories{?page}{?pageSize}]

List all available attribute categories.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|attributeCategoryDbId|string|The ID which uniquely identifies this attribute category within the given database server|
|attributeCategoryName|string|A human readable name for this attribute category. Very similar to Trait class. (examples: "morphologic", "phenologic", "agronomic", "physiologic", "abiotic stress", "biotic stress", "biochemic", "quality traits", "fertility", etc.)|


 

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
            "totalPages": 1
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array||
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|crop|string|Crop name (examples: "Maize", "Wheat")|
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|institution|string|Name of institution submitting the variable|
|language|string|2 letter ISO code for the language of submission of the variable.|
|method|object|Method metadata|
|class|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.|
|description|string|Method description.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scale|object|Scale metadata|
|dataType|string|Class of the scale, entries can be     "Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal             scale that combines the expressions of the different traits composing the complex             trait. For exemple a severity trait might be expressed by a 2 digit and 2 character             code. The first 2 digits are the percentage of the plant covered by a fungus and the 2             characters refer to the delay in development, e.g. "75VD" means "75%" of the plant is              Crop Ontology & Integrated Breeding Platform  Curation Guidelines  5/6/2016 9             infected and the plant is very delayed.      "Date" - The date class is for events expressed in a time format, e.g. yyyymmddThh:mm:ssZ or dd/mm/yy      "Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months      "Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories      "Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectar, branches      "Ordinal" - Ordinal scales are scales composed of ordered categories      "Text" - A free text is used to express the trait.   |
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|scaleName|string|Name of the scale|
|validValues|object||
|categories|array[string]|List of possible values and their meaning (examples: ["0=low", "1=medium", "2=high"]|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|scientist|string|Name of scientist submitting the variable.|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|synonyms|array[string]|Other variable names|
|trait|object||
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|class|string|Trait class. (examples: "morphological trait", "phenological trait", "agronomical trait", "physiological trait", "abiotic stress trait", "biotic stress trait", "biochemical trait", "quality traits trait", "fertility trait", etc.)|
|description|string|The description of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|synonyms|array[string]|Other trait names|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitName|string|The human readable name of a trait|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|attributeCategoryDbId|string|General category for the attribute. very similar to Trait class.|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|description|string|A human readable description of this attribute|


 

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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/m1",
                                "type": "RDF",
                                "url": "https://ontology.org/m1"
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
                "ontologyReference": {
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/s1",
                                "type": "OBO",
                                "url": "https://ontology.org/s1"
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/t1",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org/t1"
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/m3",
                                "type": "OBO",
                                "url": "https://ontology.org/m3"
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
                "ontologyReference": {
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/s3",
                                "type": "WEBPAGE",
                                "url": "https://ontology.org/s3"
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "https://ontology.org/t3",
                                "type": "RDF",
                                "url": "https://ontology.org/t3"
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

