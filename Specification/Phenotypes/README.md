
# Group Phenotypes

API to retrieve and submit data (phenotypes, environment variables) from studies. While the study calls focus on one study, calls in this section are for cross-study phenotypic data retrieval and submission.




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

+ Response 200 (metadata)
```
{
    "pagination": {
        "pageSize": 0,
        "currentPage": 0,
        "totalCount": 0,
        "totalPages": 0
    },
    "status": [],
    "datafiles": []
}
```+ Response 200 (result)
```
{
    "observations": [
        {
            "observationDbId": "153453453",
            "observationVariableDbId": "18020",
            "observationUnitDbId": "333888"
        },
        {
            "observationDbId": "23456",
            "observationVariableDbId": "18021",
            "observationUnitDbId": "333888"
        },
        {
            "observationDbId": "34567",
            "observationVariableDbId": "18022",
            "observationUnitDbId": "333888"
        }
    ]
}
```