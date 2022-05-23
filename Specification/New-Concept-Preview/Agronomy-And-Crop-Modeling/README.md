
# Group Agronomy and Crop Modeling

Agronomy and Crop Modeling description




### Get - /events [GET /brapi/v2/events{?studyDbId}{?observationUnitDbId}{?eventDbId}{?eventType}{?dateRangeStart}{?dateRangeEnd}{?page}{?pageSize}]

Get list of events



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">additionalInfo</span></td><td>object</td><td>Additional arbitrary info</td></tr>
<tr><td><span style="font-weight:bold;">date</span></td><td>object</td><td></td></tr>
<tr><td>date<br><span style="font-weight:bold;margin-left:5px">.discreteDates</span></td><td>array[string]</td><td>A list of dates when the event occurred <br/>MIAPPE V1.1 (DM-68) Event date - Date and time of the event.</td></tr>
<tr><td>date<br><span style="font-weight:bold;margin-left:5px">.endDate</span></td><td>string<br>(date-time)</td><td>The end of a continous or regularly repetitive event <br/>MIAPPE V1.1 (DM-68) Event date - Date and time of the event.</td></tr>
<tr><td>date<br><span style="font-weight:bold;margin-left:5px">.startDate</span></td><td>string<br>(date-time)</td><td>The begining of a continous or regularly repetitive event <br/>MIAPPE V1.1 (DM-68) Event date - Date and time of the event.</td></tr>
<tr><td><span style="font-weight:bold;">eventDbId</span></td><td>string</td><td>Internal database identifier</td></tr>
<tr><td><span style="font-weight:bold;">eventDescription</span></td><td>string</td><td>A detailed, human-readable description of this event <br/>MIAPPE V1.1 (DM-67) Event description - Description of the event, including details such as amount applied and possibly duration of the event. </td></tr>
<tr><td><span style="font-weight:bold;">eventParameters</span></td><td>array[object]</td><td>A list of objects describing additional event parameters. Each of the following accepts a human-readable value or URI</td></tr>
<tr><td>eventParameters<br><span style="font-weight:bold;margin-left:5px">.code</span></td><td>string</td><td>The shortened code name of an event parameter  ICASA "Code_Display"</td></tr>
<tr><td>eventParameters<br><span style="font-weight:bold;margin-left:5px">.codeValueDescription</span></td><td>string</td><td>If the event parameter 'unit' field is 'code', then use 'codeValueDescription' to add a human readable description to the value.</td></tr>
<tr><td>eventParameters<br><span style="font-weight:bold;margin-left:5px">.name</span></td><td>string</td><td>The full name of an event parameter  ICASA "Variable_Name"</td></tr>
<tr><td>eventParameters<br><span style="font-weight:bold;margin-left:5px">.parameterDescription</span></td><td>string</td><td>A human readable description of this event parameter. This description is ussually associated with the 'name' and 'code' of an event parameter.</td></tr>
<tr><td>eventParameters<br><span style="font-weight:bold;margin-left:5px">.unit</span></td><td>string</td><td>The unit or data type of the value.  <br>If the 'value' comes from a standardized vocabulary or an encoded list of values, then 'unit' should be 'code'.  <br>If the 'value' IS NOT a number, then 'unit' should specify a data type eg. 'text', 'boolean', 'date', etc.  <br>If the value IS a number, then 'unit' should specify the units used eg. 'ml', 'cm', etc <br>ICASA "Unit_or_type"</td></tr>
<tr><td>eventParameters<br><span style="font-weight:bold;margin-left:5px">.value</span></td><td>string</td><td>The single value of this event parameter. This single value is accurate for all the dates in the date range. If 'value' is populated then 'valuesByDate' should NOT be populated.</td></tr>
<tr><td>eventParameters<br><span style="font-weight:bold;margin-left:5px">.valuesByDate</span></td><td>array[string]</td><td>An array of values corrisponding to each timestamp in the 'discreteDates' array of this event. The 'valuesByDate' array should exactly match the size of the 'discreteDates' array. If 'valuesByDate' is populated then 'value' should NOT be populated.</td></tr>
<tr><td><span style="font-weight:bold;">eventType</span></td><td>string</td><td>General category for this event (e.g. fertilizer, irrigation, tillage). Each eventType should correspond to exactly one eventTypeDbId, if provided. <br/>ICASA Management events allow for the following types: planting, fertilizer, irrigation, tillage, organic_material, harvest, bed_prep, inorg_mulch, inorg_mul_rem, chemicals, mowing, observation, weeding, puddling, flood_level, other <br/>MIAPPE V1.1 (DM-65) Event type - Short name of the event.</td></tr>
<tr><td><span style="font-weight:bold;">eventTypeDbId</span></td><td>string</td><td>An identifier for this event type, in the form of an ontology class reference <br/>ICASA Management events allow for the following types: planting, fertilizer, irrigation, tillage, organic_material, harvest, bed_prep, inorg_mulch, inorg_mul_rem, chemicals, mowing, observation, weeding, puddling, flood_level, other <br/>MIAPPE V1.1 (DM-66) Event accession number - Accession number of the event type in a suitable controlled vocabulary (Crop Ontology).</td></tr>
<tr><td><span style="font-weight:bold;">observationUnitDbIds</span></td><td>array[string]</td><td>A list of the affected observation units. If this parameter is not given, it is understood that the event affected all units in the study</td></tr>
<tr><td><span style="font-weight:bold;">studyDbId</span></td><td>string</td><td>The study in which the event occurred</td></tr>
<tr><td><span style="font-weight:bold;">studyName</span></td><td>string</td><td>The human readable name of a study</td></tr>
</table>


 

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
                "date": {
                    "discreteDates": [
                        "2018-10-08T18:15:11Z",
                        "2018-11-09T18:16:12Z",
                        "2018-11-19T18:16:12Z"
                    ],
                    "endDate": "2018-10-08T18:15:11Z",
                    "startDate": "2018-10-08T18:15:11Z"
                },
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
                "studyDbId": "2cc2001f",
                "studyName": "2cc2001f"
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

