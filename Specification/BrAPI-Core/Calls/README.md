# Group Calls
The '/calls' call is used to find the available BrAPI calls on a particular server. 




## Calls [/brapi/v1/calls] 




### Get Calls  [GET /brapi/v1/calls{?dataType}{?page}{?pageSize}]

Implementation Notes

Having a consistent structure for the path string of each call is very 
important for teams to be able to connect and find errors. Read more on Github.

Here are the rules for the path of each call that should be returned

Every word in the call path should match the documentation exactly, both in 
spelling and capitalization. Note that path strings are all lower case, but 
path parameters are camel case.

Each path should start relative to \"/\" and therefore should not include \"/\"

No leading or trailing slashes (\"/\") 

Path parameters are wrapped in curly braces (\"{}\"). The name of the path parameter 
should be spelled exactly as it is specified in the documentation.

Examples 

GOOD   "call": "germplasm/{germplasmDbId}/pedigree" 

BAD    "call": "germplasm/{id}/pedigree"

BAD    "call": "germplasm/{germplasmdbid}/pedigree" 

BAD    "call": "brapi/v1/germplasm/{germplasmDbId}/pedigree" 

BAD    "call": "/germplasm/{germplasmDbId}/pedigree/" 

BAD    "call": "germplasm/<germplasmDbId>/pedigree"



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|Array of available calls on this server|
|call|string|The name of the available call as recorded in the documentation|
|dataTypes|array[string]|The possible data formats returned by the available call|
|methods|array[string]|The possible HTTP Methods to be used with the available call|
|versions|array[string]|The supported versions of a particular call|


 

+ Parameters
    + dataType (Optional, ) ... The data format supported by the call.
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
                "call": "germplasm",
                "dataTypes": [
                    "application/json"
                ],
                "methods": [
                    "GET",
                    "POST"
                ],
                "versions": [
                    "1.2",
                    "1.3"
                ]
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

