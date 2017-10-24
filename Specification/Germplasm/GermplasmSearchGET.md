##  Germplasm Search [/brapi/v1/germplasm-search?germplasmName={germplasmName}&germplasmDbId={germplasmDdId}&germplasmPUI={germplasmPUI}&pageSize={pageSize}&page={page}]

Implemented by: GnpIS, Germinate (GET only)

Notes:
The germplasm and gerplasm MCPD calls were merged.  The MCPD fields are optional and indicated as such with the [MCPD] prefix in the description field of the 'Response data types' table. Please use the 'features' hash of the 'calls' call to communicate with clients as to whether MCPD is supported by your implementation.

Adresses these needs:
1. General germplasm search mechanism that accepts POST for complex queries
2. possibility to search germplams by more parameters than those alowed by the existing germplasm search
3. possibility to get MCPD details by PUID rather than dbId

###### Response data types
|Variable|Datatype|Description|Required|
|------|------|------|:-----:|
|metadata|object|pagination, status|Y|
|pagination|object|pageSize, currentPage, totalCount, totalPages|Y|
|status|list|code, message|Y|
|result|object|data|Y|
|data|array of objects|Array (possibly empty) of germplasm records|Y|
|germplasmDbId|string|Internal database identifier|Y|
|defaultDisplayName|string|A string that can be displayed to the user|Y|
|accessionNumber|string|This is the unique identifier for accessions within a genebank, and is assigned when a sample is entered into the genebank collection||
|germplasmName|string|Name of the germplasm. It can be the prefered name and does not have to be unique||
|germplasmPUI|string|Permanent identifier (e.g. URI, DOI, LSID)||
|pedigree|string|Cross name with optional selection history.||
|seedSource|string|Seed source||
|synonyms|array of string|List of other germplasm name||
|commonCropName|string|[MCPD] Common name fo the crop (e.g. wheat, rice, maize, cassava, banana)||
|instituteCode|string|[MCPD] Institute that has bred the material. Note: The code may consist of the 3-letter ISO 3166 country code of the country where the institute is located plus a number (e.g. COL001) as recommended by FAO WIEWS |Y|
|instituteName|string|[MCPD] Name of the institute (or person) that bred the material.||
|biologicalStatusOfAccessionCode|string|[MCPD] 400) Breeding/research material 410) Breeder's line 411) Synthetic population 412) Hybrid 413) Founder stock/base population 414) Inbred line (parent of hybrid cultivar) 415) Segregating population 416) Clonal selection 420) Genetic stock 421) Mutant (e.g. induced/insertion mutants, tilling populations) 422) Cytogenetic stocks  423) Other genetic stocks (e.g. mapping populations)500) Advanced or improved cultivar (conventional breeding methods) 600) GMO (by genetic engineering) 999) Other||
|countryOfOriginCode|string|[MCPD] 3-letter ISO 3166-1 code of the country in which the sample was originally collected (e.g. landrace, crop wild relative, farmers' variety), bred or selected (breeding lines, GMOs, segregating populations, hybrids, modern cultivars, etc.).||
|typeOfGermplasmStorageCode|array of string|[MCPD] If germplasm is maintained under different types of storage, multiple choices are allowed. 10) Seed collection 11) Short term 12) Medium term 13) Long term 20) Field collection 30) In vitro collection 40) Cryopreserved collection 50) DNA collection 99) Other (elaborate in REMARKS field)||
|genus|string|[MCPD] Genus name for taxon. Initial uppercase letter required.||
|species|string|[MCPD] Specific epithet portion of the scientific name in lowercase letters.||
|taxonIds|array of object{"sourceName":"taxonId"}| The list of IDs for this SPECIES in different source. If present, NCBI Taxon should be always listed, as "ncbiTaxon" preferably with a purl ||
|speciesAuthority|string|[MCDP]||
|subtaxa|string|[MCPD] Subtaxon can be used to store any additional taxonomic identifier. The following abbreviations are allowed: ‘subsp.’ (for subspecies); ‘convar.’ (for convariety); ‘var.’ (for variety); ‘f.’ (for form); ‘Group’ (for ‘cultivar group’).|
|subtaxaAuthority|string|[MCDP] ||
|donors|array of object|[MCPD] code of the donor institute and Identifier assigned to an accession by the donor, and permanent identifier.||
|acquisitionDate|string|[MCPD] Date on which the accession entered the collection where YYYY is the year, MM is the month and DD is the day. Missing data (MM or DD) should be indicated with hyphens or ‘00’ [double zero].|

### Germplasm search through GET [GET]

Use GET when parameter size is less than 2K bytes.

+ Parameters
   + germplasmPUI (optional, string, `http://data.inra.fr/accession/234Col342`) ... Permanent unique identifier (DOI, URI, etc.)
   + germplasmDbId (optional, string, `986`) ... Internal database identifier
   + germplasmName (optional, string, `Pah`, `Pahang`) ... Name of the germplasm
   + pageSize (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
   + page (optional, integer, `10`) ... Which result page is requested

+ Response 200 (application/json)

        {
            "metadata": {
                "status": [],
                "datafiles": [],
                "pagination": {
                    "pageSize": 1000,
                    "currentPage": 0,
                    "totalCount": 2,
                    "totalPages": 1
                }
            },
            "result": {
                "data": [
                    {
                        "germplasmDbId": "01BEL084609",
                        "defaultDisplayName": "Pahang",
                        "accessionNumber": "ITC0609",
                        "germplasmName": "Pahang",
                        "germplasmPUI": "http://www.crop-diversity.org/mgis/accession/01BEL084609",
                        "pedigree": "TOBA97/SW90.1057",
                        "germplasmSeedSource": "Female GID:4/Male GID:4",
                        "synonyms": [ ],
                        "commonCropName": "banana",
                        "instituteCode": "01BEL084",
                        "instituteName": "ITC",
                        "biologicalStatusOfAccessionCode": 412,
                        "countryOfOriginCode": "UNK",
                        "typeOfGermplasmStorageCode": [10],
                        "genus": "Musa",
                        "species": "acuminata",
                        "taxonIds": [{"ncbiTaxon":"http://purl.obolibrary.org/obo/NCBITaxon_4641"}, {"ciradTaxon":"23-E"}],
                        "speciesAuthority": "",
                        "subtaxa": "sp malaccensis var pahang",
                        "subtaxaAuthority": "",
                        "donors": [
                            {
                                "donorAccessionNumber": "",
                                "donorInstituteCode": "",
                                "germplasmPUI": ""
                            }
                        ],
                        "acquisitionDate": "19470131"
                    }, {
                        "germplasmDbId": "03REL084609",
                        "defaultDisplayName": "Pah",
                        "accessionNumber": "ITC0685",
                        "germplasmName": "Pah",
                        "germplasmPUI": "doi:10.15454/328757862534E12",
                        "pedigree": "TOBA97/SW90.1057",
                        "germplasmSeedSource": "Female GID:4/Male GID:4",
                        "synonyms": [ ],
                        "commonCropName": "banana",
                        "instituteCode": "01BEL084",
                        "instituteName": "ITC",
                        "biologicalStatusOfAccessionCode": 412,
                        "countryOfOriginCode": "UNK",
                        "typeOfGermplasmStorageCode": [10],
                        "genus": "Musa",
                        "species": "acuminata",
                        "taxonIds": [{"ncbiTaxon":"4641"}, {"ciradTaxon":"23-E"}],
                        "speciesAuthority": "",
                        "subtaxa": "sp malaccensis var pah",
                        "subtaxaAuthority": "",
                        "donors": [
                            {
                                "donorAccessionNumber": "",
                                "donorInstituteCode": "",
                                "germplasmPUI": ""
                            }
                        ],
                        "acquisitionDate": "19770131"
                    }
                ]
            }
        }
