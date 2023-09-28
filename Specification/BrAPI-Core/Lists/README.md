# Group Lists
Calls for manipulating generic lists of item IDs





### Get - /lists [GET /brapi/v2/lists{?listType}{?listName}{?listDbId}{?listSource}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get filtered set of generic lists



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + listType (Optional, string) ... A flag to indicate the type of objects that are referenced in a List
    + listName (Optional, string) ... The human readable name of a List
    + listDbId (Optional, string) ... The unique identifier of a List
    + listSource (Optional, string) ... A short tag to indicate the source of a list
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + externalReferenceID (Optional, string) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 <br>An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceId (Optional, string) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, string) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
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
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": "germplasm"
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




### Post - /lists [POST /brapi/v2/lists]

Create new list objects in the database

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">data</span></td><td>array[string]</td><td>The array of DbIds of the BrAPI objects contained in a List</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": "germplasm"
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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
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
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": "germplasm"
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




### Get - /lists/{listDbId} [GET /brapi/v2/lists/{listDbId}]

Get a specific generic lists



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">data</span></td><td>array[string]</td><td>The array of DbIds of the BrAPI objects contained in a List</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + listDbId (Required, string) ... The unique identifier of a List
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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
        "listDbId": "6f621cfa",
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": "germplasm"
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




### Put - /lists/{listDbId} [PUT /brapi/v2/lists/{listDbId}/]

Update an existing generic list

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">data</span></td><td>array[string]</td><td>The array of DbIds of the BrAPI objects contained in a List</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">data</span></td><td>array[string]</td><td>The array of DbIds of the BrAPI objects contained in a List</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + listDbId (Required, string) ... The unique identifier of a List
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "data": [
        "758a78c0",
        "2c78f9ee"
    ],
    "dateCreated": "2018-01-01T14:47:23-0600",
    "dateModified": "2018-01-01T14:47:23-0600",
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
    "listDescription": "This is a list of germplasm I would like to investigate next season",
    "listName": "MyGermplasm_Sept_2020",
    "listOwnerName": "Bob Robertson",
    "listOwnerPersonDbId": "58db0628",
    "listSize": 53,
    "listSource": "GeneBank Repository 1.3",
    "listType": "germplasm"
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
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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
        "listDbId": "6f621cfa",
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": "germplasm"
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




### Post - /lists/{listDbId}/data [POST /brapi/v2/lists/{listDbId}/data]

Add new data members to a specific List

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">data</span></td><td>array[string]</td><td>The array of DbIds of the BrAPI objects contained in a List</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + listDbId (Required, string) ... The unique identifier of a generic List
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    "758a78c0",
    "2c78f9ee"
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
        "additionalInfo": {},
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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
        "listDbId": "6f621cfa",
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": "germplasm"
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




### **Deprecated** Post - /lists/{listDbId}/items [POST /brapi/v2/lists/{listDbId}/items]

**Deprecated in v2.1** Please use `POST /lists/{listDbId}/data`. Github issue number #444 
<br/> Add new data to a specific generic lists

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">data</span></td><td>array[string]</td><td>The array of DbIds of the BrAPI objects contained in a List</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + listDbId (Required, string) ... The unique identifier of a List
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    "758a78c0",
    "2c78f9ee"
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
        "additionalInfo": {},
        "data": [
            "758a78c0",
            "2c78f9ee"
        ],
        "dateCreated": "2018-01-01T14:47:23-0600",
        "dateModified": "2018-01-01T14:47:23-0600",
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
        "listDbId": "6f621cfa",
        "listDescription": "This is a list of germplasm I would like to investigate next season",
        "listName": "MyGermplasm_Sept_2020",
        "listOwnerName": "Bob Robertson",
        "listOwnerPersonDbId": "58db0628",
        "listSize": 53,
        "listSource": "GeneBank Repository 1.3",
        "listType": "germplasm"
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




### Post - /search/lists [POST /brapi/v2/search/lists]

Submit a search request for Lists <br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/lists/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">dateCreatedRangeEnd</span></td><td>string<br>(date-time)</td><td>Define the end for an interval of time and only include Lists that are created within this interval.</td></tr>
<tr><td><span style="font-weight:bold;">dateCreatedRangeStart</span></td><td>string<br>(date-time)</td><td>Define the begining for an interval of time and only include Lists that are created within this interval.</td></tr>
<tr><td><span style="font-weight:bold;">dateModifiedRangeEnd</span></td><td>string<br>(date-time)</td><td>Define the end for an interval of time and only include Lists that are modified within this interval.</td></tr>
<tr><td><span style="font-weight:bold;">dateModifiedRangeStart</span></td><td>string<br>(date-time)</td><td>Define the begining for an interval of time and only include Lists that are modified within this interval.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">listDbIds</span></td><td>array[string]</td><td>An array of primary database identifiers to identify a set of Lists</td></tr>
<tr><td><span style="font-weight:bold;">listNames</span></td><td>array[string]</td><td>An array of human readable names to identify a set of Lists</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerNames</span></td><td>array[string]</td><td>An array of names for the people or entities who are responsible for a set of Lists</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbIds</span></td><td>array[string]</td><td>An array of primary database identifiers to identify people or entities who are responsible for a set of Lists</td></tr>
<tr><td><span style="font-weight:bold;">listSources</span></td><td>array[string]</td><td>An array of terms identifying lists from different sources (ie 'USER', 'SYSTEM', etc)</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string</td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "dateCreatedRangeEnd": "2018-01-01T14:47:23-0600",
    "dateCreatedRangeStart": "2018-01-01T14:47:23-0600",
    "dateModifiedRangeEnd": "2018-01-01T14:47:23-0600",
    "dateModifiedRangeStart": "2018-01-01T14:47:23-0600",
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
    "listDbIds": [
        "55f20cf6",
        "3193ca3d"
    ],
    "listNames": [
        "Planing List 1",
        "Bobs List"
    ],
    "listOwnerNames": [
        "Bob Robertson",
        "Rob Robertson"
    ],
    "listOwnerPersonDbIds": [
        "bob@bob.com",
        "rob@bob.com"
    ],
    "listSources": [
        "USER",
        "SYSTEM",
        "EXTERNAL"
    ],
    "listType": "germplasm",
    "page": 0,
    "pageSize": 1000,
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
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
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": "germplasm"
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




### Get - /search/lists/{searchResultsDbId} [GET /brapi/v2/search/lists/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `List` search request <br/>
Clients should submit a search request using the corresponding `POST /search/lists` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">listDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier for a List</td></tr>
<tr><td><span style="font-weight:bold;">listName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Human readable name of a List</td></tr>
<tr><td><span style="font-weight:bold;">listType</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A flag to indicate the type of objects that are referenced in a List</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">dateCreated</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was first created</td></tr>
<tr><td><span style="font-weight:bold;">dateModified</span></td><td>string<br>(date-time)</td><td>Timestamp when the entity was last updated</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">listDescription</span></td><td>string</td><td>Description of a List</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerName</span></td><td>string</td><td>Human readable name of a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listOwnerPersonDbId</span></td><td>string</td><td>The unique identifier for a List Owner. (usually a user or person)</td></tr>
<tr><td><span style="font-weight:bold;">listSize</span></td><td>integer</td><td>The number of elements in a List</td></tr>
<tr><td><span style="font-weight:bold;">listSource</span></td><td>string</td><td>The description of where a List originated from</td></tr>
</table>


 

+ Parameters
    + searchResultsDbId (Required, string) ... Unique identifier which references the search results
    + page (Optional, integer) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




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
                "dateCreated": "2018-01-01T14:47:23-0600",
                "dateModified": "2018-01-01T14:47:23-0600",
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
                "listDbId": "6f621cfa",
                "listDescription": "This is a list of germplasm I would like to investigate next season",
                "listName": "MyGermplasm_Sept_2020",
                "listOwnerName": "Bob Robertson",
                "listOwnerPersonDbId": "58db0628",
                "listSize": 53,
                "listSource": "GeneBank Repository 1.3",
                "listType": "germplasm"
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

