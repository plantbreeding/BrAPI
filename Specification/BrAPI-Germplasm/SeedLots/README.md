# Group SeedLots






### Get - /seedlots [GET /brapi/v2/seedlots{?seedLotDbId}{?germplasmDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Seed Lot descriptions available in a system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|amount|number|Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|locationDbId|string|DbId of the storage location|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|seedLotName|string|A human readable name for this Seed Lot|
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)|


 

+ Parameters
    + seedLotDbId (Optional, ) ... Unique id for a seed lot on this server
    + germplasmDbId (Optional, ) ... The internal id of the germplasm
    + externalReferenceID (Optional, ) ... Search for Germplasm by an external reference
    + externalReferenceSource (Optional, ) ... Search for Germplasm by an external reference
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
                "createdDate": "2018-01-01T14:47:23-0600",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
                    }
                ],
                "germplasmDbId": "029d705d",
                "lastUpdated": "2018-01-01T14:47:23-0600",
                "locationDbId": "7989c44c",
                "programDbId": "e972d569",
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

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|amount|number|Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|locationDbId|string|DbId of the storage location|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|seedLotDescription|string|A general description of this Seed Lot|
|seedLotName|string|A human readable name for this Seed Lot|
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|amount|number|Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|locationDbId|string|DbId of the storage location|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|seedLotName|string|A human readable name for this Seed Lot|
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "amount": 561,
        "createdDate": "2018-01-01T14:47:23-0600",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            },
            {
                "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                "referenceSource": "BrAPI Example Server"
            }
        ],
        "germplasmDbId": "029d705d",
        "lastUpdated": "2018-01-01T14:47:23-0600",
        "locationDbId": "7989c44c",
        "programDbId": "e972d569",
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
                "createdDate": "2018-01-01T14:47:23-0600",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
                    }
                ],
                "germplasmDbId": "029d705d",
                "lastUpdated": "2018-01-01T14:47:23-0600",
                "locationDbId": "7989c44c",
                "programDbId": "e972d569",
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




### Get - /seedlots/transactions [GET /brapi/v2/seedlots/transactions{?transactionDbId}{?seedLotDbId}{?germplasmDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Seed Lot Transactions



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|amount|number|The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|transactionDbId|string|Unique DbId for the Seed Lot Transaction|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)|


 

+ Parameters
    + transactionDbId (Optional, ) ... Unique id for a transaction on this server
    + seedLotDbId (Optional, ) ... Unique id for a seed lot on this server
    + germplasmDbId (Optional, ) ... The internal id of the germplasm
    + externalReferenceID (Optional, ) ... Search for Germplasm by an external reference
    + externalReferenceSource (Optional, ) ... Search for Germplasm by an external reference
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
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

|Field|Type|Description|
|---|---|---| 
|seedLots|array[object]||
|additionalInfo|object|Additional arbitrary info|
|amount|number|The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|amount|number|The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|transactionDbId|string|Unique DbId for the Seed Lot Transaction|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "seedLots": [
        {
            "additionalInfo": {},
            "amount": 45,
            "externalReferences": [
                {
                    "referenceID": "doi:10.155454/12349537E12",
                    "referenceSource": "DOI"
                },
                {
                    "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                    "referenceSource": "OBO Library"
                },
                {
                    "referenceID": "75a50e76",
                    "referenceSource": "Remote Data Collection Upload Tool"
                },
                {
                    "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                    "referenceSource": "BrAPI Example Server"
                }
            ],
            "fromSeedLotDbId": "11eef13b",
            "toSeedLotDbId": "59339b90",
            "transactionDescription": "f9cd88d2",
            "transactionTimestamp": "2018-01-01T14:47:23-0600",
            "units": "seeds"
        }
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
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

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|amount|number|Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|locationDbId|string|DbId of the storage location|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|seedLotName|string|A human readable name for this Seed Lot|
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)|


 

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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
        "createdDate": "2018-01-01T14:47:23-0600",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            },
            {
                "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                "referenceSource": "BrAPI Example Server"
            }
        ],
        "germplasmDbId": "029d705d",
        "lastUpdated": "2018-01-01T14:47:23-0600",
        "locationDbId": "7989c44c",
        "programDbId": "e972d569",
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




### Put - /seedlots/{seedLotDbId} [PUT /brapi/v2/seedlots/{seedLotDbId}]

Update an existing Seed Lot

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|amount|number|Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|locationDbId|string|DbId of the storage location|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|seedLotDescription|string|A general description of this Seed Lot|
|seedLotName|string|A human readable name for this Seed Lot|
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|amount|number|Current balance of seeds in this lot. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|locationDbId|string|DbId of the storage location|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|seedLotName|string|A human readable name for this Seed Lot|
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, kg, tree, etc)|


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "amount": 561,
    "createdDate": "2018-01-01T14:47:23-0600",
    "externalReferences": [
        {
            "referenceID": "doi:10.155454/12349537E12",
            "referenceSource": "DOI"
        },
        {
            "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
            "referenceSource": "OBO Library"
        },
        {
            "referenceID": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        },
        {
            "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
            "referenceSource": "BrAPI Example Server"
        }
    ],
    "germplasmDbId": "029d705d",
    "lastUpdated": "2018-01-01T14:47:23-0600",
    "locationDbId": "7989c44c",
    "programDbId": "e972d569",
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
        "createdDate": "2018-01-01T14:47:23-0600",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12349537E12",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            },
            {
                "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                "referenceSource": "BrAPI Example Server"
            }
        ],
        "germplasmDbId": "029d705d",
        "lastUpdated": "2018-01-01T14:47:23-0600",
        "locationDbId": "7989c44c",
        "programDbId": "e972d569",
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

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|amount|number|The amount of units being transfered. Could be a count (seeds, bulbs, etc) or a weight (kg of seed).|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID||The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|transactionDbId|string|Unique DbId for the Seed Lot Transaction|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, kg, etc)|


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
    + transactionDbId (Optional, ) ... Unique id for a Transaction that has occured
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
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xlsx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xlsx"
            }
        ],
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
                        "referenceID": "doi:10.155454/12349537E12",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    },
                    {
                        "referenceID": "https://test-server.brapi.org/brapi/v2/object/8557af36",
                        "referenceSource": "BrAPI Example Server"
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

