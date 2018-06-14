# Group Germplasm
Fun Fact: The plural of germplasm is germplasm (no "s").





## Breedingmethods/{breedingmethoddbid} [Get /brapi/v1/breedingmethods/{breedingMethodDbId}]



<a>example.com/brapi/v1/breedingmethods/{breedingMethodDbId}</a> 

+ Parameters
    + breedingMethodDbId (Required, string) ... Internal database identifier for a breeding method


+ Response 200 (application/json)
```
{
    "result": {
        "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate.",
        "abbreviation": "MBCR",
        "name": "Male Backcross",
        "breedingMethodDbId": "BM987"
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

## Breedingmethods [Get /brapi/v1/breedingmethods{?pageSize}{?page}]

 Scope: Germplasm
Get the list of germplasm breeding methods available in a system.
<a>example.com/brapi/v1/breedingmethods</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate.",
                "abbreviation": "MBCR",
                "name": "Male Backcross",
                "breedingMethodDbId": "BM987"
            },
            {
                "description": "Derivation through selection of a single plant, inflorescence, fruit or seed from a population",
                "abbreviation": "DSP",
                "name": "Single plant selection",
                "breedingMethodDbId": "BM324"
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

## Germplasm-search [Get /brapi/v1/germplasm-search{?germplasmPUI}{?germplasmDbId}{?germplasmName}{?commonCropName}{?pageSize}{?page}]

 Implemented by: GnpIS, Germinate (GET only)
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Notes: The germplasm and germplasm MCPD calls were merged.  The MCPD fields are optional and indicated as such with the [MCPD] prefix in the description field of the "Response data types" table. Please use the "features" hash of the "calls" call to communicate with clients as to whether MCPD is supported by your implementation.
Addresses these needs: 1. General germplasm search mechanism that accepts POST for complex queries 2. possibility to search germplasm by more parameters than those allowed by the existing germplasm search 3. possibility to get MCPD details by PUID rather than dbId
Use GET when parameter size is less than 2K bytes. <a href="https://test-server.brapi.org/brapi/v1/germplasm"> test-server.brapi.org/brapi/v1/germplasm-search</a>  

+ Parameters
    + germplasmPUI (Optional, string) ... Permanent unique identifier (DOI, URI, etc.)
    + germplasmDbId (Optional, string) ... Internal database identifier
    + germplasmName (Optional, string) ... Name of the germplasm
    + commonCropName (Optional, string) ... The common crop name related to this germplasm
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "countryOfOriginCode": "UNK",
                "commonCropName": "banana",
                "defaultDisplayName": "Pahang",
                "species": "acuminata",
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "germplasmDbId": "01BEL084609",
                "synonyms": [],
                "pedigree": "TOBA97/SW90.1057",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "donors": [
                    {
                        "germplasmPUI": "",
                        "donorAccessionNumber": "",
                        "donorInstituteCode": ""
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "23-E"
                    }
                ],
                "acquisitionDate": "1947-01-31",
                "germplasmName": "Pahang",
                "subtaxa": "sp malaccensis var pahang",
                "instituteName": "ITC",
                "subtaxaAuthority": "",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "speciesAuthority": "",
                "accessionNumber": "ITC0609"
            },
            {
                "countryOfOriginCode": "UNK",
                "commonCropName": "banana",
                "defaultDisplayName": "Pah",
                "species": "acuminata",
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "germplasmDbId": "03REL084609",
                "synonyms": [],
                "pedigree": "TOBA97/SW90.1057",
                "germplasmPUI": "doi:10.15454/328757862534E12",
                "donors": [
                    {
                        "germplasmPUI": "",
                        "donorAccessionNumber": "",
                        "donorInstituteCode": ""
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "23-E"
                    }
                ],
                "acquisitionDate": "1977-01-31",
                "germplasmName": "Pah",
                "subtaxa": "sp malaccensis var pah",
                "instituteName": "ITC",
                "subtaxaAuthority": "",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "speciesAuthority": "",
                "accessionNumber": "ITC0685"
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

## Germplasm-search [Post /brapi/v1/germplasm-search]

 Implemented by: GnpIS, Germinate (GET only)
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Notes: The germplasm and germplasm MCPD calls were merged.  The MCPD fields are optional and indicated as such with the [MCPD] prefix in the description field of the "Response data types" table. Please use the "features" hash of the "calls" call to communicate with clients as to whether MCPD is supported by your implementation.
Addresses these needs: 1. General germplasm search mechanism that accepts POST for complex queries 2. possibility to search germplasm by more parameters than those allowed by the existing germplasm search 3. possibility to get MCPD details by PUID rather than dbId
Use POST for large queries (>2K bytes).  

+ Parameters
 
+ Request (application/json)
/definitions/germplasmSearchRequest

+ Response 200 (application/json)
```
{
    "result": {
        "data": [
            {
                "countryOfOriginCode": "UNK",
                "commonCropName": "banana",
                "defaultDisplayName": "Pahang",
                "species": "acuminata",
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "germplasmDbId": "01BEL084609",
                "synonyms": [],
                "pedigree": "TOBA97/SW90.1057",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "donors": [
                    {
                        "germplasmPUI": "",
                        "donorAccessionNumber": "",
                        "donorInstituteCode": ""
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "23-E"
                    }
                ],
                "acquisitionDate": "1947-01-31",
                "germplasmName": "Pahang",
                "subtaxa": "sp malaccensis var pahang",
                "instituteName": "ITC",
                "subtaxaAuthority": "",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "speciesAuthority": "",
                "accessionNumber": "ITC0609"
            },
            {
                "countryOfOriginCode": "UNK",
                "commonCropName": "banana",
                "defaultDisplayName": "Pah",
                "species": "acuminata",
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "germplasmDbId": "03REL084609",
                "synonyms": [],
                "pedigree": "TOBA97/SW90.1057",
                "germplasmPUI": "doi:10.15454/328757862534E12",
                "donors": [
                    {
                        "germplasmPUI": "",
                        "donorAccessionNumber": "",
                        "donorInstituteCode": ""
                    }
                ],
                "taxonIds": [
                    {
                        "sourceName": "ncbiTaxon",
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "sourceName": "ciradTaxon",
                        "taxonId": "23-E"
                    }
                ],
                "acquisitionDate": "1977-01-31",
                "germplasmName": "Pah",
                "subtaxa": "sp malaccensis var pah",
                "instituteName": "ITC",
                "subtaxaAuthority": "",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "speciesAuthority": "",
                "accessionNumber": "ITC0685"
            }
        ]
    },
    "metadata": {
        "pagination": {
            "pageSize": 100,
            "currentPage": 1,
            "totalPages": 2,
            "totalCount": 102
        },
        "status": [],
        "datafiles": []
    }
}
```

## Germplasm/{germplasmdbid} [Get /brapi/v1/germplasm/{germplasmDbId}]

 Scope: CORE. Status: ACCEPTED.
Implementation target date: PAG2016
Implemented by: Tripal Brapi module, Germinate, Cassavabase
Note: Germplasm Details by germplasmDbId was merged with Germplasm Multi Crop Passport Data. The MCPD fields are optional and marked with the prefix [MCPD].
<a href="https://test-server.brapi.org/brapi/v1/germplasm"> test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}</a>  

+ Parameters
    + germplasmDbId (Required, string) ... The internal id of the germplasm


+ Response 200 (application/json)
```
{
    "result": {
        "countryOfOriginCode": "UNK",
        "commonCropName": "banana",
        "defaultDisplayName": "Pahang",
        "species": "acuminata",
        "typeOfGermplasmStorageCode": [
            10
        ],
        "instituteCode": "01BEL084",
        "genus": "Musa",
        "germplasmDbId": "01BEL084609",
        "synonyms": [],
        "taxonIds": [
            {
                "sourceName": "ncbiTaxon",
                "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
            },
            {
                "sourceName": "ciradTaxon",
                "taxonId": "23-E"
            }
        ],
        "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
        "donors": [
            {
                "donorGermplasmPUI": "",
                "donorAccessionNumber": "",
                "donorInstituteCode": ""
            }
        ],
        "pedigree": "TOBA97/SW90.1057",
        "acquisitionDate": "1947-01-31",
        "germplasmName": "Pahang",
        "subtaxa": "sp malaccensis var pahang",
        "seedSource": "ITC0609-2016-77",
        "instituteName": "ITC",
        "subtaxaAuthority": "",
        "biologicalStatusOfAccessionCode": 412,
        "speciesAuthority": "",
        "accessionNumber": "ITC0609"
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

## Germplasm/{germplasmdbid}/markerprofiles [Get /brapi/v1/germplasm/{germplasmDbId}/markerprofiles]

 Retrieve the markerProfileDbIds for a given Germplasm ID
Scope: GENOTYPING.
Status: ACCEPTED.
Implementation target date: PAG2016
Implemented by: Germinate, Cassavabase
<a href="https://test-server.brapi.org/brapi/v1/germplasm"> test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/markerprofiles</a>  

+ Parameters
    + germplasmDbId (Required, string) ... the internal id of the germplasm


+ Response 200 (application/json)
```
{
    "result": {
        "markerprofileDbIds": [
            "3939",
            "4484",
            "3993"
        ],
        "germplasmDbId": "01BEL084609"
    },
    "metadata": {
        "pagination": {
            "pageSize": 0,
            "currentPage": 0,
            "totalPages": 0,
            "totalCount": 0
        },
        "status": [
            {
                "code": "",
                "message": ""
            }
        ],
        "datafiles": []
    }
}
```

## Germplasm/{germplasmdbid}/pedigree [Get /brapi/v1/germplasm/{germplasmDbId}/pedigree{?notation}{?includeSiblings}]


Scope: CORE. Status: ACCEPTED.
Implementation target date: PAG2016
Implemented by: Germinate, Tripal Brapi Module, Cassavabase (without notation option)
(http://wheat.pw.usda.gov/ggpages/gopher/administration/Template%20for%20Germplasm%20records.html) or [Lamacraft] (http://link.springer.com/article/10.1007%2FBF00021556).
<a href="https://test-server.brapi.org/brapi/v1/germplasm"> test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/pedigree</a>  

+ Parameters
    + germplasmDbId (Required, string) ... the internal id of the germplasm
    + notation (Optional, string) ... text representation of the pedigree
    + includeSiblings (Optional, boolean) ... include array of siblings in response


+ Response 200 (application/json)
```
{
    "result": {
        "crossingPlan": "OPEN_POLLINATION",
        "crossingYear": "2018",
        "pedigree": "Cree / Bonanza",
        "defaultDisplayName": "Pahang 1",
        "siblings": [
            {
                "germplasmDbId": "383",
                "defaultDisplayName": "Pahang 2"
            },
            {
                "germplasmDbId": "384",
                "defaultDisplayName": "Pahang 3"
            }
        ],
        "parent2Name": "Bonanza",
        "parent2Type": "MALE",
        "familyCode": "Cree_x_Bonanza_2018",
        "parent2DbId": "143",
        "parent1Name": "Cree",
        "parent1DbId": "166",
        "germplasmDbId": "01BEL084609",
        "parent1Type": "FEMALE"
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

## Germplasm/{germplasmdbid}/progeny [Get /brapi/v1/germplasm/{germplasmDbId}/progeny]

 Scope: Germplasm
Get the germplasmDbIds for all the Progeny of a particular germplasm.
<a href="https://test-server.brapi.org/brapi/v1/germplasm"> test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/progeny</a>  

+ Parameters
    + germplasmDbId (Required, string) ... the internal id of the germplasm


+ Response 200 (application/json)
```
{
    "result": {
        "defaultDisplayName": "Pahang",
        "germplasmDbId": "382",
        "progeny": [
            {
                "parentType": "FEMALE",
                "germplasmDbId": "402",
                "defaultDisplayName": "Child 1"
            },
            {
                "parentType": "MALE",
                "germplasmDbId": "403",
                "defaultDisplayName": "Child 2"
            },
            {
                "parentType": "SELF",
                "germplasmDbId": "405",
                "defaultDisplayName": "Pahang Selfed"
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