
# Group High-Dimensional Phenotypes

High-Dimensional Phenotypes description




### Get - /metabolomics [GET /brapi/v2/metabolomics{?metabolomicsProtocolDbId}{?observationUnitDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of Metabolomics Protocols



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|description|
|equipment|object||
|analysisType|string|MS or NMR. If NMR is selected, the rest of Equipment are not needed|
|chromatographyColumn|string|User free text to specify brand of chromotography column|
|chromatographySystem|string|User free text to specify brand of chromotography system|
|chromatographyType|string|description|
|msInstrumentName|string|User free text to specify brand of MS system|
|msInstrumentType|string|User free text, e.g. time of flight (TOF), triple quadropole|
|msIonMode|string|Negative, Positive, Both|
|msType|string|Electron Ionization (EI), Electrospray Ionization (ESI), Atmospheric Pressure Chemical Ionization (APCI), Matrix Assisted Laser Desorption Ionization (MALDI), Other (please specify below)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|headerColumns|array[object]|Column definitions for any matrix with this protocol|
|chebi|string|CHEBI id; standard formula|
|chemicalFormula|string|standard formula|
|chemicalSpecies|object|Family of chemical|
|compoundDbId|string|compound ID in this (breedbase) database to link to other files|
|inchi|string|InCHI is another standard universal formula|
|inchiKey|string|shortened version of inchi; users choose one or the other|
|massToCharge|string|m/z ratio, standard from output, should be a number|
|metaboliteIdentification|string|Name of compound|
|pubChemURL|string|pubchem URL is another standard|
|retentionTime|string|retention time, also standard from machine output; users shoud confirm that unit is 'seconds'|
|spectraSource|object|The source database that defines the connection between spectra and compound|
|database|string|Database identifier (Name or URL)|
|databaseVersion|string|Family of chemical|
|synonyms|array[string]|Name of compound|
|phenotypeUnits|string|Free text, e.g. relative abundance, BLUP, drBLUP, concentration (specifiy units, e.g. ug/g)|
|protocol|object||
|chromatography|string|the LC protocol, instrument settings, calibration procedure|
|massSpectrometry|string|instrument settings, calibration procedure|
|metaboliteIdentification|string|metabolite annotations were assigned to peaks|
|phenotype|string|BLUPs were calculated from the peak area|
|rawDataTransformation|string|the LCMS machine files were transformed into peak area|
|sampleCollection|string|the tissue, time point, if the sample was frozen|
|sampleExtraction|string|the extraction protocol used|
|protocolDbId|string|The ID which uniquely identifies the Metabolomics Matrix|
|publications|array[string]|Relevent publication(s), DOI with details|


 

+ Parameters
    + metabolomicsProtocolDbId (Optional, ) ... description
    + observationUnitDbId (Optional, ) ... description
    + externalReferenceID (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceID` parameter)
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
                "additionalInfo": {},
                "documentationURL": "https://wiki.brapi.org",
                "equipment": {
                    "analysisType": "MS",
                    "chromatographyColumn": "brand of chromotography column",
                    "chromatographySystem": "brand of chromotography system",
                    "chromatographyType": "LC",
                    "msInstrumentName": "brand of MS system",
                    "msInstrumentType": "TOF",
                    "msIonMode": "Negative",
                    "msType": "EI"
                },
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "headerColumns": [
                    {
                        "chebi": "f60f15b2",
                        "chemicalFormula": "f60f15b2",
                        "chemicalSpecies": "f60f15b2",
                        "compoundDbId": "f60f15b2",
                        "inchi": "f60f15b2",
                        "inchiKey": "f60f15b2",
                        "massToCharge": "f60f15b2",
                        "metaboliteIdentification": "f60f15b2",
                        "pubChemURL": "f60f15b2",
                        "retentionTime": "f60f15b2",
                        "spectraSource": {
                            "database": "f60f15b2",
                            "databaseVersion": "f60f15b2"
                        },
                        "synonyms": [
                            "f60f15b2"
                        ]
                    }
                ],
                "phenotypeUnits": "BLUP",
                "protocol": {
                    "chromatography": "the LC protocol, instrument settings, calibration procedure",
                    "massSpectrometry": "instrument settings, calibration procedure",
                    "metaboliteIdentification": "metabolite annotations were assigned to peaks",
                    "phenotype": "BLUPs were calculated from the peak area",
                    "rawDataTransformation": "the LCMS machine files were transformed into peak area",
                    "sampleCollection": "the tissue, time point, if the sample was frozen",
                    "sampleExtraction": "the extraction protocol used"
                },
                "protocolDbId": "f60f15b2",
                "publications": [
                    "publications1",
                    "publications2"
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




### Get - /metabolomics/{metabolomicsProtocolDbId} [GET /brapi/v2/metabolomics/{metabolomicsProtocolDbId}]

Get a single Metabolomics Protocol by Id. This can be used to quickly get the details of a MetabolomicsProtocol when you have the Id from another entity.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|documentationURL|string (uri)|description|
|equipment|object||
|analysisType|string|MS or NMR. If NMR is selected, the rest of Equipment are not needed|
|chromatographyColumn|string|User free text to specify brand of chromotography column|
|chromatographySystem|string|User free text to specify brand of chromotography system|
|chromatographyType|string|description|
|msInstrumentName|string|User free text to specify brand of MS system|
|msInstrumentType|string|User free text, e.g. time of flight (TOF), triple quadropole|
|msIonMode|string|Negative, Positive, Both|
|msType|string|Electron Ionization (EI), Electrospray Ionization (ESI), Atmospheric Pressure Chemical Ionization (APCI), Matrix Assisted Laser Desorption Ionization (MALDI), Other (please specify below)|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|headerColumns|array[object]|Column definitions for any matrix with this protocol|
|chebi|string|CHEBI id; standard formula|
|chemicalFormula|string|standard formula|
|chemicalSpecies|object|Family of chemical|
|compoundDbId|string|compound ID in this (breedbase) database to link to other files|
|inchi|string|InCHI is another standard universal formula|
|inchiKey|string|shortened version of inchi; users choose one or the other|
|massToCharge|string|m/z ratio, standard from output, should be a number|
|metaboliteIdentification|string|Name of compound|
|pubChemURL|string|pubchem URL is another standard|
|retentionTime|string|retention time, also standard from machine output; users shoud confirm that unit is 'seconds'|
|spectraSource|object|The source database that defines the connection between spectra and compound|
|database|string|Database identifier (Name or URL)|
|databaseVersion|string|Family of chemical|
|synonyms|array[string]|Name of compound|
|phenotypeUnits|string|Free text, e.g. relative abundance, BLUP, drBLUP, concentration (specifiy units, e.g. ug/g)|
|protocol|object||
|chromatography|string|the LC protocol, instrument settings, calibration procedure|
|massSpectrometry|string|instrument settings, calibration procedure|
|metaboliteIdentification|string|metabolite annotations were assigned to peaks|
|phenotype|string|BLUPs were calculated from the peak area|
|rawDataTransformation|string|the LCMS machine files were transformed into peak area|
|sampleCollection|string|the tissue, time point, if the sample was frozen|
|sampleExtraction|string|the extraction protocol used|
|protocolDbId|string|The ID which uniquely identifies the Metabolomics Matrix|
|publications|array[string]|Relevent publication(s), DOI with details|


 

+ Parameters
    + metabolomicsProtocolDbId (Required, ) ... Filter by the common crop name. Exact match.
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
        "additionalInfo": {},
        "documentationURL": "https://wiki.brapi.org",
        "equipment": {
            "analysisType": "MS",
            "chromatographyColumn": "brand of chromotography column",
            "chromatographySystem": "brand of chromotography system",
            "chromatographyType": "LC",
            "msInstrumentName": "brand of MS system",
            "msInstrumentType": "TOF",
            "msIonMode": "Negative",
            "msType": "EI"
        },
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "headerColumns": [
            {
                "chebi": "f60f15b2",
                "chemicalFormula": "f60f15b2",
                "chemicalSpecies": "f60f15b2",
                "compoundDbId": "f60f15b2",
                "inchi": "f60f15b2",
                "inchiKey": "f60f15b2",
                "massToCharge": "f60f15b2",
                "metaboliteIdentification": "f60f15b2",
                "pubChemURL": "f60f15b2",
                "retentionTime": "f60f15b2",
                "spectraSource": {
                    "database": "f60f15b2",
                    "databaseVersion": "f60f15b2"
                },
                "synonyms": [
                    "f60f15b2"
                ]
            }
        ],
        "phenotypeUnits": "BLUP",
        "protocol": {
            "chromatography": "the LC protocol, instrument settings, calibration procedure",
            "massSpectrometry": "instrument settings, calibration procedure",
            "metaboliteIdentification": "metabolite annotations were assigned to peaks",
            "phenotype": "BLUPs were calculated from the peak area",
            "rawDataTransformation": "the LCMS machine files were transformed into peak area",
            "sampleCollection": "the tissue, time point, if the sample was frozen",
            "sampleExtraction": "the extraction protocol used"
        },
        "protocolDbId": "f60f15b2",
        "publications": [
            "publications1",
            "publications2"
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




### Get - /metabolomics/{metabolomicsProtocolDbId}/matrix [GET /brapi/v2/metabolomics/{metabolomicsProtocolDbId}/matrix{?studyDbId}{?observationUnitDbId}]

Get a Metabolomics data matrix by MetabolomicsProtocolDbId



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|description|
|observationUnitName|string|description|
|protocolDbId|string|description|
|row|array[string]|description|
|sampleDbId|string|description|
|tissue_type|string|description|


 

+ Parameters
    + metabolomicsProtocolDbId (Required, ) ... Path parameter protocol id
    + studyDbId (Optional, ) ... filter by study
    + observationUnitDbId (Optional, ) ... filter by study
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
                "additionalInfo": {},
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "e3675c4a",
                "observationUnitName": "Plot ABC",
                "protocolDbId": "fe6f5c50",
                "row": [
                    "0.0355",
                    "0.1442",
                    "0.4322",
                    "0.5473"
                ],
                "sampleDbId": "e3675c4a",
                "tissue_type": "root"
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




### Get - /nirs [GET /brapi/v2/nirs{?nirsProtocolDbId}{?observationUnitDbId}{?externalReferenceID}{?externalReferenceSource}{?page}{?pageSize}]

Get a filtered list of NIRS Protocols



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|deviceType|string|description|
|documentationURL|string (uri)|description|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|header_column_names|array[integer]|description|
|protocolDbId|string|The ID which uniquely identifies the NIRS Matrix|


 

+ Parameters
    + nirsProtocolDbId (Optional, ) ... description
    + observationUnitDbId (Optional, ) ... description
    + externalReferenceID (Optional, ) ... An external reference ID. Could be a simple string or a URI. (use with `externalReferenceSource` parameter)
    + externalReferenceSource (Optional, ) ... An identifier for the source system or database of an external reference (use with `externalReferenceID` parameter)
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
                "additionalInfo": {},
                "deviceType": "SCIO",
                "documentationURL": "https://wiki.brapi.org",
                "externalReferences": [
                    {
                        "referenceID": "doi:10.155454/12341234",
                        "referenceSource": "DOI"
                    },
                    {
                        "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                        "referenceSource": "OBO Library"
                    },
                    {
                        "referenceID": "75a50e76",
                        "referenceSource": "Remote Data Collection Upload Tool"
                    }
                ],
                "header_column_names": [
                    740,
                    742,
                    744,
                    746
                ],
                "protocolDbId": "f60f15b2"
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




### Get - /nirs/{nirsProtocolDbId} [GET /brapi/v2/nirs/{nirsProtocolDbId}]

Get a single NIRS Protocol by Id. This can be used to quickly get the details of a NIRSProtocol when you have the Id from another entity.



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|additionalInfo|object|Additional arbitrary info|
|deviceType|string|description|
|documentationURL|string (uri)|description|
|externalReferences|array[object]|An array of external reference ids. These are references to this piece of data in an external system. Could be a simple string or a URI.|
|referenceID|string|The external reference ID. Could be a simple string or a URI.|
|referenceSource|string|An identifier for the source system or database of this reference|
|header_column_names|array[integer]|description|
|protocolDbId|string|The ID which uniquely identifies the NIRS Matrix|


 

+ Parameters
    + nirsProtocolDbId (Required, ) ... Filter by the common crop name. Exact match.
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
        "additionalInfo": {},
        "deviceType": "SCIO",
        "documentationURL": "https://wiki.brapi.org",
        "externalReferences": [
            {
                "referenceID": "doi:10.155454/12341234",
                "referenceSource": "DOI"
            },
            {
                "referenceID": "http://purl.obolibrary.org/obo/ro.owl",
                "referenceSource": "OBO Library"
            },
            {
                "referenceID": "75a50e76",
                "referenceSource": "Remote Data Collection Upload Tool"
            }
        ],
        "header_column_names": [
            740,
            742,
            744,
            746
        ],
        "protocolDbId": "f60f15b2"
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




### Get - /nirs/{nirsProtocolDbId}/matrix [GET /brapi/v2/nirs/{nirsProtocolDbId}/matrix{?studyDbId}{?observationUnitDbId}]

Get a NIRS data matrix by NIRSProtocolDbId



**Response Fields** 

|Field|Type|Description|
|---|---|---| 
|data|array[object]||
|additionalInfo|object|Additional arbitrary info|
|observationTimeStamp|string (date-time)|The date and time when this observation was made|
|observationUnitDbId|string|description|
|observationUnitName|string|description|
|protocolDbId|string|description|
|row|array[string]|description|
|sampleDbId|string|description|
|tissue_type|string|description|


 

+ Parameters
    + nirsProtocolDbId (Required, ) ... Path parameter protocol id
    + studyDbId (Optional, ) ... filter by study
    + observationUnitDbId (Optional, ) ... filter by study
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
                "additionalInfo": {},
                "observationTimeStamp": "2018-01-01T14:47:23-0600",
                "observationUnitDbId": "e3675c4a",
                "observationUnitName": "Plot ABC",
                "protocolDbId": "fe6f5c50",
                "row": [
                    "0.0355",
                    "0.1442",
                    "0.4322",
                    "0.5473"
                ],
                "sampleDbId": "e3675c4a",
                "tissue_type": "root"
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

