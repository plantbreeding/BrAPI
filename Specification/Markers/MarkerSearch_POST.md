      
### Markers Search (POST) [POST /brapi/v1/markers-search]
+ Request
  + Body
  
            {
                "markerDbIds": ["1185", "1186"], 
                    // The database IDs of the markers to search for
                "name": "11_1*", 
                    // The search pattern for a marker name or synonym.
                "matchMethod": "wildcard", 
                    // Possible values are 'case_insensitive', 'exact' (case sensitive), 'wildcard' (case insensitive). Wildcard uses both '*' and '%' for any number of characters and '?' for one character matching. Default is exact.
                "includeSynonyms": true, 
                    // Whether to include synonyms in the output.
                "type": "SNP", 
                    // The type of the marker.    
                "pageSize": 1000,
                    // The size of the pages to be returned. Default is `1000`.
                "page": 0
                    // Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
            }

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
