# Group Germplasm
Fun Fact: The plural of germplasm is germplasm (no "s").





## Search [/brapi/v1/search] 




### Post Search Germplasm  [POST /brapi/v1/search/germplasm]

Search for a set of germplasm based on some criteria

Addresses these needs 

- General germplasm search mechanism that accepts POST for complex queries 

- Possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

- Possibility to get MCPD details by PUID rather than dbId

See Search Services for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm|
|commonCropNames|array[string]|List crops to search by|
|accessionNumbers|array[string]|List unique identifiers for accessions within a genebank|
|studyDbIds|array[string]|Search for Germplasm that are associated with a particular Study|
|parentDbIds|array[string]|Search for Germplasm with these parents|
|germplasmSpecies|array[string]|List of Species names to identify germplasm|
|germplasmGenus|array[string]|List of Genus names to identify germplasm|
|germplasmPUIs|array[string]|List of Permanent Unique Identifiers to identify germplasm|
|germplasmNames|array[string]|List of human readable names to identify germplasm|
|progenyDbIds|array[string]|Search for Germplasm with these children|
|xrefs|array[string]|Search for Germplasm by an external reference|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accessionNumbers": [
        "accessionNumbers1",
        "accessionNumbers2"
    ],
    "commonCropNames": [
        "commonCropNames1",
        "commonCropNames2"
    ],
    "germplasmDbIds": [
        "germplasmDbIds1",
        "germplasmDbIds2"
    ],
    "germplasmGenus": [
        "germplasmGenus1",
        "germplasmGenus2"
    ],
    "germplasmNames": [
        "germplasmNames1",
        "germplasmNames2"
    ],
    "germplasmPUIs": [
        "germplasmPUIs1",
        "germplasmPUIs2"
    ],
    "germplasmSpecies": [
        "germplasmSpecies1",
        "germplasmSpecies2"
    ],
    "parentDbIds": [
        "parentDbIds1",
        "parentDbIds2"
    ],
    "progenyDbIds": [
        "progenyDbIds1",
        "progenyDbIds2"
    ],
    "studyDbIds": [
        "studyDbIds1",
        "studyDbIds2"
    ],
    "xrefs": [
        "xrefs1",
        "xrefs2"
    ]
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "searchResultDbId": "551ae08c"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Search Germplasm by searchResultsDbId  [GET /brapi/v1/search/germplasm/{searchResultsDbId}{?page}{?pageSize}]

See Search Services for additional implementation details.

Addresses these needs: 

1. General germplasm search mechanism that accepts POST for complex queries 

2. possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

3. possibility to get MCPD details by PUID rather than dbId



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|commonCropName|string|Common name for the crop (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|donors|array[object]|List of donor institutes (MCPD)|
|germplasmPUI|string||
|donorInstituteCode|string||
|donorAccessionNumber|string||
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|pedigree|string|The cross name and optional selection history.|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|seedSource|string|The source of the seed |
|xref|string|External reference to another system|
|seedSourceDescription|string|Description of the material source|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|longitudeDecimal|string|Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|latitudeDegrees|string|Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|altitude|string|Elevation of collecting site expressed in meters above sea level. Negative values are allowed.|
|latitudeDecimal|string|Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|additionalInfo|object|Additional arbitrary info|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Permanent unique identifier which references the search results
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A0000003",
                "acquisitionDate": "2018-01-01",
                "additionalInfo": {},
                "biologicalStatusOfAccessionCode": "421",
                "breedingMethodDbId": "ffcce7ef",
                "commonCropName": "Maize",
                "countryOfOriginCode": "BES",
                "defaultDisplayName": "A0000003",
                "documentationURL": "https://wiki.brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A0000123",
                        "donorInstituteCode": "PER001",
                        "germplasmPUI": "http://pui.per/accession/A0000003"
                    }
                ],
                "germplasmDbId": "d4076594",
                "germplasmGenus": "Aspergillus",
                "germplasmName": "A0000003",
                "germplasmOrigin": [
                    {
                        "altitude": "35",
                        "coordinateUncertainty": "20",
                        "latitudeDecimal": "-44.6975",
                        "latitudeDegrees": "103020S",
                        "longitudeDecimal": "+120.9123",
                        "longitudeDegrees": "0762510W"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
                "germplasmSpecies": "fructus",
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute",
                "pedigree": "A0000001/A0000002",
                "seedSource": "A0000001/A0000002",
                "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
                "speciesAuthority": "Smith, 1822",
                "subtaxa": "Aspergillus fructus A",
                "subtaxaAuthority": "Smith, 1822",
                "synonyms": [
                    "variety_1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "sourceName",
                        "taxonId": "taxonId"
                    }
                ],
                "typeOfGermplasmStorageCode": [
                    "10",
                    "11"
                ],
                "xref": "http://pui.per/accession/A0000079"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```



## Breedingmethods [/brapi/v1/breedingmethods] 




### Get Breedingmethods by breedingMethodDbId  [GET /brapi/v1/breedingmethods/{breedingMethodDbId}]

Get the details of a specific Breeding Method used to produce Germplasm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviation|string|an abbreviation for the name of this breeding method|
|breedingMethodName|string|human readable name of the breeding method|
|description|string|human readable description of the breeding method|
|breedingMethodDbId|string|the unique identifier for this breeding method|


 

+ Parameters
    + breedingMethodDbId (Required, ) ... Internal database identifier for a breeding method
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "abbreviation": "MB",
        "breedingMethodDbId": "ffcce7ef",
        "breedingMethodName": "Male Backcross",
        "description": "Backcross to recover a specific gene."
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Get Breedingmethods  [GET /brapi/v1/breedingmethods{?page}{?pageSize}]

Get the list of germplasm breeding methods available in a system.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|abbreviation|string|an abbreviation for the name of this breeding method|
|breedingMethodName|string|human readable name of the breeding method|
|description|string|human readable description of the breeding method|
|breedingMethodDbId|string|the unique identifier for this breeding method|


 

+ Parameters
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "abbreviation": "MB",
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "description": "Backcross to recover a specific gene."
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```



## Germplasm [/brapi/v1/germplasm] 




### Get Germplasm  [GET /brapi/v1/germplasm{?germplasmPUI}{?germplasmDbId}{?germplasmName}{?commonCropName}{?accessionNumber}{?germplasmGenus}{?germplasmSpecies}{?studyDbIds}{?parentDbId}{?progenyDbId}{?xref}{?page}{?pageSize}]

Addresses these needs

- General germplasm search mechanism that accepts POST for complex queries 

- Possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

- Possibility to get MCPD details by PUID rather than dbId



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|commonCropName|string|Common name for the crop (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|donors|array[object]|List of donor institutes (MCPD)|
|germplasmPUI|string||
|donorInstituteCode|string||
|donorAccessionNumber|string||
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|pedigree|string|The cross name and optional selection history.|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|seedSource|string|The source of the seed |
|xref|string|External reference to another system|
|seedSourceDescription|string|Description of the material source|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|longitudeDecimal|string|Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|latitudeDegrees|string|Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|altitude|string|Elevation of collecting site expressed in meters above sea level. Negative values are allowed.|
|latitudeDecimal|string|Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|additionalInfo|object|Additional arbitrary info|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|


 

+ Parameters
    + germplasmPUI (Optional, ) ... Permanent unique identifier (DOI, URI, etc.)
    + germplasmDbId (Optional, ) ... Internal database identifier
    + germplasmName (Optional, ) ... Name of the germplasm
    + commonCropName (Optional, ) ... The common crop name related to this germplasm
    + accessionNumber (Optional, ) ... Unique identifiers for accessions within a genebank
    + germplasmGenus (Optional, ) ... Genus name to identify germplasm
    + germplasmSpecies (Optional, ) ... Species name to identify germplasm
    + studyDbIds (Optional, ) ... Search for Germplasm that are associated with a particular Study
    + parentDbId (Optional, ) ... Search for Germplasm with this parent
    + progenyDbId (Optional, ) ... Search for Germplasm with this child
    + xref (Optional, ) ... Search for Germplasm by an external reference
    + page (Optional, ) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A0000003",
                "acquisitionDate": "2018-01-01",
                "additionalInfo": {},
                "biologicalStatusOfAccessionCode": "421",
                "breedingMethodDbId": "ffcce7ef",
                "commonCropName": "Maize",
                "countryOfOriginCode": "BES",
                "defaultDisplayName": "A0000003",
                "documentationURL": "https://wiki.brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A0000123",
                        "donorInstituteCode": "PER001",
                        "germplasmPUI": "http://pui.per/accession/A0000003"
                    }
                ],
                "germplasmDbId": "d4076594",
                "germplasmGenus": "Aspergillus",
                "germplasmName": "A0000003",
                "germplasmOrigin": [
                    {
                        "altitude": "35",
                        "coordinateUncertainty": "20",
                        "latitudeDecimal": "-44.6975",
                        "latitudeDegrees": "103020S",
                        "longitudeDecimal": "+120.9123",
                        "longitudeDegrees": "0762510W"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
                "germplasmSpecies": "fructus",
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute",
                "pedigree": "A0000001/A0000002",
                "seedSource": "A0000001/A0000002",
                "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
                "speciesAuthority": "Smith, 1822",
                "subtaxa": "Aspergillus fructus A",
                "subtaxaAuthority": "Smith, 1822",
                "synonyms": [
                    "variety_1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "sourceName",
                        "taxonId": "taxonId"
                    }
                ],
                "typeOfGermplasmStorageCode": [
                    "10",
                    "11"
                ],
                "xref": "http://pui.per/accession/A0000079"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Post Germplasm  [POST /brapi/v1/germplasm]

Addresses these needs

- General germplasm search mechanism that accepts POST for complex queries 

- Possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

- Possibility to get MCPD details by PUID rather than dbId

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|Common name for the crop (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|donors|array[object]|List of donor institutes (MCPD)|
|germplasmPUI|string||
|donorInstituteCode|string||
|donorAccessionNumber|string||
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|pedigree|string|The cross name and optional selection history.|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank (MCPD)|
|seedSource|string|The source of the seed |
|xref|string|External reference to another system|
|seedSourceDescription|string|Description of the material source|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|longitudeDecimal|string|Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|latitudeDegrees|string|Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|altitude|string|Elevation of collecting site expressed in meters above sea level. Negative values are allowed.|
|latitudeDecimal|string|Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|additionalInfo|object|Additional arbitrary info|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|commonCropName|string|Common name for the crop (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|donors|array[object]|List of donor institutes (MCPD)|
|germplasmPUI|string||
|donorInstituteCode|string||
|donorAccessionNumber|string||
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|pedigree|string|The cross name and optional selection history.|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|seedSource|string|The source of the seed |
|xref|string|External reference to another system|
|seedSourceDescription|string|Description of the material source|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|longitudeDecimal|string|Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|latitudeDegrees|string|Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|altitude|string|Elevation of collecting site expressed in meters above sea level. Negative values are allowed.|
|latitudeDecimal|string|Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|additionalInfo|object|Additional arbitrary info|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "accessionNumber": "A0000003",
        "acquisitionDate": "2018-01-01",
        "additionalInfo": {},
        "biologicalStatusOfAccessionCode": "421",
        "breedingMethodDbId": "ffcce7ef",
        "commonCropName": "Maize",
        "countryOfOriginCode": "BES",
        "defaultDisplayName": "A0000003",
        "documentationURL": "https://wiki.brapi.org",
        "donors": [
            {
                "donorAccessionNumber": "A0000123",
                "donorInstituteCode": "PER001",
                "germplasmPUI": "http://pui.per/accession/A0000003"
            }
        ],
        "germplasmGenus": "Aspergillus",
        "germplasmName": "A0000003",
        "germplasmOrigin": [
            {
                "altitude": "35",
                "coordinateUncertainty": "20",
                "latitudeDecimal": "-44.6975",
                "latitudeDegrees": "103020S",
                "longitudeDecimal": "+120.9123",
                "longitudeDegrees": "0762510W"
            }
        ],
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
        "germplasmSpecies": "fructus",
        "instituteCode": "PER001",
        "instituteName": "The BrAPI Institute",
        "pedigree": "A0000001/A0000002",
        "seedSource": "A0000001/A0000002",
        "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
        "speciesAuthority": "Smith, 1822",
        "subtaxa": "Aspergillus fructus A",
        "subtaxaAuthority": "Smith, 1822",
        "synonyms": [
            "variety_1"
        ],
        "taxonIds": [
            {
                "sourceName": "sourceName",
                "taxonId": "taxonId"
            }
        ],
        "typeOfGermplasmStorageCode": [
            "10",
            "11"
        ],
        "xref": "http://pui.per/accession/A0000079"
    }
]
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "data": [
            {
                "accessionNumber": "A0000003",
                "acquisitionDate": "2018-01-01",
                "additionalInfo": {},
                "biologicalStatusOfAccessionCode": "421",
                "breedingMethodDbId": "ffcce7ef",
                "commonCropName": "Maize",
                "countryOfOriginCode": "BES",
                "defaultDisplayName": "A0000003",
                "documentationURL": "https://wiki.brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A0000123",
                        "donorInstituteCode": "PER001",
                        "germplasmPUI": "http://pui.per/accession/A0000003"
                    }
                ],
                "germplasmDbId": "d4076594",
                "germplasmGenus": "Aspergillus",
                "germplasmName": "A0000003",
                "germplasmOrigin": [
                    {
                        "altitude": "35",
                        "coordinateUncertainty": "20",
                        "latitudeDecimal": "-44.6975",
                        "latitudeDegrees": "103020S",
                        "longitudeDecimal": "+120.9123",
                        "longitudeDegrees": "0762510W"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
                "germplasmSpecies": "fructus",
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute",
                "pedigree": "A0000001/A0000002",
                "seedSource": "A0000001/A0000002",
                "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
                "speciesAuthority": "Smith, 1822",
                "subtaxa": "Aspergillus fructus A",
                "subtaxaAuthority": "Smith, 1822",
                "synonyms": [
                    "variety_1"
                ],
                "taxonIds": [
                    {
                        "sourceName": "sourceName",
                        "taxonId": "taxonId"
                    }
                ],
                "typeOfGermplasmStorageCode": [
                    "10",
                    "11"
                ],
                "xref": "http://pui.per/accession/A0000079"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```





### Get Germplasm by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}]

Germplasm Details by germplasmDbId was merged with Germplasm Multi Crop Passport Data. The MCPD fields are optional and marked with the prefix [MCPD].



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|Common name for the crop (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|donors|array[object]|List of donor institutes (MCPD)|
|germplasmPUI|string||
|donorInstituteCode|string||
|donorAccessionNumber|string||
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|pedigree|string|The cross name and optional selection history.|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|seedSource|string|The source of the seed |
|xref|string|External reference to another system|
|seedSourceDescription|string|Description of the material source|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|longitudeDecimal|string|Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|latitudeDegrees|string|Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|altitude|string|Elevation of collecting site expressed in meters above sea level. Negative values are allowed.|
|latitudeDecimal|string|Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|additionalInfo|object|Additional arbitrary info|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|


 

+ Parameters
    + germplasmDbId (Required, ) ... The internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "accessionNumber": "A0000003",
        "acquisitionDate": "2018-01-01",
        "additionalInfo": {},
        "biologicalStatusOfAccessionCode": "421",
        "breedingMethodDbId": "ffcce7ef",
        "commonCropName": "Maize",
        "countryOfOriginCode": "BES",
        "defaultDisplayName": "A0000003",
        "documentationURL": "https://wiki.brapi.org",
        "donors": [
            {
                "donorAccessionNumber": "A0000123",
                "donorInstituteCode": "PER001",
                "germplasmPUI": "http://pui.per/accession/A0000003"
            }
        ],
        "germplasmDbId": "d4076594",
        "germplasmGenus": "Aspergillus",
        "germplasmName": "A0000003",
        "germplasmOrigin": [
            {
                "altitude": "35",
                "coordinateUncertainty": "20",
                "latitudeDecimal": "-44.6975",
                "latitudeDegrees": "103020S",
                "longitudeDecimal": "+120.9123",
                "longitudeDegrees": "0762510W"
            }
        ],
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
        "germplasmSpecies": "fructus",
        "instituteCode": "PER001",
        "instituteName": "The BrAPI Institute",
        "pedigree": "A0000001/A0000002",
        "seedSource": "A0000001/A0000002",
        "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
        "speciesAuthority": "Smith, 1822",
        "subtaxa": "Aspergillus fructus A",
        "subtaxaAuthority": "Smith, 1822",
        "synonyms": [
            "variety_1"
        ],
        "taxonIds": [
            {
                "sourceName": "sourceName",
                "taxonId": "taxonId"
            }
        ],
        "typeOfGermplasmStorageCode": [
            "10",
            "11"
        ],
        "xref": "http://pui.per/accession/A0000079"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Put Germplasm by germplasmDbId  [PUT /brapi/v1/germplasm/{germplasmDbId}]

Germplasm Details by germplasmDbId was merged with Germplasm Multi Crop Passport Data. The MCPD fields are optional and marked with the prefix [MCPD].

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|Common name for the crop (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|donors|array[object]|List of donor institutes (MCPD)|
|germplasmPUI|string||
|donorInstituteCode|string||
|donorAccessionNumber|string||
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|pedigree|string|The cross name and optional selection history.|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank (MCPD)|
|seedSource|string|The source of the seed |
|xref|string|External reference to another system|
|seedSourceDescription|string|Description of the material source|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|longitudeDecimal|string|Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|latitudeDegrees|string|Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|altitude|string|Elevation of collecting site expressed in meters above sea level. Negative values are allowed.|
|latitudeDecimal|string|Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|additionalInfo|object|Additional arbitrary info|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|Common name for the crop (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|donors|array[object]|List of donor institutes (MCPD)|
|germplasmPUI|string||
|donorInstituteCode|string||
|donorAccessionNumber|string||
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|pedigree|string|The cross name and optional selection history.|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.|
|seedSource|string|The source of the seed |
|xref|string|External reference to another system|
|seedSourceDescription|string|Description of the material source|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|longitudeDecimal|string|Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|latitudeDegrees|string|Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|altitude|string|Elevation of collecting site expressed in meters above sea level. Negative values are allowed.|
|latitudeDecimal|string|Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|additionalInfo|object|Additional arbitrary info|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|


 

+ Parameters
    + germplasmDbId (Required, ) ... The internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accessionNumber": "A0000003",
    "acquisitionDate": "2018-01-01",
    "additionalInfo": {},
    "biologicalStatusOfAccessionCode": "421",
    "breedingMethodDbId": "ffcce7ef",
    "commonCropName": "Maize",
    "countryOfOriginCode": "BES",
    "defaultDisplayName": "A0000003",
    "documentationURL": "https://wiki.brapi.org",
    "donors": [
        {
            "donorAccessionNumber": "A0000123",
            "donorInstituteCode": "PER001",
            "germplasmPUI": "http://pui.per/accession/A0000003"
        }
    ],
    "germplasmGenus": "Aspergillus",
    "germplasmName": "A0000003",
    "germplasmOrigin": [
        {
            "altitude": "35",
            "coordinateUncertainty": "20",
            "latitudeDecimal": "-44.6975",
            "latitudeDegrees": "103020S",
            "longitudeDecimal": "+120.9123",
            "longitudeDegrees": "0762510W"
        }
    ],
    "germplasmPUI": "http://pui.per/accession/A0000003",
    "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
    "germplasmSpecies": "fructus",
    "instituteCode": "PER001",
    "instituteName": "The BrAPI Institute",
    "pedigree": "A0000001/A0000002",
    "seedSource": "A0000001/A0000002",
    "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
    "speciesAuthority": "Smith, 1822",
    "subtaxa": "Aspergillus fructus A",
    "subtaxaAuthority": "Smith, 1822",
    "synonyms": [
        "variety_1"
    ],
    "taxonIds": [
        {
            "sourceName": "sourceName",
            "taxonId": "taxonId"
        }
    ],
    "typeOfGermplasmStorageCode": [
        "10",
        "11"
    ],
    "xref": "http://pui.per/accession/A0000079"
}
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "accessionNumber": "A0000003",
        "acquisitionDate": "2018-01-01",
        "additionalInfo": {},
        "biologicalStatusOfAccessionCode": "421",
        "breedingMethodDbId": "ffcce7ef",
        "commonCropName": "Maize",
        "countryOfOriginCode": "BES",
        "defaultDisplayName": "A0000003",
        "documentationURL": "https://wiki.brapi.org",
        "donors": [
            {
                "donorAccessionNumber": "A0000123",
                "donorInstituteCode": "PER001",
                "germplasmPUI": "http://pui.per/accession/A0000003"
            }
        ],
        "germplasmDbId": "d4076594",
        "germplasmGenus": "Aspergillus",
        "germplasmName": "A0000003",
        "germplasmOrigin": [
            {
                "altitude": "35",
                "coordinateUncertainty": "20",
                "latitudeDecimal": "-44.6975",
                "latitudeDegrees": "103020S",
                "longitudeDecimal": "+120.9123",
                "longitudeDegrees": "0762510W"
            }
        ],
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
        "germplasmSpecies": "fructus",
        "instituteCode": "PER001",
        "instituteName": "The BrAPI Institute",
        "pedigree": "A0000001/A0000002",
        "seedSource": "A0000001/A0000002",
        "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
        "speciesAuthority": "Smith, 1822",
        "subtaxa": "Aspergillus fructus A",
        "subtaxaAuthority": "Smith, 1822",
        "synonyms": [
            "variety_1"
        ],
        "taxonIds": [
            {
                "sourceName": "sourceName",
                "taxonId": "taxonId"
            }
        ],
        "typeOfGermplasmStorageCode": [
            "10",
            "11"
        ],
        "xref": "http://pui.per/accession/A0000079"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Get Germplasm Mcpd by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/mcpd]

Get all MCPD details of a germplasm

<a target="_blank" href="https://www.bioversityinternational.org/fileadmin/user_upload/online_library/publications/pdfs/FAOBIOVERSITY_MULTI-CROP_PASSPORT_DESCRIPTORS_V.2.1_2015_2020.pdf"> MCPD v2.1 spec can be found here </a>

Implementation Notes

- When the MCPD spec identifies a field which can have multiple values returned, the JSON response should be an array instead of a semi-colon separated string.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|commonCropName|string|MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "macadamia", "mas". |
|safetyDuplicateInstitutes|array[object]||
|instituteCode|string|MCPD (v2.1) (DUPLSITE) 25. FAO WIEWS code of the institute(s) where a safety duplicate of the accession is maintained. Follows INSTCODE standard.|
|instituteName|string|MCPD (v2.1) (DUPLINSTNAME) 25.1  Name of the institute where a safety duplicate of the accession is maintained.|
|subtaxon|string|MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").|
|collectingInfo|object|Information about the collection of this germplasm|
|collectingInstitutes|array[object]|Institutes which collected the sample|
|instituteAddress|string|MCPD (v2.1) (COLLINSTADDRESS) 4.1.1  Address of the institute collecting the sample. This descriptor should be used only if COLLCODE cannot be filled since the FAO WIEWS code for this institute is not available. Multiple values are separated by a semicolon without space.|
|instituteCode|string|MCPD (v2.1) (COLLCODE) 4.  FAO WIEWS code of the institute collecting the sample. If the holding institute has collected the material, the collecting institute code (COLLCODE) should be the same as the holding institute code (INSTCODE). Follows INSTCODE standard. Multiple values are separated by a semicolon without space.|
|instituteName|string|MCPD (v2.1) (COLLNAME) 4.1  Name of the institute collecting the sample. This descriptor should be used only if COLLCODE cannot be filled because the FAO WIEWS code for this institute is not available. Multiple values are separated by a semicolon without space.|
|collectingDate|string (date)|MCPD (v2.1) (COLLDATE) 17. Collecting date of the sample [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|collectingMissionIdentifier|string|MCPD (v2.1) (COLLMISSID) 4.2 Identifier of the collecting mission used by the Collecting Institute (4 or 4.1) (e.g. "CIATFOR052", "CN426").|
|collectingNumber|string|MCPD (v2.1) (COLLNUMB) 3. Original identifier assigned by the collector(s) of the sample, normally composed of the name or initials of the collector(s) followed by a number (e.g. "AB009909"). This identifier is essential for identifying duplicates held in different collections.|
|collectingSite|object|Information about the location where the sample was collected|
|longitudeDegrees|string|MCPD (v2.1) (LONGITUDE) 15.4 Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|latitudeDegrees|string|MCPD (v2.1) (LATITUDE) 15.2 Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|elevation|string|MCPD (v2.1) (ELEVATION) 16. Elevation of collecting site expressed in metres above sea level. Negative values are allowed.|
|locationDescription|string|MCPD (v2.1) (COLLSITE) 14. Location information below the country level that describes where the accession was collected, preferable in English. This might include the distance in kilometres and direction from the nearest town, village or map grid reference point, (e.g. 7 km south of Curitiba in the state of Parana).|
|latitudeDecimal|string|MCPD (v2.1) (DECLATITUDE) 15.1 Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|spatialReferenceSystem|string|MCPD (v2.1) (COORDDATUM) 15.6 The geodetic datum or spatial reference system upon which the coordinates given in decimal latitude and decimal longitude are based (e.g. WGS84, ETRS89, NAD83). The GPS uses the WGS84 datum.|
|longitudeDecimal|string|MCPD (v2.1) (DECLONGITUDE) 15.3 Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|coordinateUncertainty|string|MCPD (v2.1) (COORDUNCERT) 15.5 Uncertainty associated with the coordinates in metres. Leave the value empty if the uncertainty is unknown.|
|georeferencingMethod|string|MCPD (v2.1) (GEOREFMETH) 15.7  The georeferencing method used (GPS, determined from map, gazetteer, or estimated using software). Leave the value empty if georeferencing method is not known.|
|subtaxonAuthority|string|MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|germplasmPUI|string|MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level (http://www.planttreaty.org/doi). Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties (e.g. NOR017:NGB17773:ALLIUM).|
|alternateIDs|array[string]|MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon. |
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|acquisitionDate|string (date)|MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|breedingInstitutes|array[object]||
|instituteCode|string|MCPD (v2.1) (BREDCODE) 18. FAO WIEWS code of the institute that has bred the material. If the holding institute has bred the material, the breeding institute code (BREDCODE) should be the same as the holding institute code (INSTCODE). Follows INSTCODE standard. Multiple values are separated by a semicolon without space.|
|instituteName|string|MCPD (v2.1) (BREDNAME) 18.1  Name of the institute (or person) that bred the material. This descriptor should be used only if BREDCODE can not be filled because the FAO WIEWS code for this institute is not available. Multiple names are separated by a semicolon without space.|
|ancestralData|string|MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|accessionNames|array[string]|MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space. Example: Accession name: Bogatyr;Symphony;Emma.|
|storageTypeCodes|array[string]|MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.) 10) Seed collection 11) Short term 12) Medium term 13) Long term 20) Field collection 30) In vitro collection 40) Cryopreserved collection 50) DNA collection 99) Other (elaborate in REMARKS field)|
|genus|string|MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.|
|germplasmDbId|string|A unique identifier which identifies a germplasm in this database|
|species|string|MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp." |
|speciesAuthority|string|MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|accessionNumber|string|MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|donorInfo|object|Information about the donor|
|donorInstitute|object||
|instituteCode|string|MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|instituteName|string|MCPD (v2.1) (DONORNAME) 22.1  Name of the donor institute (or person). This descriptor should be used only if DONORCODE cannot be filled because the FAO WIEWS code for this institute is not available.|
|donorAccessionPui|string|PUI (DOI mostly) of the accession in the donor system.|
|donorAccessionNumber|string|MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|acquisitionSourceCode|string|MCPD (v2.1) (COLLSRC) 21. The coding scheme proposed can be used at 2 different levels of detail: either by using the general codes (in bold-face) such as 10, 20, 30, 40, etc., or by using the more specific codes, such as 11, 12, etc. 10) Wild habitat 11) Forest or woodland 12) Shrubland 13) Grassland 14) Desert or tundra 15) Aquatic habitat 20) Farm or cultivated habitat 21) Field 22) Orchard 23) Backyard, kitchen or home garden (urban, peri-urban or rural) 24) Fallow land 25) Pasture 26) Farm store 27) Threshing floor 28) Park 30) Market or shop 40) Institute, Experimental station, Research organization, Genebank 50) Seed company 60) Weedy, disturbed or ruderal habitat 61) Roadside 62) Field margin 99) Other (Elaborate in REMARKS field) |
|remarks|string|MCPD (v2.1) (REMARKS) 28. The remarks field is used to add notes or to elaborate on descriptors with value 99 or 999 (= Other). Prefix remarks with the field name they refer to and a colon (:) without space (e.g. COLLSRC:riverside). Distinct remarks referring to different fields are separated by semi-colons without space.|
|instituteCode|string|MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. COL001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|countryOfOrigin|string|MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers" variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note: Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|mlsStatus|string|MCPD (v2.1) (MLSSTAT) 27. The status of an accession with regards to the Multilateral System (MLS) of the International Treaty on Plant Genetic Resources for Food and Agriculture. Leave the value empty if the status is not known 0 No (not included) 1 Yes (included) 99 Other (elaborate in REMARKS field, e.g. "under development")|


 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "accessionNames": [
            "Bogatyr",
            "Symphony",
            "Emma"
        ],
        "accessionNumber": "A0000003",
        "acquisitionDate": "2018-01-01",
        "acquisitionSourceCode": "26",
        "alternateIDs": [
            "3",
            "http://pui.per/accession/A0000003",
            "A0000003"
        ],
        "ancestralData": "A0000001/A0000002",
        "biologicalStatusOfAccessionCode": "421",
        "breedingInstitutes": [
            {
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute"
            }
        ],
        "collectingInfo": {
            "collectingDate": "2018-01-01",
            "collectingInstitutes": [
                {
                    "instituteAddress": "123 Main Street, Lima, Peru, 5555",
                    "instituteCode": "PER001",
                    "instituteName": "The BrAPI Institute"
                }
            ],
            "collectingMissionIdentifier": "CIATFOR052",
            "collectingNumber": "AB009909",
            "collectingSite": {
                "coordinateUncertainty": "20",
                "elevation": "35",
                "georeferencingMethod": "WGS84",
                "latitudeDecimal": "+42.445295",
                "latitudeDegrees": "42 26 43.1 N",
                "locationDescription": "South east hill near institute buildings",
                "longitudeDecimal": "-076.471934",
                "longitudeDegrees": "76 28 19.0 W",
                "spatialReferenceSystem": "WGS84"
            }
        },
        "commonCropName": "malting barley",
        "countryOfOrigin": "Peru",
        "donorInfo": {
            "donorAccessionNumber": "A0090204",
            "donorAccessionPui": "http://pui.per/accession/A0010025",
            "donorInstitute": {
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute"
            }
        },
        "genus": "Aspergillus",
        "germplasmDbId": "31c4efbc",
        "germplasmPUI": "http://pui.per/accession/A040365",
        "instituteCode": "PER001",
        "mlsStatus": "0",
        "remarks": "This is an example remark to demonstrate that any notable information can be put here",
        "safetyDuplicateInstitutes": [
            {
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute"
            }
        ],
        "species": "fructus",
        "speciesAuthority": "Smith, 1822",
        "storageTypeCodes": [
            "11",
            "13'"
        ],
        "subtaxon": "Aspergillus fructus A",
        "subtaxonAuthority": "Smith, 1822"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Get Germplasm Pedigree by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/pedigree{?notation}{?includeSiblings}]

Get the parentage information of a specific Germplasm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|parent1DbId|string|The germplasm DbId of the first parent of this germplasm|
|familyCode|string|The code representing the family|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|parent2Type|string|The type of parent the second parent is. ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|pedigree|string|The string representation of the pedigree.|
|defaultDisplayName|string|A human readable name for a germplasm|
|parent1Type|string|The type of parent the first parent is. ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2Name|string|The human readable name of the second parent of this germplasm|
|crossingProjectDbId|string|The crossing project used to generate this germplasm|
|siblings|array[object]|List of sibling germplasm |
|defaultDisplayName|string||
|germplasmDbId|string||
|parent1Name|string|the human readable name of the first parent of this germplasm|
|parent2DbId|string|The germplasm DbId of the second parent of this germplasm|
|crossingYear|integer|The year the parents were originally crossed|


 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + notation (Optional, ) ... text representation of the pedigree
    + includeSiblings (Optional, ) ... include array of siblings in response
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "crossingProjectDbId": "625e745a",
        "crossingYear": 2005,
        "defaultDisplayName": "A0021004",
        "familyCode": "F0000203",
        "germplasmDbId": "1098ebaf",
        "parent1DbId": "a55847ed",
        "parent1Name": "A0000592",
        "parent1Type": "FEMALE",
        "parent2DbId": "14c46b32",
        "parent2Name": "A0040035",
        "parent2Type": "MALE",
        "pedigree": "A0000001/A0000002",
        "siblings": [
            {
                "defaultDisplayName": "A0021005",
                "germplasmDbId": "334f53a3"
            },
            {
                "defaultDisplayName": "A0021006",
                "germplasmDbId": "7bbbda8c"
            },
            {
                "defaultDisplayName": "A0021007",
                "germplasmDbId": "ab1d9b26"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```





### Get Germplasm Progeny by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/progeny]

Get the germplasmDbIds for all the Progeny of a particular germplasm.

Implementation Notes

- Regarding the ''parentType'' field in the progeny object. Given a germplasm A having a progeny B and C, ''parentType'' for progeny B refers to the ''parentType'' of A toward B.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|defaultDisplayName|string|A human readable name for a germplasm|
|progeny|array[object]|List of germplasm entities which are direct children of this germplasm|
|parentType|string|Given a germplasm A having a progeny B and C, 'parentType' for progeny B item refers to the 'parentType' of A toward B.|
|defaultDisplayName|string|The human readable name of a progeny germplasm|
|germplasmDbId|string|The unique identifier of a progeny germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|


 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [
            {
                "fileDescription": "This is an Excel data file",
                "fileMD5Hash": "c2365e900c81a89cf74d83dab60df146",
                "fileName": "datafile.xslx",
                "fileSize": 4398,
                "fileType": "application/vnd.ms-excel",
                "fileURL": "https://wiki.brapi.org/examples/datafile.xslx"
            }
        ],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 1,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "defaultDisplayName": "A0021004",
        "germplasmDbId": "01b974dc",
        "progeny": [
            {
                "defaultDisplayName": "A0021011",
                "germplasmDbId": "e8d5dad7",
                "parentType": "FEMALE"
            },
            {
                "defaultDisplayName": "A0021012",
                "germplasmDbId": "ac07fbd8",
                "parentType": "FEMALE"
            },
            {
                "defaultDisplayName": "A0021013",
                "germplasmDbId": "07f45f67",
                "parentType": "FEMALE"
            }
        ]
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

+ Response 404 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - The requested object DbId is not found"
```

