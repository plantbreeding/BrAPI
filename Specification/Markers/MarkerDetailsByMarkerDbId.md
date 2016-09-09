## Marker Details by markerDbId [/brapi/v1/markers/{markerDbId}]

Status: ACCEPTED
Implemented By: 

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|object|data|Y|
|data|array of objects|Array (possibly empty) of marker records|Y|
|type|string|The type of marker, e.g. SNP|Y|
|markerDbId|string|Internal db identifier|Y|
|defaultDisplayName|string|A string representing the marker that will be meaningful to the user|Y|
|synonyms|array of string|List of other names for this marker||
|refAlt|array of string|List of the reference (as the first item) and alternatives (the remaining items)||
|analysisMethods|array of string|List of the genotyping platforms used to interrogate the marker||

### Marker Details by id [GET]
+ Parameters
    + markerDbId (required, string, `1185`) ... the internal id of the marker
    
+ Response 200 (application/json)

        {
            "metadata": {
                "status": null,
                "datafiles": [],
                "pagination": {}
            },
            "result": {
                "markerDbId": "1185",
                "defaultDisplayName": "11_10002",
                "type": "SNP",
                "synonyms": ["i_11_10002", "POPA1_0002"],
                "refAlt": ["A", "T"],
                "analysisMethods": ["illumina", "kasp"]
            }
        }
