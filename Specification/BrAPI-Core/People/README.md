# Group People
Calls for maintaining information about people





### Get - /people [GET /brapi/v2/people{?firstName}{?lastName}{?personDbId}{?userID}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get filtered list of people



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">personDbId</span></td><td>string</td><td>Unique ID for a person</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


 

+ Parameters
    + firstName (Optional, ) ... A persons first name
    + lastName (Optional, ) ... A persons last name
    + personDbId (Optional, ) ... The unique ID of a person
    + userID (Optional, ) ... A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceId (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">personDbId</span></td><td>string</td><td>Unique ID for a person</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


 

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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">personDbId</span></td><td>string</td><td>Unique ID for a person</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


 

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
        "datafiles": [],
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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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




### Put - /people/{personDbId} [PUT /brapi/v2/people/{personDbId}/]

Update an existing Person

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">personDbId</span></td><td>string</td><td>Unique ID for a person</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


 

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
            "referenceId": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceId": "75a50e76",
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
        "datafiles": [],
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
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
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

Submit a search request for `People`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/people/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">emailAddresses</span></td><td>array[string]</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">firstNames</span></td><td>array[string]</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastNames</span></td><td>array[string]</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddresses</span></td><td>array[string]</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleNames</span></td><td>array[string]</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">personDbIds</span></td><td>array[string]</td><td>Unique ID for this person</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumbers</span></td><td>array[string]</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">userIDs</span></td><td>array[string]</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">personDbId</span></td><td>string</td><td>Unique ID for a person</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "emailAddresses": [
        "bob@bob.com",
        "rob@bob.com"
    ],
    "externalReferenceIDs": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceIds": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceSources": [
        "DOI",
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
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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
        "datafiles": [],
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

Get the results of a `People` search request <br/>
Clients should submit a search request using the corresponding `POST /search/people` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>description of this person</td></tr>
<tr><td><span style="font-weight:bold;">emailAddress</span></td><td>string</td><td>email address for this person</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">firstName</span></td><td>string</td><td>Persons first name</td></tr>
<tr><td><span style="font-weight:bold;">lastName</span></td><td>string</td><td>Persons last name</td></tr>
<tr><td><span style="font-weight:bold;">mailingAddress</span></td><td>string</td><td>physical address of this person</td></tr>
<tr><td><span style="font-weight:bold;">middleName</span></td><td>string</td><td>Persons middle name</td></tr>
<tr><td><span style="font-weight:bold;">personDbId</span></td><td>string</td><td>Unique ID for a person</td></tr>
<tr><td><span style="font-weight:bold;">phoneNumber</span></td><td>string</td><td>phone number of this person</td></tr>
<tr><td><span style="font-weight:bold;">userID</span></td><td>string</td><td>A systems user ID associated with this person. Different from personDbId because you could have a person who is not a user of the system.</td></tr>
</table>


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
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
        "datafiles": [],
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
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
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
        "datafiles": [],
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

