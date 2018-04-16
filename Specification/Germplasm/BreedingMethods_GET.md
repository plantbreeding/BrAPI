## Breeding Methods [/brapi/v1/breedingmethods]
Scope: Germplasm

Get the list of germplasm breeding methods available in a system.

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|breedingMethodDbId|string|Internal db identifier|Y|
|abbreviation|string|Short string used as a human readable identifier|Y|
|name|string|Full human readable name of the breeding method|Y|
|description|string|Descriptive paragraph of the breeding method|Y|



### GET List of Breeding Methods [GET /brapi/v1/breedingmethods{?pageSize}{?page}]
+ Parameters
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
+ Response 200 (application/json)
    
        { 
            "metadata" : {
                "pagination": {
                    "pageSize":1000, 
                    "currentPage":0, 
                    "totalCount":2, 
                    "totalPages":1 
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data": [
                        {
                            "breedingMethodDbId": "BM987",
                            "abbreviation": "MBCR",
                            "name": "Male Backcross",
                            "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate."
                        },
                        {
                            "breedingMethodDbId": "BM324",
                            "abbreviation": "DSP",
                            "name": "Single plant selection",
                            "description": "Derivation through selection of a single plant, inflorescence, fruit or seed from a population"
                        }
                    ]
            }
        }

