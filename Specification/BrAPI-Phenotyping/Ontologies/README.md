
# Group Ontologies

API to manage the details of stored Ontologies. This could be a reference a local Ontology or a remote public Ontology.  






### Get - /ontologies [GET /brapi/v2/ontologies{?ontologyName}{?ontologyDbId}{?page}{?pageSize}]

Retrieve a list of ontologies available in the system. 
Each Ontology record describes the metadata of an existing ontology, it does not include all the terms that are part of that ontology.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td><span style="font-weight:bold;">ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">authors</span></td><td>string</td><td>Ontology's list of authors (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>Ontology copyright</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Human readable description of Ontology</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">licence</span></td><td>string</td><td>Ontology licence</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + ontologyName (Optional, ) ... The human readable identifier for an ontology definition
    + ontologyDbId (Optional, ) ... The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology Use `GET /ontologies` to find the list of available ontologies on a server.
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
                "authors": "Bob Robertson, Rob Robertson",
                "copyright": "Copyright 1987, Bob Robertson",
                "description": "This is an example ontology that does not exist",
                "documentationURL": "https://wiki.brapi.org/ontology",
                "licence": "MIT Open source licence",
                "ontologyDbId": "18e186cd",
                "ontologyName": "The Official Ontology",
                "version": "V1.3.2"
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




### Post - /ontologies [POST /brapi/v2/ontologies]

Use this endpoint to create a new Ontology record in the database
Each Ontology record describes the metadata of an existing ontology, it does not include all the terms that are part of that ontology.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">authors</span></td><td>string</td><td>Ontology's list of authors (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>Ontology copyright</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Human readable description of Ontology</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">licence</span></td><td>string</td><td>Ontology licence</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td><span style="font-weight:bold;">ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">authors</span></td><td>string</td><td>Ontology's list of authors (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>Ontology copyright</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Human readable description of Ontology</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">licence</span></td><td>string</td><td>Ontology licence</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "authors": "Bob Robertson, Rob Robertson",
        "copyright": "Copyright 1987, Bob Robertson",
        "description": "This is an example ontology that does not exist",
        "documentationURL": "https://wiki.brapi.org/ontology",
        "licence": "MIT Open source licence",
        "ontologyName": "The Official Ontology",
        "version": "V1.3.2"
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
                "authors": "Bob Robertson, Rob Robertson",
                "copyright": "Copyright 1987, Bob Robertson",
                "description": "This is an example ontology that does not exist",
                "documentationURL": "https://wiki.brapi.org/ontology",
                "licence": "MIT Open source licence",
                "ontologyDbId": "18e186cd",
                "ontologyName": "The Official Ontology",
                "version": "V1.3.2"
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




### Get - /ontologies/{ontologyDbId} [GET /brapi/v2/ontologies/{ontologyDbId}]

Use this endpoint to retrieve a specific Ontology record by its ontologyDbId. 
Each Ontology record describes the metadata of an existing ontology, it does not include all the terms that are part of that ontology.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td><span style="font-weight:bold;">ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">authors</span></td><td>string</td><td>Ontology's list of authors (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>Ontology copyright</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Human readable description of Ontology</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">licence</span></td><td>string</td><td>Ontology licence</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + ontologyDbId (Required, ) ... The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology Use `GET /ontologies` to find the list of available ontologies on a server.
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
        "authors": "Bob Robertson, Rob Robertson",
        "copyright": "Copyright 1987, Bob Robertson",
        "description": "This is an example ontology that does not exist",
        "documentationURL": "https://wiki.brapi.org/ontology",
        "licence": "MIT Open source licence",
        "ontologyDbId": "18e186cd",
        "ontologyName": "The Official Ontology",
        "version": "V1.3.2"
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




### Put - /ontologies/{ontologyDbId} [PUT /brapi/v2/ontologies/{ontologyDbId}/]

Use this endpoint to update a specific Ontology record. 
Each Ontology record describes the metadata of an existing ontology, it does not include all the terms that are part of that ontology.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">authors</span></td><td>string</td><td>Ontology's list of authors (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>Ontology copyright</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Human readable description of Ontology</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">licence</span></td><td>string</td><td>Ontology licence</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td><span style="font-weight:bold;">ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">authors</span></td><td>string</td><td>Ontology's list of authors (no specific format)</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>Ontology copyright</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>Human readable description of Ontology</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">licence</span></td><td>string</td><td>Ontology licence</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
</table>


 

+ Parameters
    + ontologyDbId (Required, ) ... The unique identifier for an ontology definition. Use this parameter to filter results based on a specific ontology Use `GET /ontologies` to find the list of available ontologies on a server.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "authors": "Bob Robertson, Rob Robertson",
    "copyright": "Copyright 1987, Bob Robertson",
    "description": "This is an example ontology that does not exist",
    "documentationURL": "https://wiki.brapi.org/ontology",
    "licence": "MIT Open source licence",
    "ontologyName": "The Official Ontology",
    "version": "V1.3.2"
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
        "authors": "Bob Robertson, Rob Robertson",
        "copyright": "Copyright 1987, Bob Robertson",
        "description": "This is an example ontology that does not exist",
        "documentationURL": "https://wiki.brapi.org/ontology",
        "licence": "MIT Open source licence",
        "ontologyDbId": "18e186cd",
        "ontologyName": "The Official Ontology",
        "version": "V1.3.2"
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

