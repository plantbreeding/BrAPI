## Breeding Methods [/brapi/v2/breedingmethods?breedingMethodType=&pageSize=&page=]

Call to retrive all breeding methods available in the database.

Scope: PHENOTYPING
Status: PROPOSED

### List breeding methods [GET]
+ Parameters
    + breedingMethodType (optional, integer, `cross|selection`) 
    + pageSize (optional, integer, `10`)
    + page (optional, integer, `1`)
+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 0,
                    "totalCount": 10,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : { 
                "data" : [
                    {
                        "breedingMethodDbId": 9,
                        "breedingMEthodType": "crossing"
                        "abbreviation": "MBCR",
                        "name": "Male Backcross",
                        "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate."
                        },
                        {
                        "breedingMethodDbId": 10,
                        "breedingMEthodType": "selection"
                        "abbreviation": "DSP",
                        "name": "Single plant selection",
                        "description": "Derivation through selection of a single plant, inflorescence, fruit or seed from a population"
                        }
                ]
            }
        }
