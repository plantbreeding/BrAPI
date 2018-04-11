### Scores through POST [POST /brapi/v1/allelematrix-search]


**This call may support asynchronous processing. See the "Asynchronous Processing" section for more information**

Use POST when parameter size is greater than 2K bytes.

- If no format is specified, this call returns the data in JSON form.
- If a format (other than JSON) is specified and the server supports this format, it will return the link to the exported data file in the "datafiles" field of the "metadata".
- If more than one format is requested at a time, the server will throw a "501 Not Implemented" error.

The format of the tsv response can be found on GitHub (https://github.com/plantbreeding/Documentation/wiki/BrAPI-TSV-Expected-Formats)

+ Request (application/json)
    
        {    
            "markerprofileDbId": ["993","994","995], // (required) The markerprofile db ids. Not Required if 'markerDbId' or 'matrixDbId' is present.
            "markerDbId": ["322","323","324"], // (required) ids of the markers. if none are specified, results are returned for all markers in the database. Not Required if 'markerprofileDbId' or 'matrixDbId' is present.
            "matrixDbId": ["457","458","459"], // (required) ids of the complete matrix. Not Required if 'markerprofileDbId' or 'markerDbId' is present.
            "expandHomozygotes" : true,  //(optional) Should homozygotes NOT be collapsed into a single orrucance?
            "unknownString" : "-", //(optional) The string to use as a representation for missing data.
            "sepPhased" : "|",  //(optional) The string to use as a separator for phased allele calls.
            "sepUnphased" : "/", // (optional)The string to use as a separator for unphased allele calls.
            "format" : "tsv", // (optional) If specified, this indicates that the server should return the data in the specified data format. The link to the data file is then returned in the "datafiles" field of the "metadata". Initially only "tsv" is supported which returns the data in a tab-delimited format. MarkerprofileDbIds along the top, markerDbIds along the side and allele calls in the center. 
            "pageSize" : 100, // (optional)the number of allele calls reported per response page.
            "page" : 1 // (optional) the requested response page
        }

+ Response 200 (application/json)

        {
            "metadata": {   
                "pagination": {
                    "pageSize": 100,
                    "currentPage": 1,
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

+ Response 200 (application/json)

        {
            "metadata": {  
                "pagination": {
                    "pageSize": 0,
                    "currentPage": 0,
                    "totalCount": 0,
                    "totalPages": 0
                },
                "status": [],
                "datafiles": [ "https://my-fancy-server/files/allelematrix-1234.tsv" ]
            },
            "result" : {
                "data" : []
            }
        }
