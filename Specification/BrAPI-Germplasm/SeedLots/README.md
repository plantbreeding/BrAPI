# Group SeedLots






### Get - /seedlots [GET /brapi/v2/seedlots{?seedLotDbId}{?germplasmDbId}{?germplasmName}{?crossDbId}{?crossName}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Seed Lot descriptions available in a system.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>contentMixture</td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture.<br>crossDbId</td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>crossName</td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>germplasmDbId</td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>germplasmName</td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>mixturePercentage</td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td>createdDate</td><td>string (date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>lastUpdated</td><td>string (date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td>programDbId</td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>programName</td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>seedLotDbId</td><td>string</td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td>seedLotDescription</td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td>seedLotName</td><td>string</td><td>A human readable name for this Seed Lot</td></tr>
<tr><td>sourceCollection</td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td>storageLocation</td><td>string</td><td>Description the storage location</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Optional, ) ... Unique id for a seed lot on this server
    + germplasmDbId (Optional, ) ... The internal id of the germplasm
    + germplasmName (Optional, ) ... Name of the germplasm
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
                "amount": 561,
                "contentMixture": [
                    {
                        "crossDbId": "d105fd6f",
                        "crossName": "my_Crosses_2018_01",
                        "germplasmDbId": "029d705d",
                        "germplasmName": "A0000003",
                        "mixturePercentage": 100
                    }
                ],
                "createdDate": "2018-01-01T14:47:23-0600",
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
                "lastUpdated": "2018-01-01T14:47:23-0600",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "programDbId": "e972d569",
                "programName": "Tomatillo_Breeding_Program",
                "seedLotDbId": "261ecb09",
                "seedLotDescription": "This is a description of a seed lot",
                "seedLotName": "Seed Lot Alpha",
                "sourceCollection": "nursery",
                "storageLocation": "The storage location is an massive, underground, bunker.",
                "units": "seeds"
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




### Post - /seedlots [POST /brapi/v2/seedlots]

Add new Seed Lot descriptions to a server

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>contentMixture</td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture.<br>crossDbId</td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>crossName</td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>germplasmDbId</td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>germplasmName</td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>mixturePercentage</td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td>createdDate</td><td>string (date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>lastUpdated</td><td>string (date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td>programDbId</td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>programName</td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>seedLotDescription</td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td>seedLotName</td><td>string</td><td>A human readable name for this Seed Lot</td></tr>
<tr><td>sourceCollection</td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td>storageLocation</td><td>string</td><td>Description the storage location</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>contentMixture</td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture.<br>crossDbId</td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>crossName</td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>germplasmDbId</td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>germplasmName</td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>mixturePercentage</td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td>createdDate</td><td>string (date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>lastUpdated</td><td>string (date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td>programDbId</td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>programName</td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>seedLotDbId</td><td>string</td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td>seedLotDescription</td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td>seedLotName</td><td>string</td><td>A human readable name for this Seed Lot</td></tr>
<tr><td>sourceCollection</td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td>storageLocation</td><td>string</td><td>Description the storage location</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "amount": 561,
        "contentMixture": [
            {
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
                "germplasmDbId": "029d705d",
                "germplasmName": "A0000003",
                "mixturePercentage": 100
            }
        ],
        "createdDate": "2018-01-01T14:47:23-0600",
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
        "lastUpdated": "2018-01-01T14:47:23-0600",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "programDbId": "e972d569",
        "programName": "Tomatillo_Breeding_Program",
        "seedLotDescription": "This is a description of a seed lot",
        "seedLotName": "Seed Lot Alpha",
        "sourceCollection": "nursery",
        "storageLocation": "The storage location is an massive, underground, bunker.",
        "units": "seeds"
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
                "amount": 561,
                "contentMixture": [
                    {
                        "crossDbId": "d105fd6f",
                        "crossName": "my_Crosses_2018_01",
                        "germplasmDbId": "029d705d",
                        "germplasmName": "A0000003",
                        "mixturePercentage": 100
                    }
                ],
                "createdDate": "2018-01-01T14:47:23-0600",
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
                "lastUpdated": "2018-01-01T14:47:23-0600",
                "locationDbId": "3cfdd67d",
                "locationName": "Location 1",
                "programDbId": "e972d569",
                "programName": "Tomatillo_Breeding_Program",
                "seedLotDbId": "261ecb09",
                "seedLotDescription": "This is a description of a seed lot",
                "seedLotName": "Seed Lot Alpha",
                "sourceCollection": "nursery",
                "storageLocation": "The storage location is an massive, underground, bunker.",
                "units": "seeds"
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




### Get - /seedlots/transactions [GET /brapi/v2/seedlots/transactions{?transactionDbId}{?seedLotDbId}{?germplasmDbId}{?germplasmName}{?crossDbId}{?crossName}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Seed Lot Transactions



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>fromSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td>toSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td>transactionDbId</td><td>string</td><td>Unique DbId for the Seed Lot Transaction</td></tr>
<tr><td>transactionDescription</td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td>transactionTimestamp</td><td>string (date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


 

+ Parameters
    + transactionDbId (Optional, ) ... Unique id for a transaction on this server
    + seedLotDbId (Optional, ) ... Unique id for a seed lot on this server
    + germplasmDbId (Optional, ) ... The internal id of the germplasm
    + germplasmName (Optional, ) ... Name of the germplasm
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
                "amount": 45,
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
                "fromSeedLotDbId": "11eef13b",
                "toSeedLotDbId": "59339b90",
                "transactionDbId": "28e46db9",
                "transactionDescription": "f9cd88d2",
                "transactionTimestamp": "2018-01-01T14:47:23-0600",
                "units": "seeds"
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




### Post - /seedlots/transactions [POST /brapi/v2/seedlots/transactions]

Add new Seed Lot Transaction to be recorded

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>fromSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td>toSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td>transactionDescription</td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td>transactionTimestamp</td><td>string (date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>fromSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td>toSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td>transactionDbId</td><td>string</td><td>Unique DbId for the Seed Lot Transaction</td></tr>
<tr><td>transactionDescription</td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td>transactionTimestamp</td><td>string (date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "amount": 45,
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
        "fromSeedLotDbId": "11eef13b",
        "toSeedLotDbId": "59339b90",
        "transactionDescription": "f9cd88d2",
        "transactionTimestamp": "2018-01-01T14:47:23-0600",
        "units": "seeds"
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
                "amount": 45,
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
                "fromSeedLotDbId": "11eef13b",
                "toSeedLotDbId": "59339b90",
                "transactionDbId": "28e46db9",
                "transactionDescription": "f9cd88d2",
                "transactionTimestamp": "2018-01-01T14:47:23-0600",
                "units": "seeds"
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




### Get - /seedlots/{seedLotDbId} [GET /brapi/v2/seedlots/{seedLotDbId}]

Get a specific Seed Lot by seedLotDbId



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>contentMixture</td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture.<br>crossDbId</td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>crossName</td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>germplasmDbId</td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>germplasmName</td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>mixturePercentage</td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td>createdDate</td><td>string (date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>lastUpdated</td><td>string (date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td>programDbId</td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>programName</td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>seedLotDbId</td><td>string</td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td>seedLotDescription</td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td>seedLotName</td><td>string</td><td>A human readable name for this Seed Lot</td></tr>
<tr><td>sourceCollection</td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td>storageLocation</td><td>string</td><td>Description the storage location</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
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
        "amount": 561,
        "contentMixture": [
            {
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
                "germplasmDbId": "029d705d",
                "germplasmName": "A0000003",
                "mixturePercentage": 100
            }
        ],
        "createdDate": "2018-01-01T14:47:23-0600",
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
        "lastUpdated": "2018-01-01T14:47:23-0600",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "programDbId": "e972d569",
        "programName": "Tomatillo_Breeding_Program",
        "seedLotDbId": "261ecb09",
        "seedLotDescription": "This is a description of a seed lot",
        "seedLotName": "Seed Lot Alpha",
        "sourceCollection": "nursery",
        "storageLocation": "The storage location is an massive, underground, bunker.",
        "units": "seeds"
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




### Put - /seedlots/{seedLotDbId} [PUT /brapi/v2/seedlots/{seedLotDbId}/]

Update an existing Seed Lot

**Request Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>contentMixture</td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture.<br>crossDbId</td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>crossName</td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>germplasmDbId</td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>germplasmName</td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>mixturePercentage</td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td>createdDate</td><td>string (date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>lastUpdated</td><td>string (date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td>programDbId</td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>programName</td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>seedLotDescription</td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td>seedLotName</td><td>string</td><td>A human readable name for this Seed Lot</td></tr>
<tr><td>sourceCollection</td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td>storageLocation</td><td>string</td><td>Description the storage location</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>contentMixture</td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture.<br>crossDbId</td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>crossName</td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture.<br>germplasmDbId</td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>germplasmName</td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture.<br>mixturePercentage</td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td>createdDate</td><td>string (date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>lastUpdated</td><td>string (date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td>locationDbId</td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td>locationName</td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td>programDbId</td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>programName</td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td>seedLotDbId</td><td>string</td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td>seedLotDescription</td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td>seedLotName</td><td>string</td><td>A human readable name for this Seed Lot</td></tr>
<tr><td>sourceCollection</td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td>storageLocation</td><td>string</td><td>Description the storage location</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "amount": 561,
    "contentMixture": [
        {
            "crossDbId": "d105fd6f",
            "crossName": "my_Crosses_2018_01",
            "germplasmDbId": "029d705d",
            "germplasmName": "A0000003",
            "mixturePercentage": 100
        }
    ],
    "createdDate": "2018-01-01T14:47:23-0600",
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
    "lastUpdated": "2018-01-01T14:47:23-0600",
    "locationDbId": "3cfdd67d",
    "locationName": "Location 1",
    "programDbId": "e972d569",
    "programName": "Tomatillo_Breeding_Program",
    "seedLotDescription": "This is a description of a seed lot",
    "seedLotName": "Seed Lot Alpha",
    "sourceCollection": "nursery",
    "storageLocation": "The storage location is an massive, underground, bunker.",
    "units": "seeds"
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
        "amount": 561,
        "contentMixture": [
            {
                "crossDbId": "d105fd6f",
                "crossName": "my_Crosses_2018_01",
                "germplasmDbId": "029d705d",
                "germplasmName": "A0000003",
                "mixturePercentage": 100
            }
        ],
        "createdDate": "2018-01-01T14:47:23-0600",
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
        "lastUpdated": "2018-01-01T14:47:23-0600",
        "locationDbId": "3cfdd67d",
        "locationName": "Location 1",
        "programDbId": "e972d569",
        "programName": "Tomatillo_Breeding_Program",
        "seedLotDbId": "261ecb09",
        "seedLotDescription": "This is a description of a seed lot",
        "seedLotName": "Seed Lot Alpha",
        "sourceCollection": "nursery",
        "storageLocation": "The storage location is an massive, underground, bunker.",
        "units": "seeds"
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




### Get - /seedlots/{seedLotDbId}/transactions [GET /brapi/v2/seedlots/{seedLotDbId}/transactions{?transactionDbId}{?transactionDirection}{?page}{?pageSize}]

Get all Transactions related to a specific Seed Lot



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td>additionalInfo</td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td>amount</td><td>number</td><td>The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td>externalReferences</td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceID</td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceId</td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences.<br>referenceSource</td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td>fromSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td>toSeedLotDbId</td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td>transactionDbId</td><td>string</td><td>Unique DbId for the Seed Lot Transaction</td></tr>
<tr><td>transactionDescription</td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td>transactionTimestamp</td><td>string (date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td>units</td><td>string</td><td>Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
    + transactionDbId (Optional, ) ... Unique id for a Transaction that has occurred
    + transactionDirection (Optional, ) ... Filter results to only include transactions directed to the specific Seed Lot (TO), away from the specific Seed Lot (FROM), or both (BOTH). The default value for this parameter is BOTH
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
                "amount": 45,
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
                "fromSeedLotDbId": "11eef13b",
                "toSeedLotDbId": "59339b90",
                "transactionDbId": "28e46db9",
                "transactionDescription": "f9cd88d2",
                "transactionTimestamp": "2018-01-01T14:47:23-0600",
                "units": "seeds"
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

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

