## Variable data type list [/brapi/v1/variables/datatypes&pageSize={pageSize}&page={page}]

Call to retrieve a list of data types the variable can have.

### Variable data type list [GET]

+ Parameters
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `10`) ... Which result page is requested
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
