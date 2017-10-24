## Markers Search [/brapi/v1/markers?name={name}&type={type}&matchMethod={matchMethod}&include={synonyms}&pageSize={pageSize}&page={page}]
Scope: CORE.  Status: ACCEPTED.

Implemented by: Germinate

Other service requests use the server's internal `markerDbId`. This service returns marker records that provide the markerDbId.
For the requested name or synonym, returns an array (possibly empty) of marker records that match the search criteria.
- If there is none, an empty array is returned.
- If there is one or more than one match, returns an array of all marker records that match the search criteria.

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

### Search names to retrieve marker records [GET]
+ Parameters
    + name (optional, string, `11_10002 11_1% 11_1* 11_10?02`) ... The name or synonym.
    + matchMethod (optional, string, `wildcard`) ... Possible values are 'case_insensitive', 'exact'
    (case sensitive), 'wildcard' (which is case insensitive). Wildcard uses both '*' and '%' for any number of characters
    and '?' for one character matching. Default is exact.
    + include (optional, string, `synonyms`) ... Whether to include synonyms in the output.
    + type (optional, string, `SNP`) ... The type of the marker.    
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "data": [
                    {
                        "markerDbId": "1185",
                        "defaultDisplayName": "11_10002",
                        "type": "SNP",
                        "synonyms": ["i_11_10002", "POPA1_0002"],
                        "refAlt": ["A", "T"],
                        "analysisMethods": ["illumina", "kasp"]
                    },
                    {
                        "markerDbId": "1186",
                        "defaultDisplayName": "11_11159",
                        "type": "SNP",
                        "synonyms": ["i_11_11159", "POPA1_1159"],
                        "refAlt": ["A", "T"],
                        "analysisMethods": ["illumina", "kasp"]
                    }
                ]
            }
        }
