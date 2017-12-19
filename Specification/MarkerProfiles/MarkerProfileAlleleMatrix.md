## MarkerProfile Allele Matrix [/brapi/v1/allelematrix-search]
Status: ACCEPTED.

Implemented by: Germinate (POST only), Cassavabase

Used by: Flapjack (POST only)

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

This uses a more efficient data structure and pagination for large number of markers.

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|markerprofileDbIds| list of strings | | Y |
|data| array | Is an array of arrays; each inner array has three entries: "markerDbId", "markerprofileDbId", "alleleCall". Scores have to be represented as described further up. e.g. unknown data as "N", etc. Missing data can be skipped. | Y |

### Scores through GET [GET /brapi/v1/allelematrix-search{?markerprofileDbId}{?markerDbId}{?matrixDbId}{?format}{?expandHomozygotes}{?unknownString}{?sepPhased}{?sepUnphased}{?pageSize}{?page}]

Use GET when parameter size is less than 2K bytes.
This method may support asynchronous processing.

+ Parameters
    + markerprofileDbId (required, array, `993,994,995`) ... The markerprofile db ids. Not Required if 'markerDbId' or 'matrixDbId' is present.
    + markerDbId (required, array, `322,323,324`) ... ids of the markers. if none are specified, results are returned for all markers in the database. Not Required if 'markerprofileDbId' or 'matrixDbId' is present.
    + matrixDbId (required, array, `457,458,459`) . . . ids of the complete matrix. Not Required if 'markerprofileDbId' or 'markerDbId' is present.
    + format (optional, string, `tsv`) ... format for the datafile to be downloaded. tsv and csv currently supported; flapjack may be supported.
    + expandHomozygotes (optional, boolean, `false`) ... Should homozygotes NOT be collapsed into a single occurrence?
    + unknownString (optional, string, `-`) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (optional, string, `|`) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (optional, string, `/`) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".    
    + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
    + page (optional, integer, `0`) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.

+ Response 200 (application/json)

        {
            "metadata": {   
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 1,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : { 
                "data": [
                    ["1", "1", "A/B"],
                    ["1", "2", "B"],
                    ["2", "1", "A"],
                    ["2", "2", "A/B"]
                ]
            }
        }
