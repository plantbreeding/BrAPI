## List attribute categories [/brapi/v1/attributes/categories/?pageSize=10&page=2] 
Scope: OTHER. Status: ACCEPTED.
Implementation target date: PAG2016

### Germplasm attribute categories [GET]
List all available attribute categories.
+ Parameters
    + pageSize (optional, number, `10000`) Number of attributes to return in one response
    + page (optional, number, `1`) ... Required if `pageSize` is given; and requires that `pageSize` be given. The first page is 1, not 0.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 10,
                    "totalPages": 1
                },
                "status": null,
                "datafiles": []
            },
            "result" : { 
                "data" : [
                    {
                        "attributeCategoryDbId": 1, 
                        "name": "Morphological"
                    },
                    {
                        "attributeCategoryDbId": 2, 
                        "name": "Agronomic"
                    }
                ]
            ]
        }
