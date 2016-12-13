## Germplasm Pedigree [/brapi/v1/germplasm/{id}/pedigree?notation=purdy]
Scope: CORE. Status: ACCEPTED.  
Implementation target date: PAG2016
Implemented by: Germinate, Tripal Brapi Module, Cassavabase (without notation option)

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|germplasmDbId|string|Internal db identifier|Y|
|defaultDisplayName|string|A string representing the germplasm that will be meaningful to the user|Y|
|pedigree|string|Cross name with optional selection history.|Y|
|parent1Id|string|germplasmDbId of parent1||
|parent2Id|string|germplasmDbId of parent2||

(http://wheat.pw.usda.gov/ggpages/gopher/administration/Template%20for%20Germplasm%20records.html) or [Lamacraft] (http://link.springer.com/article/10.1007%2FBF00021556).  
### Germplasm pedigree by id [GET]
+ Parameters
    + id (required, number, `382`) ... the internal id of the germplasm
    + notation (optional, string, `purdy`) ... text representation of the pedigree
+ Response 200 (application/json)
    
        { 
            "metadata" : {
                "pagination": null,
                "status": null,
                "datafiles": []
            }
            "result" : {
                "germplasmDbId": 382,
                "pedigree" : "Cree / Bonanza",
                "parent1Id" : 166,
                "parent2Id" : 143
            }
        }

+ Response 400 (application/json)

    
        { 
            "metadata" : {
                "pagination" : null,
                "status" : {
                    "message": "",
                    "exception" :  { } 
                },
                "datafiles": []
            },
            "result": {}
        }
