## Allele Matrices [/brapi/v1/allelematrices]
Implemented by: GOBII

Used by: Flapjack

This resource is used for reading and writing genomic matrices:
+ GET provides a list of available matrices, optionally filtered by study;

### Matrices through GET [GET /brapi/v1/allelematrices{?studyDbId}{?pageSize}{?page}]
+ Parameters
    + studyDbId (required, string, `abc123`) ... restricts the list of matrices to a specific study. 
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    
+ Response 200 (application/json)

        {
            "metadata": {   
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : { 
                "data":[
                    {
                        "name": "testDs1",
                        "matrixDbId": "27",
                        "description": "a test dataset",
                        "lastUpdated": "2017-06-12",
                        "studyDbId": "abc123"
                    },
                    {
                        "name": "testDs2",
                        "matrixDbId": "28",
                        "description": "a second test dataset",
                        "lastUpdated": "2017-06-12",
                        "studyDbId": "abc123"
                    }
                ]
            }
        }
                                                                                                                           

