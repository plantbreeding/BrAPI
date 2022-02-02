# Group Germplasm Attribute Values
Germplasm "attributes" are simply-inherited characteristics (characterization descriptors) that are not environment-dependent but 
inherent in the germplasm line.  They include genes, QTLs, and genetic "traits" like wheat grain 
hardness.  They are often evaluated by genotyping for diagnostic markers.






### Get - /attributevalues [GET /brapi/v2/attributevalues{?attributeValueDbId}{?attributeDbId}{?attributeName}{?germplasmDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get the Germplasm Attribute Values



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|attributeValueDbId|string|The ID which uniquely identifies this attribute value within the given database server|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


 

+ Parameters
    + attributeValueDbId (Optional, ) ... The unique id for an attribute value
    + attributeDbId (Optional, ) ... The unique id for an attribute
    + attributeName (Optional, ) ... The human readable name for an attribute
    + germplasmDbId (Optional, ) ... Get all attributes associated with this germplasm
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. Use this parameter to only return results associated with the given program. Use `GET /programs` to find the list of available programs on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
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
                "attributeDbId": "e529dd5a",
                "attributeName": "Weevil Resistance",
                "attributeValueDbId": "33edbab7",
                "determinedDate": "2018-01-01T14:47:23-0600",
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
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "value": "Present"
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




### Post - /attributevalues [POST /brapi/v2/attributevalues]

Create new Germplasm Attribute Values

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|attributeValueDbId|string|The ID which uniquely identifies this attribute value within the given database server|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "attributeDbId": "e529dd5a",
        "attributeName": "Weevil Resistance",
        "determinedDate": "2018-01-01T14:47:23-0600",
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
        "germplasmDbId": "d4076594",
        "germplasmName": "A0000003",
        "value": "Present"
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
                "attributeDbId": "e529dd5a",
                "attributeName": "Weevil Resistance",
                "attributeValueDbId": "33edbab7",
                "determinedDate": "2018-01-01T14:47:23-0600",
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
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "value": "Present"
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




### Get - /attributevalues/{attributeValueDbId} [GET /brapi/v2/attributevalues/{attributeValueDbId}]

Get the details for a specific Germplasm Attribute



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|attributeValueDbId|string|The ID which uniquely identifies this attribute value within the given database server|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


 

+ Parameters
    + attributeValueDbId (Required, ) ... The unique id for an attribute value
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
        "attributeDbId": "e529dd5a",
        "attributeName": "Weevil Resistance",
        "attributeValueDbId": "33edbab7",
        "determinedDate": "2018-01-01T14:47:23-0600",
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
        "germplasmDbId": "d4076594",
        "germplasmName": "A0000003",
        "value": "Present"
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




### Put - /attributevalues/{attributeValueDbId} [PUT /brapi/v2/attributevalues/{attributeValueDbId}/]

Update an existing Germplasm Attribute Value

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|attributeValueDbId|string|The ID which uniquely identifies this attribute value within the given database server|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


 

+ Parameters
    + attributeValueDbId (Required, ) ... The unique id for an attribute value
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "attributeDbId": "e529dd5a",
    "attributeName": "Weevil Resistance",
    "determinedDate": "2018-01-01T14:47:23-0600",
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
    "germplasmDbId": "d4076594",
    "germplasmName": "A0000003",
    "value": "Present"
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
        "attributeDbId": "e529dd5a",
        "attributeName": "Weevil Resistance",
        "attributeValueDbId": "33edbab7",
        "determinedDate": "2018-01-01T14:47:23-0600",
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
        "germplasmDbId": "d4076594",
        "germplasmName": "A0000003",
        "value": "Present"
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




### Post - /search/attributevalues [POST /brapi/v2/search/attributevalues]

Submit a search request for Germplasm `AttributeValues`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/attributevalues/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|attributeDbIds|array[string]|List of Germplasm Attribute IDs to search for|
|attributeNames|array[string]|List of human readable Germplasm Attribute names to search for|
|attributeValueDbIds|array[string]|List of Germplasm Attribute Value IDs to search for|
|commonCropNames|array[string]|The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.|
|dataTypes|array[string]|List of scale data types to filter search results|
|externalReferenceIDs|array[string]|**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceIds|array[string]|List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceSources|array[string]|List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm to search for|
|germplasmNames|array[string]|List of human readable names to identify germplasm to search for|
|methodDbIds|array[string]|List of methods to filter search results|
|ontologyDbIds|array[string]|List of ontology IDs to search for|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|programDbIds|array[string]|A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.|
|programNames|array[string]|Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.|
|scaleDbIds|array[string]|List of scales to filter search results|
|traitClasses|array[string]|List of trait classes to filter search results|
|traitDbIds|array[string]|List of trait unique ID to filter search results|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|attributeValueDbId|string|The ID which uniquely identifies this attribute value within the given database server|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "attributeDbIds": [
        "2ef15c9f",
        "318e7f7d"
    ],
    "attributeNames": [
        "Plant Height 1",
        "Root Color"
    ],
    "attributeValueDbIds": [
        "ca4636d0",
        "c8a92409"
    ],
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "dataTypes": [
        "Numerical",
        "Ordinal",
        "Text"
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
    "germplasmDbIds": [
        "e9c6edd7",
        "1b1df4a6"
    ],
    "germplasmNames": [
        "A0000003",
        "A0000477"
    ],
    "methodDbIds": [
        "07e34f83",
        "d3d5517a"
    ],
    "ontologyDbIds": [
        "f44f7b23",
        "a26b576e"
    ],
    "page": 0,
    "pageSize": 1000,
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "scaleDbIds": [
        "a13ecffa",
        "7e1afe4f"
    ],
    "traitClasses": [
        "morphological",
        "phenological",
        "agronomical"
    ],
    "traitDbIds": [
        "ef81147b",
        "78d82fad"
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
                "attributeDbId": "e529dd5a",
                "attributeName": "Weevil Resistance",
                "attributeValueDbId": "33edbab7",
                "determinedDate": "2018-01-01T14:47:23-0600",
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
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "value": "Present"
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




### Get - /search/attributevalues/{searchResultsDbId} [GET /brapi/v2/search/attributevalues/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a Germplasm `AttributeValues` search request <br/>
Clients should submit a search request using the corresponding `POST /search/attributevalues` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|A human readable name for this attribute|
|attributeValueDbId|string|The ID which uniquely identifies this attribute value within the given database server|
|determinedDate|string (date-time)|The date the value of this attribute was determined for a given germplasm|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|value|string|The value of this attribute for a given germplasm|


 

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
                "attributeDbId": "e529dd5a",
                "attributeName": "Weevil Resistance",
                "attributeValueDbId": "33edbab7",
                "determinedDate": "2018-01-01T14:47:23-0600",
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
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "value": "Present"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

