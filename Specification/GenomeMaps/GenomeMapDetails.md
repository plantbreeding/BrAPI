## Genome Map Details [/brapi/v1/maps/{mapDbId}]

Status: ACCEPTED

Implemented by: Germinate, Cassavabase

Used by: Flapjack

### Get map details [GET /brapi/v1/maps/{mapDbId}]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup

+ Paramters
    + mapDbId (required, string, `abc123`) ... the internal db id of a selected map
    
+ Response 200 (application/json)
            
        {
            "metadata" : {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0
                },
                "status" : [],
                "datafiles": []
            },
            "result": {
                "mapDbId": "abc123",
                "name": "Some map",
                "type": "Genetic",
                "unit": "cM",
                "linkageGroups": [    
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

