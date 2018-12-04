# Group Germplasm
Fun Fact: The plural of germplasm is germplasm (no "s").





## Breedingmethods [/brapi/v1/breedingmethods] 




### Get Breedingmethods by breedingMethodDbId  [GET /brapi/v1/breedingmethods/{breedingMethodDbId}]

Get the details of a specific Breeding Method used to produce Germplasm

 

+ Parameters
    + breedingMethodDbId (Required, ) ... Internal database identifier for a breeding method
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "abbreviation": "MBCR",
        "breedingMethodDbId": "bm1",
        "breedingMethodName": "Male Backcross",
        "description": "Backcross to recover a specific gene.",
        "name": "Male Backcross"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Breedingmethods  [GET /brapi/v1/breedingmethods{?page}{?pageSize}]

Get the list of germplasm breeding methods available in a system.

 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "abbreviation": "MBCR",
                "breedingMethodDbId": "bm1",
                "breedingMethodName": "Male Backcross",
                "description": "Backcross to recover a specific gene.",
                "name": "Male Backcross"
            },
            {
                "abbreviation": "FBCR",
                "breedingMethodDbId": "bm2",
                "breedingMethodName": "Female Backcross",
                "description": "Backcross to recover a specific gene.",
                "name": "Female Backcross"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```



## Germplasm-search [/brapi/v1/germplasm-search] 




### **Deprecated** Get Germplasm-search  [GET /brapi/v1/germplasm-search{?germplasmPUI}{?germplasmDbId}{?germplasmName}{?commonCropName}{?page}{?pageSize}]

DEPRECATED in V1.3 - see GET /germplasm

 

+ Parameters
    + germplasmPUI (Optional, ) ... Permanent unique identifier (DOI, URI, etc.)
    + germplasmDbId (Optional, ) ... Internal database identifier
    + germplasmName (Optional, ) ... Name of the germplasm
    + commonCropName (Optional, ) ... The common crop name related to this germplasm
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A000003",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000003",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000003",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "3",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name003",
                "germplasmPUI": "http://pui.per/accession/A000003",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000002",
                "seedSource": "A000001/A000002",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            },
            {
                "accessionNumber": "A000004",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000004",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000004",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "4",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name004",
                "germplasmPUI": "http://pui.per/accession/A000004",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000003",
                "seedSource": "open pollination",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 4"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            }
        ]
    }
}
```





### **Deprecated** Post Germplasm-search  [POST /brapi/v1/germplasm-search]

DEPRECATED in V1.3 - see POST /search/germplasm

 

+ Parameters


 
+ Request (application/json)
```
{
    "accessionNumbers": [
        "accessionNumbers0",
        "accessionNumbers1"
    ],
    "commonCropNames": [
        "commonCropNames0",
        "commonCropNames1"
    ],
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "germplasmGenus": [
        "germplasmGenus0",
        "germplasmGenus1"
    ],
    "germplasmNames": [
        "germplasmNames0",
        "germplasmNames1"
    ],
    "germplasmPUIs": [
        "germplasmPUIs0",
        "germplasmPUIs1"
    ],
    "germplasmSpecies": [
        "germplasmSpecies0",
        "germplasmSpecies1"
    ],
    "page": 0,
    "pageSize": 0
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A000003",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000003",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000003",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "3",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name003",
                "germplasmPUI": "http://pui.per/accession/A000003",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000002",
                "seedSource": "A000001/A000002",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            },
            {
                "accessionNumber": "A000004",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000004",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000004",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "4",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name004",
                "germplasmPUI": "http://pui.per/accession/A000004",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000003",
                "seedSource": "open pollination",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 4"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            }
        ]
    }
}
```



## Germplasm [/brapi/v1/germplasm] 




### Get Germplasm  [GET /brapi/v1/germplasm{?germplasmPUI}{?germplasmDbId}{?germplasmName}{?commonCropName}{?page}{?pageSize}]

Addresses these needs

- General germplasm search mechanism that accepts POST for complex queries 

- Possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

- Possibility to get MCPD details by PUID rather than dbId

 

+ Parameters
    + germplasmPUI (Optional, ) ... Permanent unique identifier (DOI, URI, etc.)
    + germplasmDbId (Optional, ) ... Internal database identifier
    + germplasmName (Optional, ) ... Name of the germplasm
    + commonCropName (Optional, ) ... The common crop name related to this germplasm
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A000003",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000003",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000003",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "3",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name003",
                "germplasmPUI": "http://pui.per/accession/A000003",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000002",
                "seedSource": "A000001/A000002",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            },
            {
                "accessionNumber": "A000004",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000004",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000004",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "4",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name004",
                "germplasmPUI": "http://pui.per/accession/A000004",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000003",
                "seedSource": "open pollination",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 4"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Germplasm Attributes by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/attributes{?attributeDbIds}{?attributeList}{?page}{?pageSize}]

Values for all attributes by default.

 

+ Parameters
    + germplasmDbId (Required, ) ... The germplasm characterized
    + attributeDbIds (Optional, ) ... Restrict the response to only the listed attributeDbIds.
    + attributeList (Optional, ) ... **Deprecated** Use "attributeDbIds" instead
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 5,
            "totalPages": 3
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "attributeCode": "RHT",
                "attributeDbId": "ATT01",
                "attributeName": "Rht-B1b",
                "determinedDate": "2017-03-17",
                "value": "Heterozygous"
            },
            {
                "attributeCode": "WEV",
                "attributeDbId": "ATT02",
                "attributeName": "Weevil Resistance",
                "determinedDate": "2017-03-17",
                "value": "Present"
            }
        ],
        "germplasmDbId": "3"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Germplasm by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}]

Germplasm Details by germplasmDbId was merged with Germplasm Multi Crop Passport Data. The MCPD fields are optional and marked with the prefix [MCPD].

 

+ Parameters
    + germplasmDbId (Required, ) ... The internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "accessionNumber": "A000003",
        "acquisitionDate": "2001-01-01",
        "biologicalStatusOfAccessionCode": 500,
        "breedingMethodDbId": "bm1",
        "commonCropName": "G000003",
        "countryOfOriginCode": "COUNTRY1",
        "defaultDisplayName": "G000003",
        "documentationURL": "https://brapi.org",
        "donors": [],
        "genus": "Fructus",
        "germplasmDbId": "3",
        "germplasmGenus": "Fructus",
        "germplasmName": "Name003",
        "germplasmPUI": "http://pui.per/accession/A000003",
        "germplasmSpecies": "novus",
        "instituteCode": "PER001",
        "instituteName": "INST1",
        "pedigree": "A000001/A000002",
        "seedSource": "A000001/A000002",
        "species": "novus",
        "speciesAuthority": "L",
        "subtaxa": "subtaxa",
        "subtaxaAuthority": "N",
        "synonyms": [
            "variety 1"
        ],
        "taxonIds": [
            {
                "sourceName": "ncbiTaxon",
                "taxonId": "2340"
            },
            {
                "sourceName": "ciradTaxon",
                "taxonId": "E312"
            }
        ],
        "typeOfGermplasmStorageCode": []
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Germplasm Mcpd by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/mcpd]

Get all MCPD details of a germplasm

<a target="_blank" href="https://www.bioversityinternational.org/fileadmin/user_upload/online_library/publications/pdfs/FAOBIOVERSITY_MULTI-CROP_PASSPORT_DESCRIPTORS_V.2.1_2015_2020.pdf"> MCPD v2.1 spec can be found here </a>

Implementation Notes

- When the MCPD spec identifies a field which can have multiple values returned, the JSON response should be an array instead of a semi-colon seperated string.

 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "accessionNames": [
            "Name003"
        ],
        "accessionNumber": "A000003",
        "acquisitionDate": "2001-01-01",
        "acquisitionSourceCode": "11",
        "alternateIDs": [
            "3",
            "http://pui.per/accession/A000003",
            "A000003"
        ],
        "ancestralData": "A000001/A000002",
        "biologicalStatusOfAccessionCode": "500",
        "breedingInstitutes": [
            {
                "instituteCode": "PER001",
                "instituteName": "INST1"
            }
        ],
        "collectingInfo": {
            "collectingDate": "2001-01-01",
            "collectingInstitutes": [
                {
                    "instituteAddress": "INST1",
                    "instituteCode": "PER001",
                    "instituteName": "INST1"
                }
            ],
            "collectingMissionIdentifier": "3",
            "collectingNumber": "A000003",
            "collectingSite": {
                "coordinateUncertainty": "20m",
                "elevation": "20m",
                "georeferencingMethod": "WGS84",
                "latitudeDecimal": "+42.445295",
                "latitudeDegrees": "42 26 43.1 N",
                "locationDescription": "INST1",
                "longitudeDecimal": "-076.471934",
                "longitudeDegrees": "76 28 19.0 W",
                "spatialReferenceSystem": "WGS84"
            }
        },
        "commonCropName": "G000003",
        "countryOfOrigin": "COUNTRY1",
        "donorInfo": {
            "donorAccessionNumber": "A000003",
            "donorInstitute": {
                "instituteCode": "PER001",
                "instituteName": "INST1"
            }
        },
        "genus": "Fructus",
        "germplasmDbId": "3",
        "germplasmPUI": "http://pui.per/accession/A000003",
        "instituteCode": "PER001",
        "mlsStatus": "0",
        "remarks": "G000003",
        "safetyDuplicateInstitues": [
            {
                "instituteCode": "PER001",
                "instituteName": "INST1"
            }
        ],
        "species": "novus",
        "speciesAuthority": "L",
        "storageTypeCodes": [],
        "subtaxon": "subtaxa",
        "subtaxonAuthority": "N"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Germplasm Markerprofiles by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/markerprofiles]

Retrieve the markerProfileDbIds for a given Germplasm ID

 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "germplasmDbId": "3",
        "markerProfileDbIds": [
            "G3-P2"
        ],
        "markerprofileDbIds": [
            "G3-P2"
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Germplasm Pedigree by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/pedigree{?notation}{?includeSiblings}]

Get the parentage information of a specific Germplasm

 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + notation (Optional, ) ... text representation of the pedigree
    + includeSiblings (Optional, ) ... include array of siblings in response
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "crossingPlan": "OPEN_POLLINATION",
        "crossingYear": "2018",
        "defaultDisplayName": "G000003",
        "familyCode": "Cree_x_Bonanza_2018",
        "germplasmDbId": "3",
        "parent1DbId": "1",
        "parent1Id": "1",
        "parent1Name": "G000001",
        "parent1Type": "FEMALE",
        "parent2DbId": "2",
        "parent2Id": "2",
        "parent2Name": "G000002",
        "parent2Type": "MALE",
        "pedigree": "A000001/A000002",
        "siblings": []
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```





### Get Germplasm Progeny by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/progeny]

Get the germplasmDbIds for all the Progeny of a particular germplasm.

Implementation Notes

- Regarding the 'parentType' field in the progeny object. Given a germplasm A having a progeny B and C, 'parentType' for progeny B refers to the 'parentType' of A toward B.

 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "defaultDisplayName": "G000002",
        "germplasmDbId": "3",
        "progeny": [
            {
                "defaultDisplayName": "G000004",
                "germplasmDbId": "4",
                "parentType": "MALE"
            },
            {
                "defaultDisplayName": "G000005",
                "germplasmDbId": "5",
                "parentType": "MALE"
            },
            {
                "defaultDisplayName": "G000006",
                "germplasmDbId": "6",
                "parentType": "MALE"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```



## Search [/brapi/v1/search] 




### Post Search Germplasm  [POST /brapi/v1/search/germplasm]

Search for a set of germplasm based on some criteria

Addresses these needs 

- General germplasm search mechanism that accepts POST for complex queries 

- Possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

- Possibility to get MCPD details by PUID rather than dbId

See Search Services for additional implementation details.

 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accessionNumbers": [
        "accessionNumbers0",
        "accessionNumbers1"
    ],
    "commonCropNames": [
        "commonCropNames0",
        "commonCropNames1"
    ],
    "germplasmDbIds": [
        "germplasmDbIds0",
        "germplasmDbIds1"
    ],
    "germplasmGenus": [
        "germplasmGenus0",
        "germplasmGenus1"
    ],
    "germplasmNames": [
        "germplasmNames0",
        "germplasmNames1"
    ],
    "germplasmPUIs": [
        "germplasmPUIs0",
        "germplasmPUIs1"
    ],
    "germplasmSpecies": [
        "germplasmSpecies0",
        "germplasmSpecies1"
    ],
    "page": 0,
    "pageSize": 0
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "result": {
        "searchResultDbId": "551ae08c-4548-4bde-ad70-f23beb25e2ea"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```





### Get Search Germplasm by searchResultsDbId  [GET /brapi/v1/search/germplasm/{searchResultsDbId}{?page}{?pageSize}]

See Search Services for additional implementation details.
Addresses these needs: 1. General germplasm search mechanism that accepts POST for complex queries 2. possibility to search germplasm by more parameters than those allowed by the existing germplasm search 3. possibility to get MCPD details by PUID rather than dbId

 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization 

<strong>Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 2,
            "totalCount": 2,
            "totalPages": 1
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A000003",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000003",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000003",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "3",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name003",
                "germplasmPUI": "http://pui.per/accession/A000003",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000002",
                "seedSource": "A000001/A000002",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            },
            {
                "accessionNumber": "A000004",
                "acquisitionDate": "2001-01-01",
                "biologicalStatusOfAccessionCode": 500,
                "breedingMethodDbId": "bm1",
                "commonCropName": "G000004",
                "countryOfOriginCode": "COUNTRY1",
                "defaultDisplayName": "G000004",
                "documentationURL": "https://brapi.org",
                "donors": [],
                "genus": "Fructus",
                "germplasmDbId": "4",
                "germplasmGenus": "Fructus",
                "germplasmName": "Name004",
                "germplasmPUI": "http://pui.per/accession/A000004",
                "germplasmSpecies": "novus",
                "instituteCode": "PER001",
                "instituteName": "INST1",
                "pedigree": "A000001/A000003",
                "seedSource": "open pollination",
                "species": "novus",
                "speciesAuthority": "L",
                "subtaxa": "subtaxa",
                "subtaxaAuthority": "N",
                "synonyms": [
                    "variety 4"
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "2340"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "E312"
                    }
                ],
                "typeOfGermplasmStorageCode": []
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Malformed JSON Request Object\nERROR - 2018-10-08T20:15:11Z - Invalid query parameter\nERROR - 2018-10-08T20:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T20:15:11Z - The requested object DbId is not found"
```

