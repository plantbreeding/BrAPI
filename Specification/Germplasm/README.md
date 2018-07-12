# Group Germplasm
Fun Fact: The plural of germplasm is germplasm (no "s").





## Get Breedingmethods by breedingMethodDbId  [GET /brapi/v1/breedingmethods/{breedingMethodDbId}]



<a>example.com/brapi/v1/breedingmethods/{breedingMethodDbId}</a> 

+ Parameters
    + breedingMethodDbId (Required, string) ... Internal database identifier for a breeding method


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
        "breedingMethodDbId": "BM987",
        "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate.",
        "name": "Male Backcross"
    }
}
```



## Get Breedingmethods  [GET /brapi/v1/breedingmethods{?pageSize}{?page}]

 Scope: Germplasm
Get the list of germplasm breeding methods available in a system.
<a>example.com/brapi/v1/breedingmethods</a> 

+ Parameters
    + pageSize (Optional, integer) ... The size of the pages to be returned. Default is `1000`.
    + page (Optional, integer) ... Which result page is requested. The page indexing starts at 0 (the first page is 'page'= 0). Default is `0`.


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
            {
                "abbreviation": "MBCR",
                "breedingMethodDbId": "BM987",
                "description": "Backcross to recover a specific gene. The coding in the genealogical table records which parent was used as the male in each cycle. Each entity kept separate.",
                "name": "Male Backcross"
            },
            {
                "abbreviation": "DSP",
                "breedingMethodDbId": "BM324",
                "description": "Derivation through selection of a single plant, inflorescence, fruit or seed from a population",
                "name": "Single plant selection"
            }
        ]
    }
}
```



## Get Germplasm-search  [GET /brapi/v1/germplasm-search{?germplasmPUI}{?germplasmDbId}{?germplasmName}{?commonCropName}{?pageSize}{?page}]

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
            {
                "accessionNumber": "ITC0609",
                "acquisitionDate": "1947-01-31",
                "biologicalStatusOfAccessionCode": 412,
                "commonCropName": "banana",
                "countryOfOriginCode": "UNK",
                "defaultDisplayName": "Pahang",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "genus": "Musa",
                "germplasmDbId": "01BEL084609",
                "germplasmName": "Pahang",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "instituteCode": "01BEL084",
                "instituteName": "ITC",
                "pedigree": "TOBA97/SW90.1057",
                "species": "acuminata",
                "speciesAuthority": "",
                "subtaxa": "sp malaccensis var pahang",
                "subtaxaAuthority": "",
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
                "typeOfGermplasmStorageCode": [
                    10
                ]
            },
            {
                "accessionNumber": "ITC0685",
                "acquisitionDate": "1977-01-31",
                "biologicalStatusOfAccessionCode": 412,
                "commonCropName": "banana",
                "countryOfOriginCode": "UNK",
                "defaultDisplayName": "Pah",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "genus": "Musa",
                "germplasmDbId": "03REL084609",
                "germplasmName": "Pah",
                "germplasmPUI": "doi:10.15454/328757862534E12",
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "instituteCode": "01BEL084",
                "instituteName": "ITC",
                "pedigree": "TOBA97/SW90.1057",
                "species": "acuminata",
                "speciesAuthority": "",
                "subtaxa": "sp malaccensis var pah",
                "subtaxaAuthority": "",
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
                "typeOfGermplasmStorageCode": [
                    10
                ]
            }
        ]
    }
}
```



## Post Germplasm-search  [POST /brapi/v1/germplasm-search]

 Implemented by: GnpIS, Germinate (GET only)
See <a href="#introduction/search-services">Search Services</a> for additional implementation details.
Notes: The germplasm and germplasm MCPD calls were merged.  The MCPD fields are optional and indicated as such with the [MCPD] prefix in the description field of the "Response data types" table. Please use the "features" hash of the "calls" call to communicate with clients as to whether MCPD is supported by your implementation.
Addresses these needs: 1. General germplasm search mechanism that accepts POST for complex queries 2. possibility to search germplasm by more parameters than those allowed by the existing germplasm search 3. possibility to get MCPD details by PUID rather than dbId
Use POST for large queries (>2K bytes).  

+ Parameters
 
+ Request (application/json)
```
/definitions/germplasmSearchRequest
```



+ Response 200 (application/json)
```
{
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 1,
            "pageSize": 100,
            "totalCount": 102,
            "totalPages": 2
        },
        "status": []
    },
    "result": {
        "data": [
            {
                "accessionNumber": "ITC0609",
                "acquisitionDate": "1947-01-31",
                "biologicalStatusOfAccessionCode": 412,
                "commonCropName": "banana",
                "countryOfOriginCode": "UNK",
                "defaultDisplayName": "Pahang",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "genus": "Musa",
                "germplasmDbId": "01BEL084609",
                "germplasmName": "Pahang",
                "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "instituteCode": "01BEL084",
                "instituteName": "ITC",
                "pedigree": "TOBA97/SW90.1057",
                "species": "acuminata",
                "speciesAuthority": "",
                "subtaxa": "sp malaccensis var pahang",
                "subtaxaAuthority": "",
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
                "typeOfGermplasmStorageCode": [
                    10
                ]
            },
            {
                "accessionNumber": "ITC0685",
                "acquisitionDate": "1977-01-31",
                "biologicalStatusOfAccessionCode": 412,
                "commonCropName": "banana",
                "countryOfOriginCode": "UNK",
                "defaultDisplayName": "Pah",
                "donors": [
                    {
                        "donorAccessionNumber": "",
                        "donorInstituteCode": "",
                        "germplasmPUI": ""
                    }
                ],
                "genus": "Musa",
                "germplasmDbId": "03REL084609",
                "germplasmName": "Pah",
                "germplasmPUI": "doi:10.15454/328757862534E12",
                "germplasmSeedSource": "Female GID:4/Male GID:4",
                "instituteCode": "01BEL084",
                "instituteName": "ITC",
                "pedigree": "TOBA97/SW90.1057",
                "species": "acuminata",
                "speciesAuthority": "",
                "subtaxa": "sp malaccensis var pah",
                "subtaxaAuthority": "",
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
                "typeOfGermplasmStorageCode": [
                    10
                ]
            }
        ]
    }
}
```



## Get Germplasm by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}]

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
        "accessionNumber": "ITC0609",
        "acquisitionDate": "1947-01-31",
        "biologicalStatusOfAccessionCode": 412,
        "commonCropName": "banana",
        "countryOfOriginCode": "UNK",
        "defaultDisplayName": "Pahang",
        "donors": [
            {
                "donorAccessionNumber": "",
                "donorGermplasmPUI": "",
                "donorInstituteCode": ""
            }
        ],
        "genus": "Musa",
        "germplasmDbId": "01BEL084609",
        "germplasmName": "Pahang",
        "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
        "instituteCode": "01BEL084",
        "instituteName": "ITC",
        "pedigree": "TOBA97/SW90.1057",
        "seedSource": "ITC0609-2016-77",
        "species": "acuminata",
        "speciesAuthority": "",
        "subtaxa": "sp malaccensis var pahang",
        "subtaxaAuthority": "",
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
        "typeOfGermplasmStorageCode": [
            10
        ]
    }
}
```



## Get Germplasm Markerprofiles by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/markerprofiles]

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
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": [
            {
                "code": "",
                "message": ""
            }
        ]
    },
    "result": {
        "germplasmDbId": "01BEL084609",
        "markerprofileDbIds": [
            "3939",
            "4484",
            "3993"
        ]
    }
}
```



## Get Germplasm Pedigree by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/pedigree{?notation}{?includeSiblings}]


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
        "defaultDisplayName": "Pahang 1",
        "familyCode": "Cree_x_Bonanza_2018",
        "germplasmDbId": "01BEL084609",
        "parent1DbId": "166",
        "parent1Name": "Cree",
        "parent1Type": "FEMALE",
        "parent2DbId": "143",
        "parent2Name": "Bonanza",
        "parent2Type": "MALE",
        "pedigree": "Cree / Bonanza",
        "siblings": [
            {
                "defaultDisplayName": "Pahang 2",
                "germplasmDbId": "383"
            },
            {
                "defaultDisplayName": "Pahang 3",
                "germplasmDbId": "384"
            }
        ]
    }
}
```



## Get Germplasm Progeny by germplasmDbId  [GET /brapi/v1/germplasm/{germplasmDbId}/progeny]

 Scope: Germplasm
Get the germplasmDbIds for all the Progeny of a particular germplasm.
<a href="https://test-server.brapi.org/brapi/v1/germplasm"> test-server.brapi.org/brapi/v1/germplasm/{germplasmDbId}/progeny</a>  

+ Parameters
    + germplasmDbId (Required, string) ... the internal id of the germplasm


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
        "defaultDisplayName": "Pahang",
        "germplasmDbId": "382",
        "progeny": [
            {
                "defaultDisplayName": "Child 1",
                "germplasmDbId": "402",
                "parentType": "FEMALE"
            },
            {
                "defaultDisplayName": "Child 2",
                "germplasmDbId": "403",
                "parentType": "MALE"
            },
            {
                "defaultDisplayName": "Pahang Selfed",
                "germplasmDbId": "405",
                "parentType": "SELF"
            }
        ]
    }
}
```

