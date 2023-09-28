# Group SeedLots






### Get - /seedlots [GET /brapi/v2/seedlots{?seedLotDbId}{?crossDbId}{?crossName}{?commonCropName}{?programDbId}{?germplasmDbId}{?germplasmName}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Seed Lot descriptions available in a system.



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The current balance of the amount of material in a SeedLot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">contentMixture</span></td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossDbId</span></td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossName</span></td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.mixturePercentage</span></td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td><span style="font-weight:bold;">createdDate</span></td><td>string<br>(date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">lastUpdated</span></td><td>string<br>(date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDescription</span></td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">sourceCollection</span></td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td><span style="font-weight:bold;">storageLocation</span></td><td>string</td><td>Description the storage location</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being counted in a SeedLot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Optional, string) ... Unique id for a seed lot on this server
    + crossDbId (Optional, string) ... Search for Cross with this unique id
    + crossName (Optional, string) ... Search for Cross with this human readable name
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + germplasmDbId (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + germplasmName (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` by its human readable name. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
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
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The current balance of the amount of material in a SeedLot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">contentMixture</span></td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossDbId</span></td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossName</span></td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.mixturePercentage</span></td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td><span style="font-weight:bold;">createdDate</span></td><td>string<br>(date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">lastUpdated</span></td><td>string<br>(date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDescription</span></td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">sourceCollection</span></td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td><span style="font-weight:bold;">storageLocation</span></td><td>string</td><td>Description the storage location</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being counted in a SeedLot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The current balance of the amount of material in a SeedLot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">contentMixture</span></td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossDbId</span></td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossName</span></td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.mixturePercentage</span></td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td><span style="font-weight:bold;">createdDate</span></td><td>string<br>(date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">lastUpdated</span></td><td>string<br>(date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDescription</span></td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">sourceCollection</span></td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td><span style="font-weight:bold;">storageLocation</span></td><td>string</td><td>Description the storage location</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being counted in a SeedLot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
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




### Get - /seedlots/transactions [GET /brapi/v2/seedlots/transactions{?transactionDbId}{?seedLotDbId}{?crossDbId}{?crossName}{?commonCropName}{?programDbId}{?germplasmDbId}{?germplasmName}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Seed Lot Transactions



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">transactionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Unique DbId for the Seed Lot Transaction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The number of units being transfered between SeedLots. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fromSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td><span style="font-weight:bold;">toSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td><span style="font-weight:bold;">transactionDescription</span></td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td><span style="font-weight:bold;">transactionTimestamp</span></td><td>string<br>(date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being transfered between SeedLots in a transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


 

+ Parameters
    + transactionDbId (Optional, string) ... Unique id for a transaction on this server
    + seedLotDbId (Optional, string) ... Unique id for a seed lot on this server
    + crossDbId (Optional, string) ... Search for Cross with this unique id
    + crossName (Optional, string) ... Search for Cross with this human readable name
    + commonCropName (Optional, string) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, string) ... Use this parameter to only return results associated with the given `Program` unique identifier. <br/>Use `GET /programs` to find the list of available `Programs` on a server.
    + germplasmDbId (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` unique identifier. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
    + germplasmName (Optional, string) ... Use this parameter to only return results associated with the given `Germplasm` by its human readable name. <br/>Use `GET /germplasm` to find the list of available `Germplasm` on a server.
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
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The number of units being transfered between SeedLots. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fromSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td><span style="font-weight:bold;">toSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td><span style="font-weight:bold;">transactionDescription</span></td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td><span style="font-weight:bold;">transactionTimestamp</span></td><td>string<br>(date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being transfered between SeedLots in a transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">transactionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Unique DbId for the Seed Lot Transaction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The number of units being transfered between SeedLots. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fromSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td><span style="font-weight:bold;">toSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td><span style="font-weight:bold;">transactionDescription</span></td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td><span style="font-weight:bold;">transactionTimestamp</span></td><td>string<br>(date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being transfered between SeedLots in a transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


 

+ Parameters
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
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
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The current balance of the amount of material in a SeedLot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">contentMixture</span></td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossDbId</span></td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossName</span></td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.mixturePercentage</span></td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td><span style="font-weight:bold;">createdDate</span></td><td>string<br>(date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">lastUpdated</span></td><td>string<br>(date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDescription</span></td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">sourceCollection</span></td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td><span style="font-weight:bold;">storageLocation</span></td><td>string</td><td>Description the storage location</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being counted in a SeedLot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Required, string) ... Unique id for a seed lot on this server
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
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The current balance of the amount of material in a SeedLot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">contentMixture</span></td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossDbId</span></td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossName</span></td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.mixturePercentage</span></td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td><span style="font-weight:bold;">createdDate</span></td><td>string<br>(date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">lastUpdated</span></td><td>string<br>(date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDescription</span></td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">sourceCollection</span></td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td><span style="font-weight:bold;">storageLocation</span></td><td>string</td><td>Description the storage location</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being counted in a SeedLot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">seedLotDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Unique DbId for the Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">seedLotName</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>A human readable name for this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The current balance of the amount of material in a SeedLot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">contentMixture</span></td><td>array[object]</td><td>The mixture of germplasm present in the seed lot. <br/> If this seed lot only contains a single germplasm, the response should contain the name  and DbId of that germplasm with a mixturePercentage value of 100 <br/> If the seed lot contains a mixture of different germplasm, the response should contain  the name and DbId every germplasm present. The mixturePercentage field should contain  the ratio of each germplasm in the total mixture. All of the mixturePercentage values  in this array should sum to equal 100.</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossDbId</span></td><td>string</td><td>The unique DbId for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.crossName</span></td><td>string</td><td>The human readable name for a cross contained in this seed lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmDbId</span></td><td>string</td><td>The unique DbId of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.germplasmName</span></td><td>string</td><td>The human readable name of the Germplasm contained in this Seed Lot</td></tr>
<tr><td>contentMixture<br><span style="font-weight:bold;margin-left:5px">.mixturePercentage</span></td><td>integer</td><td>The percentage of the given germplasm in the seed lot mixture.</td></tr>
<tr><td><span style="font-weight:bold;">createdDate</span></td><td>string<br>(date-time)</td><td>The time stamp for when this seed lot was created</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">lastUpdated</span></td><td>string<br>(date-time)</td><td>The timestamp for the last update to this Seed Lot (including transactions)</td></tr>
<tr><td><span style="font-weight:bold;">locationDbId</span></td><td>string</td><td>The unique identifier for a Location</td></tr>
<tr><td><span style="font-weight:bold;">locationName</span></td><td>string</td><td>A human readable name for a location</td></tr>
<tr><td><span style="font-weight:bold;">programDbId</span></td><td>string</td><td>The unique DbId of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">programName</span></td><td>string</td><td>The human readable name of the breeding program this Seed Lot belongs to</td></tr>
<tr><td><span style="font-weight:bold;">seedLotDescription</span></td><td>string</td><td>A general description of this Seed Lot</td></tr>
<tr><td><span style="font-weight:bold;">sourceCollection</span></td><td>string</td><td>The description of the source where this material was originally collected (wild, nursery, etc)</td></tr>
<tr><td><span style="font-weight:bold;">storageLocation</span></td><td>string</td><td>Description the storage location</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being counted in a SeedLot (seeds, bulbs, kg, tree, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Required, string) ... Unique id for a seed lot on this server
    + Authorization (Optional, string) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
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
<tr><td><span style="font-weight:bold;">transactionDbId</span></td><td>string<br><span style="font-size: smaller; color: red;">(Required)</span></td><td>Unique DbId for the Seed Lot Transaction</td></tr>
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>A free space containing any additional information related to a particular object. A data source may provide any JSON object, unrestricted by the BrAPI specification.</td></tr>
<tr><td><span style="font-weight:bold;">amount</span></td><td>number</td><td>The number of units being transfered between SeedLots. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).</td></tr>
<tr><td><span style="font-weight:bold;">externalReferences</span></td><td>array[object]</td><td>An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceID</span></td><td>string</td><td>**Deprecated in v2.1** Please use `referenceId`. Github issue number #460  <br>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceId</span></td><td>string</td><td>The external reference ID. Could be a simple string or a URI.</td></tr>
<tr><td>externalReferences<br><span style="font-weight:bold;margin-left:5px">.referenceSource</span></td><td>string</td><td>An identifier for the source system or database of this reference</td></tr>
<tr><td><span style="font-weight:bold;">fromSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered out of</td></tr>
<tr><td><span style="font-weight:bold;">toSeedLotDbId</span></td><td>string</td><td>The identifier for the Seed Lot being transfered into</td></tr>
<tr><td><span style="font-weight:bold;">transactionDescription</span></td><td>string</td><td>A general description of this Seed Lot Transaction</td></tr>
<tr><td><span style="font-weight:bold;">transactionTimestamp</span></td><td>string<br>(date-time)</td><td>The time stamp for when the transaction occurred</td></tr>
<tr><td><span style="font-weight:bold;">units</span></td><td>string</td><td>A description of the things being transfered between SeedLots in a transaction (seeds, bulbs, kg, etc)</td></tr>
</table>


 

+ Parameters
    + seedLotDbId (Required, string) ... Unique id for a seed lot on this server
    + transactionDbId (Optional, string) ... Unique id for a Transaction that has occurred
    + transactionDirection (Optional, string) ... Filter results to only include transactions directed to the specific Seed Lot (TO), away from the specific Seed Lot (FROM), or both (BOTH). The default value for this parameter is BOTH
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

