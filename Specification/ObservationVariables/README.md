# Group Observation Variables

Implemented by: GnpIS

API to retrieve list and details of observation variables. An observation variable is composed by the unique combination of one Trait, one Method and one Scale.




## Methods [/brapi/v1/methods] 




### Get Methods  [GET /brapi/v1/methods{?page}{?pageSize}]

Returns a list of Methods available on a server.

An Observation Variable has 3 critical parts: A Trait being observed, a Method for making the observation, and a Scale on which the observation can be measured and compared with other observations.

 

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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "class": "class0",
                "description": "description0",
                "formula": "formula0",
                "methodDbId": "methodDbId0",
                "methodName": "methodName0",
                "name": "name0",
                "ontologyRefernce": {
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
            },
            {
                "class": "class1",
                "description": "description1",
                "formula": "formula1",
                "methodDbId": "methodDbId1",
                "methodName": "methodName1",
                "name": "name1",
                "ontologyRefernce": {
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
                "reference": "reference1"
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
    "ontologyRefernce": {
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
        "pagination": {},
        "status": []
    },
    "result": {
        "class": "class0",
        "description": "description0",
        "formula": "formula0",
        "methodDbId": "methodDbId0",
        "methodName": "methodName0",
        "name": "name0",
        "ontologyRefernce": {
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

 

+ Parameters
    + methodDbId (Required, ) ... Id of the method to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "class": "class0",
        "description": "description0",
        "formula": "formula0",
        "methodDbId": "methodDbId0",
        "methodName": "methodName0",
        "name": "name0",
        "ontologyRefernce": {
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
    "ontologyRefernce": {
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
        "pagination": {},
        "status": []
    },
    "result": {
        "class": "class0",
        "description": "description0",
        "formula": "formula0",
        "methodDbId": "methodDbId0",
        "methodName": "methodName0",
        "name": "name0",
        "ontologyRefernce": {
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
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "authors": "Bob",
                "copyright": "2017 Ontology.org",
                "description": "Ontology.org",
                "documentationURL": null,
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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "dataType": "Code",
                "decimalPlaces": 0,
                "name": "name0",
                "ontologyRefernce": {
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
                "scaleDbId": "scaleDbId0",
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
            },
            {
                "dataType": "Duration",
                "decimalPlaces": 0,
                "name": "name1",
                "ontologyRefernce": {
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
                "scaleDbId": "scaleDbId1",
                "scaleName": "scaleName1",
                "validValues": {
                    "categories": [
                        "categories0",
                        "categories1"
                    ],
                    "max": 0,
                    "min": 0
                },
                "xref": "xref1"
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

 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataType": "Code",
    "decimalPlaces": 0,
    "ontologyRefernce": {
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
        "pagination": {},
        "status": []
    },
    "result": {
        "dataType": "Code",
        "decimalPlaces": 0,
        "name": "name0",
        "ontologyRefernce": {
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
        "scaleDbId": "scaleDbId0",
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

 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {},
        "status": []
    },
    "result": {
        "dataType": "Code",
        "decimalPlaces": 0,
        "name": "name0",
        "ontologyRefernce": {
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
        "scaleDbId": "scaleDbId0",
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

 

+ Parameters
    + scaleDbId (Required, ) ... Id of the scale to retrieve details of.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "dataType": "Code",
    "decimalPlaces": 0,
    "ontologyRefernce": {
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
        "pagination": {},
        "status": []
    },
    "result": {
        "dataType": "Code",
        "decimalPlaces": 0,
        "name": "name0",
        "ontologyRefernce": {
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
        "scaleDbId": "scaleDbId0",
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
                "date": "2018-10-02",
                "defaultValue": "10",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Standard rolled measuring tape",
                    "formula": "a^2 + b^2 = c^2",
                    "methodDbId": "m1",
                    "name": "Tape Measure",
                    "reference": "google.com"
                },
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 1,
                    "name": "Centimeter",
                    "scaleDbId": "s1",
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
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t1",
                    "xref": "xref"
                },
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-02",
                "defaultValue": "10",
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Dried sample on electric scale",
                    "formula": "NA",
                    "methodDbId": "m2",
                    "name": "Dry Electric Scale",
                    "reference": "google.com"
                },
                "name": "Root weight",
                "observationVariableDbId": "MO_123:100004",
                "observationVariableName": "Root weight",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 3,
                    "name": "Kilogram",
                    "scaleDbId": "s2",
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
                    "attribute": "root weight",
                    "class": "Numeric",
                    "description": "root weight",
                    "entity": "entity",
                    "mainAbbreviation": "RW",
                    "name": "Root Weight",
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t2",
                    "xref": "xref"
                },
                "xref": "MO_123:100004"
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
                    "MO_123:100002"
                ],
                "traitDbId": "t1",
                "traitId": "xref",
                "traitName": null
            },
            {
                "defaultValue": "0",
                "description": "root weight",
                "name": "Root Weight",
                "observationVariables": [
                    "MO_123:100004"
                ],
                "traitDbId": "t2",
                "traitId": "xref",
                "traitName": null
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
    "ontologyRefernce": {
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
        "pagination": {},
        "status": []
    },
    "result": {
        "alternativeAbbreviations": [
            "alternativeAbbreviations0",
            "alternativeAbbreviations1"
        ],
        "attribute": "attribute0",
        "class": "class0",
        "description": "description0",
        "entity": "entity0",
        "mainAbbreviation": "mainAbbreviation0",
        "name": "name0",
        "ontologyRefernce": {
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
        "traitDbId": "traitDbId0",
        "traitName": "traitName0",
        "xref": "xref0"
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
        "defaultValue": null,
        "description": null,
        "name": null,
        "observationVariables": null,
        "traitDbId": null,
        "traitId": null,
        "traitName": null
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
    "ontologyRefernce": {
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
        "pagination": {},
        "status": []
    },
    "result": {
        "alternativeAbbreviations": [
            "alternativeAbbreviations0",
            "alternativeAbbreviations1"
        ],
        "attribute": "attribute0",
        "class": "class0",
        "description": "description0",
        "entity": "entity0",
        "mainAbbreviation": "mainAbbreviation0",
        "name": "name0",
        "ontologyRefernce": {
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
        "traitDbId": "traitDbId0",
        "traitName": "traitName0",
        "xref": "xref0"
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



## Variables-search [/brapi/v1/variables-search] 




### **Deprecated** Post Variables-search  [POST /brapi/v1/variables-search]

Search observation variables. 
See Search Services for additional implementation details.

 

+ Parameters


 
+ Request (application/json)
```
{
    "datatypes": [
        "Code",
        "Duration"
    ],
    "methodDbIds": [
        "methodDbIds0",
        "methodDbIds1"
    ],
    "names": [
        "names0",
        "names1"
    ],
    "observationVariableDbIds": [
        "observationVariableDbIds0",
        "observationVariableDbIds1"
    ],
    "ontologyDbIds": [
        "ontologyDbIds0",
        "ontologyDbIds1"
    ],
    "ontologyXrefs": [
        "ontologyXrefs0",
        "ontologyXrefs1"
    ],
    "page": 0,
    "pageSize": 0,
    "scaleDbIds": [
        "scaleDbIds0",
        "scaleDbIds1"
    ],
    "traitClasses": [
        "traitClasses0",
        "traitClasses1"
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
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Standard rolled measuring tape",
                    "formula": "a^2 + b^2 = c^2",
                    "methodDbId": "m1",
                    "methodName": null,
                    "name": "Tape Measure",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 1,
                    "name": "Centimeter",
                    "ontologyRefernce": null,
                    "scaleDbId": "s1",
                    "scaleName": null,
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
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t1",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Dried sample on electric scale",
                    "formula": "NA",
                    "methodDbId": "m2",
                    "methodName": null,
                    "name": "Dry Electric Scale",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Root weight",
                "observationVariableDbId": "MO_123:100004",
                "observationVariableName": "Root weight",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 3,
                    "name": "Kilogram",
                    "ontologyRefernce": null,
                    "scaleDbId": "s2",
                    "scaleName": null,
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
                    "attribute": "root weight",
                    "class": "Numeric",
                    "description": "root weight",
                    "entity": "entity",
                    "mainAbbreviation": "RW",
                    "name": "Root Weight",
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t2",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100004"
            }
        ]
    }
}
```



## Variables [/brapi/v1/variables] 




### Get Variables  [GET /brapi/v1/variables{?page}{?pageSize}{?observationVariableDbId}{?traitClass}]

Call to retrieve a list of observationVariables available in the system.

 

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
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Numeric",
                    "description": "Standard rolled measuring tape",
                    "formula": "a^2 + b^2 = c^2",
                    "methodDbId": "m1",
                    "methodName": null,
                    "name": "Tape Measure",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "observationVariableName": "Plant height",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": "Numerical",
                    "decimalPlaces": 1,
                    "name": "Centimeter",
                    "ontologyRefernce": null,
                    "scaleDbId": "s1",
                    "scaleName": null,
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
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t1",
                    "traitName": null,
                    "xref": "xref"
                },
                "xref": "MO_123:100002"
            },
            {
                "contextOfUse": [],
                "crop": "maize",
                "date": "2018-10-26",
                "defaultValue": "10",
                "documentationURL": null,
                "growthStage": "1",
                "institution": "1",
                "language": "English",
                "method": {
                    "class": "Categorical",
                    "description": "Comparing sample color to standard color palette",
                    "formula": "NA",
                    "methodDbId": "m3",
                    "methodName": null,
                    "name": "Standard Color Palette",
                    "ontologyRefernce": null,
                    "reference": "google.com"
                },
                "name": "Carotenoid",
                "observationVariableDbId": "MO_123:100003",
                "observationVariableName": "Carotenoid",
                "ontologyDbId": "MO_123",
                "ontologyName": "Ontology.org",
                "ontologyRefernce": null,
                "scale": {
                    "dataType": null,
                    "decimalPlaces": 0,
                    "name": "Color",
                    "ontologyRefernce": null,
                    "scaleDbId": "s3",
                    "scaleName": null,
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
                    "ontologyRefernce": null,
                    "status": "active",
                    "synonyms": [],
                    "traitDbId": "t3",
                    "traitName": null,
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
        "date": "2018-10-02",
        "defaultValue": "10",
        "growthStage": "1",
        "institution": "1",
        "language": "English",
        "method": {
            "class": "Numeric",
            "description": "Standard rolled measuring tape",
            "formula": "a^2 + b^2 = c^2",
            "methodDbId": "m1",
            "name": "Tape Measure",
            "reference": "google.com"
        },
        "name": "Plant height",
        "observationVariableDbId": "MO_123:100002",
        "observationVariableName": "Plant height",
        "ontologyDbId": "MO_123",
        "ontologyName": "Ontology.org",
        "scale": {
            "dataType": "Numerical",
            "decimalPlaces": 1,
            "name": "Centimeter",
            "scaleDbId": "s1",
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
            "status": "active",
            "synonyms": [],
            "traitDbId": "t1",
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





### **Deprecated** Get Variables Datatypes  [GET /brapi/v1/variables/datatypes{?page}{?pageSize}]

DEPRECATED in v1.3 - See documentation on BrAPI fixed set of data types, references from the Crop Ontology

 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 3,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            "Categorical",
            "Numerical"
        ]
    }
}
```

