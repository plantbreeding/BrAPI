# Group Germplasm
Fun Fact: The plural of germplasm is germplasm (no "s").





## Breedingmethods [/brapi/v1/breedingmethods] 




### Get Breedingmethods by breedingMethodDbId  [GET /brapi/v1/breedingmethods/{breedingMethodDbId}]

Get the details of a specific Breeding Method used to produce Germplasm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|abbreviation|string|an abbreviation for the name of this breeding method|
|breedingMethodDbId|string|the unique identifier for this breeding method|
|breedingMethodName|string|human readable name of the breeding method|
|description|string|human readable description of the breeding method|


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|abbreviation|string|an abbreviation for the name of this breeding method|
|breedingMethodDbId|string|the unique identifier for this breeding method|
|breedingMethodName|string|human readable name of the breeding method|
|description|string|human readable description of the breeding method|


 

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



## Germplasm [/brapi/v1/germplasm] 




### Get Germplasm  [GET /brapi/v1/germplasm{?germplasmPUI}{?germplasmDbId}{?germplasmName}{?commonCropName}{?page}{?pageSize}]

Addresses these needs

- General germplasm search mechanism that accepts POST for complex queries 

- Possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

- Possibility to get MCPD details by PUID rather than dbId



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|acquisitionDate|string (date)|The date this germplasm was aquired by the genebank (MCPD)|
|biologicalStatusOfAccessionCode|integer|The 3 digit code representing the biological status of the accession (MCPD)|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|commonCropName|string|Common name for the crop (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes (MCPD)|
|donorAccessionNumber|string||
|donorInstituteCode|string||
|germplasmPUI|string||
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|pedigree|string|The cross name and optional selection history.|
|seedSource|string|The source of the seed |
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|


 

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





### Get Germplasm Attributes by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/attributes{?attributeDbIds}{?page}{?pageSize}]

Values for all attributes by default.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]|List of attributes associated with the given germplasm|
|attributeCode|string|Short abbreviation which represents this attribute|
|attributeDbId|string|The ID which uniquely identifies this attribute within the given database server|
|attributeName|string|The human readable name of this attribute|
|determinedDate|string (date)|The date the value of this attribute was determined for a given germplasm|
|value|string|The value of this attribute for a given germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|


 

+ Parameters
    + germplasmDbId (Required, ) ... The germplasm characterized
    + attributeDbIds (Optional, ) ... Restrict the response to only the listed attributeDbIds.
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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|acquisitionDate|string (date)|The date this germplasm was aquired by the genebank (MCPD)|
|biologicalStatusOfAccessionCode|integer|The 3 digit code representing the biological status of the accession (MCPD)|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|commonCropName|string|Common name for the crop (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes (MCPD)|
|donorAccessionNumber|string||
|donorInstituteCode|string||
|germplasmPUI|string||
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|pedigree|string|The cross name and optional selection history.|
|seedSource|string|The source of the seed |
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNames|array[string]|MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space. Example: Accession name: Bogatyr;Symphony;Emma.|
|accessionNumber|string|MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string|MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|acquisitionSourceCode|string|MCPD (v2.1) (COLLSRC) 21. The coding scheme proposed can be used at 2 different levels of detail: either by using the general codes (in boldface) such as 10, 20, 30, 40, etc., or by using the more specific codes, such as 11, 12, etc. 10) Wild habitat 11) Forest or woodland 12) Shrubland 13) Grassland 14) Desert or tundra 15) Aquatic habitat 20) Farm or cultivated habitat 21) Field 22) Orchard 23) Backyard, kitchen or home garden (urban, peri-urban or rural) 24) Fallow land 25) Pasture 26) Farm store 27) Threshing floor 28) Park 30) Market or shop 40) Institute, Experimental station, Research organization, Genebank 50) Seed company 60) Weedy, disturbed or ruderal habitat 61) Roadside 62) Field margin 99) Other (Elaborate in REMARKS field) |
|alternateIDs|array[string]|MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon. |
|ancestralData|string|MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes (in boldface) such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc. 100) Wild 110) Natural 120) Semi-natural/wild 130) Semi-natural/sown 200) Weedy 300) Traditional cultivar/landrace 400) Breeding/research material 410) Breeders line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids) 423) Other genetic stocks (e.g. mapping populations) 500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other (Elaborate in REMARKS field)|
|breedingInstitutes|array[object]||
|instituteCode|string|MCPD (v2.1) (BREDCODE) 18. FAO WIEWS code of the institute that has bred the material. If the holding institute has bred the material, the breeding institute code (BREDCODE) should be the same as the holding institute code (INSTCODE). Follows INSTCODE standard. Multiple values are separated by a semicolon without space.|
|instituteName|string|MCPD (v2.1) (BREDNAME) 18.1  Name of the institute (or person) that bred the material. This descriptor should be used only if BREDCODE cannot be filled because the FAO WIEWS code for this institute is not available. Multiple names are separated by a semicolon without space.|
|collectingInfo|object|Information about the collection of this germplasm|
|collectingDate|string|MCPD (v2.1) (COLLDATE) 17. Collecting date of the sample [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|collectingInstitutes|array[object]|Institutes which collected the sample|
|instituteAddress|string|MCPD (v2.1) (COLLINSTADDRESS) 4.1.1  Address of the institute collecting the sample. This descriptor should be used only if COLLCODE cannot be filled since the FAO WIEWS code for this institute is not available. Multiple values are separated by a semicolon without space.|
|instituteCode|string|MCPD (v2.1) (COLLCODE) 4.  FAO WIEWS code of the institute collecting the sample. If the holding institute has collected the material, the collecting institute code (COLLCODE) should be the same as the holding institute code (INSTCODE). Follows INSTCODE standard. Multiple values are separated by a semicolon without space.|
|instituteName|string|MCPD (v2.1) (COLLNAME) 4.1  Name of the institute collecting the sample. This descriptor should be used only if COLLCODE cannot be filled because the FAO WIEWS code for this institute is not available. Multiple values are separated by a semicolon without space.|
|collectingMissionIdentifier|string|MCPD (v2.1) (COLLMISSID) 4.2 Identifier of the collecting mission used by the Collecting Institute (4 or 4.1) (e.g. "CIATFOR052", "CN426").|
|collectingNumber|string|MCPD (v2.1) (COLLNUMB) 3. Original identifier assigned by the collector(s) of the sample, normally composed of the name or initials of the collector(s) followed by a number (e.g. "FM9909"). This identifier is essential for identifying duplicates held in different collections.|
|collectingSite|object|Information about the location where the sample was collected|
|coordinateUncertainty|string|MCPD (v2.1) (COORDUNCERT) 15.5 Uncertainty associated with the coordinates in metres. Leave the value empty if the uncertainty is unknown.|
|elevation|string|MCPD (v2.1) (ELEVATION) 16. Elevation of collecting site expressed in metres above sea level. Negative values are allowed.|
|georeferencingMethod|string|MCPD (v2.1) (GEOREFMETH) 15.7  The georeferencing method used (GPS, determined from map, gazetteer, or estimated using software). Leave the value empty if georeferencing method is not known.|
|latitudeDecimal|string|MCPD (v2.1) (DECLATITUDE) 15.1 Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|latitudeDegrees|string|MCPD (v2.1) (LATITUDE) 15.2 Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|locationDescription|string|MCPD (v2.1) (COLLSITE) 14. Location information below the country level that describes where the accession was collected, preferable in English. This might include the distance in kilometres and direction from the nearest town, village or map grid reference point, (e.g. 7 km south of Curitiba in the state of Parana).|
|longitudeDecimal|string|MCPD (v2.1) (DECLONGITUDE) 15.3 Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|MCPD (v2.1) (LONGITUDE) 15.4 Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|spatialReferenceSystem|string|MCPD (v2.1) (COORDDATUM) 15.6 The geodetic datum or spatial reference system upon which the coordinates given in decimal latitude and decimal longitude are based (e.g. WGS84, ETRS89, NAD83). The GPS uses the WGS84 datum.|
|commonCropName|string|MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "macadamia", "mas". |
|countryOfOrigin|string|MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers" variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note: Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|donorInfo|object|Information about the donor|
|donorAccessionNumber|string|MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstitute|object||
|instituteCode|string|MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|instituteName|string|MCPD (v2.1) (DONORNAME) 22.1  Name of the donor institute (or person). This descriptor should be used only if DONORCODE cannot be filled because the FAO WIEWS code for this institute is not available.|
|genus|string|MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.|
|germplasmDbId|string|A unique identifier which identifies a germplasm in this database|
|germplasmPUI|string|MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level (http://www.planttreaty.org/doi). Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties (e.g. NOR017:NGB17773:ALLIUM).|
|instituteCode|string|MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. COL001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|mlsStatus|string|MCPD (v2.1) (MLSSTAT) 27. The status of an accession with regards to the Multilateral System (MLS) of the International Treaty on Plant Genetic Resources for Food and Agriculture. Leave the value empty if the status is not known 0 No (not included) 1 Yes (included) 99 Other (elaborate in REMARKS field, e.g. "under development")|
|remarks|string|MCPD (v2.1) (REMARKS) 28. The remarks field is used to add notes or to elaborate on descriptors with value 99 or 999 (= Other). Prefix remarks with the field name they refer to and a colon (:) without space (e.g. COLLSRC:riverside). Distinct remarks referring to different fields are separated by semicolons without space.|
|safetyDuplicateInstitues|array[object]||
|instituteCode|string|MCPD (v2.1) (DUPLSITE) 25. FAO WIEWS code of the institute(s) where a safety duplicate of the accession is maintained. Follows INSTCODE standard.|
|instituteName|string|MCPD (v2.1) (DUPLINSTNAME) 25.1  Name of the institute where a safety duplicate of the accession is maintained.|
|species|string|MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp." |
|speciesAuthority|string|MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypeCodes|array[string]|MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.) 10) Seed collection 11) Short term 12) Medium term 13) Long term 20) Field collection 30) In vitro collection 40) Cryopreserved collection 50) DNA collection 99) Other (elaborate in REMARKS field)|
|subtaxon|string|MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").|
|subtaxonAuthority|string|MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|markerProfileDbIds|array[string]|The ID which uniquely identifies a marker profile within the given database server|


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|crossingPlan|string|The crossing strategy used to generate this germplasm|
|crossingYear|string|The year the parents were originally crossed|
|defaultDisplayName|string|A human readable name for a germplasm|
|familyCode|string|The code representing the family|
|germplasmDbId|string| The ID which uniquely identifies a germplasm|
|parent1DbId|string|The germplasm DbId of the first parent of this germplasm|
|parent1Name|string|the human readable name of the first parent of this germplasm|
|parent1Type|string|The type of parent the first parent is. ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|parent2DbId|string|The germplasm DbId of the second parent of this germplasm|
|parent2Name|string|The human readable name of the second parent of this germplasm|
|parent2Type|string|The type of parent the second parent is. ex. 'MALE', 'FEMALE', 'SELF', 'POPULATION', etc.|
|pedigree|string|The string representation of the pedigree.|
|siblings|array[object]|List of sibling germplasm |
|defaultDisplayName|string||
|germplasmDbId|string||


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|defaultDisplayName|string|A human readable name for a germplasm|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|progeny|array[object]|List of germplasm entities which are direct children of this germplasm|
|defaultDisplayName|string|The human readable name of a progeny germplasm|
|germplasmDbId|string|The unique identifier of a progeny germplasm|
|parentType|string|Given a germplasm A having a progeny B and C, 'parentType' for progeny B item refers to the 'parentType' of A toward B.|


 

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

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNumbers|array[string]|List unique identifiers for accessions within a genebank|
|commonCropNames|array[string]|List crops to search by|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm|
|germplasmGenus|array[string]|List of Genus names to identify germplasm|
|germplasmNames|array[string]|List of human readable names to identify germplasm|
|germplasmPUIs|array[string]|List of Permanent Unique Identifiers to identify germplasm|
|germplasmSpecies|array[string]|List of Species names to identify germplasm|
|page|integer|Which page of the "data" array to return. The page indexing starts at 0 (page=0 will return the first page). Default is 0.|
|pageSize|integer|The maximum number of items to return per page of the "data" array. Default is 1000.|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|searchResultDbId|string||


 

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



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection|
|acquisitionDate|string (date)|The date this germplasm was aquired by the genebank (MCPD)|
|biologicalStatusOfAccessionCode|integer|The 3 digit code representing the biological status of the accession (MCPD)|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|commonCropName|string|Common name for the crop (MCPD)|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected (MCPD)|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes (MCPD)|
|donorAccessionNumber|string||
|donorInstituteCode|string||
|germplasmPUI|string||
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server|
|germplasmGenus|string|Genus name for taxon. Initial uppercase letter required. (MCPD)|
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique.|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm|
|germplasmSpecies|string|Specific epithet portion of the scientific name in lowercase letters. (MCPD)|
|instituteCode|string|The code for the Institute that has bred the material. (MCPD)|
|instituteName|string|The name of the institution which bred the material (MCPD)|
|pedigree|string|The cross name and optional selection history.|
|seedSource|string|The source of the seed |
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name (MCPD)|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier. (MCPD)|
|subtaxaAuthority|string| The authority organization responsible for tracking and maintaining the subtaxon information (MCPD)|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|
|typeOfGermplasmStorageCode|array[string]|The 2 digit code representing the type of storage this germplasm is kept in at a genebank. (MCPD)|


 

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

