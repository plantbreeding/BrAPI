## Germplasm Markerprofiles  [/brapi/v1/germplasm/{germplasmDbId}/markerprofiles]
Retrieve the markerProfileDbIds for a given Germplasm ID  
Scope: GENOTYPING. 
Status: ACCEPTED.
Implementation target date: PAG2016
Implemented by: Germinate, Cassavabase

### Markerprofiles by germplasmDbId [GET /brapi/v1/germplasm/{germplasmDbId}/markerprofiles]
+ Parameters
   + germplasmDbId (required, string, `382`) ... the internal id of the germplasm
+ Response 200 (application/json)
        
        {
            "metadata" : {
                "pagination" : {
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [ {
                    "message": "",
                    "code" : "" 
                } ],
                "datafiles": []
            },
            "result" :  {
                "germplasmDbId" : "39393",
                "markerprofileDbIds" : [
                    "3939", "4484", "3993"
                ]
            } 
        }

