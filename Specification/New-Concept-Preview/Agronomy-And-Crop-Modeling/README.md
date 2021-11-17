
# Group Agronomy and Crop Modeling

Agronomy and Crop Modeling description




### Get - /events [GET /brapi/v2/events{?studyDbId}{?observationUnitDbId}{?eventDbId}{?eventType}{?dateRangeStart}{?dateRangeEnd}{?page}{?pageSize}]

Get list of events



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|date|array[string]|A list of dates when the event occurred  MIAPPE V1.1 (DM-68) Event date - Date and time of the event.|
|eventDbId|string|Internal database identifier|
|eventDescription|string|A detailed, human-readable description of this event  MIAPPE V1.1 (DM-67) Event description - Description of the event, including details such as amount applied and possibly duration of the event. |
|eventParameters|array[object]|A list of objects describing additional event parameters. Each of the following accepts a human-readable value or URI|
|code|string|The shortened code name of an event parameter  ICASA "Code_Display"|
|name|string|The full name of an event parameter  ICASA "Variable_Name"|
|unit|string|The unit or data type of the value. If the value IS NOT a number, then this field should specify a data type eg. text, boolean, date, etc. If the value IS a number, then this field should specify the units used eg. ml, cm, etc  ICASA "Unit_or_type"|
|value|string|The value of this event parameter|
|eventType|string|General category for this event (e.g. Sowing, Watering, Rain). Each eventType should correspond to exactly one eventTypeDbId, if provided.  ICASA "event"  MIAPPE V1.1 (DM-65) Event type - Short name of the event.|
|eventTypeDbId|string|An identifier for this event type, in the form of an ontology class reference  MIAPPE V1.1 (DM-66) Event accession number - Accession number of the event type in a suitable controlled vocabulary (Crop Ontology).|
|observationUnitDbIds|array[string]|A list of the affected observation units. If this parameter is not given, it is understood that the event affected all units in the study|
|studyDbId|string|The study in which the event occurred|


 

+ Parameters
    + studyDbId (Optional, ) ... Filter based on study unique identifier in which the events occurred
    + observationUnitDbId (Optional, ) ... Filter based on an ObservationUnit unique identifier in which the events occurred
    + eventDbId (Optional, ) ... Filter based on an Event DbId
    + eventType (Optional, ) ... Filter based on an Event Type
    + dateRangeStart (Optional, ) ... Filter based on an Date Range
    + dateRangeEnd (Optional, ) ... Filter based on an Date Range
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
                "date": [
                    "2018-10-08T18:15:11Z",
                    "2018-11-09T18:16:12Z"
                ],
                "eventDbId": "8566d4cb",
                "eventDescription": "A set of plots was watered",
                "eventParameters": [
                    {
                        "code": "tiimp",
                        "name": "tillage_implement",
                        "unit": "code",
                        "value": "TI001"
                    },
                    {
                        "code": "tidep",
                        "name": "tillage_operations_depth",
                        "unit": "cm",
                        "value": "20"
                    },
                    {
                        "code": "timix",
                        "name": "till_mix_effectiveness",
                        "unit": "percent",
                        "value": "50"
                    }
                ],
                "eventType": "tillage",
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

