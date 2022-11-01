
# Group Programs

A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. A Program can contain multiple Trials. A Trial can contain multiple Studies. 




### Get - /programs [GET /brapi/v2/programs{?abbreviation}{?programType}{?commonCropName}{?programDbId}{?programName}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of breeding Programs. This list can be filtered by common crop name to narrow results to a specific crop.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
</table>


 

+ Parameters
    + abbreviation (Optional, ) ... A shortened version of the human readable name for a Program
    + programType (Optional, ) ... The type of program entity this object represents<br/> 'STANARD' represents a standard, permenant breeding program<br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding 
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + programName (Optional, ) ... Use this parameter to only return results associated with the given `Program` by its human readable name. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
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
                "abbreviation": "P1",
                "additionalInfo": {},
                "commonCropName": "Tomatillo",
                "documentationURL": "https://wiki.brapi.org",
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
                "fundingInformation": "EU: FP7-244374",
                "leadPersonDbId": "fe6f5c50",
                "leadPersonName": "Bob Robertson",
                "objective": "Make a better tomatillo",
                "programDbId": "f60f15b2",
                "programName": "Tomatillo_Breeding_Program",
                "programType": "STANDARD"
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




### Post - /programs [POST /brapi/v2/programs]

Add new breeding Programs to the database. The `programDbId` is set by the server, all other fields are take from the request body, or a default value is used.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "abbreviation": "P1",
        "additionalInfo": {},
        "commonCropName": "Tomatillo",
        "documentationURL": "https://wiki.brapi.org",
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
        "fundingInformation": "EU: FP7-244374",
        "leadPersonDbId": "fe6f5c50",
        "leadPersonName": "Bob Robertson",
        "objective": "Make a better tomatillo",
        "programName": "Tomatillo_Breeding_Program",
        "programType": "STANDARD"
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
                "abbreviation": "P1",
                "additionalInfo": {},
                "commonCropName": "Tomatillo",
                "documentationURL": "https://wiki.brapi.org",
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
                "fundingInformation": "EU: FP7-244374",
                "leadPersonDbId": "fe6f5c50",
                "leadPersonName": "Bob Robertson",
                "objective": "Make a better tomatillo",
                "programDbId": "f60f15b2",
                "programName": "Tomatillo_Breeding_Program",
                "programType": "STANDARD"
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




### Get - /programs/{programDbId} [GET /brapi/v2/programs/{programDbId}]

Get a single breeding Program by Id. This can be used to quickly get the details of a Program when you have the Id from another entity.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
</table>


 

+ Parameters
    + programDbId (Required, ) ... Filter by the common crop name. Exact match.
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
        "abbreviation": "P1",
        "additionalInfo": {},
        "commonCropName": "Tomatillo",
        "documentationURL": "https://wiki.brapi.org",
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
        "fundingInformation": "EU: FP7-244374",
        "leadPersonDbId": "fe6f5c50",
        "leadPersonName": "Bob Robertson",
        "objective": "Make a better tomatillo",
        "programDbId": "f60f15b2",
        "programName": "Tomatillo_Breeding_Program",
        "programType": "STANDARD"
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




### Put - /programs/{programDbId} [PUT /brapi/v2/programs/{programDbId}/]

Update the details of an existing breeding Program.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
</table>


 

+ Parameters
    + programDbId (Required, ) ... Filter by the common crop name. Exact match.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "abbreviation": "P1",
    "additionalInfo": {},
    "commonCropName": "Tomatillo",
    "documentationURL": "https://wiki.brapi.org",
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
    "fundingInformation": "EU: FP7-244374",
    "leadPersonDbId": "fe6f5c50",
    "leadPersonName": "Bob Robertson",
    "objective": "Make a better tomatillo",
    "programName": "Tomatillo_Breeding_Program",
    "programType": "STANDARD"
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
        "abbreviation": "P1",
        "additionalInfo": {},
        "commonCropName": "Tomatillo",
        "documentationURL": "https://wiki.brapi.org",
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
        "fundingInformation": "EU: FP7-244374",
        "leadPersonDbId": "fe6f5c50",
        "leadPersonName": "Bob Robertson",
        "objective": "Make a better tomatillo",
        "programDbId": "f60f15b2",
        "programName": "Tomatillo_Breeding_Program",
        "programType": "STANDARD"
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




### Post - /search/programs [POST /brapi/v2/search/programs]

Submit a search request for `Programs`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/programs/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviations</span></td><td>array[string]</td><td>A list of shortened human readable names for a set of Programs</td></tr>
<tr><td><span style="font-weight:bold;">commonCropNames</span></td><td>array[string]</td><td>The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIDs</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460  <br>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceIds</span></td><td>array[string]</td><td>List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">externalReferenceSources</span></td><td>array[string]</td><td>List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbIds</span></td><td>array[string]</td><td>The person DbIds of the program leader to search for</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonNames</span></td><td>array[string]</td><td>The names of the program leader to search for</td></tr>
<tr><td><span style="font-weight:bold;">objectives</span></td><td>array[string]</td><td>A program objective to search for</td></tr>
<tr><td><span style="font-weight:bold;">page</span></td><td>integer</td><td>Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.</td></tr>
<tr><td><span style="font-weight:bold;">pageSize</span></td><td>integer</td><td>The size of the pages to be returned. Default is `1000`.</td></tr>
<tr><td><span style="font-weight:bold;">programDbIds</span></td><td>array[string]</td><td>A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programNames</span></td><td>array[string]</td><td>Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.</td></tr>
<tr><td><span style="font-weight:bold;">programTypes</span></td><td>array[string]</td><td>The type of program entity this object represents <br/> 'STANARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding </td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "abbreviations": [
        "P1",
        "P2"
    ],
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
    "leadPersonDbIds": [
        "d8bd96c7",
        "a2b9c8e7"
    ],
    "leadPersonNames": [
        "Bob Robertson",
        "Rob Robertson"
    ],
    "objectives": [
        "Objective Code One",
        "This is a longer objective search query"
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
    "programTypes": [
        "STANARD",
        "PROJECT"
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
                "abbreviation": "P1",
                "additionalInfo": {},
                "commonCropName": "Tomatillo",
                "documentationURL": "https://wiki.brapi.org",
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
                "fundingInformation": "EU: FP7-244374",
                "leadPersonDbId": "fe6f5c50",
                "leadPersonName": "Bob Robertson",
                "objective": "Make a better tomatillo",
                "programDbId": "f60f15b2",
                "programName": "Tomatillo_Breeding_Program",
                "programType": "STANDARD"
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




### Get - /search/programs/{searchResultsDbId} [GET /brapi/v2/search/programs/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Programs` search request <br/>
Clients should submit a search request using the corresponding `POST /search/programs` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">abbreviation</span></td><td>string</td><td>A shortened version of the human readable name for a Program</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestriced by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">commonCropName</span></td><td>string</td><td>Common name for the crop which this program is for</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string<br>(uri)</td><td>A URL to the human readable documentation of an object</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fundingInformation</span></td><td>string</td><td>Information describing the grant or funding source for this program</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonDbId</span></td><td>string</td><td>The unique identifier of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">leadPersonName</span></td><td>string</td><td>The name of the program leader</td></tr>
<tr><td><span style="font-weight:bold;">objective</span></td><td>string</td><td>The primary objective of the program</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The ID which uniquely identifies the program</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>Human readable name of the program</td></tr>
<tr><td><span style="font-weight:bold;">programType</span></td><td>string</td><td>The type of program entity this object represents <br/> 'STANDARD' represents a standard, permenant breeding program <br/> 'PROJECT' represents a short term project, usually with a set time limit based on funding   </td></tr>
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
                "abbreviation": "P1",
                "additionalInfo": {},
                "commonCropName": "Tomatillo",
                "documentationURL": "https://wiki.brapi.org",
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
                "fundingInformation": "EU: FP7-244374",
                "leadPersonDbId": "fe6f5c50",
                "leadPersonName": "Bob Robertson",
                "objective": "Make a better tomatillo",
                "programDbId": "f60f15b2",
                "programName": "Tomatillo_Breeding_Program",
                "programType": "STANDARD"
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

