## List Seasons [/brapi/v1/seasons?year=&pageSize=&page=]

Call to retrive all seasons (or years) in the database. (Added by Jan-Erik and Lukas 5/26/2016)

### List seasons or years [GET]
+ Parameters
    + year (optional, String, `2015`)
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
                "status": {},
                "datafiles": []
            },
            "result" : { 
                "data" : [
                    { "seasonDbId": "237", "season": "Fall", "year": "2015" }, 
                    { "seasonDbId": "238", "season": "Spring", "year": "2016" }
                ]
            }
        }
