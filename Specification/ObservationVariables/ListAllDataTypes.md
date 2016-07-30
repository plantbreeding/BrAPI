## List all Data Types [/brapi/v1/variables/datatypes]

Call to retrieve a list of data types the variable can have.

### List all data types [GET]
+ Response 200 (application/json)
        
        {
            "metadata": {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 6,
                    "totalPages": 1
                },
                "status": {},
                "datafiles": []
            },
            "result": ["Numeric", "Categorical", "Date", "Text", "Picture", "Boolean"]
        }  
