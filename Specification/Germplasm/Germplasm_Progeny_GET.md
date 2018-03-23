## Germplasm Progeny [/brapi/v1/germplasm/{germplasmDbId}/progeny]
Scope: Germplasm

Get the germplasmDbIds for all the Progeny of a particular germplasm.

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|germplasmDbId|string|Internal db identifier|Y|
|defaultDisplayName|string|A string representing the germplasm that will be meaningful to the user|Y|
|progeny|array|List of progeny of this germplasm|Y|
|progeny.germplasmDbId|string|Internal db identifier for a progeny germplasm|Y|
|progeny.defaultDisplayName|string|A string representing the progeny germplasm that will be meaningful to the user|Y|
|progeny.parentType|string|The type of parent this germplasm is to a given progeny (MALE, FEMALE, SELF)|Y|



### Germplasm Progeny by id [GET /brapi/v1/germplasm/{germplasmDbId}/progeny]
+ Parameters
   + germplasmDbId (required, string, `382`) ... the internal id of the germplasm
+ Response 200 (application/json)
    
        { 
            "metadata" : {
                "pagination": {
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "germplasmDbId": "382",
                "defaultDisplayName": "Pahang",
                "progeny" : [
                    {
                        "germplasmDbId": "402",
                        "defaultDisplayName": "Child 1",
                        "parentType": "FEMALE"
                    }, {
                        "germplasmDbId": "403",
                        "defaultDisplayName": "Child 2",
                        "parentType": "MALE"
                    }, { 
                        "germplasmDbId": "405",
                        "defaultDisplayName": "Pahang Selfed",
                        "parentType": "SELF"
                    }
                ]
            }
        }

