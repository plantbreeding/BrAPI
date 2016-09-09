## Variable data type list [/brapi/v1/variables/datatypes]

Call to retrieve a list of data types the variable can have.

### Variable data type list [GET]

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 6,
                    "totalPages": 1
                },
                "status": null,
                "datafiles": []
            },
            "result": {
                "data": ["Numeric", "Categorical", "Date", "Text", "Picture", "Boolean"]
            }
        }  
