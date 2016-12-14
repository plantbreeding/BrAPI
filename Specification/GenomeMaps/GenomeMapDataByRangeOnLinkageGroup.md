## Genome Map Data by range on linkageGroup [/brapi/v1/maps/{mapDbId}/positions/{linkageGroupId}?min={min}&max={max}&pageSize={pageSize}&page={page}]

### Get map data by range on linkageGroup [GET]

markers ordered by linkageGroup and position

+ Parameters
   + mapDbId (required, string, `6`) ... unique id of the map
   + linkageGroupId (required, string)
   + min (optional) ... minimum position on linkage group
   + max (optional) ... maximumn position on linkage group

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination" : { 
	            "pageSize": 30, 
                    "currentPage": 2, 
                    "totalCount": 40, 
                    "totalPages":2 
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

       
