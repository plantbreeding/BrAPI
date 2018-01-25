## Genome Map Details [/brapi/v1/maps/{mapDbId}]

Status: ACCEPTED

Implemented by: Germinate, Cassavabase

Used by: Flapjack

### Get map details [GET /brapi/v1/maps/{mapDbId}{?pageSize}{?page}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup

+ Paramters
    + mapDbId (required, string, `abc123`) ... the internal db id of a selected map
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    
+ Response 200 (application/json)
            
        {
            "metadata" : {
                "pagination" : { 
                    "pageSize":1000, 
                    "currentPage":0, 
                    "totalCount":2, 
                    "totalPages":1
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "mapDbId": "abc123",
                "name": "Some map",
                "type": "Genetic",
                "unit": "cM",
                "data": [    
                    {
                        "linkageGroupName": "1",
                        "markerCount": 100000,
                        "maxPosition": 10000000
                    },
                    {
                        "linkageGroupName": "2",
                        "markerCount": 1247,
                        "maxPosition": 12347889
                    }
                ]
            }
        }

