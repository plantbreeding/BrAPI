## Markerprofile data [/brapi/v1/markerprofiles/{markerprofileDbId}?unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=&pageSize=&page= ]
Scope: GENOTYPING.
Status: ACCEPTED.
Implemented by: Germinate, Cassavabase

For the requested markerprofile ID, returns the allele call for each marker. 
[Example] (http://malt.pw.usda.gov/t3/wheatplus/brapi/v1/markerprofiles/1784_99/count?analysisMethod=GoldenGate)
   
**Allele encodings**

- Unknown data will by default be encoded by "N"
- Homozygotes are returned as a single occurance, e.g. AA -> A, GG -> G
- Phased heterozygotes are by default separated by a pipe ("|") and unphased heterozygotes are by default separated by a forward slash ("/")
- Dominant markers such as DArTs: 1 for present, 0 for absent

**Parameters**

- If the user would like to use an empty string ("") for any of the parameters, the value should be set to the reserved word "empty_string", e.g. sepUnphased=empty_string.

**Open issue:**
The pages of data will need to be sorted sensibly in order for the
requested page to be delivered consistently.  By map or genome position?
Alphabetically?
###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|markerprofileDbId|string|Unique in the database. Can be a catenation of unique IDs for germplasm and extract.|Y|
|germplasmDbId|string||Y|
|extractDbId|string||Y|
|analysisMethod|string|||
|data|object|array of marker-name/score pairs|Y|
|metadata|object|pagination, status, datafiles|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list||Y|

### Alleles By Markerprofile Id [GET]

+ Parameters
    + markerprofileDbId (required, number, `993`) ... The server's internal id for the markerprofile
    + expandHomozygotes (optional, boolean, `false`) ... Should homozygotes NOT be collapsed into a single orrucance?
    + unknownString (optional, string, `-`) ... The string to use as a representation for missing data or the reserved word "empty_string".
    + sepPhased (optional, string, `|`) ... The string to use as a separator for phased allele calls or the reserved word "empty_string".
    + sepUnphased (optional, string, `/`) ... The string to use as a separator for unphased allele calls or the reserved word "empty_string".
    + pageSize (optional, number, `10000`) ... The number of allele call results (marker/allele pairs) to be returned in the response. If multiple experiments are requested, some responses will contain the last results from one experiment followed by the first results from the next.
    + page (optional, number, `1`) ... Required if `pageSize` is given; and requires that `pageSize` be given. The first page is 1, not 0.

+ Response 200 (application/json)

        {
            "metadata" : {
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 0,
                    "totalCount": 10,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
        
            "result": {
                "germplasmDbId": "993",
                "uniqueDisplayName": "MyNameHere",
                "extractDbId" : "38383", 
                "markerprofileDbId": "37484",
                "analysisMethod": "GBS-Pst1",
                "data" : [ { "marker1": "A" }, { "marker2":"A/B" }, ... ]
           }
        }


