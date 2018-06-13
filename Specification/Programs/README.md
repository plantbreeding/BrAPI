
# Group Programs

A Program can contain multiple Trials. A Trial can contain multiple Studies. 



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
    "result": {
        "data": [
            {
                "name": "Wheat Resistance Program",
                "objective": "Disease resistance",
                "abbreviation": "DRP1",
                "leadPerson": "Dr. Henry Beachell",
                "programDbId": "123"
            },
            {
                "name": "Wheat Improvement Program",
                "objective": "Yield improvement",
                "abbreviation": "DRP2",
                "leadPerson": "Dr. Norman Borlaug",
                "programDbId": "456"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

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
    "result": {
        "data": [
            {
                "name": "Wheat Resistance Program",
                "objective": "Disease resistance",
                "abbreviation": "DRP1",
                "leadPerson": "Dr. Henry Beachell",
                "programDbId": "123"
            },
            {
                "name": "Wheat Improvement Program",
                "objective": "Yield improvement",
                "abbreviation": "DRP2",
                "leadPerson": "Dr. Norman Borlaug",
                "programDbId": "456"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```