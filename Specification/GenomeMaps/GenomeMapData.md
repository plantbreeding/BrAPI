## Genome Map Data [/brapi/v1/maps/{mapDbId}/positions?linkageGroupId={linkageGroupId}&linkageGroupId={linkageGroupId}&pageSize={pageSize}&page={page}]

Status: ACCEPTED.

Implemented by: Germinate

Used by: Flapjack

### Get map data [GET]

markers ordered by linkageGroup and position

+ Parameters
   + mapDbId (required, string, `6`) ... unique id of the map
   + linkageGroupId (optional, string, `123`) ... the linkage group id

+ Response 200 (application/json)

        {
            "metadata" : { 
                "pagination" : { "pageSize": 30, "currentPage": 2, "totalCount": 40, "totalPages":2 },
                "status": {},
                "datafiles": []
            },
            "result": { 
                "data" : [
                    {
                        "markerDbId": 1,
                        "markerName": "marker1",
                        "location": "1000",
                        "linkageGroup": "1A"
                    }, {
                        "markerDbId": 2,
                        "markerName": "marker2",
                        "location": "1001",
                        "linkageGroup": "1A"
                    }
                ]
            }
        }
