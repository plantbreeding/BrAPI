## Seasons [/brapi/v1/seasons?year={year}&pageSize={pageSize}&page={page}]

Call to retrive all seasons (or years) in the database. (Added by Jan-Erik and Lukas 5/26/2016)

Scope: PHENOTYPING

### List seasons or years [GET]
+ Parameters
    + year (optional, String, `2015`)
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata" : {
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
                "data" : [
                    { "seasonDbId": "237", "season": "Fall", "year": "2015" }, 
                    { "seasonDbId": "238", "season": "Spring", "year": "2016" }
                ]
            }
        }
