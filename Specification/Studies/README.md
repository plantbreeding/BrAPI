
# Group Study

Study is defined as a phenotyping experiment conducted at a single geographic location. One Trial can have multiple studies conducted (e.g. multi location international trials).

Note that dates should be provided in extended ISO 8601 format (for example, "YYYY-MM-DD").




## Observationlevels [Get /brapi/v1/observationLevels{?pageSize}{?page}]

 Call to retrieve the list of supported observation levels. Observation levels indicate the granularity level at which the measurements are taken. The values are used to supply the `observationLevel` parameter in the observation unit details call.  

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            "plant",
            "plot"
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Seasons [Get /brapi/v1/seasons{?year}{?pageSize}{?page}]

 Call to retrive all seasons (or years) in the database. (Added by Jan-Erik and Lukas 5/26/2016) Scope: PHENOTYPING.
<a href="https://test-server.brapi.org/brapi/v1/seasons"> test-server.brapi.org/brapi/v1/seasons</a> 

+ Parameters
    + year (Optional, string) ... 
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "seasonDbId": "237",
                "year": "2015",
                "season": "Fall"
            },
            {
                "seasonDbId": "238",
                "year": "2016",
                "season": "Spring"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies-search [Get /brapi/v1/studies-search{?studyType}{?programDbId}{?locationDbId}{?seasonDbId}{?trialDbId}{?studyDbId}{?germplasmDbIds}{?observationVariableDbIds}{?pageSize}{?page}{?active}{?sortBy}{?sortOrder}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016.
Implemented by: Germinate
Used by: Flapjack, Cassavabase
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Get list of studies
StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies-search</a> 

+ Parameters
    + studyType (Optional, string) ... Filter based on study type e.g. Nursery, Trial or Genotype.
    + programDbId (Optional, string) ... Program filter to only return studies associated with given program id.
    + locationDbId (Optional, string) ... Filter by location
    + seasonDbId (Optional, string) ... Filter by season or year
    + trialDbId (Optional, string) ... Filter by trial
    + studyDbId (Optional, string) ... Filter by study DbId
    + germplasmDbIds (Optional, array) ... Filter studies where specified germplasm have been used/tested
    + observationVariableDbIds (Optional, array) ... Filter studies where specified observation variables have been measured
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + active (Optional, boolean) ... Filter active status true/false.
    + sortBy (Optional, string) ... Sort order. Name of the field to sort by.
    + sortOrder (Optional, string) ... Sort order direction. Ascending/Descending.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "name": "Earlygenerationtesting",
                "startDate": "2007-06-01",
                "endDate": "2008-12-31",
                "locationName": "Kenya",
                "additionalInfo": {
                    "property2Name": "property2Value",
                    "property1Name": "property1Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "35",
                "locationDbId": "23",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "active": "true",
                "programName": "Drought Resistance Program A",
                "studyType": "Trial",
                "trialDbId": "7",
                "programDbId": "27",
                "trialName": "InternationalTrialA"
            },
            {
                "name": "Earlygenerationtesting",
                "startDate": "2005-06-01",
                "endDate": "2008-12-31",
                "locationName": "Zimbabwe",
                "additionalInfo": {
                    "property2Name": "property2Value",
                    "property1Name": "property1Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "345",
                "locationDbId": "33",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "active": "true",
                "programName": "Drought Resistance Program B",
                "studyType": "Trial",
                "trialDbId": "7",
                "programDbId": "58",
                "trialName": "InternationalTrialA"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies-search [Post /brapi/v1/studies-search]

 Scope: PHENOTYPING. Status: ACCEPTED. Implementation target date: PAG2016.
Implemented by: Germinate
Used by: Flapjack, Cassavabase
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Get list of studies
StartDate and endDate should be ISO8601 format for dates: YYYY-MM-DD
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies-search</a> 

+ Parameters
 
+ Request (application/json)
/definitions/studySearchRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "name": "Earlygenerationtesting",
                "startDate": "2007-06-01",
                "endDate": "2008-12-31",
                "locationName": "Kenya",
                "additionalInfo": {
                    "property2Name": "property2Value",
                    "property1Name": "property1Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "35",
                "locationDbId": "23",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "active": "true",
                "programName": "Drought Resistance Program A",
                "studyType": "Trial",
                "trialDbId": "7",
                "programDbId": "27",
                "trialName": "InternationalTrialA"
            },
            {
                "name": "Earlygenerationtesting",
                "startDate": "2005-06-01",
                "endDate": "2008-12-31",
                "locationName": "Zimbabwe",
                "additionalInfo": {
                    "property2Name": "property2Value",
                    "property1Name": "property1Value",
                    "property3Name": "property3Value"
                },
                "studyDbId": "345",
                "locationDbId": "33",
                "seasons": [
                    "2007 Spring",
                    "2008 Fall"
                ],
                "active": "true",
                "programName": "Drought Resistance Program B",
                "studyType": "Trial",
                "trialDbId": "7",
                "programDbId": "58",
                "trialName": "InternationalTrialA"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid} [Get /brapi/v1/studies/{studyDbId}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implemented by: Germinate, GnpIS
Notes: an additionalInfo field was added to provide a controlled vocabulary for less common data fields.
Retrieve the information of the study required for field data collection
More linked data: * observation variables: ```/brapi/v1/studies/{studyDbId}/observationVariables``` * germplasm: ```/brapi/v1/studies/{studyDbId}/germplasm``` * observation units: ```/brapi/v1/studies/{studyDbId}/observationUnits``` * layout: ```brapi/v1/studies/{studyDbId}/layout```
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.


+ Response 200 (application/json)
```
{
    "result": {
        "startDate": "2005-06-01",
        "trialName": "International Yield Trial",
        "studyDescription": "some free text description that could include scientific goal, some tracability and whatever makes sense",
        "license": "https://creativecommons.org/licenses/by/4.0",
        "location": {
            "name": "Ibadan",
            "additionalInfo": {
                "property2Name": "property2Value",
                "property1Name": "property1Value",
                "AnnualMeanRain": "value",
                "SoilDescription": "23"
            },
            "abbreviation": "IB",
            "instituteAddress": "route foo, Clermont Ferrand, France",
            "instituteName": "INRA - GDEC",
            "locationDbId": "1",
            "latitude": -21.5,
            "altitude": 12,
            "countryCode": "NGA",
            "longitude": 165.5,
            "countryName": "Nigeria"
        },
        "seasons": [
            "2005 Winter",
            "2008 Summer"
        ],
        "active": "true",
        "studyName": "Earlygenerationtesting",
        "contacts": [
            {
                "instituteName": "IRRI",
                "name": "John Doe",
                "type": "Scientist",
                "contactDbId": "C025",
                "email": "j.doe@mail.com",
                "orcid": "0000-0002-0607-8728"
            },
            {
                "instituteName": "IRRI",
                "name": "Dave Peters",
                "type": null,
                "contactDbId": "C026",
                "email": null,
                "orcid": null
            }
        ],
        "endDate": "2008-12-31",
        "additionalInfo": {
            "principalInvestigator": "Dr. Breeder",
            "property2Name": "property2Value",
            "property1Name": "property1Value",
            "studyObjective": "Increase yield",
            "publications": "pmid:24039865287545"
        },
        "studyDbId": "35",
        "lastUpdate": {
            "version": "1.1",
            "timestamp": "2015-06-16T00:53:26Z"
        },
        "studyType": "Yield study",
        "trialDbId": "57",
        "dataLinks": [
            {
                "type": "Image archive",
                "url": "http://data.inra.fr/archive/multi-spect-flowering.zip",
                "name": "image-archive12.zip"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/germplasm [Get /brapi/v1/studies/{studyDbId}/germplasm{?pageSize}{?page}]

 Scope: PHENOTYPING
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/germplasm</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "pedigree": "TOBA97/SW90.1057",
                "germplasmName": "Pahang",
                "seedSource": "SS1",
                "entryNumber": "1",
                "synonyms": [
                    "01BEL084609"
                ],
                "germplasmDbId": "382",
                "accessionNumber": "ITC0609"
            },
            {
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084727",
                "pedigree": "TOBA97/SW90.1057",
                "germplasmName": "Pahang",
                "seedSource": "SS2",
                "entryNumber": "2",
                "synonyms": [
                    "01BEL084727"
                ],
                "germplasmDbId": "394",
                "accessionNumber": "ITC0727"
            }
        ],
        "studyDbId": "35",
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/layout [Get /brapi/v1/studies/{studyDbId}/layout{?pageSize}{?page}]

 Retrive the layout details for a study. Returns an array of observation unit position data which describes where each unit and germplasm is located within the study layout
Retrieve the plot layout of the study with id {id}.
For each observationUnit within a study, return the `block`, `replicate`, and `entryType` values as well as the `X` and `Y` coordinates. `entryType` can be "check", "test", or "filler".
Also return some human readable meta data about the observationUnit and germplasm.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/layout</a>  

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationUnitDbId": "11",
                "additionalInfo": {},
                "replicate": 1,
                "germplasmName": "ZIPA_68",
                "entryType": "check/test/filler",
                "studyDbId": "35",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "X": 1,
                "germplasmDbId": "143",
                "blockNumber": 1,
                "Y": 1
            },
            {
                "observationUnitDbId": "12",
                "additionalInfo": {},
                "replicate": 1,
                "germplasmName": "ZIPA_69",
                "entryType": "check/test/filler",
                "studyDbId": "35",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "observationLevel": "plot",
                "X": 1,
                "germplasmDbId": "144",
                "blockNumber": 1,
                "Y": 2
            },
            {
                "observationUnitDbId": "13",
                "additionalInfo": {},
                "replicate": 1,
                "germplasmName": "ZIPA_70",
                "entryType": "check/test/filler",
                "studyDbId": "35",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "observationLevel": "plot",
                "X": 1,
                "germplasmDbId": "145",
                "blockNumber": 1,
                "Y": 3
            },
            {
                "observationUnitDbId": "11",
                "additionalInfo": {},
                "replicate": 2,
                "germplasmName": "ZIPA_68",
                "entryType": "check/test/filler",
                "studyDbId": "35",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "X": 2,
                "germplasmDbId": "143",
                "blockNumber": 2,
                "Y": 1
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 4
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/layout [Put /brapi/v1/studies/{studyDbId}/layout]

 Modify a study layout
Update the layout data for a set of observation units within a study. Each layout object is a subset of fields within an observationUnit, so it doesnt make sense to create a new layout object by itself.
Implementation Notes:
+ If any of the fields in the request object is missing, that piece of data will not be updated. + If an observationUnitDbId can not be found within the given study, an error will be returned. + `entryType` can have the values "check", "test", or "filler". + The response should match the structure of the response from `GET studies/{studyDbId}/layout`, but it should only contain the layout objects which have been updated by the PUT request. Also, pagination is not available in the response.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/layout</a>  

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
 
+ Request (application/json)
/definitions/studyLayoutRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationUnitDbId": "11",
                "additionalInfo": {},
                "replicate": 1,
                "germplasmName": "ZIPA_68",
                "entryType": "check/test/filler",
                "studyDbId": "1",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "X": 1,
                "germplasmDbId": "143",
                "blockNumber": 1,
                "Y": 1
            },
            {
                "observationUnitDbId": "12",
                "additionalInfo": {},
                "replicate": 1,
                "germplasmName": "ZIPA_69",
                "entryType": "check/test/filler",
                "studyDbId": "1",
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "observationLevel": "plot",
                "X": 1,
                "germplasmDbId": "144",
                "blockNumber": 1,
                "Y": 2
            },
            {
                "observationUnitDbId": "13",
                "additionalInfo": {},
                "replicate": 1,
                "germplasmName": "ZIPA_70",
                "entryType": "check/test/filler",
                "studyDbId": "1",
                "observationUnitName": "ZIPA_70_Ibadan_2014",
                "observationLevel": "plot",
                "X": 1,
                "germplasmDbId": "145",
                "blockNumber": 1,
                "Y": 3
            },
            {
                "observationUnitDbId": "11",
                "additionalInfo": {},
                "replicate": 2,
                "germplasmName": "ZIPA_68",
                "entryType": "check/test/filler",
                "studyDbId": "1",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "X": 2,
                "germplasmDbId": "143",
                "blockNumber": 2,
                "Y": 1
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 4
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/observationunits [Get /brapi/v1/studies/{studyDbId}/observationunits{?observationLevel}{?pageSize}{?page}]

 The main API call for field data collection, to retrieve all the observation units within a study.
Scope: PHENOTYPING
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationunits</a> 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
    + observationLevel (Optional, string) ... The granularity level of observation units. Either `plotNumber` or `plantNumber` fields will be relavant depending on whether granularity is plot or plant respectively.
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "replicate": "1",
                "blockNumber": "1",
                "observationUnitName": "Test-2016-location-34-575",
                "observationUnitXref": [
                    {
                        "source": "biosampleEBI",
                        "id": "SAMEA179865230"
                    },
                    {
                        "source": "gnpis.lot",
                        "id": "INRA:CoeSt6 _SMH03"
                    },
                    {
                        "source": "kernelDB",
                        "id": "239865"
                    }
                ],
                "plotNumber": "1",
                "germplasmDbId": "1",
                "observationUnitDbId": "abc-123",
                "pedigree": "IR-8-FP/IR-8-MP",
                "observations": [
                    {
                        "observationVariableDbId": "18020",
                        "value": "25.63",
                        "observationVariableName": "Plant_height",
                        "collector": "Mr. Technician",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationDbId": "153453453"
                    },
                    {
                        "observationVariableDbId": "51496",
                        "value": "Light Green",
                        "observationVariableName": "GW100_g",
                        "collector": "Mr. Technician",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationDbId": "23453454345"
                    }
                ],
                "germplasmName": "IR-8",
                "plantNumber": "0",
                "entryNumber": "1",
                "observationLevel": "plot",
                "X": "1",
                "Y": "1",
                "entryType": "Test entry"
            },
            {
                "pedigree": "IR-9-FP/IR-9-MP",
                "observations": [
                    {
                        "observationVariableDbId": "18020",
                        "value": "34.95",
                        "observationVariableName": "Plant_height",
                        "collector": "Mr. Technician",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationDbId": "3"
                    },
                    {
                        "observationVariableDbId": "51496",
                        "value": "Blue",
                        "observationVariableName": "GW100_g",
                        "collector": "Mr. Technician",
                        "observationTimeStamp": "2015-06-16T00:53:26Z",
                        "observationDbId": "4"
                    }
                ],
                "replicate": "1",
                "germplasmName": "IR-9",
                "plantNumber": "0",
                "observationLevel": "plot",
                "entryType": "Check entry",
                "observationUnitName": "Test-2016-location-34-456",
                "enrtyNumber": "2",
                "plotNumber": "2",
                "X": "1",
                "Y": "2",
                "germplasmDbId": "2",
                "observatioUnitDbId": "abc-456",
                "blockNumber": "2"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/observationunits [Post /brapi/v1/studies/{studyDbId}/observationunits{?format}]

This call has been deprecated in V1.1. Use instead: "PUT /studies/{studyDbId}/observationunits" and "PUT /studies/{studyDbId}/observationunits/zip" 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
    + format (Required, string) ... (default is JSON, but can be zip) In case where JSON data is zipped for faster transfer speed (as in the case of the IRRI handheld implementation), the zipped JSON file will be listed in datafiles. The zipped file contains a JSON file with the same structure as the BrAPI call.
 
+ Request (application/json)
{
    "properties": {
        "result": {
            "$ref": "#/definitions/newObservationsRequestDeprecated"
        },
        "metadata": {
            "$ref": "#/definitions/metadata"
        }
    },
    "title": "newObservationsRequestWrapperDeprecated"
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "code": "42",
                "message": "Could not update values for Observation Units"
            }
        ]
    }
}
```

## Studies/{studydbid}/observationunits [Put /brapi/v1/studies/{studyDbId}/observationunits]

Use this call for uploading new Observations as JSON to a system.

Note: If 'observationUnitDbId' or 'observationDbId' is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If 'observationUnitDbId' or 'observationDbId' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds. 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
 
+ Request (application/json)
{
    "items": {
        "$ref": "#/definitions/newObservationUnitRequest"
    },
    "title": "newObservationUnitRequestList",
    "type": "array"
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "code": "Error",
                "message": "Could not update values for Observation Units"
            }
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "results": {
        "observationUnitDbIds": [
            "123abc",
            "456def"
        ]
    },
    "metadata": {
        "status": [
            {
                "code": "1",
                "message": "Upload Successful"
            }
        ]
    }
}
```

## Studies/{studydbid}/observationunits/zip [Post /brapi/v1/studies/{studyDbId}/observationunits/zip]

Note: If 'observationUnitDbId' or 'observationDbId' is populated, they should be considered updates to existing records. If an existing record of that DbId is not found, the document should be treated as new records and assigned new DbIds. If 'observationUnitDbId' or 'observationDbId' is un-populated (empty string or null) the document should be treated as new records and assigned new DbIds. 

+ Parameters
    + studyDbId (Required, string) ... The study these observation units are related to.
 
+ Request (application/json)
{
    "format": "binary",
    "type": "string"
}

+ Response 400 (application/json)
```
{
    "metadata": {
        "status": [
            {
                "code": "Error",
                "message": "Could not update values for Observation Units"
            }
        ]
    }
}
```+ Response 200 (application/json)
```
{
    "results": {
        "observationUnitDbIds": [
            "123abc",
            "456def"
        ]
    },
    "metadata": {
        "status": [
            {
                "code": "1",
                "message": "Upload Successful"
            }
        ]
    }
}
```

## Studies/{studydbid}/observationvariables [Get /brapi/v1/studies/{studyDbId}/observationvariables{?pageSize}{?page}]

 Scope: PHENOTYPING
List all the observation variables measured in the study.
Refer to the data type definition of variables in `/Specification/ObservationVariables/README.md`.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationvariables</a> 

+ Parameters
    + studyDbId (Required, string) ... string database unique identifier
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                },
                "defaultValue": "0",
                "ontologyName": "Cassava",
                "method": {
                    "reference": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "scale": {
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "xref": null,
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "scaleDbId": "CO_334:0100526",
                    "name": "ug/g"
                }
            },
            {
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "name": "caro_spectro",
                "trait": {
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "class": "physiological trait",
                    "traitDbId": "CO_334:0100620",
                    "attribute": "carotenoid",
                    "entity": "root",
                    "mainAbbreviation": "CC",
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content"
                },
                "ontologyName": "Cassava",
                "date": "2016-05-13",
                "scientist": "",
                "scale": {
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "xref": null,
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "scaleDbId": "CO_334:0100526",
                    "name": "ug/g"
                },
                "observationVariableDbId": "CO_334:0100622",
                "crop": "Cassava",
                "ontologyDbId": "CO_334",
                "status": "recommended",
                "language": "EN",
                "institution": "",
                "growthStage": "mature",
                "defaultValue": "0",
                "xref": "TL_455:0003001",
                "method": {
                    "reference": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "synonyms": [
                    "Carotenoid content by spectro"
                ]
            }
        ],
        "studyDbId": "35",
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/observationvariables [Get /brapi/v1/studies/{studyDbId}/observationVariables]



<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observationVariables</a> 

+ Parameters
    + studyDbId (Required, string) ... string database unique identifier


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationVariableDbId": "CO_334:0100632",
                "name": "CT_M_C",
                "ontologyDbId": "CO_334",
                "trait": {
                    "name": "Canopy temperature",
                    "traitDbId": "CO_334:0100630"
                },
                "defaultValue": null,
                "ontologyName": "Cassava",
                "method": null,
                "scale": null
            },
            {
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "name": "caro_spectro",
                "trait": {
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "class": "physiological trait",
                    "traitDbId": "CO_334:0100620",
                    "attribute": "carotenoid",
                    "entity": "root",
                    "mainAbbreviation": "CC",
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "description": "Cassava storage root pulp carotenoid content"
                },
                "ontologyName": "Cassava",
                "date": "2016-05-13",
                "scientist": "",
                "scale": {
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    },
                    "xref": null,
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "scaleDbId": "CO_334:0100526",
                    "name": "ug/g"
                },
                "observationVariableDbId": "CO_334:0100622",
                "crop": "Cassava",
                "ontologyDbId": "CO_334",
                "status": "recommended",
                "language": "EN",
                "institution": "",
                "growthStage": "mature",
                "defaultValue": null,
                "xref": "TL_455:0003001",
                "method": {
                    "reference": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "class": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "synonyms": [
                    "Carotenoid content by spectro"
                ]
            }
        ],
        "studyDbId": "123",
        "trialName": "myBestTrial"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/observations [Get /brapi/v1/studies/{studyDbId}/observations{?observationVariableDbIds}{?pageSize}{?page}]


Retrieve all observations where there are measurements for the given observation variables.
observationTimestamp should be ISO8601 format with timezone: YYYY-MM-DDThh:mm:ss+hhmm
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observations</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + observationVariableDbIds (Optional, array) ... Numeric `id` of that variable (combination of trait, unit and method)
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "value": "5",
                "observationUnitDbId": "11",
                "operator": "Jane Doe",
                "germplasmName": "Pahang",
                "studyDbId": "35",
                "observationTimeStamp": "2015-11-05T15:12:56+01:00",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "observationVariableName": "Yield",
                "germplasmDbId": "8383",
                "observationDbId": "12345"
            },
            {
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "value": "22.3",
                "observationUnitDbId": "11",
                "operator": "Jane Doe",
                "germplasmName": "Pahang",
                "studyDbId": "35",
                "observationTimeStamp": "2015-11-05T15:13:56+01:00",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "observationVariableName": "Dry Weight",
                "germplasmDbId": "8383",
                "observationDbId": "23456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/observations [Put /brapi/v1/studies/{studyDbId}/observations]

 Implementation Guidelines: + If an `observationDbId` is "null" or an empty string in the request, a NEW observation should be created for the given study and observationUnit + If an `observationDbId` is populated but not found in the database, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client. + If an `observationDbId` is populated and found in the database, but the existing entry is not associated with the given study or observationUnit, a NEW observation should be created for the given study and observationUnit AND an NEW `observationDbId` should be assigned to it. A warning should be returned to the client. + If an `observationDbId` is populated and found in the database and is associated with the given study and observationUnit, then it should be updated with the new data given.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/observations</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
 
+ Request (application/json)
/definitions/newObservationsRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "value": "5",
                "observationUnitDbId": "11",
                "observationTimestamp": "2015-11-05T15:12:56+01:00",
                "operator": "Jane Doe",
                "germplasmName": "Pahang",
                "studyDbId": "35",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "observationVariableName": "Yield",
                "germplasmDbId": "8383",
                "observationDbId": "12345"
            },
            {
                "observationVariableDbId": "CO_334:0100632",
                "uploadedBy": "dbUserId",
                "value": "22.3",
                "observationUnitDbId": "11",
                "observationTimestamp": "2015-11-05T15:13:56+01:00",
                "operator": "Jane Doe",
                "germplasmName": "Pahang",
                "studyDbId": "35",
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "observationVariableName": "Dry Weight",
                "germplasmDbId": "8383",
                "observationDbId": "23456"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 2
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studies/{studydbid}/table [Get /brapi/v1/studies/{studyDbId}/table{?format}]

 Scope: PHENOTYPING. Status: ACCEPTED. Implemented in Cassavabase, HIDAP and Germinate. Notes: Implementation target date: after PAG2016 Retrieve the details of the study required for field data collection. Includes actual trait data.
<a href="https://test-server.brapi.org/brapi/v1/studies"> test-server.brapi.org/brapi/v1/studies/{studyDbId}/table</a> 

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
    + format (Optional, string) ... The format parameter will cause the data to be dumped to a file in the specified format. Currently, tsv and csv are supported.


+ Response 200 (application/csv)
```
"year,studyDbId,studyName,locationDbId,locationName,germplasmDbId,germplasmName,observationUnitDbId,plotNumber,replicate,blockNumber,observationTimestamp,entryType,X,Y,variable1DbId,variable2DbId,variable3DbId\n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc123,1,1,1,2017-06-16T00:53:26Z,Test Entry,1,2,25.3,103.4,50.75 \n2017,stu1,Study Name,loc1,Location Name,CIP1,CIP Name,abc124,1,1,1,2017-06-16T00:54:57Z,Test Entry,2,2,27.9,98.65,45.345\n"
```+ Response 200 (application/json)
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
        "observationVariableNames": [
            "plant height",
            "fruit weight",
            "root weight"
        ],
        "observationVariableDbIds": [
            "variable1DbId",
            "variable2DbId",
            "variable3DbId"
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
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [],
        "datafiles": []
    }
}
```+ Response 200 (application/tsv)
```
"year\tstudyDbId\tstudyName\tlocationDbId\tlocationName\tgermplasmDbId\tgermplasmName\tobservationUnitDbId\tplotNumber\treplicate\tblockNumber\tobservationTimestamp\tentryType\tX\tY\tvariable1DbId\tvariable2DbId\tvariable3DbId\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc123\t1\t1\t1\t2017-06-16T00:53:26Z\tTest Entry\t1\t2\t25.3\t103.4\t50.75\n 2017\tstu1\tStudy Name\tloc1\tLocation Name\tCIP1\tCIP Name\tabc124\t1\t1\t1\t2017-06-16T00:54:57Z\tTest Entry\t2\t2\t27.9\t98.65\t45.345\n"
```

## Studies/{studydbid}/table [Post /brapi/v1/studies/{studyDbId}/table]

 This call can be used to create new observations in bulk.
Note: If you need to update any existing observation, please use `PUT /studies/{studyDbId}/observations`. This call should only be used to create NEW observations.
Implementation Guidelines:
+ All observations submitted through this call should create NEW observation records in the database under the given observation unit. + Each "observationUnitDbId" listed should already exist in the database. If the server can not find a given "observationUnitDbId", it should report an error. (see Error Handling) + The response of this call should be the set of "observationDbIds" created from this call, along with the associated "observationUnitDbId" and "observationVariableDbId" that each observation is associated with.
Images can optionally be saved using this call by providing a zipped file of all images in the datafiles. The physical zipped file should be transferred as well in the mulit-part form data.
Scope: PHENOTYPING  

+ Parameters
    + studyDbId (Required, string) ... Identifier of the study. Usually a number, could be alphanumeric.
 
+ Request (application/json)
/definitions/newObservationsTableRequest

+ Response 200 (application/json)
```
{
    "result": {
        "observations": [
            {
                "observationVariableDbId": "variable1DbId",
                "observationUnitDbId": "1",
                "observationDbId": "12345"
            },
            {
                "observationVariableDbId": "variable2DbId",
                "observationUnitDbId": "1",
                "observationDbId": "23456"
            },
            {
                "observationVariableDbId": "variable3DbId",
                "observationUnitDbId": "1",
                "observationDbId": "34567"
            },
            {
                "observationVariableDbId": "imagevariable1DbId",
                "observationUnitDbId": "1",
                "observationDbId": "45678"
            },
            {
                "observationVariableDbId": "variable1DbId",
                "observationUnitDbId": "2",
                "observationDbId": "56789"
            },
            {
                "observationVariableDbId": "variable2DbId",
                "observationUnitDbId": "2",
                "observationDbId": "67890"
            },
            {
                "observationVariableDbId": "variable3DbId",
                "observationUnitDbId": "2",
                "observationDbId": "78901"
            },
            {
                "observationVariableDbId": "imagevariable1DbId",
                "observationUnitDbId": "2",
                "observationDbId": "89012"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [],
        "datafiles": []
    }
}
```

## Studytypes [Get /brapi/v1/studytypes{?pageSize}{?page}]

 Call to retrieve the list of study types.
Scope: PHENOTYPING. Implementation target date: PAG2016
<a href="https://test-server.brapi.org/brapi/v1/studytypes"> test-server.brapi.org/brapi/v1/studytypes</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "name": "Crossing Nursery",
                "description": "Description for Nursery study type"
            },
            {
                "name": "Yield Trial",
                "description": "Description for Trial study type"
            },
            {
                "name": "Genotype",
                "description": "Description for Genotyping study type"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 1000,
            "currentPage": 0,
            "totalPages": 1,
            "totalCount": 3
        },
        "status": [],
        "datafiles": []
    }
}
```