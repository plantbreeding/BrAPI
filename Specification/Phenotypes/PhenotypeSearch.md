## Phenotype Search [/brapi/v1/phenotypes-search]
Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.


Implemented for GnpIS and PHIS data (https://urgi.versailles.inra.fr/ws/webresources/brapi/v1/phenotypes). 
Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.
Refactor note : This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below.
Example Use cases:
- Study a panel of germplasm accross multiple studies, search parameters : {"germplasmDbIds" : [ "Syrah", "34Mtp362" ]}
- Get all data for a specific study : {"studyDbIds" : [ "383" ]}
- Get simple atomic phenotyping values : {"germplasmDbIds" : [ "Syrah", "34Mtp362" ], "observationVariableDbIds" : [ "CO_345:0000043"]}
- Study Locations for adaptation to climat change : {"locationDbIds" : [ "383838", "MONTPELLIER" ], "germplasmDbIds" : [ "all ids for a given species"]}
- Find phenotypes that are from after a certain timestamp

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|observationUnitDbId|String|internal DB id, can be a primary key, a URI or any other ID, must be unique within the calls | Y |
|studyDbId|String|internal DB id , can be a primary key, a URI or any other ID| Y |
|studyName | string |||
|studyLocationDbId| string | internal DB id , can be a primary key, a URI or any other ID |Y|
|studyLocation|string| Location name ||
|observationLevel | string | level of this observation unit. Its ID is the observationUnitDbId||
|observationLevels|string| Concatenation of the levels of this observationUnit. Used to handle non canonical level structures. Format  levelType:levelID,levelType:levelID ||
|plotNumber|string| Plot level ID. Null if not relevant because the observation unit is a higher level ||
|plantNumber|string| Plant Level ID ||
|blockNumber|string| Block Level ID ||
|replicate|string| replicate level ID ||
|programName|string|||
|germplasmDbId|Long|internal DB id , can be a primary key, a URI or any other ID|Y|
|germplasmName|string| Display name for the germplasm. MCPD Name field||
|X,Y|string|Relative position in the study. Can be row/colmun number, line/rootstock, meters, etc...||
|treatments|array of objects|list of all the factors applied to the observation unit : fertilizer, inoculation, irrigation, etc...||
|treatments.factor|string|the type of treatment/factor. EG: fertilizer, inoculation, irrigation, etc...||
|treatments.modality|string|the treatment/factor descritpion. EG: low fertilizer, yellow rust inoculation, high water, etc...||
|observationUnitXref                    |array of objects|Xref, IDs of this observation Unit in this database or other database. Handle different IDs of your individuals/plant material/seed Lot| |
|observationUnitXref.source             |string| the source/name space of the ID, for known databases use : biosampleEBI, biosampleNCBI | Y |
|observationUnitXref.id                 |string| ID  | Y |
|observations|array of objects|At least one observation. See below for details on the content.|Y|
|observations.observationDbId|string| ID or PUI (DOI, URI, LSID)||
|observations.observationVariableDbId|string| ID or PUI (DOI, URI, LSID)|Y|
|observations.observationVariableName | string | Display name||
|observations.season|string| this can be considered as a label to group data within a multiyear study. It can be a year, season, Phenotyping campain, a period accross multiple years or a list of some years ||
|observations.value|string|||
|observations.observationTimeStamp|string|ISO format "2006-07-03T10:00:38-0800"||
|observations.collector|string| Person or team who has made the observation||

### Phenotype Search [POST]

observationTimeStamp : Iso Standard 8601.
observationValue data type inferred from the ontology 

+ Request (application/json)

        {
            "germplasmDbIds" : [ "Blabla", "34Mtp362" ], // (optional, text, `986`) ... The name or synonym of external genebank accession identifiers
            "observationVariableDbIds" : [ "37373", "CO_321:00000234"], // (optional, text, `CO_321:00000234`) ... The IDs of traits, could be ontology ID, database ID or PUI
            "studyDbIds" : [ "383", "2929", "WHEAT_NETWK_2016_MONTPELLIER" ], // (optional, text, `2356`) ... The database ID / PK of the studies search parameter
            "locationDbIds" : [ "383838", "MONTPELLIER" ], // locations these traits were collected
            "programDbIds" : [ "3838", "Drought resistance CG 2020" ], // list of programs that have phenotyped this trait
            "seasonDbIds" : [ "338", "2010", "1956-2014", "2002-2003-2004", "2007 Spring" ], // (optional, text, `2001`) ... The year or Phenotyping campaign of a multiannual study (trees, grape, ...)
            "observationLevel" : "plot", // (optional, text, `plot`) ... The type of the observationUnit. Returns only the observaton unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
            "observationTimeStampRange" : ["2015-06-16T00:53:26-0800","2015-06-18T00:53:26-0800"]
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
