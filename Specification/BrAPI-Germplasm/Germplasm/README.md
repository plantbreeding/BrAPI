# Group Germplasm
Fun Fact: The plural of germplasm is germplasm (no "s").






### Get - /breedingmethods [GET /brapi/v2/breedingmethods{?page}{?pageSize}]

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
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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




### Get - /breedingmethods/{breedingMethodDbId} [GET /brapi/v2/breedingmethods/{breedingMethodDbId}]

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
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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




### Get - /germplasm [GET /brapi/v2/germplasm{?germplasmPUI}{?germplasmDbId}{?germplasmName}{?accessionNumber}{?collection}{?binomialName}{?genus}{?species}{?trialDbId}{?studyDbId}{?synonym}{?parentDbId}{?progenyDbId}{?commonCropName}{?programDbId}{?externalReferenceID}{?externalReferenceId}{?externalReferenceSource}{?page}{?pageSize}]

Addresses these needs

- General germplasm search mechanism that accepts POST for complex queries 

- Possibility to search germplasm by more parameters than those allowed by the existing germplasm search 

- Possibility to get MCPD details by PUID rather than dbId



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


 

+ Parameters
    + germplasmPUI (Optional, ) ... Permanent unique identifier (DOI, URI, etc.)
    + germplasmDbId (Optional, ) ... Internal database identifier
    + germplasmName (Optional, ) ... Name of the germplasm
    + accessionNumber (Optional, ) ... Unique identifiers for accessions within a genebank
    + collection (Optional, ) ... A specific panel/collection/population name this germplasm belongs to.
    + binomialName (Optional, ) ... The full binomial name (scientific name) to identify a germplasm
    + genus (Optional, ) ... Genus name to identify germplasm
    + species (Optional, ) ... Species name to identify germplasm
    + trialDbId (Optional, ) ... Search for Germplasm that are associated with a particular Study
    + studyDbId (Optional, ) ... Search for Germplasm that are associated with a particular Study
    + synonym (Optional, ) ... Alternative name or ID used to reference this germplasm
    + parentDbId (Optional, ) ... Search for Germplasm with this parent
    + progenyDbId (Optional, ) ... Search for Germplasm with this child
    + commonCropName (Optional, ) ... The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.Use this parameter to only return results associated with the given crop. Use `GET /commoncropnames` to find the list of available crops on a server.
    + programDbId (Optional, ) ... A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs. Use this parameter to only return results associated with the given program. Use `GET /programs` to find the list of available programs on a server.
    + externalReferenceID (Optional, ) ... **Deprecated in v2.1** Please use `externalReferenceId`. Github issue number #460 An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceId (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceId` parameter)
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "biologicalStatusOfAccessionCode": "420",
                "biologicalStatusOfAccessionDescription": "Genetic stock",
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "collection": "Rice Diversity Panel 1 (RDP1)",
                "commonCropName": "Maize",
                "countryOfOriginCode": "BES",
                "defaultDisplayName": "A0000003",
                "documentationURL": "https://wiki.brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A0000123",
                        "donorInstituteCode": "PER001"
                    }
                ],
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "genus": "Aspergillus",
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "germplasmOrigin": [
                    {
                        "coordinateUncertainty": "20",
                        "coordinates": {
                            "geometry": {
                                "coordinates": [
                                    -76.506042,
                                    42.417373,
                                    123
                                ],
                                "type": "Point"
                            },
                            "type": "Feature"
                        }
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute",
                "pedigree": "A0000001/A0000002",
                "seedSource": "INRA:095115_inra",
                "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
                "species": "fructus",
                "speciesAuthority": "Smith, 1822",
                "storageTypes": [
                    {
                        "code": "20",
                        "description": "Field collection"
                    },
                    {
                        "code": "11",
                        "description": "Short term"
                    }
                ],
                "subtaxa": "Aspergillus fructus A",
                "subtaxaAuthority": "Smith, 1822",
                "synonyms": [
                    {
                        "synonym": "variety_1",
                        "type": "Pre-Code"
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "NCBI",
                        "taxonId": "2026747"
                    }
                ]
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




### Post - /germplasm [POST /brapi/v2/germplasm]

Create new Germplasm entities on this server

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
[
    {
        "accessionNumber": "A0000003",
        "acquisitionDate": "2018-01-01",
        "additionalInfo": {},
        "biologicalStatusOfAccessionCode": "420",
        "biologicalStatusOfAccessionDescription": "Genetic stock",
        "breedingMethodDbId": "ffcce7ef",
        "breedingMethodName": "Male Backcross",
        "collection": "Rice Diversity Panel 1 (RDP1)",
        "commonCropName": "Maize",
        "countryOfOriginCode": "BES",
        "defaultDisplayName": "A0000003",
        "documentationURL": "https://wiki.brapi.org",
        "donors": [
            {
                "donorAccessionNumber": "A0000123",
                "donorInstituteCode": "PER001"
            }
        ],
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "genus": "Aspergillus",
        "germplasmName": "A0000003",
        "germplasmOrigin": [
            {
                "coordinateUncertainty": "20",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                }
            }
        ],
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
        "instituteCode": "PER001",
        "instituteName": "The BrAPI Institute",
        "pedigree": "A0000001/A0000002",
        "seedSource": "INRA:095115_inra",
        "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
        "species": "fructus",
        "speciesAuthority": "Smith, 1822",
        "storageTypes": [
            {
                "code": "20",
                "description": "Field collection"
            },
            {
                "code": "11",
                "description": "Short term"
            }
        ],
        "subtaxa": "Aspergillus fructus A",
        "subtaxaAuthority": "Smith, 1822",
        "synonyms": [
            {
                "synonym": "variety_1",
                "type": "Pre-Code"
            }
        ],
        "taxonIds": [
            {
                "sourceName": "NCBI",
                "taxonId": "2026747"
            }
        ]
    }
]
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "biologicalStatusOfAccessionCode": "420",
                "biologicalStatusOfAccessionDescription": "Genetic stock",
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "collection": "Rice Diversity Panel 1 (RDP1)",
                "commonCropName": "Maize",
                "countryOfOriginCode": "BES",
                "defaultDisplayName": "A0000003",
                "documentationURL": "https://wiki.brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A0000123",
                        "donorInstituteCode": "PER001"
                    }
                ],
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "genus": "Aspergillus",
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "germplasmOrigin": [
                    {
                        "coordinateUncertainty": "20",
                        "coordinates": {
                            "geometry": {
                                "coordinates": [
                                    -76.506042,
                                    42.417373,
                                    123
                                ],
                                "type": "Point"
                            },
                            "type": "Feature"
                        }
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute",
                "pedigree": "A0000001/A0000002",
                "seedSource": "INRA:095115_inra",
                "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
                "species": "fructus",
                "speciesAuthority": "Smith, 1822",
                "storageTypes": [
                    {
                        "code": "20",
                        "description": "Field collection"
                    },
                    {
                        "code": "11",
                        "description": "Short term"
                    }
                ],
                "subtaxa": "Aspergillus fructus A",
                "subtaxaAuthority": "Smith, 1822",
                "synonyms": [
                    {
                        "synonym": "variety_1",
                        "type": "Pre-Code"
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "NCBI",
                        "taxonId": "2026747"
                    }
                ]
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




### Get - /germplasm/{germplasmDbId} [GET /brapi/v2/germplasm/{germplasmDbId}]

Germplasm Details by germplasmDbId was merged with Germplasm Multi Crop Passport Data. The MCPD fields are optional and marked with the prefix [MCPD].



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


 

+ Parameters
    + germplasmDbId (Required, ) ... The internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "biologicalStatusOfAccessionCode": "420",
        "biologicalStatusOfAccessionDescription": "Genetic stock",
        "breedingMethodDbId": "ffcce7ef",
        "breedingMethodName": "Male Backcross",
        "collection": "Rice Diversity Panel 1 (RDP1)",
        "commonCropName": "Maize",
        "countryOfOriginCode": "BES",
        "defaultDisplayName": "A0000003",
        "documentationURL": "https://wiki.brapi.org",
        "donors": [
            {
                "donorAccessionNumber": "A0000123",
                "donorInstituteCode": "PER001"
            }
        ],
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "genus": "Aspergillus",
        "germplasmDbId": "d4076594",
        "germplasmName": "A0000003",
        "germplasmOrigin": [
            {
                "coordinateUncertainty": "20",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                }
            }
        ],
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
        "instituteCode": "PER001",
        "instituteName": "The BrAPI Institute",
        "pedigree": "A0000001/A0000002",
        "seedSource": "INRA:095115_inra",
        "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
        "species": "fructus",
        "speciesAuthority": "Smith, 1822",
        "storageTypes": [
            {
                "code": "20",
                "description": "Field collection"
            },
            {
                "code": "11",
                "description": "Short term"
            }
        ],
        "subtaxa": "Aspergillus fructus A",
        "subtaxaAuthority": "Smith, 1822",
        "synonyms": [
            {
                "synonym": "variety_1",
                "type": "Pre-Code"
            }
        ],
        "taxonIds": [
            {
                "sourceName": "NCBI",
                "taxonId": "2026747"
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




### Put - /germplasm/{germplasmDbId} [PUT /brapi/v2/germplasm/{germplasmDbId}/]

Germplasm Details by germplasmDbId was merged with Germplasm Multi Crop Passport Data. The MCPD fields are optional and marked with the prefix [MCPD].

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


 

+ Parameters
    + germplasmDbId (Required, ) ... The internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accessionNumber": "A0000003",
    "acquisitionDate": "2018-01-01",
    "additionalInfo": {},
    "biologicalStatusOfAccessionCode": "420",
    "biologicalStatusOfAccessionDescription": "Genetic stock",
    "breedingMethodDbId": "ffcce7ef",
    "breedingMethodName": "Male Backcross",
    "collection": "Rice Diversity Panel 1 (RDP1)",
    "commonCropName": "Maize",
    "countryOfOriginCode": "BES",
    "defaultDisplayName": "A0000003",
    "documentationURL": "https://wiki.brapi.org",
    "donors": [
        {
            "donorAccessionNumber": "A0000123",
            "donorInstituteCode": "PER001"
        }
    ],
    "externalReferences": [
        {
            "referenceId": "doi:10.155454/12341234",
            "referenceSource": "DOI"
        },
        {
            "referenceId": "75a50e76",
            "referenceSource": "Remote Data Collection Upload Tool"
        }
    ],
    "genus": "Aspergillus",
    "germplasmName": "A0000003",
    "germplasmOrigin": [
        {
            "coordinateUncertainty": "20",
            "coordinates": {
                "geometry": {
                    "coordinates": [
                        -76.506042,
                        42.417373,
                        123
                    ],
                    "type": "Point"
                },
                "type": "Feature"
            }
        }
    ],
    "germplasmPUI": "http://pui.per/accession/A0000003",
    "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
    "instituteCode": "PER001",
    "instituteName": "The BrAPI Institute",
    "pedigree": "A0000001/A0000002",
    "seedSource": "INRA:095115_inra",
    "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
    "species": "fructus",
    "speciesAuthority": "Smith, 1822",
    "storageTypes": [
        {
            "code": "20",
            "description": "Field collection"
        },
        {
            "code": "11",
            "description": "Short term"
        }
    ],
    "subtaxa": "Aspergillus fructus A",
    "subtaxaAuthority": "Smith, 1822",
    "synonyms": [
        {
            "synonym": "variety_1",
            "type": "Pre-Code"
        }
    ],
    "taxonIds": [
        {
            "sourceName": "NCBI",
            "taxonId": "2026747"
        }
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "biologicalStatusOfAccessionCode": "420",
        "biologicalStatusOfAccessionDescription": "Genetic stock",
        "breedingMethodDbId": "ffcce7ef",
        "breedingMethodName": "Male Backcross",
        "collection": "Rice Diversity Panel 1 (RDP1)",
        "commonCropName": "Maize",
        "countryOfOriginCode": "BES",
        "defaultDisplayName": "A0000003",
        "documentationURL": "https://wiki.brapi.org",
        "donors": [
            {
                "donorAccessionNumber": "A0000123",
                "donorInstituteCode": "PER001"
            }
        ],
        "externalReferences": [
            {
                "referenceId": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceId": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "genus": "Aspergillus",
        "germplasmDbId": "d4076594",
        "germplasmName": "A0000003",
        "germplasmOrigin": [
            {
                "coordinateUncertainty": "20",
                "coordinates": {
                    "geometry": {
                        "coordinates": [
                            -76.506042,
                            42.417373,
                            123
                        ],
                        "type": "Point"
                    },
                    "type": "Feature"
                }
            }
        ],
        "germplasmPUI": "http://pui.per/accession/A0000003",
        "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
        "instituteCode": "PER001",
        "instituteName": "The BrAPI Institute",
        "pedigree": "A0000001/A0000002",
        "seedSource": "INRA:095115_inra",
        "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
        "species": "fructus",
        "speciesAuthority": "Smith, 1822",
        "storageTypes": [
            {
                "code": "20",
                "description": "Field collection"
            },
            {
                "code": "11",
                "description": "Short term"
            }
        ],
        "subtaxa": "Aspergillus fructus A",
        "subtaxaAuthority": "Smith, 1822",
        "synonyms": [
            {
                "synonym": "variety_1",
                "type": "Pre-Code"
            }
        ],
        "taxonIds": [
            {
                "sourceName": "NCBI",
                "taxonId": "2026747"
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




### Get - /germplasm/{germplasmDbId}/mcpd [GET /brapi/v2/germplasm/{germplasmDbId}/mcpd]

Get all MCPD details of a germplasm

<a target="_blank" href="https://www.bioversityInternational.org/fileadmin/user_upload/online_library/publications/pdfs/FAOBIOVERSITY_MULTI-CROP_PASSPORT_DESCRIPTORS_V.2.1_2015_2020.pdf"> MCPD v2.1 spec can be found here </a>

Implementation Notes

- When the MCPD spec identifies a field which can have multiple values returned, the JSON response should be an array instead of a semi-colon separated string.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNames|array[string]|MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|accessionNumber|string|MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|acquisitionSourceCode|string|MCPD (v2.1) (COLLSRC) 21. The coding scheme proposed can be used at 2 different levels of detail: either by using the general codes (in bold-face) such as 10, 20, 30, 40, etc., or by using the more specific codes, such as 11, 12, etc.   10) Wild habitat  11) Forest or woodland  12) Shrubland  13) Grassland  14) Desert or tundra  15) Aquatic habitat  20) Farm or cultivated habitat  21) Field  22) Orchard  23) Backyard, kitchen or home garden (urban, peri-urban or rural)  24) Fallow land  25) Pasture  26) Farm store  27) Threshing floor  28) Park  30) Market or shop  40) Institute, Experimental station, Research organization, Genebank  50) Seed company  60) Weedy, disturbed or ruderal habitat  61) Roadside  62) Field margin  99) Other (Elaborate in REMARKS field)|
|alternateIDs|array[string]|MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon. |
|ancestralData|string|MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|breedingInstitutes|array[object]||
|instituteCode|string|MCPD (v2.1) (BREDCODE) 18. FAO WIEWS code of the institute that has bred the material. If the holding institute has bred the material, the breeding institute code (BREDCODE) should be the same as the holding institute code (INSTCODE). Follows INSTCODE standard. Multiple values are separated by a semicolon without space.|
|instituteName|string|MCPD (v2.1) (BREDNAME) 18.1  Name of the institute (or person) that bred the material. This descriptor should be used only if BREDCODE can not be filled because the FAO WIEWS code for this institute is not available. Multiple names are separated by a semicolon without space.|
|collectingInfo|object|Information about the collection of this germplasm|
|collectingDate|string (date)|MCPD (v2.1) (COLLDATE) 17. Collecting date of the sample [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|collectingInstitutes|array[object]|Institutes which collected the sample|
|instituteAddress|string|MCPD (v2.1) (COLLINSTADDRESS) 4.1.1  Address of the institute collecting the sample. This descriptor should be used only if COLLCODE can not be filled since the FAO WIEWS code for this institute is not available. Multiple values are separated by a semicolon without space.|
|instituteCode|string|MCPD (v2.1) (COLLCODE) 4.  FAO WIEWS code of the institute collecting the sample. If the holding institute has collected the material, the collecting institute code (COLLCODE) should be the same as the holding institute code (INSTCODE). Follows INSTCODE standard. Multiple values are separated by a semicolon without space.|
|instituteName|string|MCPD (v2.1) (COLLNAME) 4.1  Name of the institute collecting the sample. This descriptor should be used only if COLLCODE can not be filled because the FAO WIEWS code for this institute is not available. Multiple values are separated by a semicolon without space.|
|collectingMissionIdentifier|string|MCPD (v2.1) (COLLMISSID) 4.2 Identifier of the collecting mission used by the Collecting Institute (4 or 4.1) (e.g. "CIATFOR_052", "CN_426").|
|collectingNumber|string|MCPD (v2.1) (COLLNUMB) 3. Original identifier assigned by the collector(s) of the sample, normally composed of the name or initials of the collector(s) followed by a number (e.g. "ab109909"). This identifier is essential for identifying duplicates held in different collections.|
|collectingSite|object|Information about the location where the sample was collected|
|coordinateUncertainty|string|MCPD (v2.1) (COORDUNCERT) 15.5 Uncertainty associated with the coordinates in metres. Leave the value empty if the uncertainty is unknown.|
|elevation|string|MCPD (v2.1) (ELEVATION) 16. Elevation of collecting site expressed in metres above sea level. Negative values are allowed.|
|georeferencingMethod|string|MCPD (v2.1) (GEOREFMETH) 15.7  The georeferencing method used (GPS, determined from map, gazetteer, or estimated using software). Leave the value empty if georeferencing method is not known.|
|latitudeDecimal|string|MCPD (v2.1) (DECLATITUDE) 15.1 Latitude expressed in decimal degrees. Positive values are North of the Equator; negative values are South of the Equator (e.g. -44.6975).|
|latitudeDegrees|string|MCPD (v2.1) (LATITUDE) 15.2 Degrees (2 digits) minutes (2 digits), and seconds (2 digits) followed by N (North) or S (South) (e.g. 103020S). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 10|
|locationDescription|string|MCPD (v2.1) (COLLSITE) 14. Location information below the country level that describes where the accession was collected, preferable in English. This might include the distance in kilometres and direction from the nearest town, village or map grid reference point, (e.g. 7 km south of Townsville).|
|longitudeDecimal|string|MCPD (v2.1) (DECLONGITUDE) 15.3 Longitude expressed in decimal degrees. Positive values are East of the Greenwich Meridian; negative values are West of the Greenwich Meridian (e.g. +120.9123).|
|longitudeDegrees|string|MCPD (v2.1) (LONGITUDE) 15.4 Degrees (3 digits), minutes (2 digits), and seconds (2 digits) followed by E (East) or W (West) (e.g. 0762510W). Every missing digit (minutes or seconds) should be indicated with a hyphen. Leading zeros are required (e.g. 076|
|spatialReferenceSystem|string|MCPD (v2.1) (COORDDATUM) 15.6 The geodetic datum or spatial reference system upon which the coordinates given in decimal latitude and decimal longitude are based (e.g. WGS84). The GPS uses the WGS84 datum.|
|commonCropName|string|MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas". |
|countryOfOrigin|string|MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers" variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note: Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|donorInfo|object|Information about the donor|
|donorAccessionNumber|string|MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorAccessionPui|string|PUI (DOI mostly) of the accession in the donor system.|
|donorInstitute|object||
|instituteCode|string|MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|instituteName|string|MCPD (v2.1) (DONORNAME) 22.1  Name of the donor institute (or person). This descriptor should be used only if DONORCODE can not be filled because the FAO WIEWS code for this institute is not available.|
|genus|string|MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.|
|germplasmDbId|string|A unique identifier which identifies a germplasm in this database|
|germplasmPUI|string|MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|instituteCode|string|MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|mlsStatus|string|MCPD (v2.1) (MLSSTAT) 27. The status of an accession with regards to the Multilateral System (MLS) of the International Treaty on Plant Genetic Resources for Food and Agriculture. Leave the value empty if the status is not known 0 No (not included) 1 Yes (included) 99 Other (elaborate in REMARKS field, e.g. "under development")|
|remarks|string|MCPD (v2.1) (REMARKS) 28. The remarks field is used to add notes or to elaborate on descriptors with value 99 or 999 (= Other). Prefix remarks with the field name they refer to and a colon (:) without space (e.g. COLLSRC:riverside). Distinct remarks referring to different fields are separated by semi-colons without space.|
|safetyDuplicateInstitutes|array[object]||
|instituteCode|string|MCPD (v2.1) (DUPLSITE) 25. FAO WIEWS code of the institute(s) where a safety duplicate of the accession is maintained. Follows INSTCODE standard.|
|instituteName|string|MCPD (v2.1) (DUPLINSTNAME) 25.1  Name of the institute where a safety duplicate of the accession is maintained.|
|species|string|MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp." |
|speciesAuthority|string|MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypeCodes|array[string]|MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.) 10) Seed collection 11) Short term 12) Medium term 13) Long term 20) Field collection 30) In vitro collection 40) Cryo-preserved collection 50) DNA collection 99) Other (elaborate in REMARKS field)|
|subtaxon|string|MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").|
|subtaxonAuthority|string|MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|


 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
            "collectingMissionIdentifier": "CIATFOR_052",
            "collectingNumber": "ab109909",
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
        "germplasmPUI": "http://pui.per/accession/A0403652",
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
            "13"
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




### **Deprecated** Get - /germplasm/{germplasmDbId}/pedigree [GET /brapi/v2/germplasm/{germplasmDbId}/pedigree{?notation}{?includeSiblings}]

**Deprecated in v2.1** Please use `GET /pedigree?germplasmDbId={germplasmDbId}`. Github issue number #481 
<br/> Get the parentage information of a specific Germplasm



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|crossingProjectDbId|string|The crossing project used to generate this germplasm|
|crossingYear|integer|The year the parents were originally crossed|
|familyCode|string|The code representing the family|
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|A human readable name for a germplasm|
|parents|array[object]|List of parent nodes in the pedigree tree.|
|germplasmDbId|string|The germplasm DbId of the parent of this germplasm|
|germplasmName|string|the human readable name of the parent of this germplasm|
|parentType|string|The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. |
|pedigree|string|The string representation of the pedigree in PURDY notation.|
|siblings|array[object]|List of sibling germplasm|
|germplasmDbId|string|the germplasm DbId of the sibling|
|germplasmName|string|the germplasm name of the sibling|


 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + notation (Optional, ) ... text representation of the pedigree
    + includeSiblings (Optional, ) ... include array of siblings in response
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "familyCode": "F0000203",
        "germplasmDbId": "1098ebaf",
        "germplasmName": "A0021004",
        "parents": [
            {
                "germplasmDbId": "b66958de",
                "germplasmName": "A0000592",
                "parentType": "MALE"
            },
            {
                "germplasmDbId": "a55847ed",
                "germplasmName": "A0000592",
                "parentType": "FEMALE"
            }
        ],
        "pedigree": "A0000001/A0000002",
        "siblings": [
            {
                "germplasmDbId": "334f53a3",
                "germplasmName": "A0021005"
            },
            {
                "germplasmDbId": "7bbbda8c",
                "germplasmName": "A0021006"
            },
            {
                "germplasmDbId": "ab1d9b26",
                "germplasmName": "A0021007"
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




### **Deprecated** Get - /germplasm/{germplasmDbId}/progeny [GET /brapi/v2/germplasm/{germplasmDbId}/progeny]

**Deprecated in v2.1** Please use `GET /pedigree?germplasmDbId={germplasmDbId}`. Github issue number #481 
<br/> Get the germplasmDbIds for all the Progeny of a particular germplasm.
<br/> Implementation Notes
<br/> - Regarding the ''parentType'' field in the progeny object. Given a germplasm A having a progeny B and C, ''parentType'' for progeny B refers to the ''parentType'' of A toward B.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|germplasmDbId|string|The ID which uniquely identifies a germplasm|
|germplasmName|string|A human readable name for a germplasm|
|progeny|array[object]|List of germplasm entities which are direct children of this germplasm|
|germplasmDbId|string|The unique identifier of a progeny germplasm|
|germplasmName|string|The human readable name of a progeny germplasm|
|parentType|string|The type of parent used during crossing. Accepted values for this field are 'MALE', 'FEMALE', 'SELF', 'POPULATION', and 'CLONAL'.   In a pedigree record, the 'parentType' describes each parent of a particular germplasm.   In a progeny record, the 'parentType' is used to describe how this germplasm was crossed to generate a particular progeny.  For example, given a record for germplasm A, having a progeny B and C. The 'parentType' field for progeny B item refers  to the 'parentType' of A toward B. The 'parentType' field for progeny C item refers to the 'parentType' of A toward C. In this way, A could be a male parent to B, but a female parent to C. |


 

+ Parameters
    + germplasmDbId (Required, ) ... the internal id of the germplasm
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "germplasmDbId": "01b974dc",
        "germplasmName": "A0021004",
        "progeny": [
            {
                "germplasmDbId": "e8d5dad7",
                "germplasmName": "A0021011",
                "parentType": "FEMALE"
            },
            {
                "germplasmDbId": "ac07fbd8",
                "germplasmName": "A0021012",
                "parentType": "FEMALE"
            },
            {
                "germplasmDbId": "07f45f67",
                "germplasmName": "A0021013",
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




### Post - /search/germplasm [POST /brapi/v2/search/germplasm]

Submit a search request for `Germplasm`<br/>
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use the corresponding `GET /search/germplasm/{searchResultsDbId}` to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.

**Request Fields** 

|Field|Type|Description|
|---|---|---| 
|accessionNumbers|array[string]|List unique identifiers for accessions within a genebank|
|binomialNames|array[string]|List of the full binomial name (scientific name) to identify a germplasm|
|collections|array[string]|A specific panel/collection/population name this germplasm belongs to.|
|commonCropNames|array[string]|The BrAPI Common Crop Name is the simple, generalized, widely accepted name of the organism being researched. It is most often used in multi-crop systems where digital resources need to be divided at a high level. Things like 'Maize', 'Wheat', and 'Rice' are examples of common crop names.  Use this parameter to only return results associated with the given crops.   Use `GET /commoncropnames` to find the list of available crops on a server.|
|externalReferenceIDs|array[string]|**Deprecated in v2.1** Please use `externalReferenceIds`. Github issue number #460   List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceIds|array[string]|List of external reference IDs. Could be a simple strings or a URIs. (use with `externalReferenceSources` parameter)|
|externalReferenceSources|array[string]|List of identifiers for the source system or database of an external reference (use with `externalReferenceIDs` parameter)|
|familyCodes|array[string]|A familyCode representing the family this germplasm belongs to.|
|genus|array[string]|List of Genus names to identify germplasm|
|germplasmDbIds|array[string]|List of IDs which uniquely identify germplasm to search for|
|germplasmNames|array[string]|List of human readable names to identify germplasm to search for|
|germplasmPUIs|array[string]|List of Permanent Unique Identifiers to identify germplasm|
|instituteCodes|array[string]|The code for the institute that maintains the material.  <br/> MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|page|integer|Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.|
|pageSize|integer|The size of the pages to be returned. Default is `1000`.|
|parentDbIds|array[string]|Search for Germplasm with these parents|
|progenyDbIds|array[string]|Search for Germplasm with these children|
|programDbIds|array[string]|A BrAPI Program represents the high level organization or group who is responsible for conducting trials and studies. Things like Breeding Programs and Funded Projects are considered BrAPI Programs.   Use this parameter to only return results associated with the given programs.   Use `GET /programs` to find the list of available programs on a server.|
|programNames|array[string]|Use this parameter to only return results associated with the given program names. Program names are not required to be unique.  Use `GET /programs` to find the list of available programs on a server.|
|species|array[string]|List of Species names to identify germplasm|
|studyDbIds|array[string]|List of study identifiers to search for|
|studyNames|array[string]|List of study names to filter search results|
|synonyms|array[string]|List of alternative names or IDs used to reference this germplasm|
|trialDbIds|array[string]|The ID which uniquely identifies a trial to search for|
|trialNames|array[string]|The human readable name of a trial to search for|


**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


 

+ Parameters
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>


 
+ Request (application/json)
```
{
    "accessionNumbers": [
        "A0000003",
        "A0000477"
    ],
    "binomialNames": [
        "Aspergillus fructus",
        "Zea mays"
    ],
    "collections": [
        "RDP1",
        "MDP1"
    ],
    "commonCropNames": [
        "Tomatillo",
        "Paw Paw"
    ],
    "externalReferenceIDs": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceIds": [
        "doi:10.155454/12341234",
        "14a19841"
    ],
    "externalReferenceSources": [
        "DOI",
        "Field App Name"
    ],
    "familyCodes": [
        "fa000203",
        "fa009965"
    ],
    "genus": [
        "Aspergillus",
        "Zea"
    ],
    "germplasmDbIds": [
        "e9c6edd7",
        "1b1df4a6"
    ],
    "germplasmNames": [
        "A0000003",
        "A0000477"
    ],
    "germplasmPUIs": [
        "http://pui.per/accession/A0000003",
        "http://pui.per/accession/A0000477"
    ],
    "instituteCodes": [
        "PER001",
        "NOR001"
    ],
    "page": 0,
    "pageSize": 1000,
    "parentDbIds": [
        "72c1001f",
        "7346c553"
    ],
    "progenyDbIds": [
        "16e16a7e",
        "ce06cf9e"
    ],
    "programDbIds": [
        "8f5de35b",
        "0e2d4a13"
    ],
    "programNames": [
        "Better Breeding Program",
        "Best Breeding Program"
    ],
    "species": [
        "fructus",
        "mays"
    ],
    "studyDbIds": [
        "cf6c4bd4",
        "691e69d6"
    ],
    "studyNames": [
        "The First Bob Study 2017",
        "Wheat Yield Trial 246"
    ],
    "synonyms": [
        "variety_1",
        "2c38f9b6"
    ],
    "trialDbIds": [
        "d2593dc2",
        "9431a731"
    ],
    "trialNames": [
        "All Yield Trials 2016",
        "Disease Resistance Study Comparison Group"
    ]
}
```



+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "biologicalStatusOfAccessionCode": "420",
                "biologicalStatusOfAccessionDescription": "Genetic stock",
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "collection": "Rice Diversity Panel 1 (RDP1)",
                "commonCropName": "Maize",
                "countryOfOriginCode": "BES",
                "defaultDisplayName": "A0000003",
                "documentationURL": "https://wiki.brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A0000123",
                        "donorInstituteCode": "PER001"
                    }
                ],
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "genus": "Aspergillus",
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "germplasmOrigin": [
                    {
                        "coordinateUncertainty": "20",
                        "coordinates": {
                            "geometry": {
                                "coordinates": [
                                    -76.506042,
                                    42.417373,
                                    123
                                ],
                                "type": "Point"
                            },
                            "type": "Feature"
                        }
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute",
                "pedigree": "A0000001/A0000002",
                "seedSource": "INRA:095115_inra",
                "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
                "species": "fructus",
                "speciesAuthority": "Smith, 1822",
                "storageTypes": [
                    {
                        "code": "20",
                        "description": "Field collection"
                    },
                    {
                        "code": "11",
                        "description": "Short term"
                    }
                ],
                "subtaxa": "Aspergillus fructus A",
                "subtaxaAuthority": "Smith, 1822",
                "synonyms": [
                    {
                        "synonym": "variety_1",
                        "type": "Pre-Code"
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "NCBI",
                        "taxonId": "2026747"
                    }
                ]
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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




### Get - /search/germplasm/{searchResultsDbId} [GET /brapi/v2/search/germplasm/{searchResultsDbId}{?page}{?pageSize}]

Get the results of a `Germplasm` search request <br/>
Clients should submit a search request using the corresponding `POST /search/germplasm` endpoint.
Search requests allow a client to send a complex query for data. However, the server may not respond with the search results immediately. 
If a server needs more time to process the request, it might respond with a `searchResultsDbId`. 
Use this endpoint to retrieve the results of the search. <br/> 
Review the <a target="_blank" href="https://wiki.brapi.org/index.php/Search_Services#POST_Search_Entity">Search Services documentation</a> for additional implementation details.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection  MCPD (v2.1) (ACCENUMB) 2. This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection (e.g. "PI 113869").|
|acquisitionDate|string (date)|The date this germplasm was acquired by the genebank   MCPD (v2.1) (ACQDATE) 12. Date on which the accession entered the collection [YYYYMMDD] where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or "00" [double zero].|
|additionalInfo|object|Additional arbitrary info|
|biologicalStatusOfAccessionCode|string|MCPD (v2.1) (SAMPSTAT) 19. The coding scheme proposed can be used at 3 different levels of detail: either by using the general codes such as 100, 200, 300, 400, or by using the more specific codes such as 110, 120, etc.   100) Wild  110) Natural  120) Semi-natural/wild  130) Semi-natural/sown  200) Weedy  300) Traditional cultivar/landrace  400) Breeding/research material  410) Breeders line  411) Synthetic population  412) Hybrid  413) Founder stock/base population  414) Inbred line (parent of hybrid cultivar)  415) Segregating population  416) Clonal selection  420) Genetic stock  421) Mutant (e.g. induced/insertion mutants, tilling populations)  422) Cytogenetic stocks (e.g. chromosome addition/substitution, aneuploids,  amphiploids)  423) Other genetic stocks (e.g. mapping populations)  500) Advanced or improved cultivar (conventional breeding methods)  600) GMO (by genetic engineering)  999) Other (Elaborate in REMARKS field)|
|biologicalStatusOfAccessionDescription|string|Supplemental text description for 'biologicalStatusOfAccessionCode'|
|breedingMethodDbId|string|The unique identifier for the breeding method used to create this germplasm|
|breedingMethodName|string|human readable name of the breeding method|
|collection|string|A specific panel/collection/population name this germplasm belongs to.|
|commonCropName|string|Common name for the crop   MCPD (v2.1) (CROPNAME) 10. Common name of the crop. Example: "malting barley", "mas".|
|countryOfOriginCode|string|3-letter ISO 3166-1 code of the country in which the sample was originally collected   MCPD (v2.1) (ORIGCTY) 13. 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.). Note- Descriptors 14 to 16 below should be completed accordingly only if it was "collected".|
|defaultDisplayName|string|Human readable name used for display purposes|
|documentationURL|string (uri)|A URL to the human readable documentation of this object|
|donors|array[object]|List of donor institutes|
|donorAccessionNumber|string|The accession number assigned by the donor                                MCPD (v2.1) (DONORNUMB) 23. Identifier assigned to an accession by the donor. Follows ACCENUMB standard.|
|donorInstituteCode|string|The institute code for the donor institute <br/>MCPD (v2.1) (DONORCODE) 22. FAO WIEWS code of the donor institute. Follows INSTCODE standard.|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|**Deprecated in v2.1** Please use `referenceId`. Github issue number #460   The external reference ID. Could be a simple string or a URI.|
|referenceId|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|genus|string|Genus name for taxon. Initial uppercase letter required.  MCPD (v2.1) (GENUS) 5. Genus name for taxon. Initial uppercase letter required.  MIAPPE V1.1 (DM-43) Genus - Genus name for the organism under study, according to standard scientific nomenclature.|
|germplasmDbId|string|The ID which uniquely identifies a germplasm within the given database server  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc. This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.|
|germplasmName|string|Name of the germplasm. It can be the preferred name and does not have to be unique.  MCPD (v2.1) (ACCENAME) 11. Either a registered or other designation given to the material received, other than the donors accession number (23) or collecting number (3). First letter uppercase. Multiple names are separated by a semicolon without space.|
|germplasmOrigin|array[object]|Information for material (orchard, natural sites, ...). Geographic identification of the plants from which seeds or cutting have been taken to produce that germplasm.|
|coordinateUncertainty|string|Uncertainty associated with the coordinates in meters. Leave the value empty if the uncertainty is unknown.|
|coordinates|object|One geometry as defined by GeoJSON (RFC 7946). All coordinates are decimal values on the WGS84 geographic coordinate reference system.  Copied from RFC 7946 Section 3.1.1  A position is an array of numbers. There MUST be two or more elements. The first two elements are longitude and latitude, or easting and northing, precisely in that order and using decimal numbers. Altitude or elevation MAY be included as an optional third element.|
|geometry|object|A geometry as defined by GeoJSON (RFC 7946). In this context, only Point or Polygon geometry are allowed.|
|type|string|The literal string "Feature"|
|germplasmPUI|string|The Permanent Unique Identifier which represents a germplasm  MIAPPE V1.1 (DM-41) Biological material ID - Code used to identify the biological material in the data file. Should be unique within the Investigation. Can correspond to experimental plant ID, seed lot ID, etc This material identification is different from a BiosampleID which corresponds to Observation Unit or Samples sections below.  MIAPPE V1.1 (DM-51) Material source DOI - Digital Object Identifier (DOI) of the material source  MCPD (v2.1) (PUID) 0. Any persistent, unique identifier assigned to the accession so it can be unambiguously referenced at the global level and the information associated with it harvested through automated means. Report one PUID for each accession. The Secretariat of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA) is facilitating the assignment of a persistent unique identifier (PUID), in the form of a DOI, to PGRFA at the accession level. Genebanks not applying a true PUID to their accessions should use, and request recipients to use, the concatenation of INSTCODE, ACCENUMB, and GENUS as a globally unique identifier similar in most respects to the PUID whenever they exchange information on accessions with third parties.|
|germplasmPreprocessing|string|Description of any process or treatment applied uniformly to the germplasm, prior to the study itself. Can be provided as free text or as an accession number from a suitable controlled vocabulary.|
|instituteCode|string|The code for the institute that maintains the material.   MCPD (v2.1) (INSTCODE) 1. FAO WIEWS code of the institute where the accession is maintained. The codes consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. PER001). The current set of institute codes is available from http://www.fao.org/wiews. For those institutes not yet having an FAO Code, or for those with "obsolete" codes, see "Common formatting rules (v)".|
|instituteName|string|The name of the institute that maintains the material|
|pedigree|string|The cross name and optional selection history.  MCPD (v2.1) (ANCEST) 20. Information about either pedigree or other description of ancestral information (e.g. parent variety in case of mutant or selection). For example a pedigree 'Hanna/7*Atlas//Turk/8*Atlas' or a description 'mutation found in Hanna', 'selection from Irene' or 'cross involving amongst others Hanna and Irene'.|
|seedSource|string|An identifier for the source of the biological material <br/>MIAPPE V1.1 (DM-50) Material source ID (Holding institute/stock centre, accession) - An identifier for the source of the biological material, in the form of a key-value pair comprising the name/identifier of the repository from which the material was sourced plus the accession number of the repository for that material. Where an accession number has not been assigned, but the material has been derived from the crossing of known accessions, the material can be defined as follows: "mother_accession X father_accession", or, if father is unknown, as "mother_accession X UNKNOWN". For in situ material, the region of provenance may be used when an accession is not available.|
|seedSourceDescription|string|Description of the material source  MIAPPE V1.1 (DM-56) Material source description - Description of the material source|
|species|string|Specific epithet portion of the scientific name in lowercase letters.  MCPD (v2.1) (SPECIES) 6. Specific epithet portion of the scientific name in lowercase letters. Only the following abbreviation is allowed: "sp."   MIAPPE V1.1 (DM-44) Species - Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.|
|speciesAuthority|string|The authority organization responsible for tracking and maintaining the species name   MCPD (v2.1) (SPAUTHOR) 7. Provide the authority for the species name.|
|storageTypes|array[object]|The type of storage this germplasm is kept in at a genebank.|
|code|string|The 2 digit code representing the type of storage this germplasm is kept in at a genebank.   MCPD (v2.1) (STORAGE) 26. If germplasm is maintained under different types of storage, multiple choices are allowed, separated by a semicolon (e.g. 20;30). (Refer to FAO/IPGRI Genebank Standards 1994 for details on storage type.)   10) Seed collection  11) Short term  12) Medium term  13) Long term  20) Field collection  30) In vitro collection  40) Cryo-preserved collection  50) DNA collection  99) Other (elaborate in REMARKS field)|
|description|string|A supplemental text description of the storage type|
|subtaxa|string|Subtaxon can be used to store any additional taxonomic identifier.  MCPD (v2.1) (SUBTAXA) 8. Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: "subsp." (for subspecies); "convar." (for convariety); "var." (for variety); "f." (for form); "Group" (for "cultivar group").  MIAPPE V1.1 (DM-44) Infraspecific name - Name of any subtaxa level, including variety, crossing name, etc. It can be used to store any additional taxonomic identifier. Either free text description or key-value pair list format (the key is the name of the rank and the value is the value of  the rank). Ranks can be among the following terms: subspecies, cultivar, variety, subvariety, convariety, group, subgroup, hybrid, line, form, subform. For MCPD compliance, the following abbreviations are allowed: subsp. (subspecies); convar. (convariety); var. (variety); f. (form); Group (cultivar group).|
|subtaxaAuthority|string|The authority organization responsible for tracking and maintaining the subtaxon information  MCPD (v2.1) (SUBTAUTHOR) 9. Provide the subtaxon authority at the most detailed taxonomic level.|
|synonyms|array[object]|List of alternative names or IDs used to reference this germplasm  MCPD (v2.1) (OTHERNUMB) 24. Any other identifiers known to exist in other collections for this accession. Use the following format: INSTCODE:ACCENUMB;INSTCODE:identifier;INSTCODE and identifier are separated by a colon without space. Pairs of INSTCODE and identifier are separated by a semicolon without space. When the institute is not known, the identifier should be preceded by a colon.|
|synonym|string|Alternative name or ID used to reference this germplasm|
|type|string|A descriptive classification for this synonym|
|taxonIds|array[object]|The list of IDs for this SPECIES from different sources. If present, NCBI Taxon should be always listed as "ncbiTaxon" preferably with a purl. The rank of this ID should be species.  MIAPPE V1.1 (DM-42) Organism - An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.|
|sourceName|string|The human readable name of the taxonomy provider|
|taxonId|string|The identifier (name, ID, URI) of a particular taxonomy within the source provider|


 

+ Parameters
    + searchResultsDbId (Required, ) ... Unique identifier which references the search results
    + page (Optional, ) ... Used to request a specific page of data to be returned.The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.
    + pageSize (Optional, ) ... The size of the pages to be returned. Default is `1000`.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
                "biologicalStatusOfAccessionCode": "420",
                "biologicalStatusOfAccessionDescription": "Genetic stock",
                "breedingMethodDbId": "ffcce7ef",
                "breedingMethodName": "Male Backcross",
                "collection": "Rice Diversity Panel 1 (RDP1)",
                "commonCropName": "Maize",
                "countryOfOriginCode": "BES",
                "defaultDisplayName": "A0000003",
                "documentationURL": "https://wiki.brapi.org",
                "donors": [
                    {
                        "donorAccessionNumber": "A0000123",
                        "donorInstituteCode": "PER001"
                    }
                ],
                "externalReferences": [
                    {
                        "referenceId": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceId": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "genus": "Aspergillus",
                "germplasmDbId": "d4076594",
                "germplasmName": "A0000003",
                "germplasmOrigin": [
                    {
                        "coordinateUncertainty": "20",
                        "coordinates": {
                            "geometry": {
                                "coordinates": [
                                    -76.506042,
                                    42.417373,
                                    123
                                ],
                                "type": "Point"
                            },
                            "type": "Feature"
                        }
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A0000003",
                "germplasmPreprocessing": "EO:0007210; transplanted from study 2351 observation unit ID: pot:894",
                "instituteCode": "PER001",
                "instituteName": "The BrAPI Institute",
                "pedigree": "A0000001/A0000002",
                "seedSource": "INRA:095115_inra",
                "seedSourceDescription": "Branches were collected from a 10-year-old tree growing in a progeny trial established in a loamy brown earth soil.",
                "species": "fructus",
                "speciesAuthority": "Smith, 1822",
                "storageTypes": [
                    {
                        "code": "20",
                        "description": "Field collection"
                    },
                    {
                        "code": "11",
                        "description": "Short term"
                    }
                ],
                "subtaxa": "Aspergillus fructus A",
                "subtaxaAuthority": "Smith, 1822",
                "synonyms": [
                    {
                        "synonym": "variety_1",
                        "type": "Pre-Code"
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "NCBI",
                        "taxonId": "2026747"
                    }
                ]
            }
        ]
    }
}
```

+ Response 202 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
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
        "searchResultsDbId": "551ae08c"
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

