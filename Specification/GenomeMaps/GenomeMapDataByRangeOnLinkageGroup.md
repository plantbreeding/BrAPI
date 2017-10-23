## Genome Map Data by range on linkageGroup [/brapi/v1/maps/{mapDbId}/positions/{linkageGroupId}?min={min}&max={max}&pageSize={pageSize}&page={page}]

### Get map data by range on linkageGroup [GET]

markers ordered by linkageGroup and position

+ Parameters
   + mapDbId (required, string, `6`) ... unique id of the map
   + linkageGroupId (required, string)
   + min (optional) ... minimum position on linkage group
   + max (optional) ... maximumn position on linkage group
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
                "status" : [],
                "datafiles": []
            }    
            "result": { 
                "data" : [
                    {
                        "markerDbId": "1",
                        "markerName": "marker1",
                        "location": "1000"
                    }, {
                        "markerDbId": "2",
                        "markerName": "marker2",
                        "location": "1001"
                    }
                ]
            }
        }

       
