## Phenotype Search [/brapi/v1/phenotypes-search]
Scope: PHENOTYPING.
Status: ACCEPTED.
Implementation target: 2016. Implemented for GnpIS private data. 
Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.

###### Response data types
|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
|observationUnitDbId|Long|internal DB id ||
|studyDbId|Long|internal DB id (Primary Key)||
|studyName | string |||
|studyLocationDbId| internal DB id (primary key) ||
|studyLocation|string| Location name or ID|Y|
|programName|string|||
|germplasmDbId|Long|internal DB id (Primary Key)||
|germplasmName|string| Display name for the germplasm. MCPD Name field||
|X,Y|string|||
|XLabel,YLabel|string|Example: X=row, Y = rootstock||
|observationVariableId|string| ID or PUI (DOI, URI, LSID)||
|observationVariableDbId | string | ||
|observations.season|string| Year or season, Phenotyping campain||
|value|string|||
|observationTimeStamp|string|ISO format "2006-07-03::10:00"||
|collector|string| Person or team who has made the observaiton||
|additionalInfo|array of key/value pair|||

### Phenotype Search [POST]

observationTimeStamp : Iso Standard
observationValue data type inferred from the ontology 

+ Request (application/json)

        {
            "germplasmDbIds" : [ "Blabla", "Blabla2" ], // (optional, text, `986`) ... The name or synonym of external genebank accession identifiers
            "observationVariableDbIds" : [ 37373, 38338], // (optional, text, `CO_321:00000234`) ... The IDs of traits, could be ontology ID, database ID or PUI
            "studyDbIds" : [ 383, 2929, 3838383 ], // (optional, text, `2356`) ... The database ID / PK of the studies search parameter
            "locationDbIds" : [ 383838, 959595 ], // locations these traits were collected
            "programDbIds" : [ 3838, 33838 ], // list of programs that have phenotyped this trait
            "seasonDbIds" : [ 338, 3939 ], // (optional, text, `2001`) ... The year or Phenotyping campaign of a multiannual study (trees, grape, ...)
            "observationLevel" : "plot", // (optional, text, `plot`) ... The type of the observationUnit. Returns only the observaton unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
            "pageSize" : 100, // (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
            "page" : 1, // (optional, integer, `10`) ... Which result page is requested
        }
 
+ Response 200 (application/json)

        {
            "metadata": 
            {
                "pagination": 
                {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 10,
                    "totalPages": 1
                },

                "status": {},
                "datafiles": []
            },

            "result": 
            {
                "data": 
                [   {
                        "observationDbId": 4884848,
                        "observationUnitDbId": 20,
                        "observationUnitName": "Montpellier-2016-xyz-blabla",
                        "studyDbId": 25,
                        "studyName": "Yield",
                        "studyLocationDbId" : 88484,
                        "studyLocation": "Montpellier",
                        "programName": "Inovine",
                        "observationLevel": "plot",
                        "germplasmDbId": 3425,
                        "germplasmName": "syrah",
                        "observationVariableId": "CO_321:0000045",
                        "observationVariableDbId" : 383838,
                        "season": "2005",
                        "value": "red",
                        "observationTimeStamp": null,
                        "collector": "John Doe and team",
                        "uploadedBy" : "Mr. Upload",

                        "additionalInfo" : { 
                            "key1" : "value1",  // eg:
                            "studySet" : [ "National Network","Frost suceptibility network" ],
                            "studyPlatform": "Phenome",
                            "treatments": 
                            [ {
                                "factor": "water regimen",
                                "modality": "water deficit"
                            } ],
                             "quality": "reliability of the observation",
                            "collectionFacilityLabel": "phenodyne",
                        },
                               

                    },
                    { /// more entries...
                    },
                ],
            },
        }
    
