## Germplasm Pedigree [/brapi/v1/germplasm/{germplasmDbId}/pedigree]
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
|pedigree|string|The human readable pedigree string. Cross name with optional selection history.|Y|
|crossingPlan|string|The type of cross that was made||
|crossingYear|string|The year this cross was made||
|familyCode|string|||
|**Deprecated** parent1Id|string|**Use parent1DbId**||
|**Deprecated** parent2Id|string|**Use parent2DbId**||
|parent1DbId|string|germplasmDbId of Parent1||
|parent1Name|string|The human readable name of Parent1||
|parent1Type|string|The type of parent for Parent1 (MALE, FEMALE, SELF)||
|parent2DbId|string|germplasmDbId of Parent2||
|parent2Name|string|The human readable name of Parent2||
|parent2Type|string|The type of parent for Parent2 (MALE, FEMALE, SELF)||
|siblings|array|List of siblings with the same pedigree||
|siblings.germplasmDbId|string|germplasmDbId of a sibling germplasm||
|siblings.defaultDisplayName|string|A string representing a sibling germplasm that will be meaningful to the user||

(http://wheat.pw.usda.gov/ggpages/gopher/administration/Template%20for%20Germplasm%20records.html) or [Lamacraft] (http://link.springer.com/article/10.1007%2FBF00021556).  

### Germplasm pedigree by id [GET /brapi/v1/germplasm/{germplasmDbId}/pedigree{?notation}{?includeSiblings}]
+ Parameters
   + germplasmDbId (required, string, `382`) ... the internal id of the germplasm
   + notation (optional, string, `purdy`) ... text representation of the pedigree
   + includeSiblings (optional, boolean, `true`) ... include a siblings array or not
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
                "pedigree" : "Cree / Bonanza",
                "crossingPlan": "string",
                "crossingYear": "2018",
                "familyCode" : "string",
                "parent1DbId" : "166",
                "parent1Name" : "Cree",
                "parent1Type" : "FEMALE",
                "parent2DbId" : "143",
                "parent2Name" : "Bonanza",
                "parent2Type" : "MALE",
                "siblings": [
                    {
                        "germplasmDbId": "string",
                        "defaultDisplayName": "string"
                    }
                ]
            }
        }

