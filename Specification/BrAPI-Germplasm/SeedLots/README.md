# Group SeedLots





## Seedlots [/brapi/v1/seedlots] 




### Get Seedlots  [GET /brapi/v1/seedlots{?seedLotDbId}{?germplasmDbId}{?page}{?pageSize}]

Get a filtered list of Seed Lot descriptions available in a system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|additionalInfo|object|Additional arbitrary info|
|count|integer|Current balance of seeds in this lot|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, stock, tree, etc)|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|locationDbId|string|DbId of the storage location|
|seedLotName|string|A human readable name for this Seed Lot|


 

+ Parameters
    + seedLotDbId (Optional, ) ... Unique id for a seed lot on this server
    + germplasmDbId (Optional, ) ... The internal id of the germplasm
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "count": 561,
                "createdDate": "2018-01-01T14:47:23-0600",
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





### Post Seedlots  [POST /brapi/v1/seedlots]

Add new Seed Lot descriptions to a server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|additionalInfo|object|Additional arbitrary info|
|count|integer|Current balance of seeds in this lot|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, stock, tree, etc)|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|locationDbId|string|DbId of the storage location|
|seedLotName|string|A human readable name for this Seed Lot|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|additionalInfo|object|Additional arbitrary info|
|count|integer|Current balance of seeds in this lot|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, stock, tree, etc)|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|locationDbId|string|DbId of the storage location|
|seedLotName|string|A human readable name for this Seed Lot|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "count": 561,
        "createdDate": "2018-01-01T14:47:23-0600",
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "count": 561,
                "createdDate": "2018-01-01T14:47:23-0600",
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





### Get Seedlots by seedLotDbId  [GET /brapi/v1/seedlots/{seedLotDbId}]

Get a specific Seed Lot by seedLotDbId



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|additionalInfo|object|Additional arbitrary info|
|count|integer|Current balance of seeds in this lot|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, stock, tree, etc)|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|locationDbId|string|DbId of the storage location|
|seedLotName|string|A human readable name for this Seed Lot|


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
        "count": 561,
        "createdDate": "2018-01-01T14:47:23-0600",
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





### Put Seedlots by seedLotDbId  [PUT /brapi/v1/seedlots/{seedLotDbId}]

Update an existing Seed Lot

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|additionalInfo|object|Additional arbitrary info|
|count|integer|Current balance of seeds in this lot|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, stock, tree, etc)|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|locationDbId|string|DbId of the storage location|
|seedLotName|string|A human readable name for this Seed Lot|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|sourceCollection|string|The description of the source where this material was originally collected (wild, nursery, etc)|
|additionalInfo|object|Additional arbitrary info|
|count|integer|Current balance of seeds in this lot|
|germplasmDbId|string|Unique DbId of the Germplasm held in this Seed Lot|
|seedLotDescription|string|A general description of this Seed Lot|
|lastUpdated|string (date-time)|The timestamp for the last update to this Seed Lot (including transactions)|
|programDbId|string|Unique DbId of the breeding Program this Seed Lot belongs to|
|storageLocation|string|Description the storage location|
|units|string|Description of the things being counted in this Seed Lot (seeds, bulbs, stock, tree, etc)|
|createdDate|string (date-time)|The time stamp for when this seed lot was created|
|seedLotDbId|string|Unique DbId for the Seed Lot|
|locationDbId|string|DbId of the storage location|
|seedLotName|string|A human readable name for this Seed Lot|


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "count": 561,
    "createdDate": "2018-01-01T14:47:23-0600",
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
        "count": 561,
        "createdDate": "2018-01-01T14:47:23-0600",
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





### Get Seedlots Transactions by seedLotDbId  [GET /brapi/v1/seedlots/{seedLotDbId}/transactions{?transactionDbId}{?transactionDirection}{?page}{?pageSize}]

Get all Transactions related to a specific Seed Lot



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|count|integer|The amount of units being transfered|
|transactionDbId|string|Unique DbId for the Seed Lot Transaction|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, stock, etc)|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|


 

+ Parameters
    + seedLotDbId (Required, ) ... Unique id for a seed lot on this server
    + transactionDbId (Optional, ) ... Unique id for a Transaction that has occured
    + transactionDirection (Optional, ) ... Filter results to only include transactions directed to the specific Seed Lot (TO), away from the specific Seed Lot (FROM), or both (BOTH). The default value for this parameter is BOTH
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "count": 45,
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





### Get Seedlots Transactions  [GET /brapi/v1/seedlots/transactions{?transactionDbId}{?seedLotDbId}{?germplasmDbId}{?page}{?pageSize}]

Get a filtered list of Seed Lot Transactions



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|count|integer|The amount of units being transfered|
|transactionDbId|string|Unique DbId for the Seed Lot Transaction|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, stock, etc)|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|


 

+ Parameters
    + transactionDbId (Optional, ) ... Unique id for a transaction on this server
    + seedLotDbId (Optional, ) ... Unique id for a seed lot on this server
    + germplasmDbId (Optional, ) ... The internal id of the germplasm
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "count": 45,
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





### Post Seedlots Transactions  [POST /brapi/v1/seedlots/transactions]

Add new Seed Lot Transaction to be recorded

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|seedLots|array[object]||
|additionalInfo|object|Additional arbitrary info|
|count|integer|The amount of units being transfered|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, stock, etc)|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|count|integer|The amount of units being transfered|
|transactionDbId|string|Unique DbId for the Seed Lot Transaction|
|transactionDescription|string|A general description of this Seed Lot Transaction|
|toSeedLotDbId|string|The identifier for the Seed Lot being transfered into|
|units|string|Description of the things being transfered in this transaction (seeds, bulbs, stock, etc)|
|transactionTimestamp|string (date-time)|The time stamp for when the transaction occured|
|fromSeedLotDbId|string|The identifier for the Seed Lot being transfered out of|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "seedLots": [
        {
            "additionalInfo": {},
            "count": 45,
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
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
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
                "count": 45,
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

