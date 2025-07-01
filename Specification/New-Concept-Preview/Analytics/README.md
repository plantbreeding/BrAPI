# Group Analytics
Analytics group description





### Post - /delete/files [POST /brapi/v2/delete/files]

Submit a delete request for `Files`

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">fileDbIds</span></td><td>array[string]</td><td>A list of file Ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">fileNames</span></td><td>array[string]</td><td>File file names to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileSizeMax</span></td><td>integer</td><td>A maximum file file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileSizeMin</span></td><td>integer</td><td>A minimum file file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStampRangeEnd</span></td><td>string<br>(date-time)</td><td>The latest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStampRangeStart</span></td><td>string<br>(date-time)</td><td>The earliest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">mimeTypes</span></td><td>array[string]</td><td>A set of file file types to search for.</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbIds</span></td><td>array[string]<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique ids of the File records which have been successfully deleted</td></tr>
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
    "fileDbIds": [
        "564b64a6",
        "0d122d1d"
    ],
    "fileNames": [
        "file_01032019.jpg",
        "picture_field_1234.jpg"
    ],
    "fileSizeMax": 20000000,
    "fileSizeMin": 1000,
    "fileTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "fileTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "mimeTypes": [
        "application/json",
        "text/csv",
        "application/vcf"
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
        "fileDbIds": [
            "6a4a59d8",
            "3ff067e0"
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




### Get - /files [GET /brapi/v2/files{?fileDbId}{?fileName}{?commonCropName}{?programDbId}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get filtered set of file metadata

Implementation Notes

- ''fileURL'' should be a complete URL describing the location of the file. There is no BrAPI call for 
retrieving the file content, so it could be on a different path, or a different host.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of an file</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
</table>


 

+ Parameters
    + fileDbId (Optional, string) ... The unique identifier for a file
    + fileName (Optional, string) ... The human readable name of an file
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
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
                "copyright": "Copyright 2018 Bob Robertson",
                "dataType": "VCFW",
                "description": "This is a picture of a tomato",
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
                "fileDbId": "a55efb9c",
                "fileName": "file_0000231.jpg",
                "fileSize": 50000,
                "fileSource": "Output from analsys job xyz123",
                "fileTimeStamp": "2018-01-01T14:47:23-0600",
                "fileURL": "https://wiki.brapi.org/files/tomato",
                "mimeType": "application/vcf"
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




### Post - /files [POST /brapi/v2/files]

Create new file metadata records

Implementation Notes

- This endpoint should be implemented with 'PUT /files/{fileDbId}/filecontent' for full file upload capability

- ''fileURL'' should be a complete URL describing the location of the file. There is no BrAPI call for retrieving 
the file content, so it could be on a different path, or a different host.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of an file</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "copyright": "Copyright 2018 Bob Robertson",
        "dataType": "VCFW",
        "description": "This is a picture of a tomato",
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
        "fileName": "file_0000231.jpg",
        "fileSize": 50000,
        "fileSource": "Output from analsys job xyz123",
        "fileTimeStamp": "2018-01-01T14:47:23-0600",
        "fileURL": "https://wiki.brapi.org/files/tomato",
        "mimeType": "application/vcf"
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
                "copyright": "Copyright 2018 Bob Robertson",
                "dataType": "VCFW",
                "description": "This is a picture of a tomato",
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
                "fileDbId": "a55efb9c",
                "fileName": "file_0000231.jpg",
                "fileSize": 50000,
                "fileSource": "Output from analsys job xyz123",
                "fileTimeStamp": "2018-01-01T14:47:23-0600",
                "fileURL": "https://wiki.brapi.org/files/tomato",
                "mimeType": "application/vcf"
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




### Get - /files/{fileDbId} [GET /brapi/v2/files/{fileDbId}]

Get one file metadata object

Implementation Notes

- ''fileURL'' should be a complete URL describing the location of the file. There is no BrAPI call for 
retrieving the file content, so it could be on a different path, or a different host.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of an file</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
</table>


 

+ Parameters
    + fileDbId (Required, string) ... The unique identifier for a file
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
        "copyright": "Copyright 2018 Bob Robertson",
        "dataType": "VCFW",
        "description": "This is a picture of a tomato",
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
        "fileDbId": "a55efb9c",
        "fileName": "file_0000231.jpg",
        "fileSize": 50000,
        "fileSource": "Output from analsys job xyz123",
        "fileTimeStamp": "2018-01-01T14:47:23-0600",
        "fileURL": "https://wiki.brapi.org/files/tomato",
        "mimeType": "application/vcf"
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




### Put - /files/{fileDbId} [PUT /brapi/v2/files/{fileDbId}/]

Update an existing file metadata record

Implementation Notes

- This endpoint should be implemented with 'PUT /files/{fileDbId}/filecontent' for full file update capability

- A server may choose to modify the file metadata object based on the actually file which has been uploaded. 

- File data may be stored in a database or file system. Servers should generate and provide the "fileURL" as an 
absolute path for retrieving the file, wherever it happens to live. 

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of an file</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
</table>


 

+ Parameters
    + fileDbId (Required, string) ... The unique identifier for a file
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "copyright": "Copyright 2018 Bob Robertson",
    "dataType": "VCFW",
    "description": "This is a picture of a tomato",
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
    "fileName": "file_0000231.jpg",
    "fileSize": 50000,
    "fileSource": "Output from analsys job xyz123",
    "fileTimeStamp": "2018-01-01T14:47:23-0600",
    "fileURL": "https://wiki.brapi.org/files/tomato",
    "mimeType": "application/vcf"
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
        "copyright": "Copyright 2018 Bob Robertson",
        "dataType": "VCFW",
        "description": "This is a picture of a tomato",
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
        "fileDbId": "a55efb9c",
        "fileName": "file_0000231.jpg",
        "fileSize": 50000,
        "fileSource": "Output from analsys job xyz123",
        "fileTimeStamp": "2018-01-01T14:47:23-0600",
        "fileURL": "https://wiki.brapi.org/files/tomato",
        "mimeType": "application/vcf"
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




### Put - /files/{fileDbId}/filecontent [PUT /brapi/v2/files/{fileDbId}/filecontent]

This endpoint is used to attach an file binary file to an existing file metadata record. All of the other Files endpoints 
deal with the JSON for file metadata, but 'PUT /files/{fileDbId}/filecontent' allows you to send any binary file with a Content 
Type (MIME) of file/*. When the real file is uploaded, the server may choose to update some of the metadata to reflect the 
reality of the file that was uploaded, and should respond with the updated JSON.

Implementation Notes

- This endpoint should be implemented with 'POST /files' for full file upload capability

- This endpoint should be implemented with 'PUT /files/{fileDbId}' for full file update capability

- A server may choose to modify the file metadata object based on the actually file which has been uploaded by this endpoint. 

- File data may be stored in a database or file system. Servers should generate and provide the "fileURL" for retrieving the 
  file binary file. 



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of an file</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
</table>


 

+ Parameters
    + fileDbId (Required, string) ... The unique identifier for an file
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
        "copyright": "Copyright 2018 Bob Robertson",
        "dataType": "VCFW",
        "description": "This is a picture of a tomato",
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
        "fileDbId": "a55efb9c",
        "fileName": "file_0000231.jpg",
        "fileSize": 50000,
        "fileSource": "Output from analsys job xyz123",
        "fileTimeStamp": "2018-01-01T14:47:23-0600",
        "fileURL": "https://wiki.brapi.org/files/tomato",
        "mimeType": "application/vcf"
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




### Get - /jobs [GET /brapi/v2/jobs{?jobDbId}{?jobName}{?procedureDbId}{?procedureName}{?commonCropName}{?programDbId}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get the analysis jobs metadata summaries



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">brapiDataParameters</span></td><td>array[object]</td><td>Input data expected from a BrAPI source</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.authToken</span></td><td>string</td><td>The Bearer Auth token for the remote BrAPI server, if applicable</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiBaseURL</span></td><td>string</td><td>The base URL for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameters</span></td><td>array[object]</td><td>The list of parameters to be used to perform the BrAPI Query.</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterName</span></td><td>string</td><td>Name of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterType</span></td><td>string</td><td>The type of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterValue</span></td><td>string</td><td>The value of this parameter to be used in the BrAPI query</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiVersions</span></td><td>array[string]</td><td>The supported versions of the BrAPI spec for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The BrAPI class type expected</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.search</span></td><td>boolean</td><td>If true, use the 'POST /search/entity' endpoint instead of the basic 'GET /entity' endpoint</td></tr>
<tr><td><span style="font-weight:bold;">controlParameters</span></td><td>array[object]</td><td>The date and time the file was taken</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterValue</span></td><td>string</td><td>value sent for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of a running job.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileDataParameters</span></td><td>array[object]</td><td>Input data expected from a non-BrAPI source</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">jobCurrentStatus</span></td><td>string</td><td>The status of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">jobOutput</span></td><td>array[object]</td><td>list of output data objects from the job</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
<tr><td><span style="font-weight:bold;">jobStatusMessages</span></td><td>array[object]</td><td>A human readable message describing the current state of the Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.message</span></td><td>string</td><td>A human readable message describing the Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>The status of a Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.timestamp</span></td><td>string<br>(date-time)</td><td>timestamp for this logging message</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
</table>


 

+ Parameters
    + jobDbId (Optional, string) ... The unique identifier for a Job
    + jobName (Optional, string) ... The human readable name of a Job
    + procedureDbId (Optional, string) ... The unique identifier for a procedure
    + procedureName (Optional, string) ... The human readable name of a procedure
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
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
                "brapiDataParameters": [
                    {
                        "authToken": "Bearer ef0ab6c9...",
                        "brapiBaseURL": "https://test-server.brapi.org/brapi/v2/",
                        "brapiParameters": [
                            {
                                "brapiParameterName": "studyDbId",
                                "brapiParameterType": "string",
                                "brapiParameterValue": "65bf336c"
                            }
                        ],
                        "brapiVersions": [
                            "V2.1",
                            "V2.0",
                            "V1.3"
                        ],
                        "dataType": "Observations",
                        "parameterId": "665b33cf",
                        "search": false
                    }
                ],
                "controlParameters": [
                    {
                        "parameterId": "665b33cf",
                        "parameterValue": "100"
                    }
                ],
                "description": "Bob Robertson first attempt to run GWAS on a remote server",
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
                "fileDataParameters": [
                    {
                        "dataType": "EPW",
                        "fileSize": 50000,
                        "fileTimeStamp": "2018-01-01T14:47:23-0600",
                        "fileURL": "https://wiki.brapi.org/files/tomato",
                        "mimeType": "application/epw",
                        "parameterId": "665b33cf"
                    }
                ],
                "jobCurrentStatus": "RUNNING",
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "jobOutput": [
                    {
                        "dataType": "Observations",
                        "fileSize": 50000,
                        "fileTimeStamp": "2018-01-01T14:47:23-0600",
                        "fileURL": "https://test-server.brapi.org/brapi/v2/observations?studyDbId=4f1a2630",
                        "mimeType": "application/json"
                    }
                ],
                "jobStatusMessages": [
                    {
                        "message": "Running procedure 101, 8 out of 10 tasks complete",
                        "status": "RUNNING",
                        "timestamp": "2018-01-01T14:47:23-0600"
                    }
                ],
                "procedureDbId": "a3b45b23"
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




### Post - /jobs [POST /brapi/v2/jobs]

Submit a new analysis job

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">brapiDataParameters</span></td><td>array[object]</td><td>Input data expected from a BrAPI source</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.authToken</span></td><td>string</td><td>The Bearer Auth token for the remote BrAPI server, if applicable</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiBaseURL</span></td><td>string</td><td>The base URL for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameters</span></td><td>array[object]</td><td>The list of parameters to be used to perform the BrAPI Query.</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterName</span></td><td>string</td><td>Name of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterType</span></td><td>string</td><td>The type of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterValue</span></td><td>string</td><td>The value of this parameter to be used in the BrAPI query</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiVersions</span></td><td>array[string]</td><td>The supported versions of the BrAPI spec for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The BrAPI class type expected</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.search</span></td><td>boolean</td><td>If true, use the 'POST /search/entity' endpoint instead of the basic 'GET /entity' endpoint</td></tr>
<tr><td><span style="font-weight:bold;">controlParameters</span></td><td>array[object]</td><td>The date and time the file was taken</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterValue</span></td><td>string</td><td>value sent for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of a running job.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileDataParameters</span></td><td>array[object]</td><td>Input data expected from a non-BrAPI source</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">brapiDataParameters</span></td><td>array[object]</td><td>Input data expected from a BrAPI source</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.authToken</span></td><td>string</td><td>The Bearer Auth token for the remote BrAPI server, if applicable</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiBaseURL</span></td><td>string</td><td>The base URL for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameters</span></td><td>array[object]</td><td>The list of parameters to be used to perform the BrAPI Query.</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterName</span></td><td>string</td><td>Name of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterType</span></td><td>string</td><td>The type of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterValue</span></td><td>string</td><td>The value of this parameter to be used in the BrAPI query</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiVersions</span></td><td>array[string]</td><td>The supported versions of the BrAPI spec for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The BrAPI class type expected</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.search</span></td><td>boolean</td><td>If true, use the 'POST /search/entity' endpoint instead of the basic 'GET /entity' endpoint</td></tr>
<tr><td><span style="font-weight:bold;">controlParameters</span></td><td>array[object]</td><td>The date and time the file was taken</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterValue</span></td><td>string</td><td>value sent for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of a running job.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileDataParameters</span></td><td>array[object]</td><td>Input data expected from a non-BrAPI source</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">jobCurrentStatus</span></td><td>string</td><td>The status of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">jobOutput</span></td><td>array[object]</td><td>list of output data objects from the job</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
<tr><td><span style="font-weight:bold;">jobStatusMessages</span></td><td>array[object]</td><td>A human readable message describing the current state of the Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.message</span></td><td>string</td><td>A human readable message describing the Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>The status of a Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.timestamp</span></td><td>string<br>(date-time)</td><td>timestamp for this logging message</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "brapiDataParameters": [
            {
                "authToken": "Bearer ef0ab6c9...",
                "brapiBaseURL": "https://test-server.brapi.org/brapi/v2/",
                "brapiParameters": [
                    {
                        "brapiParameterName": "studyDbId",
                        "brapiParameterType": "string",
                        "brapiParameterValue": "65bf336c"
                    }
                ],
                "brapiVersions": [
                    "V2.1",
                    "V2.0",
                    "V1.3"
                ],
                "dataType": "Observations",
                "parameterId": "665b33cf",
                "search": false
            }
        ],
        "controlParameters": [
            {
                "parameterId": "665b33cf",
                "parameterValue": "100"
            }
        ],
        "description": "Bob Robertson first attempt to run GWAS on a remote server",
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
        "fileDataParameters": [
            {
                "dataType": "EPW",
                "fileSize": 50000,
                "fileTimeStamp": "2018-01-01T14:47:23-0600",
                "fileURL": "https://wiki.brapi.org/files/tomato",
                "mimeType": "application/epw",
                "parameterId": "665b33cf"
            }
        ],
        "jobName": "Bob Robertson First GWAS",
        "procedureDbId": "a3b45b23"
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
                "brapiDataParameters": [
                    {
                        "authToken": "Bearer ef0ab6c9...",
                        "brapiBaseURL": "https://test-server.brapi.org/brapi/v2/",
                        "brapiParameters": [
                            {
                                "brapiParameterName": "studyDbId",
                                "brapiParameterType": "string",
                                "brapiParameterValue": "65bf336c"
                            }
                        ],
                        "brapiVersions": [
                            "V2.1",
                            "V2.0",
                            "V1.3"
                        ],
                        "dataType": "Observations",
                        "parameterId": "665b33cf",
                        "search": false
                    }
                ],
                "controlParameters": [
                    {
                        "parameterId": "665b33cf",
                        "parameterValue": "100"
                    }
                ],
                "description": "Bob Robertson first attempt to run GWAS on a remote server",
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
                "fileDataParameters": [
                    {
                        "dataType": "EPW",
                        "fileSize": 50000,
                        "fileTimeStamp": "2018-01-01T14:47:23-0600",
                        "fileURL": "https://wiki.brapi.org/files/tomato",
                        "mimeType": "application/epw",
                        "parameterId": "665b33cf"
                    }
                ],
                "jobCurrentStatus": "RUNNING",
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "jobOutput": [
                    {
                        "dataType": "Observations",
                        "fileSize": 50000,
                        "fileTimeStamp": "2018-01-01T14:47:23-0600",
                        "fileURL": "https://test-server.brapi.org/brapi/v2/observations?studyDbId=4f1a2630",
                        "mimeType": "application/json"
                    }
                ],
                "jobStatusMessages": [
                    {
                        "message": "Running procedure 101, 8 out of 10 tasks complete",
                        "status": "RUNNING",
                        "timestamp": "2018-01-01T14:47:23-0600"
                    }
                ],
                "procedureDbId": "a3b45b23"
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




### Get - /jobs/{jobDbId} [GET /brapi/v2/jobs/{jobDbId}]

Get a specific analysis job



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">brapiDataParameters</span></td><td>array[object]</td><td>Input data expected from a BrAPI source</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.authToken</span></td><td>string</td><td>The Bearer Auth token for the remote BrAPI server, if applicable</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiBaseURL</span></td><td>string</td><td>The base URL for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameters</span></td><td>array[object]</td><td>The list of parameters to be used to perform the BrAPI Query.</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterName</span></td><td>string</td><td>Name of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterType</span></td><td>string</td><td>The type of the parameter from the BrAPI specification</td></tr>
<tr><td>brapiDataParameters<br>.brapiParameters<br><span style="font-weight:bold;margin-left:5px">.brapiParameterValue</span></td><td>string</td><td>The value of this parameter to be used in the BrAPI query</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.brapiVersions</span></td><td>array[string]</td><td>The supported versions of the BrAPI spec for a BrAPI compatible server</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The BrAPI class type expected</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.search</span></td><td>boolean</td><td>If true, use the 'POST /search/entity' endpoint instead of the basic 'GET /entity' endpoint</td></tr>
<tr><td><span style="font-weight:bold;">controlParameters</span></td><td>array[object]</td><td>The date and time the file was taken</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterValue</span></td><td>string</td><td>value sent for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of a running job.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileDataParameters</span></td><td>array[object]</td><td>Input data expected from a non-BrAPI source</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileSize</span></td><td>integer</td><td>The size of the image in Bytes.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td><span style="font-weight:bold;">jobCurrentStatus</span></td><td>string</td><td>The status of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">jobOutput</span></td><td>array[object]</td><td>list of output data objects from the job</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td>jobOutput<br><span style="font-weight:bold;margin-left:5px">.mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
<tr><td><span style="font-weight:bold;">jobStatusMessages</span></td><td>array[object]</td><td>A human readable message describing the current state of the Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.message</span></td><td>string</td><td>A human readable message describing the Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.status</span></td><td>string</td><td>The status of a Job</td></tr>
<tr><td>jobStatusMessages<br><span style="font-weight:bold;margin-left:5px">.timestamp</span></td><td>string<br>(date-time)</td><td>timestamp for this logging message</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
</table>


 

+ Parameters
    + jobDbId (Required, string) ... The unique identifier for a job
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
        "brapiDataParameters": [
            {
                "authToken": "Bearer ef0ab6c9...",
                "brapiBaseURL": "https://test-server.brapi.org/brapi/v2/",
                "brapiParameters": [
                    {
                        "brapiParameterName": "studyDbId",
                        "brapiParameterType": "string",
                        "brapiParameterValue": "65bf336c"
                    }
                ],
                "brapiVersions": [
                    "V2.1",
                    "V2.0",
                    "V1.3"
                ],
                "dataType": "Observations",
                "parameterId": "665b33cf",
                "search": false
            }
        ],
        "controlParameters": [
            {
                "parameterId": "665b33cf",
                "parameterValue": "100"
            }
        ],
        "description": "Bob Robertson first attempt to run GWAS on a remote server",
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
        "fileDataParameters": [
            {
                "dataType": "EPW",
                "fileSize": 50000,
                "fileTimeStamp": "2018-01-01T14:47:23-0600",
                "fileURL": "https://wiki.brapi.org/files/tomato",
                "mimeType": "application/epw",
                "parameterId": "665b33cf"
            }
        ],
        "jobCurrentStatus": "RUNNING",
        "jobDbId": "a55efb9c",
        "jobName": "Bob Robertson First GWAS",
        "jobOutput": [
            {
                "dataType": "Observations",
                "fileSize": 50000,
                "fileTimeStamp": "2018-01-01T14:47:23-0600",
                "fileURL": "https://test-server.brapi.org/brapi/v2/observations?studyDbId=4f1a2630",
                "mimeType": "application/json"
            }
        ],
        "jobStatusMessages": [
            {
                "message": "Running procedure 101, 8 out of 10 tasks complete",
                "status": "RUNNING",
                "timestamp": "2018-01-01T14:47:23-0600"
            }
        ],
        "procedureDbId": "a3b45b23"
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




### Get - /metrics [GET /brapi/v2/metrics{?jobDbId}{?jobName}{?procedureDbId}{?procedureName}{?variableDbId}{?variableName}{?parameterName}{?commonCropName}{?programDbId}{?studyDbId}{?studyName}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get the analysis metrics available on a server



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">metricDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Metric</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
</table>


 

+ Parameters
    + jobDbId (Optional, string) ... The unique identifier for a Job
    + jobName (Optional, string) ... The human readable name of a Job
    + procedureDbId (Optional, string) ... The unique identifier for a procedure
    + procedureName (Optional, string) ... The human readable name of a procedure
    + variableDbId (Optional, string) ... The unique identifier for a variable
    + variableName (Optional, string) ... The human readable name of a variable
    + parameterName (Optional, string) ... The human readable name of a procedure parameter
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + studyDbId (Optional, string) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + studyName (Optional, string) ... Use this parameter to only return results associated with the given `Study` by its human readable name. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
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
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "metricDbId": "5ceb9fa5",
                "metricDescription": "vg/(vg+ve)-designation",
                "metricName": "plotH2_designation",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "standardError": "0.0034",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "0.6637"
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




### Post - /metrics [POST /brapi/v2/metrics]

Create new Metric records

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">metricDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Metric</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
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
        "jobDbId": "a55efb9c",
        "jobName": "Bob Robertson First GWAS",
        "metricDescription": "vg/(vg+ve)-designation",
        "metricName": "plotH2_designation",
        "observationVariableDbId": "b95efca5",
        "observationVariableName": "Plant_Height_cm",
        "procedureDbId": "a3b45b23",
        "procedureName": "REMOTE-GWAS",
        "standardError": "0.0034",
        "studyDbId": "9a5c5efb",
        "studyName": "BrAPI Wheat - NY 2023",
        "value": "0.6637"
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
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "metricDbId": "5ceb9fa5",
                "metricDescription": "vg/(vg+ve)-designation",
                "metricName": "plotH2_designation",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "standardError": "0.0034",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "0.6637"
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




### Get - /metrics/{metricDbId} [GET /brapi/v2/metrics/{metricDbId}]

Get the analysis metrics available on a server



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">metricDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Metric</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
</table>


 

+ Parameters
    + metricDbId (Required, string) ... The unique identifier for a metric value
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
        "jobDbId": "a55efb9c",
        "jobName": "Bob Robertson First GWAS",
        "metricDbId": "5ceb9fa5",
        "metricDescription": "vg/(vg+ve)-designation",
        "metricName": "plotH2_designation",
        "observationVariableDbId": "b95efca5",
        "observationVariableName": "Plant_Height_cm",
        "procedureDbId": "a3b45b23",
        "procedureName": "REMOTE-GWAS",
        "standardError": "0.0034",
        "studyDbId": "9a5c5efb",
        "studyName": "BrAPI Wheat - NY 2023",
        "value": "0.6637"
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




### Put - /metrics/{metricDbId} [PUT /brapi/v2/metrics/{metricDbId}/]

Update an existing Metric record

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">metricDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Metric</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
</table>


 

+ Parameters
    + metricDbId (Required, string) ... The unique identifier for a file
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
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
    "jobDbId": "a55efb9c",
    "jobName": "Bob Robertson First GWAS",
    "metricDescription": "vg/(vg+ve)-designation",
    "metricName": "plotH2_designation",
    "observationVariableDbId": "b95efca5",
    "observationVariableName": "Plant_Height_cm",
    "procedureDbId": "a3b45b23",
    "procedureName": "REMOTE-GWAS",
    "standardError": "0.0034",
    "studyDbId": "9a5c5efb",
    "studyName": "BrAPI Wheat - NY 2023",
    "value": "0.6637"
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
        "jobDbId": "a55efb9c",
        "jobName": "Bob Robertson First GWAS",
        "metricDbId": "5ceb9fa5",
        "metricDescription": "vg/(vg+ve)-designation",
        "metricName": "plotH2_designation",
        "observationVariableDbId": "b95efca5",
        "observationVariableName": "Plant_Height_cm",
        "procedureDbId": "a3b45b23",
        "procedureName": "REMOTE-GWAS",
        "standardError": "0.0034",
        "studyDbId": "9a5c5efb",
        "studyName": "BrAPI Wheat - NY 2023",
        "value": "0.6637"
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




### Get - /predictions [GET /brapi/v2/predictions{?jobDbId}{?jobName}{?procedureDbId}{?procedureName}{?observationVariableDbId}{?observationVariableName}{?parameterName}{?commonCropName}{?programDbId}{?studyDbId}{?studyName}{?germplasmDbId}{?germplasmName}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get the analysis predictions available on a server



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">predictionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Prediction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
</table>


 

+ Parameters
    + jobDbId (Optional, string) ... The unique identifier for a Job
    + jobName (Optional, string) ... The human readable name of a Job
    + procedureDbId (Optional, string) ... The unique identifier for a procedure
    + procedureName (Optional, string) ... The human readable name of a procedure
    + observationVariableDbId (Optional, string) ... The unique identifier for a variable
    + observationVariableName (Optional, string) ... The human readable name of a variable
    + parameterName (Optional, string) ... The human readable name of a procedure parameter
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + studyDbId (Optional, string) ... Use this parameter to only return results associated with the given `Study` unique identifier. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + studyName (Optional, string) ... Use this parameter to only return results associated with the given `Study` by its human readable name. <br/>Use `GET /studies` to find the list of available `Studies` on a server.
    + germplasmDbId (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + germplasmName (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` by its human readable name. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
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
                "germplasmDbId": "029d705d",
                "germplasmName": "A0000003",
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "predictionDbId": "43ab644f",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "reliability": "0.993",
                "standardError": "28.7",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "1026.4"
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




### Post - /predictions [POST /brapi/v2/predictions]

Create new Prediction records

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">predictionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Prediction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
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
        "germplasmDbId": "029d705d",
        "germplasmName": "A0000003",
        "jobDbId": "a55efb9c",
        "jobName": "Bob Robertson First GWAS",
        "observationVariableDbId": "b95efca5",
        "observationVariableName": "Plant_Height_cm",
        "procedureDbId": "a3b45b23",
        "procedureName": "REMOTE-GWAS",
        "reliability": "0.993",
        "standardError": "28.7",
        "studyDbId": "9a5c5efb",
        "studyName": "BrAPI Wheat - NY 2023",
        "value": "1026.4"
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
                "germplasmDbId": "029d705d",
                "germplasmName": "A0000003",
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "predictionDbId": "43ab644f",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "reliability": "0.993",
                "standardError": "28.7",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "1026.4"
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




### Get - /predictions/{predictionDbId} [GET /brapi/v2/predictions/{predictionDbId}]

Get the analysis predictions available on a server



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">predictionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Prediction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
</table>


 

+ Parameters
    + predictionDbId (Required, string) ... The unique identifier for a prediction value
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
        "germplasmDbId": "029d705d",
        "germplasmName": "A0000003",
        "jobDbId": "a55efb9c",
        "jobName": "Bob Robertson First GWAS",
        "observationVariableDbId": "b95efca5",
        "observationVariableName": "Plant_Height_cm",
        "predictionDbId": "43ab644f",
        "procedureDbId": "a3b45b23",
        "procedureName": "REMOTE-GWAS",
        "reliability": "0.993",
        "standardError": "28.7",
        "studyDbId": "9a5c5efb",
        "studyName": "BrAPI Wheat - NY 2023",
        "value": "1026.4"
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




### Put - /predictions/{predictionDbId} [PUT /brapi/v2/predictions/{predictionDbId}/]

Update an existing Prediction record

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">predictionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Prediction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
</table>


 

+ Parameters
    + predictionDbId (Required, string) ... The unique identifier for a file
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
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
    "germplasmDbId": "029d705d",
    "germplasmName": "A0000003",
    "jobDbId": "a55efb9c",
    "jobName": "Bob Robertson First GWAS",
    "observationVariableDbId": "b95efca5",
    "observationVariableName": "Plant_Height_cm",
    "procedureDbId": "a3b45b23",
    "procedureName": "REMOTE-GWAS",
    "reliability": "0.993",
    "standardError": "28.7",
    "studyDbId": "9a5c5efb",
    "studyName": "BrAPI Wheat - NY 2023",
    "value": "1026.4"
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
        "germplasmDbId": "029d705d",
        "germplasmName": "A0000003",
        "jobDbId": "a55efb9c",
        "jobName": "Bob Robertson First GWAS",
        "observationVariableDbId": "b95efca5",
        "observationVariableName": "Plant_Height_cm",
        "predictionDbId": "43ab644f",
        "procedureDbId": "a3b45b23",
        "procedureName": "REMOTE-GWAS",
        "reliability": "0.993",
        "standardError": "28.7",
        "studyDbId": "9a5c5efb",
        "studyName": "BrAPI Wheat - NY 2023",
        "value": "1026.4"
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




### Get - /procedures [GET /brapi/v2/procedures{?procedureDbId}{?procedureName}{?commonCropName}{?programDbId}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get the analysis procedures available on a server



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">brapiDataParameters</span></td><td>array[object]</td><td>Input data expected from a BrAPI compliant source</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.alternativeParameters</span></td><td>array[string]</td><td>Alternate parameter ids that would provide the same input data</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The BrAPI class type expected</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterName</span></td><td>string</td><td>Human readable identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.required</span></td><td>boolean</td><td>Is this parameter required for the job to run</td></tr>
<tr><td><span style="font-weight:bold;">controlParameters</span></td><td>array[object]</td><td>Simple parameters for controlling the job</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.defaultValue</span></td><td>string</td><td>The default value used if the parameter is not provided. Required should be false if DefaultValue is present.</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.exampleValue</span></td><td>string</td><td>An example of what this parameter might look like</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterName</span></td><td>string</td><td>Human readable identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.required</span></td><td>boolean</td><td>Is this parameter required for the job to run</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of a running job.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string</td><td>A link to further documentation describing a procedure</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileDataParameters</span></td><td>array[object]</td><td>Input data expected from a non-BrAPI source</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.alternativeParameters</span></td><td>array[string]</td><td>Alternate parameter ids that would provide the same input data</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataTypes</span></td><td>array[string]</td><td>The accepted list of data types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.mimeTypes</span></td><td>array[string]</td><td>The accepted list of file MIME types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterName</span></td><td>string</td><td>Human readable identifier for this parameter</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.required</span></td><td>boolean</td><td>Is this parameter required for the job to run</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>A version number or identifier for a procedure</td></tr>
</table>


 

+ Parameters
    + procedureDbId (Optional, string) ... The unique identifier for a procedure
    + procedureName (Optional, string) ... The human readable name of a procedure
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
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
                "brapiDataParameters": [
                    {
                        "alternativeParameters": [
                            "alternativeParameters1",
                            "alternativeParameters2"
                        ],
                        "dataType": "Observations",
                        "parameterId": "665b33cf",
                        "parameterName": "Number of Cycles",
                        "required": "100"
                    }
                ],
                "controlParameters": [
                    {
                        "dataType": {
                            "additionalInfo": {},
                            "dataType": "Numerical",
                            "decimalPlaces": 2,
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
                            "ontologyReference": {
                                "documentationLinks": [
                                    {
                                        "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                        "type": "OBO"
                                    }
                                ],
                                "ontologyDbId": "6b071868",
                                "ontologyName": "The Crop Ontology",
                                "version": "7.2.3"
                            },
                            "scaleName": "Meters",
                            "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                            "units": "m",
                            "validValues": {
                                "categories": [
                                    {
                                        "label": "low",
                                        "value": "0"
                                    },
                                    {
                                        "label": "medium",
                                        "value": "5"
                                    },
                                    {
                                        "label": "high",
                                        "value": "10"
                                    }
                                ],
                                "max": 9999,
                                "maximumValue": "9999",
                                "min": 2,
                                "minimumValue": "2"
                            }
                        },
                        "defaultValue": "100",
                        "exampleValue": "100",
                        "parameterId": "665b33cf",
                        "parameterName": "Number of Cycles",
                        "required": "100"
                    }
                ],
                "description": "Bob Robertson first attempt to run GWAS on a remote server",
                "documentationURL": "https://plantbreeding.github.io/tool-documentation",
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
                "fileDataParameters": [
                    {
                        "alternativeParameters": [
                            "alternativeParameters1",
                            "alternativeParameters2"
                        ],
                        "dataTypes": [
                            "EPW",
                            "VCF"
                        ],
                        "mimeTypes": [
                            "application/epw",
                            "application/vcf"
                        ],
                        "parameterId": "665b33cf",
                        "parameterName": "Weather Data",
                        "required": "100"
                    }
                ],
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "version": "v2.3"
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




### Get - /procedures/{procedureDbId} [GET /brapi/v2/procedures/{procedureDbId}]

Get a specific analysis procedure



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">brapiDataParameters</span></td><td>array[object]</td><td>Input data expected from a BrAPI compliant source</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.alternativeParameters</span></td><td>array[string]</td><td>Alternate parameter ids that would provide the same input data</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td>The BrAPI class type expected</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterName</span></td><td>string</td><td>Human readable identifier for this parameter</td></tr>
<tr><td>brapiDataParameters<br><span style="font-weight:bold;margin-left:5px">.required</span></td><td>boolean</td><td>Is this parameter required for the job to run</td></tr>
<tr><td><span style="font-weight:bold;">controlParameters</span></td><td>array[object]</td><td>Simple parameters for controlling the job</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>object</td><td>A Scale describes the units and acceptable values for an ObservationVariable.  <br>For example, an ObservationVariable might be defined with a Trait of "plant height", a Scale of "meters", and a Method of "tape measure". This variable would be distinct from a variable with the Scale "inches" or "pixels".</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.scaleName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Name of the scale <br/>MIAPPE V1.1 (DM-92) Scale Name of the scale associated with the variable</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.dataType</span></td><td>string</td><td><p>Class of the scale, entries can be</p> <p>"Code" -  This scale class is exceptionally used to express complex traits. Code is a nominal scale that combines the expressions of the different traits composing the complex trait. For example a severity trait might be expressed by a 2 digit and 2 character code. The first 2 digits are the percentage of the plant covered by a fungus and the 2 characters refer to the delay in development, e.g. "75VD" means "75 %" of the plant is infected and the plant is very delayed.</p> <p>"Date" - The date class is for events expressed in a time format, See ISO 8601</p> <p>"Duration" - The Duration class is for time elapsed between two events expressed in a time format, e.g. days, hours, months</p> <p>"Nominal" - Categorical scale that can take one of a limited and fixed number of categories. There is no intrinsic ordering to the categories</p> <p>"Numerical" - Numerical scales express the trait with real numbers. The numerical scale defines the unit e.g. centimeter, ton per hectare, branches</p> <p>"Ordinal" - Ordinal scales are scales composed of ordered categories</p> <p>"Text" - A free text is used to express the trait.</p></td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.decimalPlaces</span></td><td>integer</td><td>For numerical, number of decimal places to be reported</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.ontologyReference</span></td><td>object</td><td>MIAPPE V1.1  (DM-85) Variable accession number - Accession number of the variable in the Crop Ontology  (DM-87) Trait accession number - Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-89) Method accession number - Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).  (DM-93) Scale accession number - Accession number of the scale in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology database unique identifier</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.ontologyName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Ontology name</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.documentationLinks</span></td><td>array[object]</td><td>links to various ontology documentation</td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.URL</span></td><td>string<br>(uri)</td><td></td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br>.documentationLinks<br><span style="font-weight:bold;margin-left:5px">.type</span></td><td>string</td><td></td></tr>
<tr><td>controlParameters<br>.dataType<br>.ontologyReference<br><span style="font-weight:bold;margin-left:5px">.version</span></td><td>string</td><td>Ontology version (no specific format)</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.scalePUI</span></td><td>string</td><td>The Permanent Unique Identifier of a Scale, usually in the form of a URI</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.units</span></td><td>string</td><td>This field can be used to describe the units used for this scale. This should be the abbreviated  form of the units, intended to be displayed with every value using this scale. Usually this only  applies when `dataType` is Numeric, but could also be included for other dataTypes when applicable.</td></tr>
<tr><td>controlParameters<br>.dataType<br><span style="font-weight:bold;margin-left:5px">.validValues</span></td><td>object</td><td></td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.categories</span></td><td>array[object]</td><td>List of possible values with optional labels</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.label</span></td><td>string</td><td>A text label for a category</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br>.categories<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The actual value for a category</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.max</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `maximumValue`. Github issue number #450  <br>Maximum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.maximumValue</span></td><td>string</td><td>Maximum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.min</span></td><td>integer</td><td>**Deprecated in v2.1** Please use `minimumValue`. Github issue number #450  <br>Minimum value for numerical scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br>.dataType<br>.validValues<br><span style="font-weight:bold;margin-left:5px">.minimumValue</span></td><td>string</td><td>Minimum value for numerical, date, and time scales. Typically used for data capture control and QC.</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.defaultValue</span></td><td>string</td><td>The default value used if the parameter is not provided. Required should be false if DefaultValue is present.</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.exampleValue</span></td><td>string</td><td>An example of what this parameter might look like</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.parameterName</span></td><td>string</td><td>Human readable identifier for this parameter</td></tr>
<tr><td>controlParameters<br><span style="font-weight:bold;margin-left:5px">.required</span></td><td>boolean</td><td>Is this parameter required for the job to run</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of a running job.</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string</td><td>A link to further documentation describing a procedure</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileDataParameters</span></td><td>array[object]</td><td>Input data expected from a non-BrAPI source</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.alternativeParameters</span></td><td>array[string]</td><td>Alternate parameter ids that would provide the same input data</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.dataTypes</span></td><td>array[string]</td><td>The accepted list of data types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.mimeTypes</span></td><td>array[string]</td><td>The accepted list of file MIME types</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterId</span></td><td>string</td><td>Unique identifier for this parameter</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.parameterName</span></td><td>string</td><td>Human readable identifier for this parameter</td></tr>
<tr><td>fileDataParameters<br><span style="font-weight:bold;margin-left:5px">.required</span></td><td>boolean</td><td>Is this parameter required for the job to run</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">version</span></td><td>string</td><td>A version number or identifier for a procedure</td></tr>
</table>


 

+ Parameters
    + procedureDbId (Required, string) ... The unique identifier for a procedure
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
        "brapiDataParameters": [
            {
                "alternativeParameters": [
                    "alternativeParameters1",
                    "alternativeParameters2"
                ],
                "dataType": "Observations",
                "parameterId": "665b33cf",
                "parameterName": "Number of Cycles",
                "required": "100"
            }
        ],
        "controlParameters": [
            {
                "dataType": {
                    "additionalInfo": {},
                    "dataType": "Numerical",
                    "decimalPlaces": 2,
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
                    "ontologyReference": {
                        "documentationLinks": [
                            {
                                "URL": "http://purl.obolibrary.org/obo/ro.owl",
                                "type": "OBO"
                            }
                        ],
                        "ontologyDbId": "6b071868",
                        "ontologyName": "The Crop Ontology",
                        "version": "7.2.3"
                    },
                    "scaleName": "Meters",
                    "scalePUI": "http://my-traits.com/trait/CO_123:0000112",
                    "units": "m",
                    "validValues": {
                        "categories": [
                            {
                                "label": "low",
                                "value": "0"
                            },
                            {
                                "label": "medium",
                                "value": "5"
                            },
                            {
                                "label": "high",
                                "value": "10"
                            }
                        ],
                        "max": 9999,
                        "maximumValue": "9999",
                        "min": 2,
                        "minimumValue": "2"
                    }
                },
                "defaultValue": "100",
                "exampleValue": "100",
                "parameterId": "665b33cf",
                "parameterName": "Number of Cycles",
                "required": "100"
            }
        ],
        "description": "Bob Robertson first attempt to run GWAS on a remote server",
        "documentationURL": "https://plantbreeding.github.io/tool-documentation",
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
        "fileDataParameters": [
            {
                "alternativeParameters": [
                    "alternativeParameters1",
                    "alternativeParameters2"
                ],
                "dataTypes": [
                    "EPW",
                    "VCF"
                ],
                "mimeTypes": [
                    "application/epw",
                    "application/vcf"
                ],
                "parameterId": "665b33cf",
                "parameterName": "Weather Data",
                "required": "100"
            }
        ],
        "procedureDbId": "a3b45b23",
        "procedureName": "REMOTE-GWAS",
        "version": "v2.3"
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




### Post - /search/files [POST /brapi/v2/search/files]

Submit a search request for `XXEntitiesXX`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/XXEntitiesXX/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>
<br/>
File Implementation Notes<br/>
- `fileURL` should be a complete URL describing the location of the file. There is no BrAPI call for retrieving the file content, so it could be on a different path, or a different host.<br/>
- `descriptiveOntologyTerm` can be thought of as Tags for the file. These could be simple descriptive words, or ontology references, or full ontology URI's.<br/>

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">fileDbIds</span></td><td>array[string]</td><td>A list of file Ids to search for</td></tr>
<tr><td><span style="font-weight:bold;">fileNames</span></td><td>array[string]</td><td>File file names to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileSizeMax</span></td><td>integer</td><td>A maximum file file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileSizeMin</span></td><td>integer</td><td>A minimum file file size to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStampRangeEnd</span></td><td>string<br>(date-time)</td><td>The latest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStampRangeStart</span></td><td>string<br>(date-time)</td><td>The earliest timestamp to search for.</td></tr>
<tr><td><span style="font-weight:bold;">mimeTypes</span></td><td>array[string]</td><td>A set of file file types to search for.</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of an file</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
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
    "fileDbIds": [
        "564b64a6",
        "0d122d1d"
    ],
    "fileNames": [
        "file_01032019.jpg",
        "picture_field_1234.jpg"
    ],
    "fileSizeMax": 20000000,
    "fileSizeMin": 1000,
    "fileTimeStampRangeEnd": "2018-01-01T14:47:23-0600",
    "fileTimeStampRangeStart": "2018-01-01T14:47:23-0600",
    "mimeTypes": [
        "application/json",
        "text/csv",
        "application/vcf"
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
                "copyright": "Copyright 2018 Bob Robertson",
                "dataType": "VCFW",
                "description": "This is a picture of a tomato",
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
                "fileDbId": "a55efb9c",
                "fileName": "file_0000231.jpg",
                "fileSize": 50000,
                "fileSource": "Output from analsys job xyz123",
                "fileTimeStamp": "2018-01-01T14:47:23-0600",
                "fileURL": "https://wiki.brapi.org/files/tomato",
                "mimeType": "application/vcf"
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




### Get - /search/files/{searchResultsDbId} [GET /brapi/v2/search/files/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Files` search request <br/>
Clients should submit a search request using the corresponding `POST /search/files` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>
<br/>
File Implementation Notes<br/>
- `fileURL` should be a complete URL describing the location of the file. There is no BrAPI call for retrieving the file content, so it could be on a different path, or a different host.<br/>
- `descriptiveOntologyTerm` can be thought of as Tags for the file. These could be simple descriptive words, or ontology references, or full ontology URI's.<br/>



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">fileDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of an file</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">copyright</span></td><td>string</td><td>The copyright information of this file. Example 'Copyright 2018 Bob Robertson'</td></tr>
<tr><td><span style="font-weight:bold;">dataType</span></td><td>string</td><td>The accepted list of data types</td></tr>
<tr><td><span style="font-weight:bold;">description</span></td><td>string</td><td>The human readable description of an file.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fileName</span></td><td>string</td><td>The name of the file file. Might be the same as 'fileName', but could be different.</td></tr>
<tr><td><span style="font-weight:bold;">fileSize</span></td><td>integer</td><td>The size of the file in Bytes.</td></tr>
<tr><td><span style="font-weight:bold;">fileSource</span></td><td>string</td><td>The description of where the file originated or how it was generated</td></tr>
<tr><td><span style="font-weight:bold;">fileTimeStamp</span></td><td>string<br>(date-time)</td><td>The date and time the file was taken</td></tr>
<tr><td><span style="font-weight:bold;">fileURL</span></td><td>string</td><td>The complete, absolute URI path to the file file. Files might be stored on a different host or path than the BrAPI web server.</td></tr>
<tr><td><span style="font-weight:bold;">mimeType</span></td><td>string</td><td>The file type of the file</td></tr>
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
                "copyright": "Copyright 2018 Bob Robertson",
                "dataType": "VCFW",
                "description": "This is a picture of a tomato",
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
                "fileDbId": "a55efb9c",
                "fileName": "file_0000231.jpg",
                "fileSize": 50000,
                "fileSource": "Output from analsys job xyz123",
                "fileTimeStamp": "2018-01-01T14:47:23-0600",
                "fileURL": "https://wiki.brapi.org/files/tomato",
                "mimeType": "application/vcf"
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




### Post - /search/metrics [POST /brapi/v2/search/metrics]

Submit a search request for `XXEntitiesXX`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/XXEntitiesXX/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">jobDbIds</span></td><td>array[string]</td><td>The unique identifiers of Jobs</td></tr>
<tr><td><span style="font-weight:bold;">jobNames</span></td><td>array[string]</td><td>The human readable names of running jobs</td></tr>
<tr><td><span style="font-weight:bold;">metricDbIds</span></td><td>array[string]</td><td>The unique identifiers of metrics</td></tr>
<tr><td><span style="font-weight:bold;">metricNames</span></td><td>array[string]</td><td>The human readable names of metrics</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbIds</span></td><td>array[string]</td><td>The DbIds of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableNames</span></td><td>array[string]</td><td>The names of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbIds</span></td><td>array[string]</td><td>The unique identifiers for procedures</td></tr>
<tr><td><span style="font-weight:bold;">procedureNames</span></td><td>array[string]</td><td>The human readable identifiers for procedures</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">metricDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Metric</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
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
    "jobDbIds": [
        "a55efb9c",
        "55e45b23"
    ],
    "jobNames": [
        "Bob Robertson First GWAS",
        "Standard QA/QC #445"
    ],
    "metricDbIds": [
        "5e23fb9c",
        "45ba55e5"
    ],
    "metricNames": [
        "plotH2_designation",
        "plotY2"
    ],
    "observationVariableDbIds": [
        "a646187d",
        "6d23513b"
    ],
    "observationVariableNames": [
        "Plant Height in meters",
        "Wheat rust score 1-5"
    ],
    "observationVariablePUIs": [
        "http://my-traits.com/trait/CO_123:0008012",
        "http://my-traits.com/trait/CO_123:0007261"
    ],
    "page": 0,
    "pageSize": 1000,
    "procedureDbIds": [
        "a3b45b23",
        "b45ba3b4"
    ],
    "procedureNames": [
        "REMOTE-GWAS",
        "QA/QC"
    ],
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
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
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "metricDbId": "5ceb9fa5",
                "metricDescription": "vg/(vg+ve)-designation",
                "metricName": "plotH2_designation",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "standardError": "0.0034",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "0.6637"
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




### Get - /search/metrics/{searchResultsDbId} [GET /brapi/v2/search/metrics/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Metrics` search request <br/>
Clients should submit a search request using the corresponding `POST /search/metrics` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">metricDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Metric</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">metricDescription</span></td><td>string</td><td>The analysis method used</td></tr>
<tr><td><span style="font-weight:bold;">metricName</span></td><td>string</td><td>The human readable name of a metric</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the metric value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the metric</td></tr>
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
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "metricDbId": "5ceb9fa5",
                "metricDescription": "vg/(vg+ve)-designation",
                "metricName": "plotH2_designation",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "standardError": "0.0034",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "0.6637"
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




### Post - /search/predictions [POST /brapi/v2/search/predictions]

Submit a search request for `XXEntitiesXX`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/XXEntitiesXX/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbIds</span></td><td>array[string]</td><td>List of IDs which uniquely identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">germplasmNames</span></td><td>array[string]</td><td>List of human readable names to identify germplasm to search for</td></tr>
<tr><td><span style="font-weight:bold;">jobDbIds</span></td><td>array[string]</td><td>The unique identifiers of Jobs</td></tr>
<tr><td><span style="font-weight:bold;">jobNames</span></td><td>array[string]</td><td>The human readable names of running jobs</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbIds</span></td><td>array[string]</td><td>The DbIds of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableNames</span></td><td>array[string]</td><td>The names of Variables to search for</td></tr>
<tr><td><span style="font-weight:bold;">observationVariablePUIs</span></td><td>array[string]</td><td>The Permanent Unique Identifier of an Observation Variable, usually in the form of a URI</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">predictionDbIds</span></td><td>array[string]</td><td>The unique identifiers for predictions</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbIds</span></td><td>array[string]</td><td>The unique identifiers for procedures</td></tr>
<tr><td><span style="font-weight:bold;">procedureNames</span></td><td>array[string]</td><td>The human readable identifiers for procedures</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">studyDbIds</span></td><td>array[string]</td><td>List of study identifiers to search for</td></tr>
<tr><td><span style="font-weight:bold;">studyNames</span></td><td>array[string]</td><td>List of study names to filter search results</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">predictionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Prediction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
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
    "jobDbIds": [
        "a55efb9c",
        "55e45b23"
    ],
    "jobNames": [
        "Bob Robertson First GWAS",
        "Standard QA/QC #445"
    ],
    "observationVariableDbIds": [
        "a646187d",
        "6d23513b"
    ],
    "observationVariableNames": [
        "Plant Height in meters",
        "Wheat rust score 1-5"
    ],
    "observationVariablePUIs": [
        "http://my-traits.com/trait/CO_123:0008012",
        "http://my-traits.com/trait/CO_123:0007261"
    ],
    "page": 0,
    "pageSize": 1000,
    "predictionDbIds": [
        "a5e45b23",
        "145b45b2"
    ],
    "procedureDbIds": [
        "a3b45b23",
        "b45ba3b4"
    ],
    "procedureNames": [
        "REMOTE-GWAS",
        "QA/QC"
    ],
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
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
                "germplasmDbId": "029d705d",
                "germplasmName": "A0000003",
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "predictionDbId": "43ab644f",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "reliability": "0.993",
                "standardError": "28.7",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "1026.4"
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




### Get - /search/predictions/{searchResultsDbId} [GET /brapi/v2/search/predictions/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Predictions` search request <br/>
Clients should submit a search request using the corresponding `POST /search/predictions` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.
<br/>



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">predictionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>The unique identifier of a Prediction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm associated with this prediction</td></tr>
<tr><td><span style="font-weight:bold;">jobDbId</span></td><td>string</td><td>The unique identifier of a Job</td></tr>
<tr><td><span style="font-weight:bold;">jobName</span></td><td>string</td><td>The human readable name of a running job</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableDbId</span></td><td>string</td><td>The unique identifier of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">observationVariableName</span></td><td>string</td><td>The human readable name of a Variable</td></tr>
<tr><td><span style="font-weight:bold;">procedureDbId</span></td><td>string</td><td>The unique identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">procedureName</span></td><td>string</td><td>The human readable identifier for a procedure</td></tr>
<tr><td><span style="font-weight:bold;">reliability</span></td><td>string</td><td>The reliability of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">standardError</span></td><td>string</td><td>The standard error of the prediction value</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The unique identifier of a Study</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a Study</td></tr>
<tr><td><span style="font-weight:bold;">value</span></td><td>string</td><td>The value of the prediction</td></tr>
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
                "germplasmDbId": "029d705d",
                "germplasmName": "A0000003",
                "jobDbId": "a55efb9c",
                "jobName": "Bob Robertson First GWAS",
                "observationVariableDbId": "b95efca5",
                "observationVariableName": "Plant_Height_cm",
                "predictionDbId": "43ab644f",
                "procedureDbId": "a3b45b23",
                "procedureName": "REMOTE-GWAS",
                "reliability": "0.993",
                "standardError": "28.7",
                "studyDbId": "9a5c5efb",
                "studyName": "BrAPI Wheat - NY 2023",
                "value": "1026.4"
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

