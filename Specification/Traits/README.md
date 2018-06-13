
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
                "defaultValue": null,
                "name": "Plant Height",
                "observationVariables": [
                    "CO_334:0100121",
                    "CO_334:0100122",
                    "CO_334:0100123"
                ],
                "traitId": "CO:123000007",
                "traitDbId": "123",
                "description": "Description of Plant Height"
            },
            {
                "defaultValue": null,
                "name": "Carotenoid content",
                "observationVariables": [
                    "CO_334:0100621",
                    "CO_334:0100622",
                    "CO_334:0100623"
                ],
                "traitId": "CO_334:0100620",
                "traitDbId": "123",
                "description": "Cassava storage root pulp carotenoid content"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
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
        "defaultValue": null,
        "name": "Plant Height",
        "observationVariables": [
            "CO_334:0100121",
            "CO_334:0100122",
            "CO_334:0100123"
        ],
        "traitId": "CO:123000007",
        "traitDbId": "123",
        "description": "Description of Plant Height"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
    }
}
```