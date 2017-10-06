## Genome Map Details [/brapi/v1/maps/{mapDbId}]

Status: ACCEPTED

Implemented by: Germinate, Cassavabase

Used by: Flapjack

### Get map details [GET]

Provides the number of markers on each linkageGroup and the max position on the linkageGroup

+ Paramters
    + mapId (required)
    + Should we provide pagination?
    
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
                "mapDbId": "id",
                "name": "Some map",
                "type": "Genetic",
                "unit": "cM",
                "linkageGroups": [    
                    {
                        "linkageGroupDbId": "1",
                        "markerCount": 100000,
                        "maxPosition": 10000000
                    },
                    {
                        "linkageGroupDbId": "2",
                        "markerCount": 1247,
                        "maxPosition": 12347889
                    }
                ]
            }
        }

