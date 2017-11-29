## List Study Types [/brapi/v1/studytypes]

Call to retrieve the list of study types.

Scope: PHENOTYPING.
Implementation target date: PAG2016

### **Deprecated** List study types [GET /brapi/v1/studyTypes?pageSize={pageSize}&page={page}]
+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)
        
        {
             "metadata" : {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 3,
                    "totalPages": 1
                },
                "status": [],
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
                        "name": "Genotype",
                        "description": "Description for Genotyping study type"
                    }
                ]
            }
        }
    

### GET /brapi/v1/studytypes [GET /brapi/v1/studytypes?pageSize={pageSize}&page={page}]
+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)
        
        {
             "metadata" : {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 3,
                    "totalPages": 1
                },
                "status": [],
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
                        "name": "Genotype",
                        "description": "Description for Genotyping study type"
                    }
                ]
            }
        }
    

