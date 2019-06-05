# Group Observation Variables

Implemented by: GnpIS

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.




## Methods [/brapi/v1/methods] 




### Get Methods  [GET /brapi/v1/methods{?page}{?pageSize}]

Returns a list of Methods available on a server.

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
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
            "totalCount": 4,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
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
            {
                "class": "Numeric",
                "description": "Dried sample on electric scale",
                "formula": "NA",
                "methodDbId": "m2",
                "methodName": "Dry Electric Scale",
                "name": "Dry Electric Scale",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org/m2",
                            "type": "WEBPAGE",
                            "url": "https://ontology.org/m2"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "reference": "google.com"
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





### Post Methods  [POST /brapi/v1/methods]

Create a new method object in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|class|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|description|string|Method description.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodName|string|Human readable name for the method|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "class": "class0",
    "description": "description0",
    "formula": "formula0",
    "methodName": "methodName0",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "URL0",
                "type": "OBO"
            },
            {
                "URL": "URL1",
                "type": "RDF"
            }
        ],
        "ontologyDbId": "ontologyDbId0",
        "ontologyName": "ontologyName0",
        "version": "version0"
    },
    "reference": "reference0"
}
```



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
        "class": "string",
        "description": "string",
        "formula": "string",
        "methodDbId": "8175d7ac-6221-4e1d-8023-91ddb8b30fd8",
        "methodName": "string",
        "name": "string",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "string",
                    "type": "OBO",
                    "url": "string"
                }
            ],
            "ontologyDbId": "MO_123",
            "ontologyName": "Ontology.org",
            "version": "17"
        },
        "reference": "string"
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





### Get Methods by methodDbId  [GET /brapi/v1/methods/{methodDbId}]

Retrieve details about a specific method

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Methods by methodDbId  [PUT /brapi/v1/methods/{methodDbId}]

Update the details of an existing method

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|class|string|Method class (examples: "Measurement", "Counting", "Estimation", "Computation", etc.)|
|description|string|Method description.|
|formula|string|For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the generic formula used for the calculation|
|methodName|string|Human readable name for the method|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|reference|string|Bibliographical reference describing the method.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "class": "class0",
    "description": "description0",
    "formula": "formula0",
    "methodName": "methodName0",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "URL0",
                "type": "OBO"
            },
            {
                "URL": "URL1",
                "type": "RDF"
            }
        ],
        "ontologyDbId": "ontologyDbId0",
        "ontologyName": "ontologyName0",
        "version": "version0"
    },
    "reference": "reference0"
}
```



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
        "class": "string",
        "description": "string",
        "formula": "string",
        "methodDbId": "m1",
        "methodName": "string",
        "name": "string",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "string",
                    "type": "OBO",
                    "url": "string"
                }
            ],
            "ontologyDbId": "MO_123",
            "ontologyName": "Ontology.org",
            "version": "17"
        },
        "reference": "string"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Ontologies [/brapi/v1/ontologies] 




### Get Ontologies  [GET /brapi/v1/ontologies{?page}{?pageSize}]

Call to retrieve a list of observation variable ontologies available in the system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|authors|string|Ontology's list of authors (no specific format)|
|copyright|string|Ontology copyright|
|description|string|Human readable description of Ontology|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|licence|string|Ontology licence|
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|


 

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
            "totalCount": 1,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "authors": "Bob",
                "copyright": "2017 Ontology.org",
                "description": "Ontology.org",
                "documentationURL": "https://ontology.org",
                "licence": "Apache",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "version": "17"
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



## Scales [/brapi/v1/scales] 




### Get Scales  [GET /brapi/v1/scales{?page}{?pageSize}]

Returns a list of Scales available on a server.

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
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
            "totalCount": 4,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
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
            {
                "dataType": "Numerical",
                "decimalPlaces": 3,
                "name": "Kilogram",
                "ontologyReference": {
                    "documentationLinks": [
                        {
                            "URL": "https://ontology.org/s2",
                            "type": "RDF",
                            "url": "https://ontology.org/s2"
                        }
                    ],
                    "ontologyDbId": "MO_123",
                    "ontologyName": "Ontology.org",
                    "version": "17"
                },
                "scaleDbId": "s2",
                "scaleName": "Kilogram",
                "validValues": {
                    "categories": [],
                    "max": 99999,
                    "min": 0
                },
                "xref": "xref"
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





### Post Scales  [POST /brapi/v1/scales]

Create a new scale object in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|dataType|string|Class of the scale, entries can be     "Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal             scale that combines the expressions of the different traits composing the complex             trait. For exemple a severity trait might be expressed by a 2 digit and 2 character             code. The first 2 digits are the percentage of the plant covered by a fungus and the 2             characters refer to the delay in development, e.g. "75VD" means "75%" of the plant is              Crop Ontology & Integrated Breeding Platform  Curation Guidelines  5/6/2016 9             infected and the plant is very delayed.      "Date" - The date class is for events expressed in a time format, e.g. yyyymmddThh:mm:ssZ or dd/mm/yy      "Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months      "Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories      "Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectar, branches      "Ordinal" - Ordinal scales are scales composed of ordered categories      "Text" - A free text is used to express the trait.   |
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleName|string|Name of the scale|
|validValues|object||
|categories|array[string]|List of possible values and their meaning (examples: ["0=low", "1=medium", "2=high"]|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataType": "Code",
    "decimalPlaces": 0,
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "URL0",
                "type": "OBO"
            },
            {
                "URL": "URL1",
                "type": "RDF"
            }
        ],
        "ontologyDbId": "ontologyDbId0",
        "ontologyName": "ontologyName0",
        "version": "version0"
    },
    "scaleName": "scaleName0",
    "validValues": {
        "categories": [
            "categories0",
            "categories1"
        ],
        "max": 0,
        "min": 0
    },
    "xref": "xref0"
}
```



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
        "dataType": "Code",
        "decimalPlaces": 0,
        "name": "string",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "string",
                    "type": "OBO",
                    "url": "string"
                }
            ],
            "ontologyDbId": "MO_123",
            "ontologyName": "Ontology.org",
            "version": "17"
        },
        "scaleDbId": "90fdedbc-6412-47ac-877b-81dd466fe6d2",
        "scaleName": "string",
        "validValues": {
            "categories": [
                "string"
            ],
            "max": 0,
            "min": 0
        },
        "xref": "string"
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





### Get Scales by scaleDbId  [GET /brapi/v1/scales/{scaleDbId}]

Retrieve details about a specific scale

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Scales by scaleDbId  [PUT /brapi/v1/scales/{scaleDbId}]

Update the details of an existing scale

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|dataType|string|Class of the scale, entries can be     "Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal             scale that combines the expressions of the different traits composing the complex             trait. For exemple a severity trait might be expressed by a 2 digit and 2 character             code. The first 2 digits are the percentage of the plant covered by a fungus and the 2             characters refer to the delay in development, e.g. "75VD" means "75%" of the plant is              Crop Ontology & Integrated Breeding Platform  Curation Guidelines  5/6/2016 9             infected and the plant is very delayed.      "Date" - The date class is for events expressed in a time format, e.g. yyyymmddThh:mm:ssZ or dd/mm/yy      "Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months      "Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories      "Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectar, branches      "Ordinal" - Ordinal scales are scales composed of ordered categories      "Text" - A free text is used to express the trait.   |
|decimalPlaces|integer|For numerical, number of decimal places to be reported|
|ontologyReference|object||
|documentationLinks|array[object]|links to various ontology documentation|
|URL|string (uri)||
|type|string||
|ontologyDbId|string|Ontology database unique identifier|
|ontologyName|string|Ontology name|
|version|string|Ontology version (no specific format)|
|scaleName|string|Name of the scale|
|validValues|object||
|categories|array[string]|List of possible values and their meaning (examples: ["0=low", "1=medium", "2=high"]|
|max|integer|Maximum value (used for field data capture control).|
|min|integer|Minimum value (used for data capture control) for numerical and date scales|
|xref|string|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataType": "Code",
    "decimalPlaces": 0,
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "URL0",
                "type": "OBO"
            },
            {
                "URL": "URL1",
                "type": "RDF"
            }
        ],
        "ontologyDbId": "ontologyDbId0",
        "ontologyName": "ontologyName0",
        "version": "version0"
    },
    "scaleName": "scaleName0",
    "validValues": {
        "categories": [
            "categories0",
            "categories1"
        ],
        "max": 0,
        "min": 0
    },
    "xref": "xref0"
}
```



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
        "dataType": "Code",
        "decimalPlaces": 0,
        "name": "string",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "string",
                    "type": "OBO",
                    "url": "string"
                }
            ],
            "ontologyDbId": "MO_123",
            "ontologyName": "Ontology.org",
            "version": "17"
        },
        "scaleDbId": "s1",
        "scaleName": "string",
        "validValues": {
            "categories": [
                "string"
            ],
            "max": 0,
            "min": 0
        },
        "xref": "string"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Search [/brapi/v1/search] 




### Post Search Variables  [POST /brapi/v1/search/variables]

Search observation variables.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|dataTypes|array[string]|List of scale data types to filter search results|
|methodDbIds|array[string]|List of methods to filter search results|
|observationVariableDbIds|array[string]|List of observation variable IDs to search for|
|observationVariableNames|array[string]|List of human readable observation variable names to search for|
|observationVariableXrefs|array[string]|List of cross references for the observation variable to search for|
|ontologyDbIds|array[string]|List of ontology IDs to search for|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|
|scaleDbIds|array[string]|List of scales to filter search results|
|scaleXrefs|array[string]|List of cross references for the scale to search for|
|traitClasses|array[string]|List of trait classes to filter search results|
|traitDbIds|array[string]|List of trait unique ID to filter search results|
|traitXrefs|array[string]|List of cross references for the trait to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataTypes": [
        "Code",
        "Duration"
    ],
    "methodDbIds": [
        "methodDbIds0",
        "methodDbIds1"
    ],
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "observationVariableNames": [
        "observationVariableNames0",
        "observationVariableNames1"
    ],
    "observationVariableXrefs": [
        "observationVariableXrefs0",
        "observationVariableXrefs1"
    ],
    "ontologyDbIds": [
        "ontologyDbIds0",
        "ontologyDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "scaleDbIds": [
        "scaleDbIds0",
        "scaleDbIds1"
    ],
    "scaleXrefs": [
        "scaleXrefs0",
        "scaleXrefs1"
    ],
    "traitClasses": [
        "traitClasses0",
        "traitClasses1"
    ],
    "traitDbIds": [
        "traitDbIds0",
        "traitDbIds1"
    ],
    "traitXrefs": [
        "traitXrefs0",
        "traitXrefs1"
    ]
}
```



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
        "searchResultDbId": "551ae08c-4548-4bde-ad70-f23beb25e2ea"
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





### Get Search Variables by searchResultsDbId  [GET /brapi/v1/search/variables/{searchResultsDbId}{?page}{?pageSize}]

Search observation variables.

See Search Services for additional implementation details.



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
|observationVariableDbId|string|Variable unique identifier|
|observationVariableName|string|Variable name (usually a short name)|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
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
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
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
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
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
                "name": "Carotenoid",
                "observationVariableDbId": "MO_123:100003",
                "observationVariableName": "Carotenoid",
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Traits [/brapi/v1/traits] 




### Get Traits  [GET /brapi/v1/traits{?page}{?pageSize}]

Call to retrieve a list of traits available in the system and their associated variables.

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|defaultValue|string|The default value of a trait (if applicable) ex. "0", "", "null"|
|description|string|The description of a trait|
|observationVariables|array[string]|List of observation variable DbIds which include this trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitName|string|The human readable name of a trait|


 

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
            "totalCount": 5,
            "totalPages": 3
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "defaultValue": "0",
                "description": "plant height",
                "name": "Plant Height",
                "observationVariables": [
                    "ATT01",
                    "MO_123:100002"
                ],
                "traitDbId": "t1",
                "traitId": "t1",
                "traitName": "Plant Height"
            },
            {
                "defaultValue": "0",
                "description": "root weight",
                "name": "Root Weight",
                "observationVariables": [
                    "ATT03",
                    "MO_123:100004"
                ],
                "traitDbId": "t2",
                "traitId": "t2",
                "traitName": "Root Weight"
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





### Post Traits  [POST /brapi/v1/traits]

Create a new trait object in the database

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
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
|traitName|string|The human readable name of a trait|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "alternativeAbbreviations": [
        "alternativeAbbreviations0",
        "alternativeAbbreviations1"
    ],
    "attribute": "attribute0",
    "class": "class0",
    "description": "description0",
    "entity": "entity0",
    "mainAbbreviation": "mainAbbreviation0",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "URL0",
                "type": "OBO"
            },
            {
                "URL": "URL1",
                "type": "RDF"
            }
        ],
        "ontologyDbId": "ontologyDbId0",
        "ontologyName": "ontologyName0",
        "version": "version0"
    },
    "status": "status0",
    "synonyms": [
        "synonyms0",
        "synonyms1"
    ],
    "traitName": "traitName0",
    "xref": "xref0"
}
```



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
        "alternativeAbbreviations": [
            "string"
        ],
        "attribute": "string",
        "class": "string",
        "description": "string",
        "entity": "string",
        "mainAbbreviation": "string",
        "name": "string",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "string",
                    "type": "OBO",
                    "url": "string"
                }
            ],
            "ontologyDbId": "MO_123",
            "ontologyName": "Ontology.org",
            "version": "17"
        },
        "status": "string",
        "synonyms": [
            "string"
        ],
        "traitDbId": "2d078dee-3d06-4deb-b0bb-2919c021a538",
        "traitName": "string",
        "xref": "string"
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





### Get Traits by traitDbId  [GET /brapi/v1/traits/{traitDbId}]

Retrieve the details of a single trait

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|defaultValue|string|The default value of a trait (if applicable) ex. "0", "", "null"|
|description|string|The description of a trait|
|observationVariables|array[string]|List of observation variable DbIds which include this trait|
|traitDbId|string|The ID which uniquely identifies a trait|
|traitName|string|The human readable name of a trait|


 

+ Parameters
    + traitDbId (Required, ) ... Id of the trait to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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
        "defaultValue": "0",
        "description": "plant height",
        "name": "Plant Height",
        "observationVariables": [
            "ATT01",
            "MO_123:100002"
        ],
        "traitDbId": "t1",
        "traitId": "t1",
        "traitName": "Plant Height"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Put Traits by traitDbId  [PUT /brapi/v1/traits/{traitDbId}]

Update an existing trait

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
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
|traitName|string|The human readable name of a trait|
|xref|string|Cross reference of the trait to an external ontology or database term e.g., Xref to a trait ontology (TO) term|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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


 

+ Parameters
    + traitDbId (Required, ) ... Id of the trait to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "alternativeAbbreviations": [
        "alternativeAbbreviations0",
        "alternativeAbbreviations1"
    ],
    "attribute": "attribute0",
    "class": "class0",
    "description": "description0",
    "entity": "entity0",
    "mainAbbreviation": "mainAbbreviation0",
    "ontologyReference": {
        "documentationLinks": [
            {
                "URL": "URL0",
                "type": "OBO"
            },
            {
                "URL": "URL1",
                "type": "RDF"
            }
        ],
        "ontologyDbId": "ontologyDbId0",
        "ontologyName": "ontologyName0",
        "version": "version0"
    },
    "status": "status0",
    "synonyms": [
        "synonyms0",
        "synonyms1"
    ],
    "traitName": "traitName0",
    "xref": "xref0"
}
```



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
        "alternativeAbbreviations": [
            "string"
        ],
        "attribute": "string",
        "class": "string",
        "description": "string",
        "entity": "string",
        "mainAbbreviation": "string",
        "name": "string",
        "ontologyReference": {
            "documentationLinks": [
                {
                    "URL": "string",
                    "type": "OBO",
                    "url": "string"
                }
            ],
            "ontologyDbId": "MO_123",
            "ontologyName": "Ontology.org",
            "version": "17"
        },
        "status": "string",
        "synonyms": [
            "string"
        ],
        "traitDbId": "t1",
        "traitName": "string",
        "xref": "string"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Variables [/brapi/v1/variables] 




### Get Variables  [GET /brapi/v1/variables{?page}{?pageSize}{?observationVariableDbId}{?traitClass}]

Call to retrieve a list of observationVariables available in the system.



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
|observationVariableDbId|string|Variable unique identifier|
|observationVariableName|string|Variable name (usually a short name)|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>
    + observationVariableDbId (Optional, ) ... Variable's unique ID
    + traitClass (Optional, ) ... Variable's trait class (phenological, physiological, morphological, etc.)




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
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
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
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
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
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-12-05",
                "defaultValue": "10",
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
                "name": "Carotenoid",
                "observationVariableDbId": "MO_123:100003",
                "observationVariableName": "Carotenoid",
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





### Get Variables by observationVariableDbId  [GET /brapi/v1/variables/{observationVariableDbId}]

Retrieve variable details



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
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
|observationVariableDbId|string|Variable unique identifier|
|observationVariableName|string|Variable name (usually a short name)|


 

+ Parameters
    + observationVariableDbId (Required, ) ... string id of the variable
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




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
        "contextOfUse": [],
        "crop": "maize",
        "date": "2018-12-05",
        "defaultValue": "10",
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
        "name": "Plant height",
        "observationVariableDbId": "MO_123:100002",
        "observationVariableName": "Plant height",
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
        "xref": "MO_123:100002"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

