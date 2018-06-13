# Group Germplasm
Fun Fact: The plural of germplasm is germplasm (no "s").





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
        "subtaxa": "sp malaccensis var pahang",
        "species": "acuminata",
        "instituteName": "ITC",
        "synonyms": [],
        "acquisitionDate": "1947-01-31",
        "seedSource": "ITC0609-2016-77",
        "countryOfOriginCode": "UNK",
        "biologicalStatusOfAccessionCode": 412,
        "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
        "speciesAuthority": "",
        "pedigree": "TOBA97/SW90.1057",
        "taxonIds": [
            {
                "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                "sourceName": "ncbiTaxon"
            },
            {
                "taxonId": "23-E",
                "sourceName": "ciradTaxon"
            }
        ],
        "typeOfGermplasmStorageCode": [
            10
        ],
        "germplasmName": "Pahang",
        "germplasmDbId": "01BEL084609",
        "donors": [
            {
                "donorAccessionNumber": "",
                "donorInstituteCode": "",
                "donorGermplasmPUI": ""
            }
        ],
        "instituteCode": "01BEL084",
        "genus": "Musa",
        "commonCropName": "banana",
        "defaultDisplayName": "Pahang",
        "subtaxaAuthority": "",
        "accessionNumber": "ITC0609"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
        "datafiles": [],
        "status": [
            {
                "message": "",
                "code": ""
            }
        ],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
    }
}
```

## Breedingmethods/{breedingmethoddbid} [Get /brapi/v1/breedingmethods/{breedingMethodDbId}]



<a>example.com/brapi/v1/breedingmethods/{breedingMethodDbId}</a> 

+ Parameters
    + breedingMethodDbId (Required, string) ... Internal database identifier for a breeding method


+ Response 200 (application/json)
```
{
    "result": {
        "name": "Male Backcross",
        "breedingMethodDbId": "BM987",
        "abbreviation": "MBCR",
        "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate."
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
                "name": "Male Backcross",
                "breedingMethodDbId": "BM987",
                "abbreviation": "MBCR",
                "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate."
            },
            {
                "name": "Single plant selection",
                "breedingMethodDbId": "BM324",
                "abbreviation": "DSP",
                "description": "Derivation through selection of a single plant, inflorescence, fruit or seed from a population"
            }
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
                "subtaxa": "sp malaccensis var pahang",
                "species": "acuminata",
                "instituteName": "ITC",
                "synonyms": [],
                "acquisitionDate": "1947-01-31",
                "countryOfOriginCode": "UNK",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "speciesAuthority": "",
                "pedigree": "TOBA97/SW90.1057",
                "taxonIds": [
                    {
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                        "sourceName": "ncbiTaxon"
                    },
                    {
                        "taxonId": "23-E",
                        "sourceName": "ciradTaxon"
                    }
                ],
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "germplasmName": "Pahang",
                "germplasmDbId": "01BEL084609",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "commonCropName": "banana",
                "defaultDisplayName": "Pahang",
                "subtaxaAuthority": "",
                "accessionNumber": "ITC0609"
            },
            {
                "subtaxa": "sp malaccensis var pah",
                "species": "acuminata",
                "instituteName": "ITC",
                "synonyms": [],
                "acquisitionDate": "1977-01-31",
                "countryOfOriginCode": "UNK",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "germplasmPUI": "doi:10.15454/328757862534E12",
                "speciesAuthority": "",
                "pedigree": "TOBA97/SW90.1057",
                "taxonIds": [
                    {
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                        "sourceName": "ncbiTaxon"
                    },
                    {
                        "taxonId": "23-E",
                        "sourceName": "ciradTaxon"
                    }
                ],
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "germplasmName": "Pah",
                "germplasmDbId": "03REL084609",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "commonCropName": "banana",
                "defaultDisplayName": "Pah",
                "subtaxaAuthority": "",
                "accessionNumber": "ITC0685"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 1,
            "totalCount": 102,
            "pageSize": 100,
            "totalPages": 2
        }
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
                "subtaxa": "sp malaccensis var pahang",
                "species": "acuminata",
                "instituteName": "ITC",
                "synonyms": [],
                "acquisitionDate": "1947-01-31",
                "countryOfOriginCode": "UNK",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "speciesAuthority": "",
                "pedigree": "TOBA97/SW90.1057",
                "taxonIds": [
                    {
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                        "sourceName": "ncbiTaxon"
                    },
                    {
                        "taxonId": "23-E",
                        "sourceName": "ciradTaxon"
                    }
                ],
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "germplasmName": "Pahang",
                "germplasmDbId": "01BEL084609",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "commonCropName": "banana",
                "defaultDisplayName": "Pahang",
                "subtaxaAuthority": "",
                "accessionNumber": "ITC0609"
            },
            {
                "subtaxa": "sp malaccensis var pah",
                "species": "acuminata",
                "instituteName": "ITC",
                "synonyms": [],
                "acquisitionDate": "1977-01-31",
                "countryOfOriginCode": "UNK",
                "biologicalStatusOfAccessionCode": 412,
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "germplasmPUI": "doi:10.15454/328757862534E12",
                "speciesAuthority": "",
                "pedigree": "TOBA97/SW90.1057",
                "taxonIds": [
                    {
                        "taxonId": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                        "sourceName": "ncbiTaxon"
                    },
                    {
                        "taxonId": "23-E",
                        "sourceName": "ciradTaxon"
                    }
                ],
                "typeOfGermplasmStorageCode": [
                    10
                ],
                "germplasmName": "Pah",
                "germplasmDbId": "03REL084609",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "instituteCode": "01BEL084",
                "genus": "Musa",
                "commonCropName": "banana",
                "defaultDisplayName": "Pah",
                "subtaxaAuthority": "",
                "accessionNumber": "ITC0685"
            }
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
                "defaultDisplayName": "Child 1",
                "germplasmDbId": "402"
            },
            {
                "parentType": "MALE",
                "defaultDisplayName": "Child 2",
                "germplasmDbId": "403"
            },
            {
                "parentType": "SELF",
                "defaultDisplayName": "Pahang Selfed",
                "germplasmDbId": "405"
            }
        ]
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
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
        "pedigree": "Cree / Bonanza",
        "parent2DbId": "143",
        "parent1DbId": "166",
        "crossingPlan": "OPEN_POLLINATION",
        "defaultDisplayName": "Pahang 1",
        "parent2Name": "Bonanza",
        "parent2Type": "MALE",
        "germplasmDbId": "01BEL084609",
        "crossingYear": "2018",
        "parent1Name": "Cree",
        "siblings": [
            {
                "defaultDisplayName": "Pahang 2",
                "germplasmDbId": "383"
            },
            {
                "defaultDisplayName": "Pahang 3",
                "germplasmDbId": "384"
            }
        ],
        "parent1Type": "FEMALE",
        "familyCode": "Cree_x_Bonanza_2018"
    },
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
    }
}
```