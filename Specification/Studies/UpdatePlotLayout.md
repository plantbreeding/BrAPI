## Update Plot Layout [/brapi/v2/studies/{id}/layout]

Call to update a study layout (X & Y coordinates).

Scope: PHENOTYPING

### Update plot layout coordinates [PUT]
+ Parameters
    + id the studyDbId with the layout to be updated (mandatory, integer, `1234`) 
+ Request body. Observation units to update:
    + {[  
        {  
            "observationUnitDbId": 122,  
            "X": 10,  
            "Y": 23  
        },  
        {  
            "observationUnitDbId": 123,  
            "X": 10,  
            "Y": 22  
        }  
        ]}  

+ Response 200 (application/json). Coordinates of the modified observation units.

    + {  
        "metadata":{  
            "pagination":{  
            "pageSize":0,  
            "currentPage":0,  
            "totalCount":0,  
            "totalPages":0  
        },  
        "status":[],  
        "datafiles":[]  
        },  
        "result":{    
            "data":[    
                {    
                "observationUnitDbId":122,  
                "X":10,  
                "Y":23  
                },  
                {  
                "observationUnitDbId":123,  
                "X":10,  
                "Y":22  
                }  
            ]  
        }  
    }  
