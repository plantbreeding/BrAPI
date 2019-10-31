# Group Observation Variables

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.




## Variables [/brapi/v1/variables] 




### Get Variables  [GET /brapi/v1/variables{?observationVariableDbId}{?traitClass}{?studyDbId}{?page}{?pageSize}]

Call to retrieve a list of observationVariables available in the system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|trait|object||
|traitDescription|string|The description of a trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|traitName|string|The human readable name of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|synonyms|array[string]|Other trait names|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|observationVariableName|string|Variable name (usually a short name)|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|method|object||
|description|string|Method description.|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|additionalInfo|object|Additional arbitrary info|
|institution|string|Name of institution submitting the variable|
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|synonyms|array[string]|Other variable names|
|scientist|string|Name of scientist submitting the variable.|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|scale|object||
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|validValues|object||
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|categories|array[string]|List of possible values (examples: ["low", "medium", "high"]|
|scaleName|string|Name of the scale|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|observationVariableDbId|string|Variable unique identifier|


 

+ Parameters
    + observationVariableDbId (Optional, ) ... Variable's unique ID
    + traitClass (Optional, ) ... Variable's trait class (phenological, physiological, morphological, etc.)
    + studyDbId (Optional, ) ... The unique ID of a studies to filter on
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": 2.0,
                "documentationURL": "https://wiki.brapi.org/documentation.html",
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
                    "additionalInfo": {},
                    "description": "A measuring tape was used",
                    "formula": "a^2 + b^2 = c^2",
                    "methodClass": "Measurement",
                    "methodDbId": "0adb2764",
                    "methodName": "Measuring Tape",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
                },
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scale": {
                    "dataType": [
                        "Code",
                        "Date",
                        "Duration",
                        "Nominal",
                        "Numerical",
                        "Ordinal",
                        "Text"
                    ],
                    "decimalPlaces": 2,
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "validValues": {
                        "categories": [
                            "low",
                            "medium",
                            "high"
                        ],
                        "max": 9999,
                        "min": 2
                    },
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "H",
                        "PH",
                        "H1"
                    ],
                    "attribute": "height",
                    "entity": "Stalk",
                    "mainAbbreviation": "PH",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "status": "recommended",
                    "synonyms": [
                        "Height",
                        "Plant Height",
                        "Stalk Height",
                        "Canopy Height"
                    ],
                    "traitClass": "phenological",
                    "traitDbId": "9b2e34f5",
                    "traitDescription": "The height of the plant",
                    "traitName": "Height",
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Post Variables  [POST /brapi/v1/variables]

Add new Observation Variables to the system.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|trait|object||
|traitDescription|string|The description of a trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|traitName|string|The human readable name of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|synonyms|array[string]|Other trait names|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|observationVariableName|string|Variable name (usually a short name)|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|method|object||
|description|string|Method description.|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|additionalInfo|object|Additional arbitrary info|
|institution|string|Name of institution submitting the variable|
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|synonyms|array[string]|Other variable names|
|scientist|string|Name of scientist submitting the variable.|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|scale|object||
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|validValues|object||
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|categories|array[string]|List of possible values (examples: ["low", "medium", "high"]|
|scaleName|string|Name of the scale|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|trait|object||
|traitDescription|string|The description of a trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|traitName|string|The human readable name of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|synonyms|array[string]|Other trait names|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|observationVariableName|string|Variable name (usually a short name)|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|method|object||
|description|string|Method description.|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|additionalInfo|object|Additional arbitrary info|
|institution|string|Name of institution submitting the variable|
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|synonyms|array[string]|Other variable names|
|scientist|string|Name of scientist submitting the variable.|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|scale|object||
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|validValues|object||
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|categories|array[string]|List of possible values (examples: ["low", "medium", "high"]|
|scaleName|string|Name of the scale|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|observationVariableDbId|string|Variable unique identifier|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": 2.0,
        "documentationURL": "https://wiki.brapi.org/documentation.html",
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
            "additionalInfo": {},
            "description": "A measuring tape was used",
            "formula": "a^2 + b^2 = c^2",
            "methodClass": "Measurement",
            "methodDbId": "0adb2764",
            "methodName": "Measuring Tape",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
        },
        "observationVariableName": "Variable Name",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scale": {
            "dataType": [
                "Code",
                "Date",
                "Duration",
                "Nominal",
                "Numerical",
                "Ordinal",
                "Text"
            ],
            "decimalPlaces": 2,
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "validValues": {
                "categories": [
                    "low",
                    "medium",
                    "high"
                ],
                "max": 9999,
                "min": 2
            },
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
            "alternativeAbbreviations": [
                "H",
                "PH",
                "H1"
            ],
            "attribute": "height",
            "entity": "Stalk",
            "mainAbbreviation": "PH",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "status": "recommended",
            "synonyms": [
                "Height",
                "Plant Height",
                "Stalk Height",
                "Canopy Height"
            ],
            "traitClass": "phenological",
            "traitDbId": "9b2e34f5",
            "traitDescription": "The height of the plant",
            "traitName": "Height",
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
    }
]
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": 2.0,
                "documentationURL": "https://wiki.brapi.org/documentation.html",
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
                    "additionalInfo": {},
                    "description": "A measuring tape was used",
                    "formula": "a^2 + b^2 = c^2",
                    "methodClass": "Measurement",
                    "methodDbId": "0adb2764",
                    "methodName": "Measuring Tape",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
                },
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scale": {
                    "dataType": [
                        "Code",
                        "Date",
                        "Duration",
                        "Nominal",
                        "Numerical",
                        "Ordinal",
                        "Text"
                    ],
                    "decimalPlaces": 2,
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "validValues": {
                        "categories": [
                            "low",
                            "medium",
                            "high"
                        ],
                        "max": 9999,
                        "min": 2
                    },
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "H",
                        "PH",
                        "H1"
                    ],
                    "attribute": "height",
                    "entity": "Stalk",
                    "mainAbbreviation": "PH",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "status": "recommended",
                    "synonyms": [
                        "Height",
                        "Plant Height",
                        "Stalk Height",
                        "Canopy Height"
                    ],
                    "traitClass": "phenological",
                    "traitDbId": "9b2e34f5",
                    "traitDescription": "The height of the plant",
                    "traitName": "Height",
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Variables by observationVariableDbId  [GET /brapi/v1/variables/{observationVariableDbId}]

Retrieve variable details



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|trait|object||
|traitDescription|string|The description of a trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|traitName|string|The human readable name of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|synonyms|array[string]|Other trait names|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|observationVariableName|string|Variable name (usually a short name)|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|method|object||
|description|string|Method description.|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|additionalInfo|object|Additional arbitrary info|
|institution|string|Name of institution submitting the variable|
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|synonyms|array[string]|Other variable names|
|scientist|string|Name of scientist submitting the variable.|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|scale|object||
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|validValues|object||
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|categories|array[string]|List of possible values (examples: ["low", "medium", "high"]|
|scaleName|string|Name of the scale|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|observationVariableDbId|string|Variable unique identifier|


 

+ Parameters
    + observationVariableDbId (Required, ) ... string id of the variable
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "additionalInfo": {},
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": 2.0,
        "documentationURL": "https://wiki.brapi.org/documentation.html",
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
            "additionalInfo": {},
            "description": "A measuring tape was used",
            "formula": "a^2 + b^2 = c^2",
            "methodClass": "Measurement",
            "methodDbId": "0adb2764",
            "methodName": "Measuring Tape",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
        },
        "observationVariableDbId": "b9b7edd1",
        "observationVariableName": "Variable Name",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scale": {
            "dataType": [
                "Code",
                "Date",
                "Duration",
                "Nominal",
                "Numerical",
                "Ordinal",
                "Text"
            ],
            "decimalPlaces": 2,
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "validValues": {
                "categories": [
                    "low",
                    "medium",
                    "high"
                ],
                "max": 9999,
                "min": 2
            },
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
            "alternativeAbbreviations": [
                "H",
                "PH",
                "H1"
            ],
            "attribute": "height",
            "entity": "Stalk",
            "mainAbbreviation": "PH",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "status": "recommended",
            "synonyms": [
                "Height",
                "Plant Height",
                "Stalk Height",
                "Canopy Height"
            ],
            "traitClass": "phenological",
            "traitDbId": "9b2e34f5",
            "traitDescription": "The height of the plant",
            "traitName": "Height",
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Put Variables by observationVariableDbId  [PUT /brapi/v1/variables/{observationVariableDbId}]

Update an existing Observation Variable



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|trait|object||
|traitDescription|string|The description of a trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|traitName|string|The human readable name of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|synonyms|array[string]|Other trait names|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|observationVariableName|string|Variable name (usually a short name)|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|method|object||
|description|string|Method description.|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|additionalInfo|object|Additional arbitrary info|
|institution|string|Name of institution submitting the variable|
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|synonyms|array[string]|Other variable names|
|scientist|string|Name of scientist submitting the variable.|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|scale|object||
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|validValues|object||
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|categories|array[string]|List of possible values (examples: ["low", "medium", "high"]|
|scaleName|string|Name of the scale|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|observationVariableDbId|string|Variable unique identifier|


 

+ Parameters
    + observationVariableDbId (Required, ) ... string id of the variable
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "additionalInfo": {},
        "commonCropName": "Maize",
        "contextOfUse": [
            "Trial evaluation",
            "Nursery evaluation"
        ],
        "defaultValue": 2.0,
        "documentationURL": "https://wiki.brapi.org/documentation.html",
        "growthStage": "flowering",
        "institution": "The BrAPI Institute",
        "language": "en",
        "method": {
            "additionalInfo": {},
            "description": "A measuring tape was used",
            "formula": "a^2 + b^2 = c^2",
            "methodClass": "Measurement",
            "methodDbId": "0adb2764",
            "methodName": "Measuring Tape",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
        },
        "observationVariableDbId": "b9b7edd1",
        "observationVariableName": "Variable Name",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "http://purl.obolibrary.org/obo/ro.owl",
                    "type": [
                        "OBO",
                        "RDF",
                        "WEBPAGE"
                    ]
                }
            ],
            "ontologyDbId": "6b071868",
            "ontologyName": "The Crop Ontology",
            "version": "7.2.3"
        },
        "scale": {
            "dataType": [
                "Code",
                "Date",
                "Duration",
                "Nominal",
                "Numerical",
                "Ordinal",
                "Text"
            ],
            "decimalPlaces": 2,
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "scaleDbId": "af730171",
            "scaleName": "Meters",
            "validValues": {
                "categories": [
                    "low",
                    "medium",
                    "high"
                ],
                "max": 9999,
                "min": 2
            },
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "scientist": "Dr. Bob Robertson",
        "status": "recommended",
        "submissionTimestamp": "2018-01-01T14:47:23-0600",
        "synonyms": [
            "Maize Height",
            "Stalk Height",
            "Corn Height"
        ],
        "trait": {
            "alternativeAbbreviations": [
                "H",
                "PH",
                "H1"
            ],
            "attribute": "height",
            "entity": "Stalk",
            "mainAbbreviation": "PH",
            "ontologyReference": {
                "documentationLinks": [
                    {
                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                        "type": [
                            "OBO",
                            "RDF",
                            "WEBPAGE"
                        ]
                    }
                ],
                "ontologyDbId": "6b071868",
                "ontologyName": "The Crop Ontology",
                "version": "7.2.3"
            },
            "status": "recommended",
            "synonyms": [
                "Height",
                "Plant Height",
                "Stalk Height",
                "Canopy Height"
            ],
            "traitClass": "phenological",
            "traitDbId": "9b2e34f5",
            "traitDescription": "The height of the plant",
            "traitName": "Height",
            "xref": "http://purl.obolibrary.org/obo/ro.owl"
        },
        "xref": "http://purl.obolibrary.org/obo/ro.owl"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```



## Search [/brapi/v1/search] 




### Post Search Variables  [POST /brapi/v1/search/variables]

Search observation variables.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|traitXrefs|array[string]|List of cross references for the trait to search for|
|ontologyDbIds|array[string]|List of ontology IDs to search for|
|traitClasses|array[string]|List of trait classes to filter search results|
|scaleXrefs|array[string]|List of cross references for the scale to search for|
|observationVariableDbIds|array[string]|List of observation variable IDs to search for|
|studyDbId|array[string]|The unique ID of a studies to filter on|
|dataTypes|array[string]|List of scale data types to filter search results|
|methodDbIds|array[string]|List of methods to filter search results|
|traitDbIds|array[string]|List of trait unique ID to filter search results|
|observationVariableXrefs|array[string]|List of cross references for the observation variable to search for|
|scaleDbIds|array[string]|List of scales to filter search results|
|observationVariableNames|array[string]|List of human readable observation variable names to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataTypes": [
        "Numerical",
        "Ordinal",
        "Text"
    ],
    "methodDbIds": [
        "07e34f83",
        "d3d5517a"
    ],
    "observationVariableDbIds": [
        "2ef15c9f",
        "318e7f7d"
    ],
    "observationVariableNames": [
        "Plant Height 1",
        "Root Color"
    ],
    "observationVariableXrefs": [
        " http://purl.obolibrary.org/obo/ro.owl",
        " http://purl.obolibrary.org/obo/ro.owl"
    ],
    "ontologyDbIds": [
        "f44f7b23",
        "a26b576e"
    ],
    "scaleDbIds": [
        "a13ecffa",
        "7e1afe4f"
    ],
    "scaleXrefs": [
        " http://purl.obolibrary.org/obo/ro.owl",
        " http://purl.obolibrary.org/obo/ro.owl"
    ],
    "studyDbId": [
        "5bcac0ae",
        "7f48e22d"
    ],
    "traitClasses": [
        "morphological",
        "phenological",
        "agronomical"
    ],
    "traitDbIds": [
        "ef81147b",
        "78d82fad"
    ],
    "traitXrefs": [
        " http://purl.obolibrary.org/obo/ro.owl",
        " http://purl.obolibrary.org/obo/ro.owl"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "searchResultDbId": "551ae08c"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Search Variables by searchResultsDbId  [GET /brapi/v1/search/variables/{searchResultsDbId}{?page}{?pageSize}]

Search observation variables.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|defaultValue|string|Variable default value. (examples: "red", "2.3", etc.)|
|trait|object||
|traitDescription|string|The description of a trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|status|string|Trait status (examples: "recommended", "obsolete", "legacy", etc.)|
|attribute|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|
|traitName|string|The human readable name of a trait|
|entity|string|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|alternativeAbbreviations|array[string]|Other frequent abbreviations of the trait, if any. These abbreviations do not have to follow a convention|
|synonyms|array[string]|Other trait names|
|mainAbbreviation|string|Main abbreviation for trait name. (examples: "Carotenoid content" => "CC")|
|traitClass|string|Trait class. (examples: "morphological", "phenological", "agronomical", "physiological", "abiotic stress", "biotic stress", "biochemical", "quality traits", "fertility", etc.)|
|observationVariableName|string|Variable name (usually a short name)|
|contextOfUse|array[string]|Indication of how trait is routinely used. (examples: ["Trial evaluation", "Nursery evaluation"])|
|method|object||
|description|string|Method description.|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodDbId|string|Method unique identifier|
|methodName|string|Human readable name for the method|
|methodClass|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|additionalInfo|object|Additional arbitrary info|
|institution|string|Name of institution submitting the variable|
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|synonyms|array[string]|Other variable names|
|scientist|string|Name of scientist submitting the variable.|
|language|string|2 letter ISO 639-1 code for the language of submission of the variable.|
|commonCropName|string|Crop name (examples: "Maize", "Wheat")|
|submissionTimestamp|string (date-time)|Timestamp when the Variable was added (ISO 8601)|
|scale|object||
|scaleDbId|string|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|dataType|string|<p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p>|
|ontologyReference|object||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|documentationLinks|array[object]|links to various ontology documentation|
|type|string||
|URL|string (uri)||
|version|string|Ontology version (no specific format)|
|validValues|object||
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|categories|array[string]|List of possible values (examples: ["low", "medium", "high"]|
|scaleName|string|Name of the scale|
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|growthStage|string|Growth stage at which measurement is made (examples: "flowering")|
|status|string|Variable status. (examples: "recommended", "obsolete", "legacy", etc.)|
|xref|string|Cross reference of the variable term to a term from an external ontology or to a database of a major system.|
|observationVariableDbId|string|Variable unique identifier|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "additionalInfo": {},
                "commonCropName": "Maize",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": 2.0,
                "documentationURL": "https://wiki.brapi.org/documentation.html",
                "growthStage": "flowering",
                "institution": "The BrAPI Institute",
                "language": "en",
                "method": {
                    "additionalInfo": {},
                    "description": "A measuring tape was used",
                    "formula": "a^2 + b^2 = c^2",
                    "methodClass": "Measurement",
                    "methodDbId": "0adb2764",
                    "methodName": "Measuring Tape",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "reference": "Smith, 1893, Really Cool Paper, Popular Journal"
                },
                "observationVariableDbId": "b9b7edd1",
                "observationVariableName": "Variable Name",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "http://purl.obolibrary.org/obo/ro.owl",
                            "type": [
                                "OBO",
                                "RDF",
                                "WEBPAGE"
                            ]
                        }
                    ],
                    "ontologyDbId": "6b071868",
                    "ontologyName": "The Crop Ontology",
                    "version": "7.2.3"
                },
                "scale": {
                    "dataType": [
                        "Code",
                        "Date",
                        "Duration",
                        "Nominal",
                        "Numerical",
                        "Ordinal",
                        "Text"
                    ],
                    "decimalPlaces": 2,
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleDbId": "af730171",
                    "scaleName": "Meters",
                    "validValues": {
                        "categories": [
                            "low",
                            "medium",
                            "high"
                        ],
                        "max": 9999,
                        "min": 2
                    },
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "scientist": "Dr. Bob Robertson",
                "status": "recommended",
                "submissionTimestamp": "2018-01-01T14:47:23-0600",
                "synonyms": [
                    "Maize Height",
                    "Stalk Height",
                    "Corn Height"
                ],
                "trait": {
                    "alternativeAbbreviations": [
                        "H",
                        "PH",
                        "H1"
                    ],
                    "attribute": "height",
                    "entity": "Stalk",
                    "mainAbbreviation": "PH",
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": [
                                    "OBO",
                                    "RDF",
                                    "WEBPAGE"
                                ]
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "status": "recommended",
                    "synonyms": [
                        "Height",
                        "Plant Height",
                        "Stalk Height",
                        "Canopy Height"
                    ],
                    "traitClass": "phenological",
                    "traitDbId": "9b2e34f5",
                    "traitDescription": "The height of the plant",
                    "traitName": "Height",
                    "xref": "http://purl.obolibrary.org/obo/ro.owl"
                },
                "xref": "http://purl.obolibrary.org/obo/ro.owl"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

