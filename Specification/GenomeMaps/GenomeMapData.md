## Genome Map Data [/brapi/v1/maps/{mapDbId}/positions?linkageGroupId={linkageGroupId}&linkageGroupId={linkageGroupId}&pageSize={pageSize}&page={page}]

Status: ACCEPTED.

Implemented by: Germinate, Cassavabase

Used by: Flapjack

### Get map data [GET]

markers ordered by linkageGroup and position

+ Parameters
   + mapDbId (required, string, `6`) ... unique id of the map
   + linkageGroupId (optional, string, `123`) ... the linkage group id
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `10`) ... Which result page is requested

+ Response 200 (application/json)

        {
            "metadata" : { 
                "pagination" : { 
                    "pageSize": 1000, 
                    "currentPage": 0, 
                    "totalCount": 2, 
                    "totalPages": 1 
                },
                "status": [],
                "datafiles": []
            },
            "result": { 
                "data" : [
                    {
                        "markerDbId": "1",
                        "markerName": "marker1",
                        "location": "1000",
                        "linkageGroup": "1A"
                    }, {
                        "markerDbId": "2",
                        "markerName": "marker2",
                        "location": "1001",
                        "linkageGroup": "1A"
                    }
                ]
            }
        }
