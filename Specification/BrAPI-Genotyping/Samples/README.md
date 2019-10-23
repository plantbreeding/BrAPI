
# Group Samples

API methods for tracking/managing plant samples and related meta-data. A 'Sample' in the context of BrAPI, is defined as the actual biological plant material collected from the field.




## Samples [/brapi/v1/samples] 




### Get Samples  [GET /brapi/v1/samples{?sampleDbId}{?observationUnitDbId}{?plateDbId}{?germplasmDbId}{?page}{?pageSize}]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleDbId|string|The ID which uniquely identifies a sample|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|sampleName|string|The name of the sample|
|notes|string|Additional notes about a sample|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|plateName|string|The human readable name of a plate|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|column|integer|The Column identifier for this samples location in the plate|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|row|string|The Row identifier for this samples location in the plate|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + sampleDbId (Optional, ) ... the internal DB id for a sample
    + observationUnitDbId (Optional, ) ... the internal DB id for an observation unit where a sample was taken from
    + plateDbId (Optional, ) ... the internal DB id for a plate of samples
    + germplasmDbId (Optional, ) ... the internal DB id for a germplasm
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
                "column": 6,
                "germplasmDbId": "7e08d538",
                "notes": "This sample was taken from the root of a tree",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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





### Post Samples  [POST /brapi/v1/samples]

Call to register the event of a sample being taken. Sample ID is assigned as a result of the operation and returned in response.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|sampleName|string|The name of the sample|
|notes|string|Additional notes about a sample|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|plateName|string|The human readable name of a plate|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|column|integer|The Column identifier for this samples location in the plate|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|row|string|The Row identifier for this samples location in the plate|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleDbId|string|The ID which uniquely identifies a sample|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|sampleName|string|The name of the sample|
|notes|string|Additional notes about a sample|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|plateName|string|The human readable name of a plate|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|column|integer|The Column identifier for this samples location in the plate|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|row|string|The Row identifier for this samples location in the plate|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "additionalInfo": {},
        "column": 6,
        "germplasmDbId": "7e08d538",
        "notes": "This sample was taken from the root of a tree",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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
                "column": 6,
                "germplasmDbId": "7e08d538",
                "notes": "This sample was taken from the root of a tree",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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





### Get Samples by sampleDbId  [GET /brapi/v1/samples/{sampleDbId}]

Used to retrieve the details of a single Sample from a Sample Tracking system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleDbId|string|The ID which uniquely identifies a sample|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|sampleName|string|The name of the sample|
|notes|string|Additional notes about a sample|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|plateName|string|The human readable name of a plate|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|column|integer|The Column identifier for this samples location in the plate|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|row|string|The Row identifier for this samples location in the plate|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + sampleDbId (Required, ) ... the internal DB id for a sample
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
        "column": 6,
        "germplasmDbId": "7e08d538",
        "notes": "This sample was taken from the root of a tree",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDbId": "cd06a61d",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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





### Put Samples by sampleDbId  [PUT /brapi/v1/samples/{sampleDbId}]

Update the details of an existing Sample

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|sampleName|string|The name of the sample|
|notes|string|Additional notes about a sample|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|plateName|string|The human readable name of a plate|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|column|integer|The Column identifier for this samples location in the plate|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|row|string|The Row identifier for this samples location in the plate|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleDbId|string|The ID which uniquely identifies a sample|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|sampleName|string|The name of the sample|
|notes|string|Additional notes about a sample|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|plateName|string|The human readable name of a plate|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|column|integer|The Column identifier for this samples location in the plate|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|row|string|The Row identifier for this samples location in the plate|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + sampleDbId (Required, ) ... the internal DB id for a sample
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "additionalInfo": {},
    "column": 6,
    "germplasmDbId": "7e08d538",
    "notes": "This sample was taken from the root of a tree",
    "observationUnitDbId": "073a3ce5",
    "plateDbId": "2dce16d1",
    "plateName": "Plate_alpha_20191022",
    "programDbId": "bd748e00",
    "row": "B",
    "sampleBarcode": "3a027b59",
    "sampleGroupDbId": "8524b436",
    "sampleName": "Sample_alpha_20191022",
    "samplePUI": "doi:10.15454/312953986E3",
    "sampleTimestamp": "2018-01-01T14:47:23-0600",
    "sampleType": "Tissue",
    "studyDbId": "64bd6bf9",
    "takenBy": "Bob",
    "tissueType": "Root",
    "trialDbId": "d34c5349",
    "well": "B6"
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
        "column": 6,
        "germplasmDbId": "7e08d538",
        "notes": "This sample was taken from the root of a tree",
        "observationUnitDbId": "073a3ce5",
        "plateDbId": "2dce16d1",
        "plateName": "Plate_alpha_20191022",
        "programDbId": "bd748e00",
        "row": "B",
        "sampleBarcode": "3a027b59",
        "sampleDbId": "cd06a61d",
        "sampleGroupDbId": "8524b436",
        "sampleName": "Sample_alpha_20191022",
        "samplePUI": "doi:10.15454/312953986E3",
        "sampleTimestamp": "2018-01-01T14:47:23-0600",
        "sampleType": "Tissue",
        "studyDbId": "64bd6bf9",
        "takenBy": "Bob",
        "tissueType": "Root",
        "trialDbId": "d34c5349",
        "well": "B6"
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



## Search [/brapi/v1/search] 




### Post Search Samples  [POST /brapi/v1/search/samples]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|sampleDbIds|array[string]|The ID which uniquely identifies a sample|
|germplasmDbIds|array[string]| The ID which uniquely identifies a germplasm|
|plateDbIds|array[string]|The ID which uniquely identifies a plate of samples|
|observationUnitDbIds|array[string]|The ID which uniquely identifies an observation unit|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "germplasmDbIds": [
        "germplasmDbIds1",
        "germplasmDbIds2"
    ],
    "observationUnitDbIds": [
        "observationUnitDbIds1",
        "observationUnitDbIds2"
    ],
    "plateDbIds": [
        "plateDbIds1",
        "plateDbIds2"
    ],
    "sampleDbIds": [
        "sampleDbIds1",
        "sampleDbIds2"
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
        "searchResultDbId": "551ae08c"
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





### Get Search Samples by searchResultsDbId  [GET /brapi/v1/search/samples/{searchResultsDbId}{?page}{?pageSize}]

Used to retrieve list of Samples from a Sample Tracking system based on some search criteria.

See Search Services for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|trialDbId|string|The ID which uniquely identifies a trial within the given database server|
|sampleType|string|The type of sample taken. ex. 'DNA', 'RNA', 'Tissue', etc|
|sampleTimestamp|string (date-time)|The date and time a sample was collected from the field|
|sampleDbId|string|The ID which uniquely identifies a sample|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbId|string|The ID which uniquely identifies an observation unit|
|sampleName|string|The name of the sample|
|notes|string|Additional notes about a sample|
|sampleBarcode|string|A unique identifier physically attached to the sample|
|samplePUI|string|A permanent unique identifier for the sample (DOI, URL, UUID, etc)|
|takenBy|string|The name or identifier of the entity which took the sample from the field|
|plateDbId|string|The ID which uniquely identifies a plate of samples|
|programDbId|string|The ID which uniquely identifies a program within the given database server|
|plateName|string|The human readable name of a plate|
|studyDbId|string|The ID which uniquely identifies a study within the given database server|
|column|integer|The Column identifier for this samples location in the plate|
|tissueType|string|The type of tissue sampled. ex. 'Leaf', 'Root', etc.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|sampleGroupDbId|string|The ID which uniquely identifies a group of samples|
|row|string|The Row identifier for this samples location in the plate|
|well|string|The Well identifier for this samples location in the plate. Ussually a concatination of Row and Column, or just a number if the samples are not part of an ordered plate.|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
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
                "column": 6,
                "germplasmDbId": "7e08d538",
                "notes": "This sample was taken from the root of a tree",
                "observationUnitDbId": "073a3ce5",
                "plateDbId": "2dce16d1",
                "plateName": "Plate_alpha_20191022",
                "programDbId": "bd748e00",
                "row": "B",
                "sampleBarcode": "3a027b59",
                "sampleDbId": "cd06a61d",
                "sampleGroupDbId": "8524b436",
                "sampleName": "Sample_alpha_20191022",
                "samplePUI": "doi:10.15454/312953986E3",
                "sampleTimestamp": "2018-01-01T14:47:23-0600",
                "sampleType": "Tissue",
                "studyDbId": "64bd6bf9",
                "takenBy": "Bob",
                "tissueType": "Root",
                "trialDbId": "d34c5349",
                "well": "B6"
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

