# Group People
Calls for maintaining information about people




## People [/brapi/v1/people] 




### Get People  [GET /brapi/v1/people{?firstName}{?lastName}{?personDbId}{?userID}{?page}{?pageSize}]

Get filtered list of people

 

+ Parameters
    + firstName (Optional, ) ... A persons first name
    + lastName (Optional, ) ... A persons last name
    + personDbId (Optional, ) ... The unique ID of a person
    + userID (Optional, ) ... A systems user ID ascociated with this person. Different from personDbId because you could have a person who is not a user of the system.
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
                "description": "Example Person",
                "emailAddress": "bob@bob.com",
                "firstName": "Bob",
                "lastName": "Robertson",
                "mailingAddress": "123 Road Street, City, State, Country, 98765",
                "middleName": "Danger",
                "personDbId": "person1",
                "phoneNumber": "+19876543210",
                "userID": "bdr45"
            },
            {
                "description": "Example Person",
                "emailAddress": "rob@bob.com",
                "firstName": "Rob",
                "lastName": "Robertson",
                "mailingAddress": "123 Road Street, City, State, Country, 98765",
                "middleName": "Danger",
                "personDbId": "person2",
                "phoneNumber": "+19876543210",
                "userID": "rdr45"
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





### Post People  [POST /brapi/v1/people]

Create a new person

 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "description": "description0",
    "emailAddress": "emailAddress0",
    "firstName": "firstName0",
    "lastName": "lastName0",
    "mailingAddress": "mailingAddress0",
    "middleName": "middleName0",
    "phoneNumber": "phoneNumber0",
    "userID": "userID0"
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
        "description": "string",
        "emailAddress": "string",
        "firstName": "Name",
        "lastName": "Smith",
        "mailingAddress": "string",
        "middleName": "string",
        "personDbId": "5bf0f4b9-0e59-4265-88e2-ea2b589e3d2f",
        "phoneNumber": "string",
        "userID": "string"
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





### Get People by personDbId  [GET /brapi/v1/people/{personDbId}]

Get a specific person

 

+ Parameters
    + personDbId (Required, ) ... The unique ID of a person
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
        "description": "Example Person",
        "emailAddress": "bob@bob.com",
        "firstName": "Bob",
        "lastName": "Robertson",
        "mailingAddress": "123 Road Street, City, State, Country, 98765",
        "middleName": "Danger",
        "personDbId": "person1",
        "phoneNumber": "+19876543210",
        "userID": "bdr45"
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





### Put People by personDbId  [PUT /brapi/v1/people/{personDbId}]

Update an existing Person

 

+ Parameters
    + personDbId (Required, ) ... The unique ID of a person
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "description": "description0",
    "emailAddress": "emailAddress0",
    "firstName": "firstName0",
    "lastName": "lastName0",
    "mailingAddress": "mailingAddress0",
    "middleName": "middleName0",
    "phoneNumber": "phoneNumber0",
    "userID": "userID0"
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
        "description": "string",
        "emailAddress": "string",
        "firstName": "Name",
        "lastName": "Nameson",
        "mailingAddress": "string",
        "middleName": "string",
        "personDbId": "person1",
        "phoneNumber": "string",
        "userID": "string"
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

