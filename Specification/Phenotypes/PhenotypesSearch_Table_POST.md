
### Phenotypes Search (Table) [POST /brapi/v1/phenotypes-search/table]

+ Request (application/json)

        {
            "germplasmDbIds" : [ "Blabla", "34Mtp362" ], // (optional) The name or synonym of external genebank accession identifiers
            "observationVariableDbIds" : [ "37373", "CO_321:00000234"], // (optional) The IDs of traits, could be ontology ID, database ID or PUI
            "studyDbIds" : [ "383", "2929", "WHEAT_NETWK_2016_MONTPELLIER" ], // (optional) The database ID / PK of the studies search parameter
            "locationDbIds" : [ "383838", "MONTPELLIER" ], // (optional) locations these traits were collected
            "trialDbIds" : [ "3838", "Drought_resistance_CG_2020" ], // (optional) list of trials to search across
            "programDbIds" : [ "3838", "Drought_resistance_CG_2020" ], // (optional) list of programs to search across
            "seasonDbIds" : [ "338", "2010", "1956-2014", "2002-2003-2004", "2007 Spring" ], // (optional) The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
            "observationLevel" : "plot", // (optional) The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnit Structure.
            "observationTimeStampRangeStart" : "2015-06-16T00:53:26-0800" // (optional) Timestamp range start
            "observationTimeStampRangeEnd" : "2015-06-18T00:53:26-0800" // (optional) Timestamp range end
            "pageSize" : 100, // (optional) The size of the pages to be returned. Default is `1000`.
            "page" : 0, // (optional) Which result page is requested
        }
 
+ Response 200 (application/json)

        {
            "metadata": {
                "pagination": {
                    "pageSize": 100,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                },
                "status": [],
                "datafiles": []
            },
            "result" : {
                "headerRow": [ "year","studyDbId","studyName","locationDbId","locationName","germplasmDbId","germplasmName","observationUnitDbId","plotNumber","replicate","blockNumber", "observationTimestamp", "entryType", "X", "Y"],
                "observationVariableDbIds": [ "variable1DbId", "variable2DbId", "variable3DbId"],  // for linking
                "observationVariableNames": [ "plant height", "fruit weight", "root weight" ],  // for display
                // the observationNames will follow the columns defined in the headerRow

                "data" :
                [
                    ["2017", "stu1", "Study Name", "loc1", "Location Name", "CIP1", "CIP Name", "abc123", 1, 1, 1, "2017-06-16T00:53:26Z", "Test Entry", "1", "2", "25.3", "103.4", "50.75"],
                    ["2017", "stu1", "Study Name", "loc1", "Location Name", "CIP1", "CIP Name", "abc124", 1, 1, 1, "2017-06-16T00:54:57Z", "Test Entry", "2", "2", "27.9", "98.65", "45.345"]
                ]
            }
        }
    