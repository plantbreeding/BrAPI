# Group People
Calls for maintaining information about people




## Search [/brapi/v1/search] 




### Post Search People  [POST /brapi/v1/search/people]

Advanced searching for the programs resource.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|firstNames|array[string]|Persons first name|
|lastNames|array[string]|Persons last name|
|phoneNumbers|array[string]|phone number of this person|
|personDbIds|array[string]|Unique ID for this person|
|emailAddresses|array[string]|email address for this person|
|middleNames|array[string]|Persons middle name|
|mailingAddresses|array[string]|physical address of this person|
|userIDs|array[string]|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "emailAddresses": [
        "bob@bob.com",
        "rob@bob.com"
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





### Get Search People by searchResultsDbId  [GET /brapi/v1/search/people/{searchResultsDbId}{?page}{?pageSize}]

Advanced searching for the people resource.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of people|
|personDbId|string|Unique ID for a person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|
|middleName|string|Persons middle name|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|firstName|string|Persons first name|
|mailingAddress|string|physical address of this person|
|phoneNumber|string|phone number of this person|
|lastName|string|Persons last name|
|additionalInfo|object|Additional arbitrary info|


 

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
                "description": "Bob likes pina coladas and getting caught in the rain.",
                "emailAddress": "bob@bob.com",
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



## People [/brapi/v1/people] 




### Get People  [GET /brapi/v1/people{?firstName}{?lastName}{?personDbId}{?userID}{?page}{?pageSize}]

Get filtered list of people



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of people|
|personDbId|string|Unique ID for a person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|
|middleName|string|Persons middle name|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|firstName|string|Persons first name|
|mailingAddress|string|physical address of this person|
|phoneNumber|string|phone number of this person|
|lastName|string|Persons last name|
|additionalInfo|object|Additional arbitrary info|


 

+ Parameters
    + firstName (Optional, ) ... A persons first name
    + lastName (Optional, ) ... A persons last name
    + personDbId (Optional, ) ... The unique ID of a person
    + userID (Optional, ) ... A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.
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
                "description": "Bob likes pina coladas and getting caught in the rain.",
                "emailAddress": "bob@bob.com",
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





### Post People  [POST /brapi/v1/people]

Create new People entities. `personDbId` is generated and managed by the server.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|
|middleName|string|Persons middle name|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|firstName|string|Persons first name|
|mailingAddress|string|physical address of this person|
|phoneNumber|string|phone number of this person|
|lastName|string|Persons last name|
|additionalInfo|object|Additional arbitrary info|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of people|
|personDbId|string|Unique ID for a person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|
|middleName|string|Persons middle name|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|firstName|string|Persons first name|
|mailingAddress|string|physical address of this person|
|phoneNumber|string|phone number of this person|
|lastName|string|Persons last name|
|additionalInfo|object|Additional arbitrary info|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "description": "Bob likes pina coladas and getting caught in the rain.",
        "emailAddress": "bob@bob.com",
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
                "description": "Bob likes pina coladas and getting caught in the rain.",
                "emailAddress": "bob@bob.com",
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





### Get People by personDbId  [GET /brapi/v1/people/{personDbId}]

Get the details for a specific Person



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|personDbId|string|Unique ID for a person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|
|middleName|string|Persons middle name|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|firstName|string|Persons first name|
|mailingAddress|string|physical address of this person|
|phoneNumber|string|phone number of this person|
|lastName|string|Persons last name|
|additionalInfo|object|Additional arbitrary info|


 

+ Parameters
    + personDbId (Required, ) ... The unique ID of a person
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
        "description": "Bob likes pina coladas and getting caught in the rain.",
        "emailAddress": "bob@bob.com",
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





### Put People by personDbId  [PUT /brapi/v1/people/{personDbId}]

Update an existing Person

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|
|middleName|string|Persons middle name|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|firstName|string|Persons first name|
|mailingAddress|string|physical address of this person|
|phoneNumber|string|phone number of this person|
|lastName|string|Persons last name|
|additionalInfo|object|Additional arbitrary info|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|personDbId|string|Unique ID for a person|
|userID|string|A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.|
|middleName|string|Persons middle name|
|description|string|description of this person|
|emailAddress|string|email address for this person|
|firstName|string|Persons first name|
|mailingAddress|string|physical address of this person|
|phoneNumber|string|phone number of this person|
|lastName|string|Persons last name|
|additionalInfo|object|Additional arbitrary info|


 

+ Parameters
    + personDbId (Required, ) ... The unique ID of a person
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "description": "Bob likes pina coladas and getting caught in the rain.",
    "emailAddress": "bob@bob.com",
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
        "description": "Bob likes pina coladas and getting caught in the rain.",
        "emailAddress": "bob@bob.com",
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

