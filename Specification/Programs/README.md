
# Group Programs

A Program can contain multiple Trials. A Trial can contain multiple Studies. 



## Programs-search [Post /brapi/v1/programs-search]

 Advanced searching for the programs resource.
Status: ACCEPTED.
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
 

+ Parameters
 
+ Request (application/json)
/definitions/programsSearchRequest

+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "abbreviation": "DRP1",
                "leadPerson": "Dr. Henry Beachell",
                "name": "Wheat Resistance Program",
                "objective": "Disease resistance",
                "programDbId": "123"
            },
            {
                "abbreviation": "DRP2",
                "leadPerson": "Dr. Norman Borlaug",
                "name": "Wheat Improvement Program",
                "objective": "Yield improvement",
                "programDbId": "456"
            }
        ]
    }
}
```

## Programs [Get /brapi/v1/programs{?programName}{?abbreviation}{?pageSize}{?page}]

 Call to retrieve a list of programs.
Status: ACCEPTED Implemented By:
<a href="https://test-server.brapi.org/brapi/v1/programs"> test-server.brapi.org/brapi/v1/programs</a> 

+ Parameters
    + programName (Optional, string) ... Filter by program name. Exact match.
    + abbreviation (Optional, string) ... Filter by program abbreviation. Exact match.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "abbreviation": "DRP1",
                "leadPerson": "Dr. Henry Beachell",
                "name": "Wheat Resistance Program",
                "objective": "Disease resistance",
                "programDbId": "123"
            },
            {
                "abbreviation": "DRP2",
                "leadPerson": "Dr. Norman Borlaug",
                "name": "Wheat Improvement Program",
                "objective": "Yield improvement",
                "programDbId": "456"
            }
        ]
    }
}
```