## Germplasm Markerprofiles  [/brapi/v1/germplasm/{id}/markerprofiles]
Retrieve the markerProfileDbIds for a given Germplasm ID  
Scope: GENOTYPING. 
Status: ACCEPTED.
Implementation target date: PAG2016
Implemented by: Germinate, Cassavabase

### Markerprofiles by germplasmDbId [GET]
+ Response 200 (application/json)
        
        {
            "metadata" : {
                "pagination" : null,
                "status" : {
                    "message": "",
                    "exception" :  { } 
                },
                "datafiles": []
            },
            "result" :  {
                germplasmDbId : 39393,
                markerProfiles : [
                    3939, 4484, 3993
                ]
            } 
        }

