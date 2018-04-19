
### Phenotype Search (POST) [POST /brapi/v1/phenotypes-search]

+ Request (application/json)

        {
            "germplasmDbIds" : [ "Blabla", "34Mtp362" ], // (optional) The name or synonym of external genebank accession identifiers
            "observationVariableDbIds" : [ "37373", "CO_321:00000234"], // (optional) The IDs of traits, could be ontology ID, database ID or PUI
            "studyDbIds" : [ "383", "2929", "WHEAT_NETWK_2016_MONTPELLIER" ], // (optional) The database ID / PK of the studies search parameter
            "locationDbIds" : [ "383838", "MONTPELLIER" ], // (optional) locations these traits were collected
            "trialDbIds" : [ "3838", "Drought_resistance_CG_2020" ], // (optional) list of trials to search across
            "programDbIds" : [ "3838", "Drought_resistance_CG_2020" ], // (optional) list of programs that have phenotyped this trait
            "seasonDbIds" : [ "338", "2010", "1956-2014", "2002-2003-2004", "2007 Spring" ], // (optional) The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
            "observationLevel" : "plot", // (optional) The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
            "observationTimeStampRangeStart" : "2015-06-16T00:53:26-0800" // (optional) Timestamp range start
            "observationTimeStampRangeEnd" : "2015-06-18T00:53:26-0800" // (optional) Timestamp range end
            "pageSize" : 100, // (optional) The size of the pages to be returned. Default is `1000`.
            "page" : 1, // (optional) Which result page is requested
        }
 
+ Response 200 (application/json)

        {
          "metadata": {
            "pagination": {
              "pageSize": 100,
              "currentPage": 1,
              "totalCount": 102,
              "totalPages": 2
            },
            "status": [],
            "datafiles": []
          },
          "result": {
            "data": [
              {
                "observationUnitDbId": "2016-Maugio-34-575-abc-123",
                "observationLevel": "plot",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "plantNumber" : null,
                "blockNumber" : "2",
                "replicate": null,
                "observationUnitName": "2016-Maugio-34-575",
                "germplasmDbId": "doi:10.155454/12349537E12",
                "germplasmName": "IR-8",
                "studyDbId": "YieldStudy2015-5",
                "studyName": "Yield wheat 2015",
                "studyLocationDbId": "mtp-north-32",
                "studyLocation": "Montpellier",
                "programName": "Whealbi",
                "X": "5",
                "Y": "15",
                "entryType": null,
                "entryNumber": null,
                "treatments": [
                  {
                    "factor": "water regimen",
                    "modality": "water deficit"
                  }
                ],
                "observationUnitXref":[
                    {"source": "biosampleEBI", "id": "SAMEA179865230"},
                    {"source": "gnpis.lot", "id": "INRA:CoeSt6 _SMH03"}, 
                    {"source": "kernelDB", "id": "239865"}
                ],
                "observations": [
                  {
                    "observationDbId": "153453453",
                    "observationVariableDbId": "CO_321:0000045",
                    "observationVariableName": "Plant_height",
                    "observationTimeStamp": "2015-06-16T00:53:26-0800",
                    "season": "2015",
                    "collector": "Mr. Technician",
                    "value": "45"
                  },
                  {
                    "observationDbId": "23453454345",
                    "observationVariableDbId": "CO_321:0000996",
                    "observationVariableName": "GW100_g",
                    "observationTimeStamp": "2015-06-16T00:53:26-0800",
                    "season": "2015",
                    "collector": "Mr. Technician",
                    "value": "3"
                  }
                ]
              },
              {
                "observationUnitDbId": "45204",
                "observationLevel": "plant",
                "observationLevels": null,
                "plotNumber": null,
                "plantNumber" : "45204",
                "blockNumber" : null,
                "replicate": "2",
                "observationUnitName": "2010-Cornell-37-99",
                "germplasmDbId": "doi:10.155499/12349537E00",
                "germplasmName": "ZE-45",
                "studyDbId": "YieldStudy2010-5",
                "studyName": "Yield wheat 2010",
                "studyLocationDbId": "88484",
                "studyLocation": "Cornell",
                "programName": "Wheat for futur",
                "X": null,
                "Y": null,
                "entryType": null,
                "entryNumber": null,
                "treatments": [],
                "observations": [
                  {
                    "observationDbId": "153453453",
                    "observationVariableDbId": "CO_321:0000045",
                    "observationVariableName": "Plant_height",
                    "observationTimeStamp": "2010-06-16T00:53:26-0800",
                    "season": "2010",
                    "collector": "Mr. Technician",
                    "value": "45"
                  },
                  {
                    "observationDbId": "23453454345",
                    "observationVariableDbId": "CO_321:0000996",
                    "observationVariableName": "GW100_g",
                    "observationTimeStamp": "2010-06-16T00:53:26-0800",
                    "season": "2010",
                    "collector": "Mr. Technician",
                    "value": "3"
                  }
                ]
              }
            ]
          }
        }
