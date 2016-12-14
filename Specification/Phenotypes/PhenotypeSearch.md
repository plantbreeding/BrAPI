## Phenotype Search [/brapi/v1/phenotypes-search]
Scope: PHENOTYPING.
Status: ACCEPTED.
Implementation target: 2016. Implemented for GnpIS data (https://urgi.versailles.inra.fr/ws/webresources/brapi/v1/phenotypes). 
Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.
Refactor note : This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below.
Example Use cases:
- Study a panel of germplasm accross multiple studies, search parameters : {"germplasmDbIds" : [ "Blabla", "34Mtp362" ]}
- Get all data for a specific study : {"studyDbIds" : [ 383 ]}
- Get simple atomic phenotyping values : {"germplasmDbIds" : [ "Blabla", "34Mtp362" ], "observationVariableDbIds" : [ 37373]}
- Study Locations for adaptation to climat change : {"locationDbIds" : [ 383838, "MONTPELLIER" ], "germplasmDbIds" : [ "all ids for a given species"]}

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|observationUnitDbId|String|internal DB id, can be a primary key, a URI or any other ID ||
|studyDbId|String|internal DB id , can be a primary key, a URI or any other ID||
|studyName | string |||
|studyLocationDbId| internal DB id , can be a primary key, a URI or any other ID ||
|studyLocation|string| Location name |Y|
|programName|string|||
|germplasmDbId|Long|internal DB id , can be a primary key, a URI or any other ID||
|germplasmName|string| Display name for the germplasm. MCPD Name field||
|X,Y|string|Relative position in the study. Can be row/colmun number, line/rootstock, meters, etc...||
|XLabel,YLabel|string|Example: X=row, Y = rootstock||
|treatments|array of objects|list of all the factors applied to the observation unit : fertilizer, inoculation, irrigation, etc...||
|treatments.factor|string|the type of treatment/factor. EG: fertilizer, inoculation, irrigation, etc...||
|treatments.factor|string|the treatment/factor descritpion. EG: low fertilizer, yellow rust inoculation, high water, etc...||
|observations|array of objects|At least one observation. See below for details on the content.|Y|
|observations.observationVariableDbId|string| ID or PUI (DOI, URI, LSID)||
|observations.observationVariableName | string | Display name||
|observations.season|string| Year or season, Phenotyping campain, can be a period accross multiple years or a list of some years ||
|observations.value|string|||
|observations.observationTimeStamp|string|ISO format "2006-07-03::10:00"||
|observations.collector|string| Person or team who has made the observaiton||
|observations.additionalInfo|array of key/value pair|||

### Phenotype Search [POST]

observationTimeStamp : Iso Standard
observationValue data type inferred from the ontology 

+ Request (application/json)

        {
            "germplasmDbIds" : [ "Blabla", "34Mtp362" ], // (optional, text, `986`) ... The name or synonym of external genebank accession identifiers
            "observationVariableDbIds" : [ 37373, "CO_321:00000234"], // (optional, text, `CO_321:00000234`) ... The IDs of traits, could be ontology ID, database ID or PUI
            "studyDbIds" : [ 383, 2929, "WHEAT_NETWK_2016_MONTPELLIER" ], // (optional, text, `2356`) ... The database ID / PK of the studies search parameter
            "locationDbIds" : [ 383838, "MONTPELLIER" ], // locations these traits were collected
            "programDbIds" : [ 3838, "Drought resistance CG 2020" ], // list of programs that have phenotyped this trait
            "seasonDbIds" : [ 338, "2010", "1956-2014", "2002-2003-2004", "2007 Spring" ], // (optional, text, `2001`) ... The year or Phenotyping campaign of a multiannual study (trees, grape, ...)
            "observationLevel" : "plot", // (optional, text, `plot`) ... The type of the observationUnit. Returns only the observaton unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
            "pageSize" : 100, // (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
            "page" : 1, // (optional, integer, `10`) ... Which result page is requested
        }
 
+ Response 200 (application/json)

        {
          "metadata": {
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
            "data": [
              {
                "observationUnitDbId": "abc-123",
                "observationLevel": "plot",
                "observationLevels": "bloc:2,rep:1,plot:abc-123",
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
                "XLabel": "row",
                "YLabel": "line",
                "treatments": [
                  {
                    "factor": "water regimen",
                    "modality": "water deficit"
                  }
                ],
                "observations": [
                  {
                    "observationDbId": "153453453",
                    "observationVariableDbId": "CO_321:0000045",
                    "observationVariableName": "Plant_height",
                    "observationTimeStamp": "2015-06-16T00:53:26Z",
                    "season": "2015",
                    "value": "45",
                    "collector": "Mr. Technician",
                    "entryType": "Test entry",
                    "quality": "reliability of the observation",
                    "collectionFacilityLabel": "phenodyne"
                  },
                  {
                    "observationDbId": "23453454345",
                    "observationVariableDbId": "CO_321:0000996",
                    "observationVariableName": "GW100_g",
                    "observationTimeStamp": "2015-06-16T00:53:26Z",
                    "season": "2015",
                    "collector": "Mr. Technician",
                    "value": "3",
                    "entryType": "Test entry",
                    "quality": "reliability of the observation",
                    "collectionFacilityLabel": "phenodyne"
                  }
                ]
              },
              {
                "observationUnitDbId": "45204",
                "observationLevel": "plot",
                "observationLevels": "",
                "observationUnitName": "2010-Cornell-37-99",
                "germplasmDbId": "doi:10.155499/12349537E00",
                "germplasmName": "ZE-45",
                "studyDbId": "YieldStudy2010-5",
                "studyName": "Yield wheat 2010",
                "studyLocationDbId": 88484,
                "studyLocation": "Cornell",
                "programName": "Wheat for futur",
                "X": "",
                "Y": "",
                "XLabel": "",
                "YLabel": "",
                "treatments": [],
                "observations": [
                  {
                    "observationDbId": "153453453",
                    "observationVariableDbId": "CO_321:0000045",
                    "observationVariableName": "Plant_height",
                    "observationTimeStamp": "2010-06-16T00:53:26Z",
                    "season": "2010",
                    "value": "45"
                  },
                  {
                    "observationDbId": "23453454345",
                    "observationVariableDbId": "CO_321:0000996",
                    "observationVariableName": "GW100_g",
                    "observationTimeStamp": "2010-06-16T00:53:26Z",
                    "season": "2010",
                    "collector": "Mr. Technician",
                    "value": "3",
                    "entryType": "Test entry",
                    "quality": "reliability of the observation",
                    "collectionFacilityLabel": "phenodyne"
                  }
                ]
              }
            ]
          }
        }