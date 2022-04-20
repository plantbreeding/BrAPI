# Group Crosses






### Get - /crosses [GET /brapi/v2/crosses{?crossingProjectDbId}{?crossingProjectName}{?crossDbId}{?crossName}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Cross entities.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossAttributes</span></td><td>array[object]</td><td>Set of custom attributes associated with a cross</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeName</span></td><td>string</td><td>the human readable name of a cross attribute</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeValue</span></td><td>string</td><td>the value of a cross attribute</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossType</span></td><td>string</td><td>the type of cross</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>the unique identifier for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectName</span></td><td>string</td><td>the human readable name for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">parent1</span></td><td>object</td><td></td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">parent2</span></td><td>object</td><td></td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossDbId</span></td><td>string</td><td>the unique identifier for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossName</span></td><td>string</td><td>the human readable name for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">pollinationEvents</span></td><td>array[object]</td><td></td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationNumber</span></td><td>string</td><td>The unique identifier for this pollination event</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationSuccessful</span></td><td>boolean</td><td>True if the pollination was successful</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>The timestamp when the pollination took place</td></tr>
<tr><td><span style="font-weight:bold;">pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>**Deprecated in v2.1** Please use `pollinationEvents`. Github issue number #265   the timestamp when the pollination took place</td></tr>
</table>


 

+ Parameters
    + crossingProjectDbId (Optional, ) ... Search for Crossing Projects with this unique id
    + crossingProjectName (Optional, ) ... The human readable name for a crossing project
    + crossDbId (Optional, ) ... Search for Cross with this unique id
    + crossName (Optional, ) ... Search for Cross with this human readable name
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... Use this parameter to only return results associated with the given Program unique identifier. <br/>Use `GET /programs` to find the list of available Programs on a server.
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
                "crossAttributes": [
                    {
                        "crossAttributeName": "Humidity Percentage",
                        "crossAttributeValue": "45"
                    }
                ],
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "my_Crosses_2018",
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
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "plannedCrossDbId": "c8905568",
                "plannedCrossName": "my_Crosses_2018_01",
                "pollinationEvents": [
                    {
                        "pollinationNumber": "pollinationNumber",
                        "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
                    }
                ],
                "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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




### Post - /crosses [POST /brapi/v2/crosses]

Create new Cross entities on this server

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossAttributes</span></td><td>array[object]</td><td>Set of custom attributes associated with a cross</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeName</span></td><td>string</td><td>the human readable name of a cross attribute</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeValue</span></td><td>string</td><td>the value of a cross attribute</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossType</span></td><td>string</td><td>the type of cross</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>the unique identifier for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectName</span></td><td>string</td><td>the human readable name for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">parent1</span></td><td>object</td><td></td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">parent2</span></td><td>object</td><td></td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossDbId</span></td><td>string</td><td>the unique identifier for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossName</span></td><td>string</td><td>the human readable name for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">pollinationEvents</span></td><td>array[object]</td><td></td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationNumber</span></td><td>string</td><td>The unique identifier for this pollination event</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationSuccessful</span></td><td>boolean</td><td>True if the pollination was successful</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>The timestamp when the pollination took place</td></tr>
<tr><td><span style="font-weight:bold;">pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>**Deprecated in v2.1** Please use `pollinationEvents`. Github issue number #265   the timestamp when the pollination took place</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossAttributes</span></td><td>array[object]</td><td>Set of custom attributes associated with a cross</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeName</span></td><td>string</td><td>the human readable name of a cross attribute</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeValue</span></td><td>string</td><td>the value of a cross attribute</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossType</span></td><td>string</td><td>the type of cross</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>the unique identifier for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectName</span></td><td>string</td><td>the human readable name for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">parent1</span></td><td>object</td><td></td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">parent2</span></td><td>object</td><td></td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossDbId</span></td><td>string</td><td>the unique identifier for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossName</span></td><td>string</td><td>the human readable name for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">pollinationEvents</span></td><td>array[object]</td><td></td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationNumber</span></td><td>string</td><td>The unique identifier for this pollination event</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationSuccessful</span></td><td>boolean</td><td>True if the pollination was successful</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>The timestamp when the pollination took place</td></tr>
<tr><td><span style="font-weight:bold;">pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>**Deprecated in v2.1** Please use `pollinationEvents`. Github issue number #265   the timestamp when the pollination took place</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "crossAttributes": [
            {
                "crossAttributeName": "Humidity Percentage",
                "crossAttributeValue": "45"
            }
        ],
        "crossName": "my_Crosses_2018_01",
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "my_Crosses_2018",
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
        "parent1": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME_419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "my_Plot_9001",
            "parentType": "MALE"
        },
        "parent2": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME_419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "my_Plot_9001",
            "parentType": "MALE"
        },
        "plannedCrossDbId": "c8905568",
        "plannedCrossName": "my_Crosses_2018_01",
        "pollinationEvents": [
            {
                "pollinationNumber": "pollinationNumber",
                "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
            }
        ],
        "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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
                "crossAttributes": [
                    {
                        "crossAttributeName": "Humidity Percentage",
                        "crossAttributeValue": "45"
                    }
                ],
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "my_Crosses_2018",
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
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "plannedCrossDbId": "c8905568",
                "plannedCrossName": "my_Crosses_2018_01",
                "pollinationEvents": [
                    {
                        "pollinationNumber": "pollinationNumber",
                        "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
                    }
                ],
                "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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




### Put - /crosses [PUT /brapi/v2/crosses/]

Update existing Cross entities on this server

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">crossAttributes</span></td><td>array[object]</td><td>Set of custom attributes associated with a cross</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeName</span></td><td>string</td><td>the human readable name of a cross attribute</td></tr>
<tr><td>crossAttributes<br><span style="font-weight:bold;margin-left:5px">.crossAttributeValue</span></td><td>string</td><td>the value of a cross attribute</td></tr>
<tr><td><span style="font-weight:bold;">crossDbId</span></td><td>string</td><td>the unique identifier for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossName</span></td><td>string</td><td>the human readable name for a cross</td></tr>
<tr><td><span style="font-weight:bold;">crossType</span></td><td>string</td><td>the type of cross</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectDbId</span></td><td>string</td><td>the unique identifier for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">crossingProjectName</span></td><td>string</td><td>the human readable name for a crossing project</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">parent1</span></td><td>object</td><td></td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent1<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">parent2</span></td><td>object</td><td></td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>the unique identifier for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>the human readable name for a germplasm</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitDbId</span></td><td>string</td><td>the unique identifier for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.observationUnitName</span></td><td>string</td><td>the human readable name for an observation unit</td></tr>
<tr><td>parent2<br><span style="font-weight:bold;margin-left:5px">.parentType</span></td><td>string</td><td>The type of parent ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossDbId</span></td><td>string</td><td>the unique identifier for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">plannedCrossName</span></td><td>string</td><td>the human readable name for a planned cross</td></tr>
<tr><td><span style="font-weight:bold;">pollinationEvents</span></td><td>array[object]</td><td></td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationNumber</span></td><td>string</td><td>The unique identifier for this pollination event</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationSuccessful</span></td><td>boolean</td><td>True if the pollination was successful</td></tr>
<tr><td>pollinationEvents<br><span style="font-weight:bold;margin-left:5px">.pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>The timestamp when the pollination took place</td></tr>
<tr><td><span style="font-weight:bold;">pollinationTimeStamp</span></td><td>string<br>(date-time)</td><td>**Deprecated in v2.1** Please use `pollinationEvents`. Github issue number #265   the timestamp when the pollination took place</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "<crossDbId_1>": {
        "additionalInfo": {},
        "crossAttributes": [
            {
                "crossAttributeName": "string",
                "crossAttributeValue": "string"
            }
        ],
        "crossName": "my_Crosses_2018_01",
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "my_Crosses_2018",
        "parent1": {
            "germplasmDbId": "d34b10c3",
            "germplasmName": "TME_419",
            "observationUnitDbId": "3f0a1798",
            "observationUnitName": "my_Plot_9001",
            "parentType": "FEMALE"
        },
        "parent2": {
            "germplasmDbId": "776a609c",
            "germplasmName": "TME_419",
            "observationUnitDbId": "2e1926a7",
            "observationUnitName": "my_Plot_9002",
            "parentType": "MALE"
        },
        "pollinationTimeStamp": "2019-08-15T18:49:00.327Z"
    },
    "<crossDbId_2>": {
        "additionalInfo": {},
        "crossAttributes": [
            {
                "crossAttributeName": "string",
                "crossAttributeValue": "string"
            }
        ],
        "crossName": "my_Crosses_2018_02",
        "crossType": "BIPARENTAL",
        "crossingProjectDbId": "696d7c92",
        "crossingProjectName": "my_Crosses_2018",
        "parent1": {
            "germplasmDbId": "c43a2fd2",
            "germplasmName": "TME_419",
            "observationUnitDbId": "3f2a37b8",
            "observationUnitName": "my_Plot_9013",
            "parentType": "FEMALE"
        },
        "parent2": {
            "germplasmDbId": "124b10ad",
            "germplasmName": "TME_419",
            "observationUnitDbId": 27194637,
            "observationUnitName": "my_Plot_9014",
            "parentType": "MALE"
        },
        "pollinationTimeStamp": "2019-08-15T18:49:00.327Z"
    }
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
                "crossAttributes": [
                    {
                        "crossAttributeName": "Humidity Percentage",
                        "crossAttributeValue": "45"
                    }
                ],
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
                "crossType": "BIPARENTAL",
                "crossingProjectDbId": "696d7c92",
                "crossingProjectName": "my_Crosses_2018",
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
                "parent1": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "parent2": {
                    "germplasmDbId": "d34b10c3",
                    "germplasmName": "TME_419",
                    "observationUnitDbId": "2e1926a7",
                    "observationUnitName": "my_Plot_9001",
                    "parentType": "MALE"
                },
                "plannedCrossDbId": "c8905568",
                "plannedCrossName": "my_Crosses_2018_01",
                "pollinationEvents": [
                    {
                        "pollinationNumber": "pollinationNumber",
                        "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
                    }
                ],
                "pollinationTimeStamp": "2018-01-01T14:47:23-0600"
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

