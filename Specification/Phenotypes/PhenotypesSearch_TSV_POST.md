
### Phenotypes Search (TSV) [POST /brapi/v1/phenotypes-search/tsv]

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
            "page" : 1, // (optional) Which result page is requested
        }
 
+ Response 200 (application/tsv)

        "year"    "studyDbId"    "studyName"    "locationDbId"    "locationName"    "germplasmDbId"    "germplasmName"    "observationUnitDbId"    "plotNumber"    "replicate"    "blockNumber"    "entryType"    "X"    "Y"     "variableDbId1"    "variableDbId2"    "variableDbId3"
        "2015"    "YieldStudy2015-5"    "Yield wheat 2015"    "mtp-north-32"    "Montpellier"    "doi:10.155454/12349537E12"    "IR-8"    "2016-Maugio-34-575-abc-123"    "120"    ""    "2"    ""    "5"    "15"    "45"    "3"    "10"
        "2016"    "YieldStudy2016-5"    "Yield wheat 2016"    "mtp-north-32"    "Montpellier"    "doi:10.155454/12349537E13"    "IR-8"    "2016-Maugio-34-575-abc-124"    "120"    ""    "2"    ""    "5"    "15"    "47"    "4"    "11"
    