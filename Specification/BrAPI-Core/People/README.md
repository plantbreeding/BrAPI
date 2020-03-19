# Group People
Calls for maintaining information about people





### Get - /people [GET /brapi/v2/people{?firstName}{?lastName}{?personDbId}{?userID}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get filtered list of people



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of people|
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|personDbId|string|Unique ID for a person|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


 

+ Parameters
    + firstName (Optional, ) ... A persons first name
    + lastName (Optional, ) ... A persons last name
    + personDbId (Optional, ) ... The unique ID of a person
    + userID (Optional, ) ... A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.
    + externalReferenceID (Optional, ) ... Search for Germplasm by an external reference
    + externalReferenceSource (Optional, ) ... Search for Germplasm by an external reference
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "description": "Bob likes pina coladas and getting caught in the rain.",
                "emailAddress": "bob@bob.com",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "firstName": "Bob",
                "lastName": "Robertson",
                "mailingAddress": "123 Street Ave, City, State, Country",
                "middleName": "Danger",
                "personDbId": "14340a54",
                "phoneNumber": "+1-555-555-5555",
                "userID": "bob-23"
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




### Post - /people [POST /brapi/v2/people]

Create new People entities. `personDbId` is generated and managed by the server.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of people|
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|personDbId|string|Unique ID for a person|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "description": "Bob likes pina coladas and getting caught in the rain.",
        "emailAddress": "bob@bob.com",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "firstName": "Bob",
        "lastName": "Robertson",
        "mailingAddress": "123 Street Ave, City, State, Country",
        "middleName": "Danger",
        "phoneNumber": "+1-555-555-5555",
        "userID": "bob-23"
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "description": "Bob likes pina coladas and getting caught in the rain.",
                "emailAddress": "bob@bob.com",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "firstName": "Bob",
                "lastName": "Robertson",
                "mailingAddress": "123 Street Ave, City, State, Country",
                "middleName": "Danger",
                "personDbId": "14340a54",
                "phoneNumber": "+1-555-555-5555",
                "userID": "bob-23"
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




### Get - /people/{personDbId} [GET /brapi/v2/people/{personDbId}]

Get the details for a specific Person



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|personDbId|string|Unique ID for a person|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


 

+ Parameters
    + personDbId (Required, ) ... The unique ID of a person
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "description": "Bob likes pina coladas and getting caught in the rain.",
        "emailAddress": "bob@bob.com",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "firstName": "Bob",
        "lastName": "Robertson",
        "mailingAddress": "123 Street Ave, City, State, Country",
        "middleName": "Danger",
        "personDbId": "14340a54",
        "phoneNumber": "+1-555-555-5555",
        "userID": "bob-23"
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




### Put - /people/{personDbId} [PUT /brapi/v2/people/{personDbId}]

Update an existing Person

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|personDbId|string|Unique ID for a person|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


 

+ Parameters
    + personDbId (Required, ) ... The unique ID of a person
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "description": "Bob likes pina coladas and getting caught in the rain.",
    "emailAddress": "bob@bob.com",
    "externalReferences": [
        {
            "referenceID": "doi:10.155454/12349537E12",
            "referenceSource": "DOI"
        },
        {
            "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
            "referenceSource": "OBO Library"
        },
        {
            "referenceID": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        }
    ],
    "firstName": "Bob",
    "lastName": "Robertson",
    "mailingAddress": "123 Street Ave, City, State, Country",
    "middleName": "Danger",
    "phoneNumber": "+1-555-555-5555",
    "userID": "bob-23"
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "description": "Bob likes pina coladas and getting caught in the rain.",
        "emailAddress": "bob@bob.com",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "firstName": "Bob",
        "lastName": "Robertson",
        "mailingAddress": "123 Street Ave, City, State, Country",
        "middleName": "Danger",
        "personDbId": "14340a54",
        "phoneNumber": "+1-555-555-5555",
        "userID": "bob-23"
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




### Post - /search/people [POST /brapi/v2/search/people]

Advanced searching for the programs resource.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|emailAddresses|array[string]|email address for this person|
|externalReferenceIDs|array[string]|List of external references for the trait to search for|
|externalReferenceSources|array[string]|List of external references sources for the trait to search for|
|firstNames|array[string]|Persons first name|
|lastNames|array[string]|Persons last name|
|mailingAddresses|array[string]|physical address of this person|
|middleNames|array[string]|Persons middle name|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|personDbIds|array[string]|Unique ID for this person|
|phoneNumbers|array[string]|phone number of this person|
|userIDs|array[string]|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of people|
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|personDbId|string|Unique ID for a person|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "emailAddresses": [
        "bob@bob.com",
        "rob@bob.com"
    ],
    "externalReferenceIDs": [
        "http://purl.obolibrary.org/obo/ro.owl",
        "14a19841"
    ],
    "externalReferenceSources": [
        "OBO Library",
        "Field App Name"
    ],
    "firstNames": [
        "Bob",
        "Rob"
    ],
    "lastNames": [
        "Robertson",
        "Smith"
    ],
    "mailingAddresses": [
        "123 Main Street",
        "456 Side Street"
    ],
    "middleNames": [
        "Danger",
        "Fight"
    ],
    "page": 0,
    "pageSize": 1000,
    "personDbIds": [
        "1e7731ab",
        "bc28cff8"
    ],
    "phoneNumbers": [
        "9995555555",
        "8884444444"
    ],
    "userIDs": [
        "bob",
        "rob"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "description": "Bob likes pina coladas and getting caught in the rain.",
                "emailAddress": "bob@bob.com",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "firstName": "Bob",
                "lastName": "Robertson",
                "mailingAddress": "123 Street Ave, City, State, Country",
                "middleName": "Danger",
                "personDbId": "14340a54",
                "phoneNumber": "+1-555-555-5555",
                "userID": "bob-23"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/people/{searchResultsDbId} [GET /brapi/v2/search/people/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the people resource.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of people|
|additionalInfo|object|Additional arbitrary info|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|firstName|string|Persons first name|
|lastName|string|Persons last name|
|mailingAddress|string|physical address of this person|
|middleName|string|Persons middle name|
|personDbId|string|Unique ID for a person|
|phoneNumber|string|phone number of this person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "description": "Bob likes pina coladas and getting caught in the rain.",
                "emailAddress": "bob@bob.com",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "firstName": "Bob",
                "lastName": "Robertson",
                "mailingAddress": "123 Street Ave, City, State, Country",
                "middleName": "Danger",
                "personDbId": "14340a54",
                "phoneNumber": "+1-555-555-5555",
                "userID": "bob-23"
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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

