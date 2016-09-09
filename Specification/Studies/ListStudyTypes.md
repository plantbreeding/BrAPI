## List Study Types [/brapi/v1/studyTypes?pageSize=&page=]

Call to retrieve the list of study types.

Implementation target date: PAG2016

### List study types [GET]
+ Parameters
    + pageSize (optional, integer, `1`)
    + page (optional, integer, `1`)

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
                        "name": "Crossing Nursery",
                        "description": "Description for Nursery study type"
                    },
                    {
                        "name": "Yield Trial",
                        "description": "Description for Trial study type"
                    },
                    {
                        "name": Genotype",
                        "description": "Description for Genotyping study type"
                    }
                ]
            }
        }
