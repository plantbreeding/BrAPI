
# Group Traits

Trait Ontology Calls. API to retrieve list of traits and their associated variables.




## Traits [Get /brapi/v1/traits{?pageSize}{?page}]

 Scope: CORE. Status: ACCEPTED.
Implemented by: Germinate, Cassavabase
Call to retrieve a list of traits available in the system and their associated variables.
<a href="https://test-server.brapi.org/brapi/v1/traits"> test-server.brapi.org/brapi/v1/traits</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "traitId": "CO:123000007",
                "description": "Description of Plant Height",
                "name": "Plant Height",
                "observationVariables": [
                    "CO_334:0100121",
                    "CO_334:0100122",
                    "CO_334:0100123"
                ],
                "traitDbId": "123",
                "defaultValue": null
            },
            {
                "traitId": "CO_334:0100620",
                "description": "Cassava storage root pulp carotenoid content",
                "name": "Carotenoid content",
                "observationVariables": [
                    "CO_334:0100621",
                    "CO_334:0100622",
                    "CO_334:0100623"
                ],
                "traitDbId": "123",
                "defaultValue": null
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "datafiles": [],
        "status": []
    }
}
```

## Traits/{traitdbid} [Get /brapi/v1/traits/{traitDbId}]

 Scope: CORE. Status: ACCEPTED.
Implemented by: Germinate
Retrieve the variables associated to a trait
<a href="https://test-server.brapi.org/brapi/v1/traits"> test-server.brapi.org/brapi/v1/traits/{traitDbId}</a> 

+ Parameters
    + traitDbId (Required, string) ... Id of the trait to retrieve details of.


+ Response 200 (application/json)
```
{
    "result": {
        "traitId": "CO:123000007",
        "description": "Description of Plant Height",
        "name": "Plant Height",
        "observationVariables": [
            "CO_334:0100121",
            "CO_334:0100122",
            "CO_334:0100123"
        ],
        "traitDbId": "123",
        "defaultValue": null
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "datafiles": [],
        "status": []
    }
}
```