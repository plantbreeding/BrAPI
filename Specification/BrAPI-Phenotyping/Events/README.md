# Group Events

An event is discrete occurrence at a particular time in the experiment (which can be natural, such as rain, or unnatural, such as planting, watering, etc). Events may be the realization of Treatments or parts of Treatments, or may be confounding to Treatments. Can be applied at the whole study level or to only a subset of observation units.  
[also see the [MIAPPE](https://www.miappe.org/) definition]


## Events [/brapi/v1/events] 


### Get events by study [GET /brapi/v1/events{?studyDbId}{?page}{?pageSize}]


+ Parameters
    + eventDbId ... Internal database identifier
    + eventTypeName ... General category for this event (e.g. Sowing, Watering, Rain). Each eventType should correspond to exactly one eventTypeDbId, if provided.
    + eventTypeDbId (Optional, ) ... An identifier for this event type, in the form of an ontology class reference.
    + date ... A list of datetimes at which this event occurred. 
    + description (Optional, ) ... A detailed, human-readable description of this event.
    + studyDbId ... The study in which the event occurred.
    + observationUnitDbId (Optional, ) ... A list of the affected observation units. If this parameter is not given, it is understood that the event affected all units in the study.
    + additionalInfo (Optional, ) ... A list of objects describing additional event parameters. Each of the following accepts a human-readable value or URI.
	    + key ... Specifies the relationship between the event and the given property. E.g. fertilizer, operator
	    + value ... The value of the property for this event. E.g. nitrogen, John Doe
	    + valueRdfType (Optional, ) ... The type of the value given above, e.g. http://xmlns.com/foaf/0.1/Agent
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
                "eventDbId": "ID12345",
                "eventTypeName": "Planting",
                "eventTypeDbId": "CO_715:0000007",
                "description": "Sowing using seed drill",
                "studyDbId": "studyX",
                "observationUnitDbId": [
                    "obsUnit1",
                    "obsUnit2"
                ],
                "date": [
                    "2017-09-08T12:00:00+01:00"
                ],
                "additionalInfo": [
                    {
                        "key": "sowing method",
                        "value": "seed drill",
                        "valueRdfType": null
                    }
                ]
            },
            {
                "eventDbId": "ID12346",
                "eventTypeName": "Fertilizing",
                "eventTypeDbId": "http://www.cropontology.org/rdf/CO_715:0000011",
                "description": "Fertilizer application: Ammonium nitrate at 3 kg/m2",
                "studyDbId": "studyY",
                "observationUnitDbId": [],
                "date": [
                    "2017-09-09T12:00:00+01:00"
                ],
                "additionalInfo": [
                    {
                        "key": "fertilizer",
                        "value": "ammonium nitrate",
                        "valueRdfType": null
                    },
                    {
                        "key": "amount",
                        "value": "3",
                        "valueRdfType": null
                    },
                    {
                        "key": "unit",
                        "value": "kg/m2"
                    },
                    {
                        "key": "http://www.phenome-fppn.fr/vocabulary/2018#hasContact",
                        "value": "http://www.phenome-fppn.fr/diaphen/id/agent/marie_dupond",
                        "valueRdfType": "http://xmlns.com/foaf/0.1/Agent"
                    }
                ]
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


