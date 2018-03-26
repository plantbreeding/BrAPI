## List attribute categories [/brapi/v1/attributes/categories] 
Scope: OTHER. Status: ACCEPTED.
Implementation target date: PAG2016

### Germplasm attribute categories [GET /brapi/v1/attributes/categories{?pageSize}{?page}]
List all available attribute categories.
+ Parameters
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : { 
                "data" : [
                    {
                        "attributeCategoryDbId": "1", 
                        "name": "Morphological"
                    },
                    {
                        "attributeCategoryDbId": "2", 
                        "name": "Agronomic"
                    }
                ]
            }
        }
