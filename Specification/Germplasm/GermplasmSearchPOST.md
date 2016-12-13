### Germplasm search through POST [POST]

Use POST for large queries (>2K bytes).

+ Request (application/json)
    
        {
            "germplasmPUI" : "http://...", // (optional, text, `http://data.inra.fr/accession/234Col342`) ... The name or synonym of external genebank accession identifier
            "germplasmDbId" : 986, // (optional, text, `986`) ... The name or synonym of external genebank accession identifier
            "germplasmSpecies" : "tomato", // (optional, text, `aestivum`) ... The name or synonym of genus or species ( merge with below ?)
            "germplasmGenus" : "Solanum lycopersicum", //(optional, text, `Triticum, Hordeum`) ... The name or synonym of genus or species
            "germplasmName" : "XYZ1", // (optional, text, `Triticum, Hordeum`) ... The name or synonym of the accession
            // the following need review (should be removed?)
            //"germplasmSubTaxa (optional, text, `cv. Charger, subsp. aestivum`) ... The name or synonym of MCPD subTaxa. Exact Match, abreviations must be MCPD compliant (‘subsp.’ for 'subspecies'; ‘convar.’ for "convariety" ‘var.’ for variety; ‘f.’ for 'form'; ‘Group’ for ‘cultivar group’)
            //+ panel (optional, text, `breedingProgramPanel2011`) ... The name of a specific panel 
            //+ collection (optional, text, `BRCCollection_Wheat`) ... The name of a specific Collection    
            "pageSize" : 100, // (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
            "page":  1 (optional, integer, `10`) ... Which result page is requested
        }
 
+ Response 200 (application/json)

        {
            "metadata": {
                "status": null,
                "datafiles": [],
                "pagination": {
                    "pageSize": 10,
                    "currentPage": 1,
                    "totalCount": 2,
                    "totalPages": 1
                }
            },
            "result": {
                "data":[
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
                        "typeOfGermplasmStorageCode": 10,
                        "genus": "Musa",
                        "species": "acuminata",
                        "speciesAuthority": "",
                        "subtaxa": "sp malaccensis var pahang",
                        "subtaxaAuthority": "",
                        "donors": 
                        [
                            {
                                "donorAccessionNumber": "",
                                "donorInstituteCode": "",
                                "germplasmPUI": ""
                            }
                        ],
                        "acquisitionDate": "19470131"
                    ,{
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
                        "typeOfGermplasmStorageCode": 10,
                        "genus": "Musa",
                        "species": "acuminata",
                        "speciesAuthority": "",
                        "subtaxa": "sp malaccensis var pah",
                        "subtaxaAuthority": "",
                        "donors": 
                        [
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

