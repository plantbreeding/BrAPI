
# Group Samples

API methods for tracking/managing plant samples and related meta-data. A 'Sample' in the context of BrAPI, is defined as the actual biological plant material collected from the field.




## Samples-search [/brapi/v1/samples-search] 




### **Deprecated** Get Samples-search  [GET /brapi/v1/samples-search{?sampleDbId}{?observationUnitDbId}{?plateDbId}{?germplasmDbId}{?page}{?pageSize}]

DEPRECATED in v1.3 - see GET /samples



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a samle|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plantDbId|string|The ID which uniquely identifies a plant. Usually 'plantNumber'|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateIndex|integer|The index number of this sample on a plate|
|plotDbId|string| The ID which uniquely identifies a plot. Usually 'plotNumber'|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc |
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|


 

+ Parameters
    + sampleDbId (Optional, ) ... the internal DB id for a sample
    + observationUnitDbId (Optional, ) ... the internal DB id for an observation unit where a sample was taken from
    + plateDbId (Optional, ) ... the internal DB id for a plate of samples
    + germplasmDbId (Optional, ) ... the internal DB id for a germplasm
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "1",
                "plantDbId": "null",
                "plateDbId": "pl1",
                "plateIndex": 0,
                "plotDbId": "1",
                "sampleDbId": "sam00",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            },
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "2",
                "plantDbId": "1",
                "plateDbId": "pl1",
                "plateIndex": 1,
                "plotDbId": "1",
                "sampleDbId": "sam01",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            }
        ]
    }
}
```





### **Deprecated** Post Samples-search  [POST /brapi/v1/samples-search]

DEPRECATED in v1.3 - see GET /search/samples

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbId|array[string]| The ID which uniquely identifies a germplasm|
|observationUnitDbId|array[string]|The ID which uniquely identifies an observation unit|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is 0.|
|pageSize|integer|The size of the pages to be returned. Default is 1000.|
|plateDbId|array[string]|The ID which uniquely identifies a plate of samples|
|sampleDbId|array[string]|The ID which uniquely identifies a sample|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a samle|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plantDbId|string|The ID which uniquely identifies a plant. Usually 'plantNumber'|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateIndex|integer|The index number of this sample on a plate|
|plotDbId|string| The ID which uniquely identifies a plot. Usually 'plotNumber'|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc |
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|


 

+ Parameters


 
+ Request (application/json)
```
{
    "germplasmDbId": [
        "germplasmDbId0",
        "germplasmDbId1"
    ],
    "observationUnitDbId": [
        "observationUnitDbId0",
        "observationUnitDbId1"
    ],
    "page": 0,
    "pageSize": 0,
    "plateDbId": [
        "plateDbId0",
        "plateDbId1"
    ],
    "sampleDbId": [
        "sampleDbId0",
        "sampleDbId1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "1",
                "plantDbId": "null",
                "plateDbId": "pl1",
                "plateIndex": 0,
                "plotDbId": "1",
                "sampleDbId": "sam00",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            },
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "2",
                "plantDbId": "1",
                "plateDbId": "pl1",
                "plateIndex": 1,
                "plotDbId": "1",
                "sampleDbId": "sam01",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            }
        ]
    }
}
```



## Samples [/brapi/v1/samples] 




### Get Samples  [GET /brapi/v1/samples{?sampleDbId}{?observationUnitDbId}{?plateDbId}{?germplasmDbId}{?page}{?pageSize}]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a samle|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plantDbId|string|The ID which uniquely identifies a plant. Usually 'plantNumber'|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateIndex|integer|The index number of this sample on a plate|
|plotDbId|string| The ID which uniquely identifies a plot. Usually 'plotNumber'|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc |
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|


 

+ Parameters
    + sampleDbId (Optional, ) ... the internal DB id for a sample
    + observationUnitDbId (Optional, ) ... the internal DB id for an observation unit where a sample was taken from
    + plateDbId (Optional, ) ... the internal DB id for a plate of samples
    + germplasmDbId (Optional, ) ... the internal DB id for a germplasm
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "1",
                "plantDbId": "null",
                "plateDbId": "pl1",
                "plateIndex": 0,
                "plotDbId": "1",
                "sampleDbId": "sam00",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            },
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "2",
                "plantDbId": "1",
                "plateDbId": "pl1",
                "plateIndex": 1,
                "plotDbId": "1",
                "sampleDbId": "sam01",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Put Samples  [PUT /brapi/v1/samples]

Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a samle|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plantDbId|string|The ID which uniquely identifies a plant. Usually 'plantNumber'|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateIndex|integer|The index number of this sample on a plate|
|plotDbId|string| The ID which uniquely identifies a plot. Usually 'plotNumber'|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc |
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|sampleDbId|string||
|sampleId|string|** Deprecated ** use sampleDbId|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbId": "germplasmDbId0",
    "notes": "notes0",
    "observationUnitDbId": "observationUnitDbId0",
    "plantDbId": "plantDbId0",
    "plateDbId": "plateDbId0",
    "plateIndex": 0,
    "plotDbId": "plotDbId0",
    "sampleDbId": "sampleDbId0",
    "sampleTimestamp": "2018-01-01T14:47:23-0600",
    "sampleType": "sampleType0",
    "studyDbId": "studyDbId0",
    "takenBy": "takenBy0",
    "tissueType": "tissueType0"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "sampleDbId": "d3636ed9-f0d5-47fd-90ea-278d95043411",
        "sampleId": "d3636ed9-f0d5-47fd-90ea-278d95043411"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Samples by sampleDbId  [GET /brapi/v1/samples/{sampleDbId}]

Used to retrieve the details of a single Sample from a Sample Tracking system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a samle|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plantDbId|string|The ID which uniquely identifies a plant. Usually 'plantNumber'|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateIndex|integer|The index number of this sample on a plate|
|plotDbId|string| The ID which uniquely identifies a plot. Usually 'plotNumber'|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc |
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|


 

+ Parameters
    + sampleDbId (Required, ) ... the internal DB id for a sample
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "germplasmDbId": "1",
        "notes": "Example Sample",
        "observationUnitDbId": "2",
        "plantDbId": "1",
        "plateDbId": "pl1",
        "plateIndex": 1,
        "plotDbId": "1",
        "sampleDbId": "sam01",
        "sampleTimestamp": "2018-01-01T00:00:00-05:00",
        "sampleType": "DNA",
        "studyDbId": "1001",
        "takenBy": "Bob",
        "tissueType": "Leaf"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Search [/brapi/v1/search] 




### Post Search Samples  [POST /brapi/v1/search/samples]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.
See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]| The ID which uniquely identifies a germplasm|
|observationUnitDbIds|array[string]|The ID which uniquely identifies an observation unit|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is 0.|
|pageSize|integer|The size of the pages to be returned. Default is 1000.|
|plateDbIds|array[string]|The ID which uniquely identifies a plate of samples|
|sampleDbIds|array[string]|The ID which uniquely identifies a sample|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "observationUnitDbIds": [
        "observationUnitDbIds0",
        "observationUnitDbIds1"
    ],
    "page": 0,
    "pageSize": 0,
    "plateDbIds": [
        "plateDbIds0",
        "plateDbIds1"
    ],
    "sampleDbIds": [
        "sampleDbIds0",
        "sampleDbIds1"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "searchResultDbId": "551ae08c-4548-4bde-ad70-f23beb25e2ea"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Search Samples by searchResultsDbId  [GET /brapi/v1/search/samples/{searchResultsDbId}{?page}{?pageSize}]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.
See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|notes|string|Additional notes about a samle|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|plantDbId|string|The ID which uniquely identifies a plant. Usually 'plantNumber'|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|plateIndex|integer|The index number of this sample on a plate|
|plotDbId|string| The ID which uniquely identifies a plot. Usually 'plotNumber'|
|sampleDbId|string|The ID which uniquely identifies a sample|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc |
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "1",
                "plantDbId": "null",
                "plateDbId": "pl1",
                "plateIndex": 0,
                "plotDbId": "1",
                "sampleDbId": "sam00",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            },
            {
                "germplasmDbId": "1",
                "notes": "Example Sample",
                "observationUnitDbId": "2",
                "plantDbId": "1",
                "plateDbId": "pl1",
                "plateIndex": 1,
                "plotDbId": "1",
                "sampleDbId": "sam01",
                "sampleTimestamp": "2018-01-01T00:00:00-05:00",
                "sampleType": "DNA",
                "studyDbId": "1001",
                "takenBy": "Bob",
                "tissueType": "Leaf"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

