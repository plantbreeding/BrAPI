## Variable data type list [/brapi/v1/variables/datatypes]

Call to retrieve a list of data types the variable can have.

### Variable data type list [GET /brapi/v1/variables/datatypes{?pageSize}{?page}]

+ Parameters
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 6,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": ["Numeric", "Categorical", "Date", "Text", "Picture", "Boolean"]
            }
        }  
