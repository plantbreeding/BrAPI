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
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "description": "description0",
                "emailAddress": "emailAddress0",
                "firstName": "firstName0",
                "lastName": "lastName0",
                "mailingAddress": "mailingAddress0",
                "middleName": "middleName0",
                "personDbId": "personDbId0",
                "phoneNumber": "phoneNumber0",
                "userID": "userID0"
            },
            {
                "description": "description1",
                "emailAddress": "emailAddress1",
                "firstName": "firstName1",
                "lastName": "lastName1",
                "mailingAddress": "mailingAddress1",
                "middleName": "middleName1",
                "personDbId": "personDbId1",
                "phoneNumber": "phoneNumber1",
                "userID": "userID1"
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
        "pagination": {},
        "status": []
    },
    "result": {
        "description": "description0",
        "emailAddress": "emailAddress0",
        "firstName": "firstName0",
        "lastName": "lastName0",
        "mailingAddress": "mailingAddress0",
        "middleName": "middleName0",
        "personDbId": "personDbId0",
        "phoneNumber": "phoneNumber0",
        "userID": "userID0"
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
        "pagination": {},
        "status": []
    },
    "result": {
        "description": "description0",
        "emailAddress": "emailAddress0",
        "firstName": "firstName0",
        "lastName": "lastName0",
        "mailingAddress": "mailingAddress0",
        "middleName": "middleName0",
        "personDbId": "personDbId0",
        "phoneNumber": "phoneNumber0",
        "userID": "userID0"
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
        "pagination": {},
        "status": []
    },
    "result": {
        "description": "description0",
        "emailAddress": "emailAddress0",
        "firstName": "firstName0",
        "lastName": "lastName0",
        "mailingAddress": "mailingAddress0",
        "middleName": "middleName0",
        "personDbId": "personDbId0",
        "phoneNumber": "phoneNumber0",
        "userID": "userID0"
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

