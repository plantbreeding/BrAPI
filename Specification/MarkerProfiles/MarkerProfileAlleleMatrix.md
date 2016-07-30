## MarkerProfile Allele Matrix [/brapi/v1/allelematrix-search?unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=&markerprofileDbId=100&markerprofileDbId=101&markerDbId=322&markerDbId=418&format=&pageSize=&page=]
Status: ACCEPTED.

Implemented by: Germinate (POST only)

Used by: Flapjack (POST only)

This uses a more efficient data structure and pagination for large number of markers.

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|markerprofileDbIds| list of strings | | Y |
|data| array | Is an array of arrays; each inner array has three entries: "markerDbId", "markerProfileDbId", "alleleCall". Scores have to be represented as described further up. e.g. unknown data as "N", etc. Missing data can be skipped. | Y |

### Scores through GET [GET]

Use GET when parameter size is less than 2K bytes.

+ Parameters
    + markerprofileDbId (required, string, `993`) ... The markerprofile db ids; for multiple, repeat the parameter.
    + markerDbId (optional, string, `322`) ... ids of the markers; if none are specified, results are returned for all markers in the database.
    + expandHomozygotes (optional, boolean, `false`) ... Should homozygotes NOT be collapsed into a single orrucance?
    + unknownString (optional, string, `-`) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (optional, string, `|`) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (optional, string, `/`) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".
    + pageSize (optional, integer, `1000`) ... the number of allele calls reported per response page.
    + page (optional, integer, `10`) ... the requested response page

+ Response 200 (application/json)

        {
            "metadata": {   
                "pagination": {
                    "pageSize": 100,
                    "currentPage": 1,
                    "totalCount": 1,
                    "totalPages": 1
                },
                "status":{},
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
