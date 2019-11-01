# Group Events

An event is discrete occurrence at a particular time in the experiment (which can be natural, such as rain, or unnatural, such as planting, watering, etc). Events may be the realization of Treatments or parts of Treatments, or may be confounding to Treatments. Can be applied at the whole study level or to only a subset of observation units.  
[also see the [MIAPPE](https://www.miappe.org/) definition]



## Events [/brapi/v1/events] 




### Get Events  [GET /brapi/v1/events{?studyDbId}{?page}{?pageSize}]

Get list of events



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|date|array[string]|A list of dates when the event occured|
|eventTypeDbId|string|An identifier for this event type, in the form of an ontology class reference|
|eventType|string|General category for this event (e.g. Sowing, Watering, Rain). Each eventType should correspond to exactly one eventTypeDbId, if provided.|
|eventParameters|array[object]|A list of objects describing additional event parameters. Each of the following accepts a human-readable value or URI|
|value|string|The value of the property for this event. E.g. nitrogen, John Doe|
|key|string|Specifies the relationship between the event and the given property. E.g. fertilizer, operator|
|rdfValue|string|The type of the value given above, e.g. http://xmlns.com/foaf/0.1/Agent|
|description|string|A detailed, human-readable description of this event|
|eventDbId|string|Internal database identifier|
|studyDbId|string|The study in which the event occurred|
|additionalInfo|object|Additional arbitrary info|
|observationUnitDbIds|array[string]|A list of the affected observation units. If this parameter is not given, it is understood that the event affected all units in the study|


 

+ Parameters
    + studyDbId (Required, ) ... Filter based on study unique identifier in which the events occured
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
                "date": [
                    "2018-10-08T18:15:11Z",
                    "2018-11-09T18:16:12Z"
                ],
                "description": "A set of plots was watered",
                "eventDbId": "8566d4cb",
                "eventParameters": [
                    {
                        "key": "http://www.phenome-fppn.fr/vocabulary/2018#hasContact,",
                        "value": "http://www.phenome-fppn.fr/diaphen/id/agent/marie_dupond,",
                        "valueRdfType": "http://xmlns.com/foaf/0.1/Agent,"
                    },
                    {
                        "key": "fertilizer",
                        "value": "nitrogen",
                        "valueRdfType": null
                    }
                ],
                "eventType": "Watering",
                "eventTypeDbId": "4e7d691e",
                "observationUnitDbIds": [
                    "8439eaff",
                    "d7682e7a",
                    "305ae51c"
                ],
                "studyDbId": "2cc2001f"
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

