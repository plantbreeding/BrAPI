## Genome Map Details [/brapi/v1/maps/{mapDbId}]

Status: ACCEPTED

Implemented by: Germinate

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
                }
                "status" : {},
                "datafiles": []
            },
            "result": {
                "mapDbId": "id",
                "name": "Some map",
                "type": "Genetic",
                "unit": "cM",
                "linkageGroups": [    
                    {
                        "linkageGroupId": 1,
                        "numberMarkers": 100000,
                        "maxPosition": 10000000
                    },
                    {
                        "linkageGroupId": 2,
                        "numberMarkers": 1247,
                        "maxPostion": 12347889
                    }
                ]
            }
        }
