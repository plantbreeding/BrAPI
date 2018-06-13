
# Group Phenotypes

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.




## Phenotypes-search/table [Post /brapi/v1/phenotypes-search/table]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.
      
observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
 
+ Request (application/json)
/definitions/phenotypesSearchRequest

+ Response 200 (application/json)
```
{
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
        "observationVariableNames": [
            "plant height",
            "fruit weight",
            "root weight"
        ],
        "observationVariableDbIds": [
            "variable1DbId",
            "variable2DbId",
            "variable3DbId"
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 1000,
            "totalPages": 1
        }
    }
}
```

## Phenotypes-search/tsv [Post /brapi/v1/phenotypes-search/tsv]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.
      
observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
 
+ Request (application/json)
/definitions/phenotypesSearchRequest

+ Response 200 (text/csv)
```
"\"year\"    \"studyDbId\"    \"studyName\"    \"locationDbId\"    \"locationName\"    \"germplasmDbId\"    \"germplasmName\"    \"observationUnitDbId\"    \"plotNumber\"    \"replicate\"    \"blockNumber\"    \"entryType\"    \"X\"    \"Y\"     \"variableDbId1\"    \"variableDbId2\"    \"variableDbId3\"\n\"2015\"    \"YieldStudy2015-5\"    \"Yield wheat 2015\"    \"mtp-north-32\"    \"Montpellier\"    \"doi:10.155454/12349537E12\"    \"IR-8\"    \"2016-Maugio-34-575-abc-123\"    \"120\"    \"\"    \"2\"    \"\"    \"5\"    \"15\"    \"45\"    \"3\"    \"10\"\n\"2016\"    \"YieldStudy2016-5\"    \"Yield wheat 2016\"    \"mtp-north-32\"    \"Montpellier\"    \"doi:10.155454/12349537E13\"    \"IR-8\"    \"2016-Maugio-34-575-abc-124\"    \"120\"    \"\"    \"2\"    \"\"    \"5\"    \"15\"    \"47\"    \"4\"    \"11\""
```

## Phenotypes-search [Post /brapi/v1/phenotypes-search]

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
/definitions/phenotypesSearchRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "entryType": "check",
                "observationUnitName": "2016-Maugio-34-575",
                "plantNumber": "0",
                "replicate": "0",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
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
                "programName": "Whealbi",
                "studyName": "Yield wheat 2015",
                "X": "5",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "entryNumber": "4",
                "studyDbId": "YieldStudy2015-5",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "season": "2015",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableName": "Plant_height",
                        "observationVariableDbId": "CO_321:0000045",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "season": "2015",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableName": "GW100_g",
                        "observationVariableDbId": "CO_321:0000996",
                        "value": "3"
                    }
                ],
                "blockNumber": "2",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "studyLocation": "Montpellier",
                "germplasmDbId": "doi:10.155454/12349537E12",
                "observationUnitDbId": "2016-Maugio-34-575-abc-123",
                "studyLocationDbId": "mtp-north-32",
                "germplasmName": "IR-8",
                "Y": "15",
                "observationLevel": "plot"
            },
            {
                "entryType": "test",
                "observationUnitName": "2010-Cornell-37-99",
                "plantNumber": "45204",
                "replicate": "2",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "programName": "Wheat for futur",
                "studyName": "Yield wheat 2010",
                "X": "6",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "entryNumber": "7",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "season": "2010",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableName": "Plant_height",
                        "observationVariableDbId": "CO_321:0000045",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "season": "2010",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableName": "GW100_g",
                        "observationVariableDbId": "CO_321:0000996",
                        "value": "3"
                    }
                ],
                "studyDbId": "YieldStudy2010-5",
                "blockNumber": "3",
                "treatments": [],
                "studyLocation": "Cornell",
                "germplasmDbId": "doi:10.155499/12349537E00",
                "observationUnitDbId": "45204",
                "studyLocationDbId": "88484",
                "germplasmName": "ZE-45",
                "Y": "15",
                "observationLevel": "plant"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 100,
            "totalPages": 1
        }
    }
}
```

## Phenotypes-search [Get /brapi/v1/phenotypes-search{?germplasmDbId}{?observationVariableDbId}{?studyDbId}{?locationDbId}{?trialDbId}{?programDbId}{?seasonDbId}{?observationLevel}{?observationTimeStampRangeStart}{?observationTimeStampRangeEnd}{?pageSize}{?page}]

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
    "result": {
        "data": [
            {
                "entryType": "check",
                "observationUnitName": "2016-Maugio-34-575",
                "plantNumber": "0",
                "replicate": "0",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
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
                "programName": "Whealbi",
                "studyName": "Yield wheat 2015",
                "X": "5",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "entryNumber": "4",
                "studyDbId": "YieldStudy2015-5",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "season": "2015",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableName": "Plant_height",
                        "observationVariableDbId": "CO_321:0000045",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "season": "2015",
                        "observationTimeStamp": "2015-06-16 08:53:26",
                        "observationVariableName": "GW100_g",
                        "observationVariableDbId": "CO_321:0000996",
                        "value": "3"
                    }
                ],
                "blockNumber": "2",
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "studyLocation": "Montpellier",
                "germplasmDbId": "doi:10.155454/12349537E12",
                "observationUnitDbId": "2016-Maugio-34-575-abc-123",
                "studyLocationDbId": "mtp-north-32",
                "germplasmName": "IR-8",
                "Y": "15",
                "observationLevel": "plot"
            },
            {
                "entryType": "test",
                "observationUnitName": "2010-Cornell-37-99",
                "plantNumber": "45204",
                "replicate": "2",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "programName": "Wheat for futur",
                "studyName": "Yield wheat 2010",
                "X": "6",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "entryNumber": "7",
                "observations": [
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "153453453",
                        "season": "2010",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableName": "Plant_height",
                        "observationVariableDbId": "CO_321:0000045",
                        "value": "45"
                    },
                    {
                        "collector": "Mr. Technician",
                        "observationDbId": "23453454345",
                        "season": "2010",
                        "observationTimeStamp": "2010-06-16 08:53:26",
                        "observationVariableName": "GW100_g",
                        "observationVariableDbId": "CO_321:0000996",
                        "value": "3"
                    }
                ],
                "studyDbId": "YieldStudy2010-5",
                "blockNumber": "3",
                "treatments": [],
                "studyLocation": "Cornell",
                "germplasmDbId": "doi:10.155499/12349537E00",
                "observationUnitDbId": "45204",
                "studyLocationDbId": "88484",
                "germplasmName": "ZE-45",
                "Y": "15",
                "observationLevel": "plant"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 2,
            "pageSize": 100,
            "totalPages": 1
        }
    }
}
```

## Phenotypes [Post /brapi/v1/phenotypes{?format}]

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
/definitions/phenotypesRequest

+ Response 200 (result)
```
{
    "observations": [
        {
            "observationUnitDbId": "333888",
            "observationDbId": "153453453",
            "observationVariableDbId": "18020"
        },
        {
            "observationUnitDbId": "333888",
            "observationDbId": "23456",
            "observationVariableDbId": "18021"
        },
        {
            "observationUnitDbId": "333888",
            "observationDbId": "34567",
            "observationVariableDbId": "18022"
        }
    ]
}
```+ Response 200 (metadata)
```
{
    "datafiles": [],
    "status": [],
    "pagination": {
        "currentPage": 0,
        "totalCount": 0,
        "pageSize": 0,
        "totalPages": 0
    }
}
```

## Phenotypes-search/csv [Post /brapi/v1/phenotypes-search/csv]

Scope: PHENOTYPING.
Status: ACCEPTED.

Returns a list of observationUnit with the observed Phenotypes.
      
observationTimeStamp : Iso Standard 8601.

observationValue data type inferred from the ontology 

+ Parameters
 
+ Request (application/json)
/definitions/phenotypesSearchRequest

+ Response 200 (text/csv)
```
"\"year\",\"studyDbId\",\"studyName\",\"locationDbId\",\"locationName\",\"germplasmDbId\",\"germplasmName\",\"observationUnitDbId\",\"plotNumber\",\"replicate\",\"blockNumber\", \"entryType\", \"X\", \"Y\", \"variableDbId1\", \"variableDbId2\", \"variableDbId3\"\n\"2015\", \"YieldStudy2015-5\", \"Yield wheat 2015\", \"mtp-north-32\", \"Montpellier\", \"doi:10.155454/12349537E12\", \"IR-8\", \"2016-Maugio-34-575-abc-123\", \"120\", \"\", \"2\", \"\", \"5\", \"15\", \"45\", \"3\", \"10\"\n\"2016\", \"YieldStudy2016-5\", \"Yield wheat 2016\", \"mtp-north-32\", \"Montpellier\", \"doi:10.155454/12349537E13\", \"IR-8\", \"2016-Maugio-34-575-abc-124\", \"120\", \"\", \"2\", \"\", \"5\", \"15\", \"47\", \"4\", \"11\""
```