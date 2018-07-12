
# Group Phenotypes

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.




## Post Phenotypes-search Csv  [POST /brapi/v1/phenotypes-search/csv]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.
      
observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
 
+ Request (application/json)
```
/definitions/phenotypesSearchRequest
```



+ Response 200 (text/csv)
```
"\"year\",\"studyDbId\",\"studyName\",\"locationDbId\",\"locationName\",\"germplasmDbId\",\"germplasmName\",\"observationUnitDbId\",\"plotNumber\",\"replicate\",\"blockNumber\", \"entryType\", \"X\", \"Y\", \"variableDbId1\", \"variableDbId2\", \"variableDbId3\"\n\"2015\", \"YieldStudy2015-5\", \"Yield wheat 2015\", \"mtp-north-32\", \"Montpellier\", \"doi:10.155454/12349537E12\", \"IR-8\", \"2016-Maugio-34-575-abc-123\", \"120\", \"\", \"2\", \"\", \"5\", \"15\", \"45\", \"3\", \"10\"\n\"2016\", \"YieldStudy2016-5\", \"Yield wheat 2016\", \"mtp-north-32\", \"Montpellier\", \"doi:10.155454/12349537E13\", \"IR-8\", \"2016-Maugio-34-575-abc-124\", \"120\", \"\", \"2\", \"\", \"5\", \"15\", \"47\", \"4\", \"11\""
```



## Get Phenotypes-search  [GET /brapi/v1/phenotypes-search{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?pageSize}{?page}]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

Implemented for GnpIS and PHIS data (https://urgi.versailles.inra.fr/ws/webresources/brapi/v1/phenotypes). 
Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.
Refactor note : This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below.
Example Use cases:
- Study a panel of germplasm accross multiple studies, search parameters : {"germplasmDbIds" : [ "Syrah", "34Mtp362" ]}
- Get all data for a specific study : {"studyDbIds" : [ "383" ]}
- Get simple atomic phenotyping values : {"germplasmDbIds" : [ "Syrah", "34Mtp362" ], "observationVariableDbIds" : [ "CO_345:0000043"]}
- Study Locations for adaptation to climat change : {"locationDbIds" : [ "383838", "MONTPELLIER" ], "germplasmDbIds" : [ "all ids for a given species"]}
- Find phenotypes that are from after a certain timestamp

observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
    + germplasmDbId (Optional, string) ... The name or synonym of external genebank accession identifiers
    + observationVariableDbId (Optional, string) ... The ID of traits, could be ontology ID, database ID or PUI
    + studyDbId (Optional, string) ... The database ID / PK of the studies search parameter
    + locationDbId (Optional, string) ... locations these traits were collected
    + trialDbId (Optional, string) ... trial to search across
    + programDbId (Optional, string) ... program that have phenotyped this trait
    + seasonDbId (Optional, string) ... The year or Phenotyping campaign of a multi-annual study (trees, grape, ...)
    + observationLevel (Optional, string) ... The type of the observationUnit. Returns only the observation unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
    + observationTimeStampRangeStart (Optional, string) ... Timestamp range start
    + observationTimeStampRangeEnd (Optional, string) ... Timestamp range end
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is 1000.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is 0.


+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 100,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "5",
                "Y": "15",
                "blockNumber": "2",
                "entryNumber": "4",
                "entryType": "check",
                "germplasmDbId": "doi:10.155454/12349537E12",
                "germplasmName": "IR-8",
                "observationLevel": "plot",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "observationUnitDbId": "2016-Maugio-34-575-abc-123",
                "observationUnitName": "2016-Maugio-34-575",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "biosampleEBI"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239865",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000045",
                        "observationVariableName": "Plant_height",
                        "season": "2015",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000996",
                        "observationVariableName": "GW100_g",
                        "season": "2015",
                        "value": "3"
                    }
                ],
                "plantNumber": "0",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "programName": "Whealbi",
                "replicate": "0",
                "studyDbId": "YieldStudy2015-5",
                "studyLocation": "Montpellier",
                "studyLocationDbId": "mtp-north-32",
                "studyName": "Yield wheat 2015",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ]
            },
            {
                "X": "6",
                "Y": "15",
                "blockNumber": "3",
                "entryNumber": "7",
                "entryType": "test",
                "germplasmDbId": "doi:10.155499/12349537E00",
                "germplasmName": "ZE-45",
                "observationLevel": "plant",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "observationUnitDbId": "45204",
                "observationUnitName": "2010-Cornell-37-99",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000045",
                        "observationVariableName": "Plant_height",
                        "season": "2010",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000996",
                        "observationVariableName": "GW100_g",
                        "season": "2010",
                        "value": "3"
                    }
                ],
                "plantNumber": "45204",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "programName": "Wheat for futur",
                "replicate": "2",
                "studyDbId": "YieldStudy2010-5",
                "studyLocation": "Cornell",
                "studyLocationDbId": "88484",
                "studyName": "Yield wheat 2010",
                "treatments": []
            }
        ]
    }
}
```



## Post Phenotypes-search  [POST /brapi/v1/phenotypes-search]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.

See <a href="#introduction/search-services">Search Services</a> for additional implementation details.

Implemented for GnpIS and PHIS data (https://urgi.versailles.inra.fr/ws/webresources/brapi/v1/phenotypes). 
Use case: this section allows to get a dataset from multiple studies. It allows to integrate data from several databases.
Refactor note : This call allows to get and integrate portions of multiple phenotyping data matrixes. A proposed evolution allowed to get a list of single observations, this functionality is still possible with this call by specifybing the observation variable, see below.
Example Use cases:
- Study a panel of germplasm accross multiple studies, search parameters : {"germplasmDbIds" : [ "Syrah", "34Mtp362" ]}
- Get all data for a specific study : {"studyDbIds" : [ "383" ]}
- Get simple atomic phenotyping values : {"germplasmDbIds" : [ "Syrah", "34Mtp362" ], "observationVariableDbIds" : [ "CO_345:0000043"]}
- Study Locations for adaptation to climat change : {"locationDbIds" : [ "383838", "MONTPELLIER" ], "germplasmDbIds" : [ "all ids for a given species"]}
- Find phenotypes that are from after a certain timestamp

observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
 
+ Request (application/json)
```
/definitions/phenotypesSearchRequest
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 100,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "X": "5",
                "Y": "15",
                "blockNumber": "2",
                "entryNumber": "4",
                "entryType": "check",
                "germplasmDbId": "doi:10.155454/12349537E12",
                "germplasmName": "IR-8",
                "observationLevel": "plot",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "observationUnitDbId": "2016-Maugio-34-575-abc-123",
                "observationUnitName": "2016-Maugio-34-575",
                "observationUnitXref": [
                    {
                        "id": "SAMEA179865230",
                        "source": "biosampleEBI"
                    },
                    {
                        "id": "INRA:CoeSt6 _SMH03",
                        "source": "gnpis.lot"
                    },
                    {
                        "id": "239865",
                        "source": "kernelDB"
                    }
                ],
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000045",
                        "observationVariableName": "Plant_height",
                        "season": "2015",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000996",
                        "observationVariableName": "GW100_g",
                        "season": "2015",
                        "value": "3"
                    }
                ],
                "plantNumber": "0",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "programName": "Whealbi",
                "replicate": "0",
                "studyDbId": "YieldStudy2015-5",
                "studyLocation": "Montpellier",
                "studyLocationDbId": "mtp-north-32",
                "studyName": "Yield wheat 2015",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ]
            },
            {
                "X": "6",
                "Y": "15",
                "blockNumber": "3",
                "entryNumber": "7",
                "entryType": "test",
                "germplasmDbId": "doi:10.155499/12349537E00",
                "germplasmName": "ZE-45",
                "observationLevel": "plant",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "observationUnitDbId": "45204",
                "observationUnitName": "2010-Cornell-37-99",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000045",
                        "observationVariableName": "Plant_height",
                        "season": "2010",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableDbId": "CO_321:0000996",
                        "observationVariableName": "GW100_g",
                        "season": "2010",
                        "value": "3"
                    }
                ],
                "plantNumber": "45204",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "programName": "Wheat for futur",
                "replicate": "2",
                "studyDbId": "YieldStudy2010-5",
                "studyLocation": "Cornell",
                "studyLocationDbId": "88484",
                "studyName": "Yield wheat 2010",
                "treatments": []
            }
        ]
    }
}
```



## Post Phenotypes-search Tsv  [POST /brapi/v1/phenotypes-search/tsv]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.
      
observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
 
+ Request (application/json)
```
/definitions/phenotypesSearchRequest
```



+ Response 200 (text/csv)
```
"\"year\"    \"studyDbId\"    \"studyName\"    \"locationDbId\"    \"locationName\"    \"germplasmDbId\"    \"germplasmName\"    \"observationUnitDbId\"    \"plotNumber\"    \"replicate\"    \"blockNumber\"    \"entryType\"    \"X\"    \"Y\"     \"variableDbId1\"    \"variableDbId2\"    \"variableDbId3\"\n\"2015\"    \"YieldStudy2015-5\"    \"Yield wheat 2015\"    \"mtp-north-32\"    \"Montpellier\"    \"doi:10.155454/12349537E12\"    \"IR-8\"    \"2016-Maugio-34-575-abc-123\"    \"120\"    \"\"    \"2\"    \"\"    \"5\"    \"15\"    \"45\"    \"3\"    \"10\"\n\"2016\"    \"YieldStudy2016-5\"    \"Yield wheat 2016\"    \"mtp-north-32\"    \"Montpellier\"    \"doi:10.155454/12349537E13\"    \"IR-8\"    \"2016-Maugio-34-575-abc-124\"    \"120\"    \"\"    \"2\"    \"\"    \"5\"    \"15\"    \"47\"    \"4\"    \"11\""
```



## Post Phenotypes-search Table  [POST /brapi/v1/phenotypes-search/table]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.
      
observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
 
+ Request (application/json)
```
/definitions/phenotypesSearchRequest
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            [
                "2017",
                "stu1",
                "Study Name",
                "loc1",
                "Location Name",
                "CIP1",
                "CIP Name",
                "abc123",
                1,
                1,
                1,
                "2017-06-16T00:53:26Z",
                "Test Entry",
                "1",
                "2",
                "25.3",
                "103.4",
                "50.75"
            ],
            [
                "2017",
                "stu1",
                "Study Name",
                "loc1",
                "Location Name",
                "CIP1",
                "CIP Name",
                "abc124",
                1,
                1,
                1,
                "2017-06-16T00:54:57Z",
                "Test Entry",
                "2",
                "2",
                "27.9",
                "98.65",
                "45.345"
            ]
        ],
        "headerRow": [
            "year",
            "studyDbId",
            "studyName",
            "locationDbId",
            "locationName",
            "germplasmDbId",
            "germplasmName",
            "observationUnitDbId",
            "plotNumber",
            "replicate",
            "blockNumber",
            "observationTimestamp",
            "entryType",
            "X",
            "Y"
        ],
        "observationVariableDbIds": [
            "variable1DbId",
            "variable2DbId",
            "variable3DbId"
        ],
        "observationVariableNames": [
            "plant height",
            "fruit weight",
            "root weight"
        ]
    }
}
```



## Post Phenotypes  [POST /brapi/v1/phenotypes{?format}]

Scope: PHENOTYPING. 

Notes: 
Along with the study specific phenotype saving calls (in the observationUnit and table formats), this call allows phenotypes to be saved and images to optionally be transferred as well.
      
Call to invoke for saving the measurements (observations) collected
from field for all the observation units.
Observation timestamp should be ISO 8601 https://www.w3.org/TR/NOTE-datetime
In case where JSON data is zipped for faster transfer speed (as in the case
of the IRRI handheld implementation), the zipped JSON file will be listed
in datafiles. The zipped file contains a JSON file with the same structure
as the BrAPI call. In this case a format parameter should be passed as well.
Images can be optionally be uploaded using this call by providing a zipfile
of all images in the datafiles, along with the actual zipfile in multi-part
form data. 

+ Parameters
    + format (Optional, string) ... In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
 
+ Request (application/json)
```
/definitions/phenotypesRequest
```



+ Response 200 (metadata)
```
{
    "datafiles": [],
    "pagination": {
        "currentPage": 0,
        "pageSize": 0,
        "totalCount": 0,
        "totalPages": 0
    },
    "status": []
}
```

+ Response 200 (result)
```
{
    "observations": [
        {
            "observationDbId": "153453453",
            "observationUnitDbId": "333888",
            "observationVariableDbId": "18020"
        },
        {
            "observationDbId": "23456",
            "observationUnitDbId": "333888",
            "observationVariableDbId": "18021"
        },
        {
            "observationDbId": "34567",
            "observationUnitDbId": "333888",
            "observationVariableDbId": "18022"
        }
    ]
}
```

