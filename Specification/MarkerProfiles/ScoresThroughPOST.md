### Scores through POST [POST]

Use POST when parameter size is greater than 2K bytes.

- If no format is specified, this call returns the data in JSON form.
- If a format (other than JSON) is specified and the server supports this format, it will return the link to the exported data file in the "datafiles" field of the "metadata".
- If more than one format is requested at a time, the server will throw a "501 Not Implemented" error.

The format of the tsv response can be found on GitHub (https://github.com/plantbreeding/Documentation/wiki/BrAPI-TSV-Expected-Formats)

+ Request (application/json)
    
        {
            "markerprofileDbId" : 9393, // (required, string, `993`) ... The markerprofile db ids; for multiple, repeat the parameter.
            "markerDbId" : 38383, (optional, string, `322`) ... ids of the markers; if none are specified, results are returned for all markers in the database.
            "expandHomozygotes" : true,  //(optional, boolean, `false`) ... Should homozygotes NOT be collapsed into a single orrucance?
            "unknownString" : "-", //(optional, string, `-`) ... The string to use as a representation for missing data.
            "sepPhased" : "|",  //(optional, string, `|`) ... The string to use as a separator for phased allele calls.
            "sepUnphased" : "/", // (optional, string, `/`) ... The string to use as a separator for unphased allele calls.
            "format" : "tsv", // (optional, string, `tsv`) ... If specified, this indicates that the server should return the data in the specified data format. The link to the data file is then returned in the "datafiles" field of the "metadata". Initially only "tsv" is supported which returns the data in a tab-delimited format. MarkerprofileDbIds along the top, markerDbIds along the side and allele calls in the center. 
            "pageSize" : 100, // (optional, integer, `1000`) ... the number of allele calls reported per response page.
            "page" : 1 // (optional, integer, `10`) ... the requested response page
        }

+ Response 200 (application/json)

        {
            "metadata": {   
                "status": null,
                "datafiles": [],
                "pagination": {
                    "pageSize": 100,
                    "currentPage": 1,
                    "totalCount": 1,
                    "totalPages": 1
                }
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

+ Response 200 (application/json)

        {
            "metadata": {  
                "pagination": {
                    "pageSize": 1,
                    "currentPage": 0,
                    "totalCount": 1,
                    "totalPages": 1
                },
                "status": {},
                "datafiles": [
                    { "url": "https://my-fancy-server/files/allelematrix-1234.tsv" }
                ]
            },
            "result" : {
                "data" : []
            }
        }
